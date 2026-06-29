"""Merge all per-vertical lead CSVs in output/ into one master call-list,
sorted by presence_score (most broken first). Re-ranks across categories so
you work the single best prospects regardless of vertical.

    python -m src.leadfinder.combine
    python -m src.leadfinder.combine --min-score 50 --no-website-only
"""
import argparse
import csv
import glob
from pathlib import Path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Merge lead CSVs into a master call-list.")
    ap.add_argument("--glob", default="output/leads_*.csv",
                    help="which CSVs to merge")
    ap.add_argument("--out", default="output/master_call_list.csv")
    ap.add_argument("--min-score", type=int, default=0,
                    help="drop leads below this presence_score")
    ap.add_argument("--no-website-only", action="store_true",
                    help="keep only leads with no website")
    args = ap.parse_args(argv)

    files = [f for f in glob.glob(args.glob)
             if Path(f).name != Path(args.out).name]
    rows = []
    for f in files:
        with open(f, newline="") as fh:
            for r in csv.DictReader(fh):
                rows.append(r)

    def keep(r):
        if int(r["presence_score"]) < args.min_score:
            return False
        if args.no_website_only and r["website"] != "(none)":
            return False
        return True

    rows = [r for r in rows if keep(r)]
    rows.sort(key=lambda r: int(r["presence_score"]), reverse=True)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["rank", "presence_score", "priority", "name", "phone", "website",
            "google_rating", "review_count", "category", "address",
            "top_problem_1", "top_problem_2", "place_id", "source"]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(rows, 1):
            r["rank"] = i
            w.writerow(r)

    print(f"Merged {len(files)} files -> {out} ({len(rows)} leads)")
    print("\nTop 20 prospects across all categories:")
    for r in rows[:20]:
        print(f"  [{int(r['presence_score']):3d}] {r['priority']:6s} "
              f"{r['name'][:30]:30s} {r['phone']:16s} {r['category']:18s} "
              f"| {r['top_problem_1']}")


if __name__ == "__main__":
    main()
