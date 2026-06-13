"""Deterministic fake businesses so the whole pipeline runs end-to-end with no
API key. Produces a realistic spread of brokenness => a realistic ranked sheet."""
import random

from .base import LeadSource
from ...shared.models import Lead

PREFIXES = [
    "Anderson", "Blue Sky", "Reliable", "Summit", "Allstar", "Bee Line",
    "Comfort", "Prime", "Valley", "Desert", "Sunrise", "Patriot", "Eagle",
    "Hometown", "Rapid", "Cool Breeze", "Precision", "Pioneer", "Cardinal",
    "Apex", "Trusted", "Golden", "First Choice", "Red Rock", "Liberty",
]


class MockSource(LeadSource):
    name = "mock"

    def __init__(self, seed: int = 42):
        self.seed = seed

    def search(self, vertical: dict, geo: dict, limit: int = 50) -> list[Lead]:
        rng = random.Random(self.seed)
        suffixes = vertical.get("mock_suffixes") or ["Services", "Co.", "& Sons"]
        areas = geo.get("areas") or [geo.get("display_name", "Town")]
        leads: list[Lead] = []

        for i in range(limit):
            prefix = PREFIXES[i % len(PREFIXES)]
            name = f"{prefix} {rng.choice(suffixes)}"
            area = rng.choice(areas)

            has_site = rng.random() > 0.45
            # Review counts skew low (most local SMBs are under-reviewed)
            review_count = rng.choice(
                [0, 0, 1, 2, 3, 5, 6, 8, 9, 12, 14, 18, 22, 31, 47, 88, 140]
            )
            rating = None if review_count == 0 else round(rng.uniform(3.3, 5.0), 1)
            photos = rng.choice([0, 0, 1, 2, 3, 4, 6, 9, 14, 25])
            has_hours = rng.random() > 0.3
            recency = None if review_count == 0 else rng.choice(
                [3, 9, 14, 21, 35, 45, 70, 120, 240, 400]
            )

            leads.append(Lead(
                name=name,
                category=vertical.get("name", ""),
                source=self.name,
                place_id=f"mock_{i:03d}",
                address=f"{rng.randint(100, 9999)} Main St, {area}",
                phone=f"(555) {rng.randint(200, 999)}-{rng.randint(1000, 9999)}",
                website=(f"https://www.{prefix.lower().replace(' ', '')}{vertical.get('mock_noun', 'co').lower()}.com"
                         if has_site else None),
                google_rating=rating,
                review_count=review_count,
                photos_count=photos,
                categories=[vertical.get("name", "")],
                has_hours=has_hours,
                latest_review_age_days=recency,
            ))
        return leads
