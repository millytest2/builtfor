"""Lead-Finding CLI.

    python -m src.leadfinder.run --vertical hvac --geo example_metro --source mock --limit 50
"""
import argparse
from collections import Counter

from ..shared import config
from .export import export_csv
from .scorer import score_leads
from .sources.mock import MockSource


def get_source(name: str):
    if name == "mock":
        return MockSource()
    if name == "google_places":
        from .sources.google_places import GooglePlacesSource
        return GooglePlacesSource()
    raise SystemExit(f"Unknown source: {name!r} (use 'mock' or 'google_places')")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Find + score local-business prospects.")
    ap.add_argument("--vertical", required=True, help="config/verticals/<name>.yaml")
    ap.add_argument("--geo", required=True, help="config/geos/<name>.yaml")
    ap.add_argument("--source", default="mock", choices=["mock", "google_places"])
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--out", default=None)
    ap.add_argument("--force", action="store_true",
                    help="allow overwriting a bigger existing sheet with fewer leads")
    args = ap.parse_args(argv)

    vertical = config.load_vertical(args.vertical)
    geo = config.load_geo(args.geo)
    scoring = config.load_scoring(vertical)

    source = get_source(args.source)
    print(f"Searching {vertical['display_name']} in {geo['display_name']} "
          f"via {source.name} (limit {args.limit})...")
    leads = source.search(vertical, geo, limit=args.limit)
    score_leads(leads, scoring)

    out = args.out or f"output/leads_{args.vertical}_{args.geo}.csv"
    export_csv(leads, out, force=args.force)

    bands = Counter(l.priority for l in leads)
    print(f"\nFound {len(leads)} leads -> {out}")
    print(f"  high: {bands['high']}   medium: {bands['medium']}   low: {bands['low']}")
    print("\nTop 10 prospects:")
    for l in sorted(leads, key=lambda x: x.presence_score, reverse=True)[:10]:
        prob = l.top_problems[0] if l.top_problems else "—"
        print(f"  [{l.presence_score:3d}] {l.priority:6s} {l.name[:32]:32s} | {prob}")


if __name__ == "__main__":
    main()
