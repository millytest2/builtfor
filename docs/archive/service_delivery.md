# The Service & How We Deliver It

## What we are (working definition)
Not a marketing agency. Not "AI automation." We're the people who **make a local
business easy to find, easy to trust, and easy to reach** — and we prove it.
Think of it as a **repair + upkeep service for a business's online presence**,
priced like a job, not a subscription-you-can't-cancel.

Everything maps to the tagline:

| | Package | Buyer | Price | The promise |
|---|---|---|---|---|
| **Get Found** | 1. Website Build | No website (or a dead one) | $400–700 one-time + $99–199/mo upkeep | A fast, high-converting site that ranks in Google *and* AI answers |
| **Get Called** | 2. Full Visibility Fix | Has a presence but it's broken | $300–800 one-time (+ optional retainer) | Google profile, reviews & listings cleaned up so they show up and get chosen |
| **Get Paid** | 3. AI Systems | Existing client, ready to scale | +$300–700/mo | Missed-call text-back, follow-up, booking — the expansion, once trust exists |

**The wedge is the Website Build.** It's the easiest to sell (leads with no website
are trivial to find and the pitch is obvious) and it puts us *inside* the business,
which is what unlocks packages 2 and 3. Land with #1, expand into #2 and #3.

---

## Package 1 — Website Build ("Get Found")  ·  $400 / $700 + $99–199/mo
For a business with no website or a broken/abandoned one.

**What "SEO / AEO / GEO" means (so you can say it plainly):**
- **SEO** — ranks in normal Google search ("plumber near me")
- **AEO** — Answer Engine Optimization: shows up in Google's AI Overview / featured answers
- **GEO** — Generative Engine Optimization: gets cited by ChatGPT, Gemini, Perplexity
  when someone asks them for a local recommendation. This is the *new* thing almost
  no competitor is doing, and it's mostly clean structured data + clear copy.

**Delivery (2–4 days), built with an AI site builder (Emergent / Webild / Replit):**
1. BEFORE audit (baseline snapshot) — `python -m src.audit.run`
2. Intake: logo, photos, services, hours, service area, phone, domain
3. Build one page (or 3–5) from our template: hero with the outcome, services,
   reviews embedded, photos, hours, map
4. Wire lead capture: **tap-to-call**, contact/booking form, click-to-text
5. SEO/AEO/GEO pass: title/meta, `LocalBusiness` + `FAQPage` schema, NAP that
   matches Google exactly, clear Q&A copy the AI engines can quote
6. Connect their domain (or provision one), verify HTTPS + mobile
7. AFTER audit → send before/after + the live link
8. **$400** = single high-converting page; **$700** = multi-page + booking + review embed

**The monthly retainer ($99–199) is real, not fluff.** Track it in the client file
(`monthly_fee`, `next_check`). Each month: uptime check, small edits (hours, photos,
seasonal offers), keep NAP synced with Google, re-run the audit, send a one-line
"here's what we did" note. That note is why they keep paying.

## Package 2 — Full Visibility Fix ("Get Called")  ·  $300–800
For a business with a real presence problem: one review, wrong hours, unclaimed or
mismanaged Google profile. (Tools like **owner.com** help here for restaurants.)
This is the audit-driven cleanup — see the checklist that follows.

1. Claim/verify GBP; complete every field (hours, categories, services, description)
2. Photos: 10–15 up; AI-enhance if needed
3. Reviews: generate their Google review link + printable QR card + "text your last
   20 happy customers" SMS template (first-push, day one)
4. Listings: match name/address/phone/hours on Apple, Bing, Yelp, Facebook, Nextdoor
5. Seed Q&A, publish a first post
6. AFTER audit → before/after report. **Done = GBP section grades A.**

## Package 3 — AI Systems ("Get Paid")  ·  +$300–700/mo
Only sold to an existing, happy client. Once we manage their presence, we already
have the access and trust to add: **missed-call text-back, lead follow-up nurture,
review-request automation, booking automation.** Built config-per-client (this repo's
Item 4). This is where Claude Code does the heavy lifting and margins are highest.

---

## The pipeline (every client, no exceptions)
| Day | Step | Tool |
|---|---|---|
| 0 | Sale on the phone → intake form, collect 50% or full | script + payment link |
| 0 | Create `config/clients/<slug>.yaml` from `_template.yaml` | the client file |
| 1 | BEFORE audit snapshot (save HTML) | `python -m src.audit.run --business "..."` |
| 1–4 | Build/fix per package checklist | Emergent/Webild + GBP |
| 2–5 | AFTER audit snapshot | same command |
| — | Send before/after + live link + invoice balance | email/SMS |
| +3 | "Seeing more calls yet?" → ask for a review + 1 referral | SMS |
| monthly | Maintenance touch + re-audit + 1-line update | `roster.py` reminds you |

**Definition of done (objective):** AFTER audit meets the bar (GBP grade A; website
package also needs Website section ≥ B), before/after delivered, review kit handed over.
If the AFTER report isn't green, the job isn't done. The report is the product.

## Tracking the money
`python -m src.clientops.roster` reads all client files and shows active clients,
**MRR**, one-time booked, progress toward your $10k/mo goal, and which retainers are
**due for a maintenance check**. That's the "keep track of it" system — one command.

## If you hand delivery to someone else (Daniel / VA / hire)
The service is deliberately **a checklist + two commands**, so a careful non-expert
can run it. Handoff kit:
1. This document (packages, pipeline, definition of done)
2. The client's filled `config/clients/<slug>.yaml` — the single source of truth
3. The audit command (BEFORE/AFTER) — tells them what to fix and proves when done
4. Access: client adds our email as GBP **Manager** (never ownership); site-builder
   and directory logins via a shared password manager, never stored in the repo
5. Escalation: anything off-checklist (suspended GBP, domain dispute, bad-review
   cleanup) → Miles. Not in scope for a delegated job.

Quality bar for delegated work = the AFTER audit is green and both reports were sent.
Same standard the client sees, so incentives line up by construction.

## Why this scales to $5–20k/mo without killing you
- Finding leads: automated (`leadfinder`)
- Grading/proof: automated (`audit`)
- Site build: AI builder from a reusable template, config-swapped
- Retainer tracking: automated (`roster`)
- Your time: ~2–8 hrs/client to deliver, then ~15 min/mo per retainer
- Math to $10k/mo: e.g. **15 sites at avg $650 one-time + 15 retainers at ~$130/mo
  = ~$1,950 recurring**, so recurring alone won't hit $10k — the model is
  **one-time cash funds the month, retainers + package-2/3 expansion build the base.**
  Realistic $10k/mo mix: ~8 active retainers (~$1k) + 6–8 new builds/mo (~$4–5k) +
  2–3 AI-system clients (~$1.5k) + visibility fixes. Sell builds steadily, convert
  the best into retainers and AI systems.
