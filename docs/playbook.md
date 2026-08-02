# Built for Main Street — The Playbook
**Single source of truth. If you and Daniel read one file, it's this one.**

---

## 1. What we are

We make a local business **easy to find, easy to trust, and easy to reach — and we
prove it.** Not a marketing agency. Not "AI automation." Closest honest description:
a **repair-and-upkeep service for a business's online presence**, priced like a job.

Tagline: **Get Found. Get Called. Get Paid.**
Site: builtformainstreet.com · hello@builtformainstreet.com · Miles 310-606-9788

The audit report card defines the scope, the fixes turn its red ✕'s green, and the
re-run audit is the receipt. That structure is what makes the work sellable, provable,
and delegatable.

## 2. What we sell

| # | Package | Who buys it | Price |
|---|---|---|---|
| 1 | **Website Build** — fast, mobile, click-to-call, SEO/AEO/GEO | No website, or a dead one | **$400–700 one-time** + $99–199/mo care plan |
| 2 | **Main Street Visibility Fix** — GBP rewrite, citations, reviews, keywords | Has a presence, but it's broken | **$397** (7–10 days) |
| 3 | **AI Systems** — missed-call text-back first | Existing, happy client | **+$300–700/mo** |

- **The wedge is #1 or #2** (whichever their problem is). Both get us inside.
- **The business is #3.** Highest margin (~95%), stickiest, and what a buyer pays for.
- **Guarantee (already on the site, keep it):** if it doesn't move the needle, we keep
  working. Retainer is earned only after the fix delivers.

**SEO / AEO / GEO in plain English:** SEO = ranks on Google. AEO = shows up in Google's
AI answers. GEO = gets recommended by ChatGPT/Perplexity. Almost no local competitor
sells the last two. Say it lightly; it makes us sound current, not like AI-hype guys.

## 3. Who we target

**Two axes, both deliberately off the guru radar.**

- **Categories:** unsexy, high-ticket, phone-dependent, owner aged 45–65 and not
  marketing-savvy — septic, fencing, tree service, small-engine repair, monument,
  excavation, foundation, propane, HVAC, plumbing.
  *Avoid as primary:* dentists, med spas, chiropractors, realtors, gyms in big metros —
  they get 10 identical calls a week.
- **Geography:** secondary/tertiary US towns (~10k–80k), Midwest/South/Mountain West.
  Two batches are already loaded in `config/geos/`.

**The nuance that decides the $100k:** barbershops, restaurants, and cafés are great for
**fast cash and case studies** — but they will never carry $1,000+/mo. The **trades**
will, because one extra captured job pays our fee for a year. Use the small guys to get
proof; build the recurring base on trades.

**Why the leads exist:** businesses with no website are invisible to Google search — you
literally cannot find them by searching. They only exist as a Maps pin. Google Places
data lists them *and* confirms who has no website. That's our unfair advantage, and it's
already automated.

## 4. What's built (verified working)

| Tool | Command | What it does |
|---|---|---|
| Lead finder | `python -m src.leadfinder.run --vertical X --geo Y --source google_places` | Finds businesses, scores how broken their presence is, ranks them |
| Merge lists | `python -m src.leadfinder.combine --min-score 50 --no-website-only` | One master call list across all categories |
| **Audit engine** | `python -m src.audit.run --business "Name, City ST"` | Graded HTML report card — the hook, the deliverable, and the before/after proof |
| Website kit | `python -m src.website.build --business "Name, City ST" --vertical X` | Mockup you can text a prospect + build brief for Emergent + schema |
| Missed-call demo | `python -m src.aisystems.missed_call.simulate` | Phone mockup of the AI receptionist — your AI sales demo |
| Roster | `python -m src.clientops.roster` | Active clients, MRR, progress to goal, maintenance due |

Plus: `outreach/cold_call_script.md`, and docs for targeting, lead-finding, delivery,
site copy, and AI systems.

**Ready right now:** 206 scored no-website leads with phone numbers.

**Not built yet:** monthly client proof report *(biggest gap — it's what keeps retainers
alive)*, AI-search visibility tracker, review engine, follow-up nurture, booking.

## 5. The number

Goal: **~$100k each per year** = ~$200k combined = **~$19–20k/mo revenue, ~$16k/mo profit.**

This does **not** happen by selling hours. At 20 hrs/week each it only happens by
assembling ~$15k/mo of recurring that other people and software deliver.

**Recommended shape — 16 full-stack clients, not 50 small ones:**

| Line | Mix | Monthly |
|---|---|---|
| Care plans | 16 × $149 | $2,384 |
| Missed-call AI | 16 × $400 | $6,400 |
| Second AI system / visibility retainer | 12 × $400 | $4,800 |
| New builds | 6/mo × $550 | $3,300 |
| Visibility fixes | 5/mo × $397 | $1,985 |
| **Revenue** | | **~$18.9k** |
| Costs (2 VAs, setter commission, tools/Twilio/API) | | ~$3.5k |
| **Profit** | | **~$15.4k/mo → ~$92k each** |

