# Built for Main Street

> **Built for Main Street helps local businesses get found, get contacted, and stop
> losing good leads.**

Niche: **independent auto repair shops**, San Fernando Valley first.

| Stage | Offer | Price |
|---|---|---|
| The door | **Visibility Check** | Free |
| Small | Up to 4 services, 3 towns, one location | $600 + $99/mo |
| **Standard** | Up to 8 services, 6 towns | **$800 + $199/mo** |
| Bigger | More, or two locations | $1,000 + $300/mo |

The tier is picked by counting services and towns on the call, quoted once, and
does not move. Full terms and hard rules: [`CLAUDE.md`](CLAUDE.md).

## Read in this order

1. [`docs/PLAYBOOK.md`](docs/PLAYBOOK.md): the whole business on one page, with the scorecard
2. [`docs/SCRIPT.md`](docs/SCRIPT.md): what to say on the phone and at the counter
3. [`docs/FOCUS.md`](docs/FOCUS.md): why auto repair
4. [`docs/OFFER.md`](docs/OFFER.md): offer reasoning and objections
5. [`docs/DELIVERY.md`](docs/DELIVERY.md): how a paid job gets built

Older versions of the offer are in `docs/archive/` and are not current.

## Assets

| What | Where |
|---|---|
| Website (source → build) | `site/src/` → `python3 site/src/build_site.py` → `site/www/` |
| Call sheet: leads, script, scorecard, pipeline | `site/callsheet.html` (published) |
| The 48 leads, dialing order | `output/call_list_50.csv` |
| Offer PDF for clients | `output/Built_for_Main_Street_Offer.pdf` (source `src/website/offer_onepager.html`) |
| Client site builder | `python3 src/build_site.py clients/<slug>.json` |
| Client agreement | `docs/legal/CLIENT_AGREEMENT.md` |

## The rest of the toolkit

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

### Website Starter Kit  ✅ (the delivery accelerator for "Get Found")
One command turns a client — or just a lead's name — into a full website kit:
tailored copy, JSON-LD schema (SEO/AEO/GEO), a paste-into-Emergent build brief, and
a **real sendable mockup HTML** (the "quick example" the sales script promises).
Pulls live Google data (address, phone, rating) when the key is set; hides weak
reviews automatically.
```bash
# Pre-sale mockup to text a lead:
python -m src.website.build --business "Ace Fence Company, Muncie IN" --vertical fencing
# From a signed client's file:
python -m src.website.build --client config/clients/ace_fence.yaml
# -> output/websites/<slug>/{mockup.html, build_brief.md, copy.md, schema.json}
```

### AI Systems — Missed-Call Text-Back  (built, **not sold**)
Parked. It sends text messages and uses an AI receptionist, and the hard rules say
no SMS before client #10 and nothing that replaces labour. Kept as code only.
```bash
python -m src.aisystems.missed_call.simulate            # visual phone-mockup demo
python -m src.aisystems.missed_call.simulate --interactive   # text it yourself
```
Deploy via n8n (no-code) or the included Twilio Flask webhook. Full guide:
`docs/archive/ai_systems.md`. Runs on a keyless template brain; uses Claude when
`ANTHROPIC_API_KEY` is set.

### Item 5 — Client Ops / Retainer Tracker  ✅
One command shows active clients, MRR, one-time booked, progress to your $10k goal,
and which retainers are due for a maintenance touch. Each client is one YAML file
(`config/clients/<slug>.yaml`, copied from `_template.yaml`) that doubles as delivery
intake and recurring tracking.
```bash
python -m src.clientops.roster            # roster + MRR + maintenance-due
```

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
