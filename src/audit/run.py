"""Audit Engine CLI — business in, graded report out.

    python -m src.audit.run --business "Carter's Septic Tank Services, Valdosta GA"
    python -m src.audit.run --business "Fade Factory, Kokomo IN" --out output/audits/fade.html

The same report is the outreach hook (send it free), the Tier-1 deliverable,
and — run again after the work — the before/after proof.
"""
import argparse
import json
import re
from pathlib import Path

import yaml

from ..shared.config import CONFIG_DIR
from . import checks, grader, report


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:60]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Audit a business's online presence.")
    ap.add_argument("--business", required=True,
                    help='Name + area, e.g. "Joe\'s Barbershop, Sedalia MO"')
    ap.add_argument("--out", default=None, help="Output HTML path")
    ap.add_argument("--json", action="store_true", help="Also dump raw data as JSON")
    args = ap.parse_args(argv)

    audit_cfg = yaml.safe_load((CONFIG_DIR / "audit.yaml").read_text())

    print(f"Looking up: {args.business} ...")
    data = checks.collect(args.business)
    if data is None:
        raise SystemExit("No Google Places match found. Add the city/state to the query.")

    graded = grader.grade(data, audit_cfg.get("cost_lines", {}))
    slug = slugify(data["name"])
    out = args.out or f"output/audits/{slug}.html"
    report.render(data, graded, audit_cfg, out)

    if args.json:
        Path(out).with_suffix(".json").write_text(
            json.dumps({"data": data, "graded": {k: v for k, v in graded.items()}}, indent=2))

    print(f"\n{data['name']} — overall {graded['overall_grade']} ({graded['overall_pct']}/100)")
    for s in graded["sections"]:
        print(f"  {s['title']:28s} {s['grade']}  ({s['pct']}%)")
    print(f"\nTop fixes:")
    for f in graded["fixes"][:4]:
        print(f"  - {f['label']}: {f['detail']}")
    print(f"\nReport -> {out}")


if __name__ == "__main__":
    main()