Push to 20 AI clients and you clear $100k each. **Sixteen relationships, not fifty** —
that's the version that fits 20 hrs/week.

At $400–700, the website build is close to a loss-leader (2–4 hrs for ~$550). That's fine — it's
the door. But it means **recurring must carry the business**, which makes the monthly
proof report and the AI layer the two most important things we build next.

## 6. Division of labor

| Miles | Daniel |
|---|---|
| Runs the tools (leads, audits, mockups, AI systems) | Volume outreach — dials, follow-ups, booking calls |
| Delivery + QC until VAs take over | Second closer; splits the call list |
| Builds/deploys AI systems (the expansion sales) | Owns the CRM/pipeline hygiene |
| Technical calls, custom asks | Referral asks, review asks, reactivation |
| Hiring + managing VAs | — |

Both close. Both make calls in months 1–3 — there is no substitute for hearing the
objections yourself before you hand it to anyone.

## 7. Step by step

### Week 1 — Get one paying client
**Miles:** rotate the Google Places API key (it's been pasted in chat). Run a fresh pull
for 2 trade categories in 5 towns. Generate 10 audits + 5 website mockups off the top of
the list. Add your number to `config/audit.yaml` (done) and confirm the Calendly link
works on mobile.
**Daniel:** learn the script cold — the opener, the "I get everything by referral"
rebuttal, and the price answer. Nothing else.
**Both:** 20 dials each, every day, before noon. Lead with the audit ("I looked you up
before I called — you don't have a website / your Google listing says X").
**Target: 1 paying client.** Discount it if you have to. You need a case study more than
you need the money.

### Weeks 2–4 — Prove the delivery
**Miles:** deliver client #1 end-to-end using `docs/service_delivery.md`. BEFORE audit →
fixes → AFTER audit → send both. **Write down every step that was slow or manual** — that
list becomes the next automation and the VA's SOP.
**Daniel:** keep dialing. 20/day. Book Miles into anything technical.
**Both:** land 2–3 more. **Target: 3–4 clients, ~$1.5–2.5k collected.**

### Months 2–3 — Repeatable, and the first AI sale
- Get to **8–12 clients.** Mix of $397 fixes and $400–700 builds.
- Convert 2–3 of the best (trades, ideally) onto **care plans**.
- **Sell one missed-call engine.** Text the phone mockup: *"want this on your line?"*
  This is the single most important sale of the year — it validates the highest-margin
  line in the whole model.
- Capture 3–5 before/after case studies. Put them on the homepage.
- **Target: ~$4–7k/mo. Both of you still doing everything.**

### Months 4–8 — Delegate delivery, you two sell
- **Hire 1–2 VAs** (~$1k/mo each). They run delivery off the checklist. They're graded
  by the AFTER audit being green — so you don't inspect work, you check a report.
- Miles moves to QC + building AI systems. Daniel moves to full-time selling.
- **Systematically upsell missed-call to every happy client.**
- Add commission setters if calendars aren't full.
- **Target: ~$10–14k/mo.**
- ⚠️ **Gate:** if you're still personally doing GBP cleanups at month 8, you've built
  yourselves a job and you will cap around $8k. Delegating by month 4 is not optional.

### Months 9–14 — The machine runs
- Delivery fully delegated. Setters filling calendars.
- Your 20 hrs becomes ~5 sales, ~5 QC, ~5 building/expanding AI systems, ~5 admin.
- Second AI system per client (follow-up or reviews) — pure margin on existing trust.
- **Target: ~$19k+/mo → ~$100k each annualized.**

### Optional exit
At ~$15k/mo MRR and ~$180k/yr profit, a services business trades at ~2–3.5× profit →
**~$350–600k.** The multiple goes up on two things: **share of revenue that's recurring**
and **how little it depends on Miles and Daniel personally.** The repo is the edge —
it makes this look like a tech-enabled product, not two guys with a Calendly. Keep your
names out of delivery, keep churn low.

## 8. Open items / honest risks

1. **No clients yet.** Everything above is built and tested; none of it is validated by a
   paying customer. That's the only real unknown.
2. **The site and the outreach point different directions.** The homepage leads with the
   $397 Visibility Fix; the cold calls lead with websites. Build a dedicated
   website-offer landing page as the destination for call/SMS links.
3. **Rotate the API key.** It was pasted in chat.
4. **The monthly proof report doesn't exist yet** — and it's what stops churn on the
   $149/mo care plans. Build it before you have 10 retainers, not after.
5. **The client cap changed.** The original plan was 12–15 clients at $10k/mo. $100k each
   needs ~16 clients at roughly double the per-client value. Same client count, richer
   accounts — which is why trades matter more than barbershops.
6. **Sales volume is the whole game.** ~16 good clients over 12 months = one or two
   closes each per month. Very doable, but only if the dials actually happen.
