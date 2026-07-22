# Built for Main Street

**Get Found. Get Called. Get Paid.**

Productized local-business growth service. Everything here is **config-driven and
clone-per-client** — no bespoke builds. Swap a config file, redeploy, done.

## The offer (v2 — current)
**Local visibility gap-fixing, productized.** Not "we build websites" — we find the
gaps costing a business calls, trust, and customers, then fix them fast:
GBP optimization, listing consistency, AI-search visibility, local SEO, trust
signals, and a high-converting site/landing page *when needed*.

**Execution loop:** sell one $300–800 fix → deliver in days → capture before/after
proof (the audit report, run twice) → repeat → referrals. Target $3k/mo, then $10k/mo.

Primary targets right now: **barbershops & local service businesses with weak/missing
websites; restaurants & cafés with obvious GBP issues.**

---

## What's built so far

### Item 1 — Lead-Finding System  ✅ (runs today)
Finds businesses in a vertical + geo, pulls presence data (name, website, phone,
rating, review count, photos, GBP completeness), scores **how broken their online
presence is** (high score = high-priority prospect), and exports a ranked CSV with
the top 1–2 problems to lead with on a call.

```bash
# Runs immediately on realistic mock data — no API key needed:
python -m src.leadfinder.run --vertical hvac --geo example_metro --source mock --limit 50

# Live data once you have a key (see .env.example):
export GOOGLE_PLACES_API_KEY=...
python -m src.leadfinder.run --vertical hvac --geo example_metro --source google_places --limit 60
```

Output → `output/leads_<vertical>_<geo>.csv` (open in Google Sheets / Excel).

### Item 2 — Audit Engine  ✅ (runs today; needs GOOGLE_PLACES_API_KEY)
Business in → graded HTML report out. Checks GBP (photos, hours, phone, website
link, description), reviews (count, rating, recency), and the live website
(HTTPS, mobile, tap-to-call, lead capture, speed). Branding/CTA in `config/audit.yaml`.

```bash
python -m src.audit.run --business "Joe's Barbershop, Sedalia MO"
# -> output/audits/joe_s_barbershop.html  (print to PDF from the browser)
```

Three uses, one engine: free outreach hook → Tier-1 deliverable → run it again
after the work for **before/after proof**.

---

## Repo structure
```
config/
  verticals/   hvac.yaml, plumbing.yaml   # search terms, mock hints, scoring overrides
  geos/        example_metro.yaml          # <-- swap to your real metro
  scoring.yaml                             # presence-score weights + thresholds
  clients/     (added in Item 4/5)
src/
  shared/      config loader, models, rate limiter, http cache
  leadfinder/  sources/ (mock, google_places), scorer, export, run
data/          cached raw API pulls (gitignored)
output/        generated sheets/reports (gitignored)
tests/
```

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env   # add keys when you have them
```

## How scoring works
A lead's **presence_score (0–100)** = how broken/weak their online presence is.
Higher = better prospect for us. Weights live in `config/scoring.yaml`:

| Signal | Weight | Why it's a sellable problem |
|---|---|---|
| No website | 30 | Losing everyone who Googles them → website build |
| Few reviews | 25 | Looks inactive vs competitors → review engine |
| Low rating | 12 | Reputation costing calls → review engine |
| Few/no photos | 11 | Profile looks unmaintained → GBP optimization |
| Incomplete GBP | 10 | Missing hours/categories → GBP optimization |
| Stale reviews | 12 | Momentum stalled → review engine |

Priority bands: **high ≥60, medium ≥35, low <35**.
