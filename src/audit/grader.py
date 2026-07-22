"""Turn collected audit data into section grades + a prioritized fix list.
Three sections: Google Business Profile, Reviews & Reputation, Website.
Each check: passed / failed / unknown, with a plain-language cost line."""


def _grade(pct: float) -> str:
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (55, "D")):
        if pct >= cutoff:
            return letter
    return "F"


def _check(checks: list, ok: bool | None, points: int, label: str,
           detail: str, cost_key: str | None):
    """ok=None -> unknown (excluded from scoring)."""
    checks.append({"ok": ok, "points": points, "label": label,
                   "detail": detail, "cost_key": cost_key})


def grade(data: dict, cost_lines: dict) -> dict:
    sections = []
    fixes = []

    # ---------- Google Business Profile ----------
    c: list = []
    _check(c, data["photos_count"] >= 5, 30, "Photos on profile",
           f"{data['photos_count']} photos found (want 5+, ideally 15+)", "few_photos")
    _check(c, data["has_hours"], 25, "Business hours listed",
           "Hours are set" if data["has_hours"] else "No hours listed — Google may show 'Hours unknown'",
           "weak_gbp")
    _check(c, bool(data["phone"]), 20, "Phone number on profile",
           data["phone"] or "No phone number on the listing", "weak_gbp")
    _check(c, bool(data["website"]), 15, "Website linked",
           data["website"] or "No website linked on the profile", "no_website")
    _check(c, data["has_description"], 10, "Business description",
           "Description present" if data["has_description"] else "No description — a free ranking signal left empty",
           "weak_gbp")
    sections.append({"key": "gbp", "title": "Google Business Profile", "checks": c})

    # ---------- Reviews & Reputation ----------
    c = []
    rc = data["review_count"]
    _check(c, rc >= 40 if rc is not None else None, 40, "Review count",
           f"{rc} Google reviews (competitive is 40+; leaders have 100+)", "low_reviews")
    rating = data["rating"]
    _check(c, (rating or 0) >= 4.5 if rating is not None else None, 30, "Average rating",
           f"{rating}★ average" if rating is not None else "No rating yet", "low_rating")
    age = data["latest_review_age_days"]
    _check(c, age <= 60 if age is not None else None, 30, "Review recency",
           f"Newest review ~{age} days ago" if age is not None else "Couldn't determine review recency",
           "stale_reviews")
    sections.append({"key": "reviews", "title": "Reviews & Reputation", "checks": c})

    # ---------- Website ----------
    c = []
    w = data["website_check"]
    _check(c, w["exists"], 35, "Website exists",
           w["url"] or "No website found anywhere", "no_website")
    if w["exists"]:
        if w["fetched"]:
            _check(c, w["https"], 10, "Secure (HTTPS)",
                   "Secure connection" if w["https"] else "Not secure — browsers warn visitors", "no_https")
            _check(c, w["mobile_viewport"], 15, "Mobile-friendly",
                   "Mobile viewport configured" if w["mobile_viewport"] else "Not built for phones", "not_mobile")
            _check(c, w["click_to_call"], 20, "Tap-to-call",
                   "Phone number is tappable" if w["click_to_call"] else "No tap-to-call link on the site",
                   "no_click_to_call")
            _check(c, w["lead_capture"], 15, "Booking / contact capture",
                   "Booking or contact form found" if w["lead_capture"] else "No way to book or send a request",
                   "no_lead_capture")
            if w["load_seconds"] is not None:
                _check(c, w["load_seconds"] <= 4.0, 5, "Load speed",
                       f"Loaded in {w['load_seconds']}s", "slow_site")
        else:
            _check(c, None, 0, "Site inspection",
                   f"Couldn't fetch the site to verify ({w['error']}) — verify manually", None)
    sections.append({"key": "website", "title": "Website & Lead Capture", "checks": c})

    # ---------- Score sections + collect fixes ----------
    for s in sections:
        known = [ch for ch in s["checks"] if ch["ok"] is not None]
        total = sum(ch["points"] for ch in known) or 1
        earned = sum(ch["points"] for ch in known if ch["ok"])
        s["pct"] = round(100 * earned / total)
        s["grade"] = _grade(s["pct"])
        for ch in s["checks"]:
            if ch["ok"] is False:
                fixes.append({"section": s["title"], "label": ch["label"],
                              "detail": ch["detail"], "points": ch["points"],
                              "cost": cost_lines.get(ch["cost_key"], "")})

    overall_pct = round(sum(s["pct"] for s in sections) / len(sections))
    fixes.sort(key=lambda f: f["points"], reverse=True)
    return {"sections": sections, "overall_pct": overall_pct,
            "overall_grade": _grade(overall_pct), "fixes": fixes}
