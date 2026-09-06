"""Pick the leads worth actually CALLING — not just the most broken ones.

The presence scorer answers "how broken is this business online?" That alone
picks bad clients: a 1-star shop scores high, but their problem is their service,
not their marketing. Fixing their Google profile just gets more people to a
business people dislike — they churn, and they blame you.

The ideal client for our service (website + optimization + AI monthly) is:
  - NO WEBSITE            -> needs offer #1, and is invisible to competitors'
                             scrapers, so nobody else is pitching them
  - GOOD RATING (>=4.0)   -> they're good at the actual work, so marketing works
  - FEW REVIEWS           -> invisible despite being good = the winnable gap
  - REACHABLE (has phone) -> we can call them today
  - HIGH-TICKET TRADE     -> one job pays our fee; can afford $400 + $300-600/mo
  - URGENCY-DRIVEN        -> missed calls cost them real money = easy AI upsell

    python -m src.leadfinder.shortlist --top 10
    python -m src.leadfinder.shortlist --top 20 --min-rating 4.3
"""
import argparse
import csv
import glob
from pathlib import Path

# Trades where one job is worth enough to fund our fee, and the phone is the
# lifeline. Urgency-driven ones score higher — missed calls hurt more.
TICKET = {
    "septic": 3, "tree_service": 3, "plumbing": 3, "hvac": 3,
    "fencing": 2, "excavation": 3, "monument": 1, "equipment_repair": 1,
    "barbershop": 0, "restaurant": 0, "cafe": 0,
}
URGENT = {"septic", "plumbing", "hvac", "tree_service"}


def _int(v, default=0):
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def _float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def fit_score(row: dict) -> float:
    """0-100: how good a CLIENT this is, not how broken they are."""
    rating = _float(row.get("google_rating"))
    reviews = _int(row.get("review_count"))
    cat = row.get("category", "")
    score = 0.0
    # Quality of the underlying business — the single most important factor.
    if rating is not None:
        score += min(35.0, max(0.0, (rating - 3.5) * 23))   # 4.0->11, 4.5->23, 5.0->35
    # Invisible despite being good: the gap we close.
    score += 25.0 if reviews <= 10 else (15.0 if reviews <= 25 else 5.0)
    # Established enough to have real revenue. Among equally-invisible 5-star
    # shops, the one with 10 reviews is a safer payer than the one with 3.
    score += min(10.0, reviews * 0.8)
    # Can they afford us / does the phone matter?
    score += TICKET.get(cat, 0) * 5
    score += 10.0 if cat in URGENT else 0.0
    return round(score, 1)


def metro(address: str) -> str:
    """'123 Main St, Valdosta, GA 31601, USA' -> 'Valdosta, GA' (zip stripped so
    multiple zips in one town cluster together)."""
    parts = [p.strip() for p in (address or "").split(",")]
    if len(parts) < 3:
        return address or "?"
    city = parts[-3]
    state = parts[-2].split()[0] if parts[-2].split() else parts[-2]
    return f"{city}, {state}"


def load_rows(pattern: str) -> list:
    rows = []
    for f in glob.glob(pattern):
        if "master" in Path(f).name or "shortlist" in Path(f).name:
            continue
        rows += list(csv.DictReader(open(f)))
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description="Shortlist the leads worth calling.")
    ap.add_argument("--glob", default="output/leads_*.csv")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--min-rating", type=float, default=4.0)
    ap.add_argument("--max-reviews", type=int, default=25)
    ap.add_argument("--cluster", action="store_true",
                    help="group by town and work the densest ones first")
    ap.add_argument("--out", default="output/shortlist.csv")
    args = ap.parse_args(argv)

    rows = load_rows(args.glob)
    picked, seen = [], set()
    for r in rows:
        if r.get("website") != "(none)":       # must need offer #1
            continue
        if not (r.get("phone") or "").strip():  # must be callable
            continue
        rating = _float(r.get("google_rating"))
        reviews = _int(r.get("review_count"))
        if rating is None or rating < args.min_rating:
            continue                            # good at the work, or skip
        if reviews < 3 or reviews > args.max_reviews:
            continue                            # real, but invisible
        if TICKET.get(r.get("category", ""), 0) < 2:
            continue                            # must afford us
        if r["phone"] in seen:
            continue
        seen.add(r["phone"])
        r["fit_score"] = fit_score(r)
        picked.append(r)

    picked.sort(key=lambda r: r["fit_score"], reverse=True)

    if args.cluster:
        # Density beats individual fit. Ten calls into ONE town lets you say "I work
        # with a couple other tree guys around here", enables referrals and in-person
        # visits, and builds local reputation. Ten calls into ten states does none.
        from collections import defaultdict
        by_town = defaultdict(list)
        for r in picked:
            by_town[metro(r["address"])].append(r)
        ranked = sorted(by_town.items(),
                        key=lambda kv: (len(kv[1]), sum(x["fit_score"] for x in kv[1])),
                        reverse=True)
        print("Lead density by town (working one town beats scattering):")
        for t, rs in ranked[:6]:
            print(f"  {len(rs):>2}  {t}")
        print()
        picked = [r for _, rs in ranked for r in rs]

    picked = picked[: args.top]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["rank", "fit_score", "presence_score", "name", "phone", "google_rating",
            "review_count", "category", "address", "top_problem_1"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(picked, 1):
            r["rank"] = i
            w.writerow(r)

    print(f"Shortlist: {len(picked)} leads worth calling -> {out}\n")
    print(f"{'#':>2} {'fit':>4} {'name':30s} {'phone':16s} {'★':>4} {'rev':>4} "
          f"{'town':18s} category")
    print("-" * 100)
    for i, r in enumerate(picked, 1):
        print(f"{i:>2} {r['fit_score']:>4} {r['name'][:30]:30s} {r['phone']:16s} "
              f"{r['google_rating']:>4} {r['review_count']:>4} "
              f"{metro(r['address'])[:18]:18s} {r['category']}")
    return picked


if __name__ == "__main__":
    main()
