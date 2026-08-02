import csv
from pathlib import Path

from ..shared.models import Lead

COLUMNS = [
    "rank", "presence_score", "priority", "name", "phone", "website",
    "google_rating", "review_count", "photos_count", "has_hours",
    "top_problem_1", "top_problem_2", "address", "place_id", "category", "source",
]


def _existing_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with open(path, newline="") as f:
        return max(0, sum(1 for _ in f) - 1)


def export_csv(leads: list[Lead], path: str, force: bool = False) -> str:
    """Write the ranked sheet. Refuses to shrink an existing file unless forced —
    a re-run with a smaller --limit would otherwise silently destroy a big pull."""
    leads = sorted(leads, key=lambda l: l.presence_score, reverse=True)
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    prior = _existing_rows(out)
    if prior > len(leads) and not force:
        raise SystemExit(
            f"Refusing to overwrite {out} ({prior} leads) with only {len(leads)}.\n"
            f"Re-run with a larger --limit, a different --out, or pass --force."
        )
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
