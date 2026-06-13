"""Live source using the new Google Places API v1 (places.googleapis.com).
Text Search returns most signals we need in one call via field mask — cheap,
no separate Details call. Cached + rate-limited.

Note: review recency isn't available from Text Search (needs Place Details,
capped at 5 reviews), so latest_review_age_days is left None and the scorer
skips that signal for live leads. The Audit Engine (Item 2) pulls it per-lead."""
import os

import requests

from .base import LeadSource
from ...shared.cache import HttpCache
from ...shared.models import Lead
from ...shared.ratelimit import RateLimiter

PLACES_URL = "https://places.googleapis.com/v1/places:searchText"
FIELD_MASK = ",".join([
    "places.id", "places.displayName", "places.formattedAddress",
    "places.nationalPhoneNumber", "places.websiteUri", "places.rating",
    "places.userRatingCount", "places.regularOpeningHours", "places.photos",
    "places.types", "places.businessStatus", "nextPageToken",
])


class GooglePlacesSource(LeadSource):
    name = "google_places"

    def __init__(self, api_key: str | None = None, cache_dir: str = "data/cache",
                 calls_per_sec: float = 5.0):
        self.api_key = api_key or os.environ.get("GOOGLE_PLACES_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "GOOGLE_PLACES_API_KEY not set. Use --source mock to test without a key."
            )
        self.rl = RateLimiter(calls_per_sec)
        self.cache = HttpCache(cache_dir)

    def search(self, vertical: dict, geo: dict, limit: int = 60) -> list[Lead]:
        leads: dict[str, Lead] = {}
        areas = geo.get("areas") or [geo.get("display_name", "")]
        for term in vertical.get("search_terms", []):
            for area in areas:
                if len(leads) >= limit:
                    return list(leads.values())
                query = f"{term} in {area}"
                for place in self._search_query(query, limit):
                    pid = place.get("id")
                    if pid and pid not in leads:
                        leads[pid] = self._to_lead(place, vertical)
                    if len(leads) >= limit:
                        break
        return list(leads.values())

    def _search_query(self, query: str, limit: int) -> list[dict]:
        results: list[dict] = []
        page_token = None
        while len(results) < limit:
            body = {"textQuery": query, "maxResultCount": 20}
            if page_token:
                body["pageToken"] = page_token
            cache_key = f"{query}|{page_token}"
            data = self.cache.get(cache_key)
            if data is None:
                self.rl.wait()
                resp = requests.post(PLACES_URL, json=body, headers={
                    "Content-Type": "application/json",
                    "X-Goog-Api-Key": self.api_key,
                    "X-Goog-FieldMask": FIELD_MASK,
                }, timeout=30)
                resp.raise_for_status()
                data = resp.json()
                self.cache.set(cache_key, data)
            results.extend(data.get("places", []))
            page_token = data.get("nextPageToken")
            if not page_token:
                break
        return results[:limit]

    def _to_lead(self, p: dict, vertical: dict) -> Lead:
        return Lead(
            name=(p.get("displayName") or {}).get("text", ""),
            category=vertical.get("name", ""),
            source=self.name,
            place_id=p.get("id"),
            address=p.get("formattedAddress", ""),
            phone=p.get("nationalPhoneNumber"),
            website=p.get("websiteUri"),
            google_rating=p.get("rating"),
            review_count=p.get("userRatingCount", 0) or 0,
            photos_count=len(p.get("photos", []) or []),
            categories=p.get("types", []) or [],
            has_hours=bool(p.get("regularOpeningHours")),
            claimed=(p.get("businessStatus") == "OPERATIONAL"),
            latest_review_age_days=None,
        )
