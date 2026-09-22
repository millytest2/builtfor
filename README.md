# Built for Main Street

**We get local businesses found. It starts with a website.**

Their Google listing fixed and a website built, together, so search engines and
AI assistants can both actually read them. $800 to build, then $149/mo.

> **Read in this order:** [`docs/OFFER.md`](docs/OFFER.md) for what we sell ·
> [`docs/PROSPECTING.md`](docs/PROSPECTING.md) for how to find and check
> prospects · [`docs/SCRIPT.md`](docs/SCRIPT.md) for what to say · [`docs/STRATEGY_10K.md`](docs/STRATEGY_10K.md) for the funnel and
> capacity math · [`docs/HANDOFF.md`](docs/HANDOFF.md) for cold-start context.

---

## The whole thing in one table

| Stage | Offer | Price |
|---|---|---|
| The door | **Visibility Check** | Free |
| The product | **The fix** | **$500 – $1,000 once**, most jobs $800 |
| Keeping it up | **Keep it live** | **$79/mo hosting** |

The monthly is hosting, not a retainer. Cancel any time and the files are
theirs. You have to host the site anyway, so charging for it passes on a cost
you already carry rather than committing you to manage anything.

**Why it works in 2026:** 35.9% of local business locations turn up in Google's
top three. Only 1.2% get named by ChatGPT. Being good at traditional local
search no longer carries over, and more than half the businesses winning
Google's map pack are absent from AI answers entirely.
(SOCi 2026 Local Visibility Index, 349,000+ locations across 2,751 brands.)

**Lead with the check, never the website.** Every prospect gets cold-called
about websites and about Google most weeks and hangs up in four seconds. Nobody
is calling them about whether an assistant can find them. That is the only part
of this pitch that is not already background noise.

**Out of scope, deliberately:** social media, blog posts, ads, logos, rebrands,
ghostwriting, chatbots talking to customers, anything replacing a person on the
payroll. AI goes behind the desk, never in front of the customer.

## Assets

| What | Where |
|---|---|
| Landing page | `site/index.html` (published) |
| Call sheet, the prospecting tool | `site/callsheet.html` (published) |
| **Top 50 prospects, ranked** | `output/top50_prospects.csv` — these 50 and only these 50 are in the call sheet (full pool of 86 in `prospects_all.csv`) |
| Lead finder, no API key | `python -m src.leadfinder.osm_find --where "..."` |
| Service brief, print source | `docs/manual/service_brief.html` |
| Outbound playbook, call + email | `docs/SCRIPT.md` · print source `docs/manual/call_script.html` |
| Delivery runbook | `docs/DELIVERY.md` · `python -m src.delivery.pack --client ...` |

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

### AI Systems — Missed-Call Text-Back  ✅ (the "Get Paid" expansion)
Turns every missed call into a captured lead: customer calls → no answer → auto
text-back → AI receptionist captures the job → owner gets an instant lead alert.
Highest-margin, stickiest recurring product (+$300–700/mo). Config-per-client.
```bash
python -m src.aisystems.missed_call.simulate            # visual phone-mockup demo
python -m src.aisystems.missed_call.simulate --interactive   # text it yourself
```
Deploy via n8n (no-code) or the included Twilio Flask webhook. Full guide:
`docs/ai_systems.md`. Runs on a keyless template brain; uses Claude when
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
