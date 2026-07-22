"""Data collection for an audit: Google Places lookup + details, and a live
website inspection. Every check degrades gracefully — missing data is reported
as 'unknown', never crashes the audit."""
import os
import re
import time
from datetime import datetime, timezone

import requests

from ..shared.cache import HttpCache
from ..shared.ratelimit import RateLimiter

SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"
DETAILS_URL = "https://places.googleapis.com/v1/places/{place_id}"
SEARCH_MASK = "places.id,places.displayName,places.formattedAddress"
DETAILS_MASK = ",".join([
    "id", "displayName", "formattedAddress", "nationalPhoneNumber",
    "websiteUri", "rating", "userRatingCount", "regularOpeningHours",
    "photos", "types", "businessStatus", "reviews", "editorialSummary",
])

_rl = RateLimiter(5.0)
_cache = HttpCache("data/cache")


def _api_key() -> str:
    key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_PLACES_API_KEY not set.")
    return key


def find_place(query: str) -> dict | None:
    """Resolve a business name (+ area) to a place_id via Text Search."""
    cache_key = f"audit_search|{query}"
    data = _cache.get(cache_key)
    if data is None:
        _rl.wait()
        resp = requests.post(SEARCH_URL, json={"textQuery": query, "maxResultCount": 1},
                             headers={"Content-Type": "application/json",
                                      "X-Goog-Api-Key": _api_key(),
                                      "X-Goog-FieldMask": SEARCH_MASK},
                             timeout=30)
        resp.raise_for_status()
        data = resp.json()
        _cache.set(cache_key, data)
    places = data.get("places", [])
    return places[0] if places else None


def place_details(place_id: str) -> dict:
    cache_key = f"audit_details|{place_id}"
    data = _cache.get(cache_key)
    if data is None:
        _rl.wait()
        resp = requests.get(DETAILS_URL.format(place_id=place_id),
                            headers={"X-Goog-Api-Key": _api_key(),
                                     "X-Goog-FieldMask": DETAILS_MASK},
                            timeout=30)
        resp.raise_for_status()
        data = resp.json()
        _cache.set(cache_key, data)
    return data


def latest_review_age_days(details: dict) -> int | None:
    """Newest review age from the (up to 5) reviews Details returns."""
    times = []
    for r in details.get("reviews", []) or []:
        ts = r.get("publishTime")
        if ts:
            try:
                times.append(datetime.fromisoformat(ts.replace("Z", "+00:00")))
            except ValueError:
                pass
    if not times:
        return None
    newest = max(times)
    return max(0, (datetime.now(timezone.utc) - newest).days)


def check_website(url: str | None) -> dict:
    """Fetch the site and inspect the basics that decide whether it produces
    calls: reachable, https, mobile viewport, tap-to-call, any lead capture,
    load time. Network failures -> fetched=False (report says 'couldn't verify')."""
    result = {
        "exists": bool(url), "url": url, "fetched": False, "https": None,
        "mobile_viewport": None, "click_to_call": None, "lead_capture": None,
        "load_seconds": None, "error": None,
    }
    if not url:
        return result
    result["https"] = url.lower().startswith("https://")
    try:
        start = time.time()
        resp = requests.get(url, timeout=20, allow_redirects=True, headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                          "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        })
        result["load_seconds"] = round(time.time() - start, 2)
        result["fetched"] = True
        html = resp.text[:400_000].lower()
        result["https"] = resp.url.lower().startswith("https://")
        result["mobile_viewport"] = 'name="viewport"' in html or "name='viewport'" in html
        result["click_to_call"] = 'href="tel:' in html or "href='tel:" in html
        result["lead_capture"] = bool(
            re.search(r"<form|calendly|booksy|square\s*appointments|schedulicity|"
                      r"acuityscheduling|vagaro|setmore|book\s*(now|online|appointment)|"
                      r"request\s*(a\s*)?(quote|estimate)", html)
        )
    except requests.RequestException as e:
        result["error"] = type(e).__name__
    return result


def collect(query: str) -> dict | None:
    """Full audit data pull for one business."""
    hit = find_place(query)
    if not hit:
        return None
    details = place_details(hit["id"])
    website = check_website(details.get("websiteUri"))
    return {
        "place_id": details.get("id"),
        "name": (details.get("displayName") or {}).get("text", query),
        "address": details.get("formattedAddress", ""),
        "phone": details.get("nationalPhoneNumber"),
        "website": details.get("websiteUri"),
        "rating": details.get("rating"),
        "review_count": details.get("userRatingCount", 0) or 0,
        "photos_count": len(details.get("photos", []) or []),
        "has_hours": bool(details.get("regularOpeningHours")),
        "has_description": bool(details.get("editorialSummary")),
        "categories": details.get("types", []) or [],
        "latest_review_age_days": latest_review_age_days(details),
        "website_check": website,
    }
