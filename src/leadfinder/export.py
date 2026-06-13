import csv
from pathlib import Path

from ..shared.models import Lead

COLUMNS = [
    "rank", "presence_score", "priority", "name", "phone", "website",
    "google_rating", "review_count", "photos_count", "has_hours",
    "top_problem_1", "top_problem_2", "address", "place_id", "category", "source",
]


def export_csv(leads: list[Lead], path: str) -> str:
    leads = sorted(leads, key=lambda l: l.presence_score, reverse=True)
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for i, l in enumerate(leads, 1):
            probs = (l.top_problems + ["", ""])[:2]
            writer.writerow([
                i, l.presence_score, l.priority, l.name, l.phone or "",
                l.website or "(none)",
                l.google_rating if l.google_rating is not None else "",
                l.review_count, l.photos_count, "yes" if l.has_hours else "no",
                probs[0], probs[1], l.address, l.place_id or "",
                l.category, l.source,
            ])
    return str(out)
