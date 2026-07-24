"""Client roster + recurring-revenue tracker.

Reads every config/clients/*.yaml (ignoring _-prefixed files) and answers the
questions you actually care about: who's active, what's my MRR, how close am I
to the goal, and who needs a maintenance touch this month.

    python -m src.clientops.roster
    python -m src.clientops.roster --goal 10000 --checks-within 30
"""
import argparse
import glob
from datetime import date, datetime
from pathlib import Path

import yaml

ACTIVE = {"active", "delivering"}


def _parse_date(s):
    if not s:
        return None
    try:
        return datetime.strptime(str(s).strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def load_clients(directory: str) -> list[dict]:
    clients = []
    for f in sorted(glob.glob(str(Path(directory) / "*.yaml"))):
        if Path(f).name.startswith("_"):
            continue
        data = yaml.safe_load(Path(f).read_text()) or {}
        data["_file"] = Path(f).name
        clients.append(data)
    return clients


def _money(n) -> str:
    return f"${n:,.0f}"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Client roster + MRR tracker.")
    ap.add_argument("--dir", default="config/clients")
    ap.add_argument("--goal", type=int, default=10000, help="MRR goal")
    ap.add_argument("--checks-within", type=int, default=30,
                    help="flag maintenance checks due within N days")
    args = ap.parse_args(argv)

    clients = load_clients(args.dir)
    if not clients:
        print(f"No client files in {args.dir}/ yet. Copy _template.yaml to "
              f"<business>.yaml when you land your first client.")
        return

    today = date.today()
    mrr = 0
    onetime_total = 0
    counts = {}
    rows = []
    checks_due = []

    for c in clients:
        e = c.get("engagement", {}) or {}
        name = (c.get("business", {}) or {}).get("name", c["_file"])
        status = (e.get("status") or "lead").lower()
        monthly = e.get("monthly_fee", 0) or 0
        onetime = e.get("price_onetime", 0) or 0
        counts[status] = counts.get(status, 0) + 1
        if status in ACTIVE:
            mrr += monthly
        onetime_total += onetime
        nxt = _parse_date(e.get("next_check"))
        if nxt and status in ACTIVE:
            days = (nxt - today).days
            if days <= args.checks_within:
                checks_due.append((days, name, nxt))
        rows.append((name, e.get("package", "-"), status, onetime, monthly,
                     e.get("next_check", "-")))

    # ----- roster table -----
    print(f"\nCLIENT ROSTER  ({len(clients)} records)  ·  {today}")
    print("-" * 78)
    print(f"{'Business':26s} {'Package':11s} {'Status':10s} "
          f"{'1-time':>8s} {'/mo':>7s}  {'Next check':10s}")
    print("-" * 78)
    for name, pkg, status, onetime, monthly, nxt in rows:
        print(f"{name[:26]:26s} {str(pkg)[:11]:11s} {status[:10]:10s} "
              f"{_money(onetime):>8s} {_money(monthly):>7s}  {nxt}")

    # ----- money -----
    print("-" * 78)
    active = sum(counts.get(s, 0) for s in ACTIVE)
    print(f"Active clients: {active}   MRR: {_money(mrr)}   "
          f"One-time booked: {_money(onetime_total)}")
    pct = min(100, round(100 * mrr / args.goal)) if args.goal else 0
    bar = "#" * (pct // 5) + "." * (20 - pct // 5)
    print(f"Goal {_money(args.goal)}/mo  [{bar}] {pct}%   "
          f"(need {_money(max(0, args.goal - mrr))} more)")
    by_status = "  ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
    print(f"Pipeline: {by_status}")

    # ----- maintenance -----
    if checks_due:
        print(f"\nMAINTENANCE DUE within {args.checks_within} days:")
        for days, name, nxt in sorted(checks_due):
            when = "OVERDUE" if days < 0 else ("today" if days == 0 else f"in {days}d")
            print(f"  {when:>8s}  {name}  ({nxt})")
    else:
        print(f"\nNo maintenance checks due within {args.checks_within} days.")


if __name__ == "__main__":
    main()
