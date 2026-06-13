"""Scores how BROKEN a business's online presence is (0-100).
Higher = weaker presence = higher-priority prospect for us.
Also derives the top 1-2 problems to lead with on a call."""
from .sources.base import LeadSource  # noqa: F401 (kept for type clarity)
from ..shared.models import Lead


def score_lead(lead: Lead, scoring: dict) -> Lead:
    w = scoring["weights"]
    t = scoring["thresholds"]
    breakdown: dict[str, float] = {}
    problems: list[tuple[float, str]] = []

    # --- No website ---
    if not lead.website:
        breakdown["no_website"] = w["no_website"]
        problems.append((w["no_website"],
                         "No website — losing every customer who Googles them first"))
    else:
        breakdown["no_website"] = 0

    # --- Review volume (scaled to target) ---
    target = t["review_count_target"]
    rc = lead.review_count or 0
    vol = w["low_reviews"] * max(0.0, (target - min(rc, target)) / target) if target else 0
    breakdown["low_reviews"] = round(vol, 1)
    if rc < t["review_count_low"]:
        problems.append((vol, f"Only {rc} Google reviews — looks inactive vs competitors"))

    # --- Rating ---
    rating = lead.google_rating
    if rating is not None and rating < t["rating_good"]:
        span = t["rating_good"] - t["rating_floor"]
        frac = min(1.0, (t["rating_good"] - rating) / span) if span > 0 else 1.0
        pts = w["low_rating"] * frac
        breakdown["low_rating"] = round(pts, 1)
        problems.append((pts, f"{rating}★ rating — reputation is costing them calls"))
    else:
        breakdown["low_rating"] = 0

    # --- Photos ---
    if lead.photos_count < t["photos_min"]:
        breakdown["few_photos"] = w["few_photos"]
        problems.append((w["few_photos"],
                         "Few/no photos on Google — profile looks unmaintained"))
    else:
        breakdown["few_photos"] = 0

    # --- GBP completeness ---
    if not lead.has_hours:
        breakdown["incomplete_gbp"] = w["incomplete_gbp"]
        problems.append((w["incomplete_gbp"],
                         "Google profile missing info (hours/categories)"))
    else:
        breakdown["incomplete_gbp"] = 0

    # --- Review recency (only if known) ---
    age = lead.latest_review_age_days
    if age is not None and age > t["review_recency_days"]:
        breakdown["stale_reviews"] = w["stale_reviews"]
        problems.append((w["stale_reviews"],
                         f"No new reviews in ~{age} days — momentum stalled"))
    else:
        breakdown["stale_reviews"] = 0

    total = max(0, min(100, round(sum(breakdown.values()))))
    lead.presence_score = total
    lead.score_breakdown = breakdown
    problems.sort(key=lambda p: p[0], reverse=True)
    lead.top_problems = [msg for _, msg in problems[:2]]

    if total >= t["priority_high"]:
        lead.priority = "high"
    elif total >= t["priority_medium"]:
        lead.priority = "medium"
    else:
        lead.priority = "low"
    return lead


def score_leads(leads: list[Lead], scoring: dict) -> list[Lead]:
    for lead in leads:
        score_lead(lead, scoring)
    return leads
