# The Service & How We Deliver It

## What the customer is actually buying (say it this way)
> **"When a local customer looks for you, they'll find you, trust what they see,
> and be able to reach you in one tap. We fix the gaps in days, and we prove it
> with a before/after report."**

Not "marketing." Not a retainer. A **fixed-scope repair job on their online
presence** — like a contractor, which is language these owners respect. The audit
report card *is* the scope: every red ✕ is a line item; delivery = turning them
green; the re-run audit = the receipt.

## The two packages

### Package A — Google Profile Rescue · $300–400 · 2 days
For businesses whose GBP is the problem (most restaurants/cafés, many barbershops).
1. Baseline audit (BEFORE snapshot — save the HTML + JSON)
2. Claim/verify the Google Business Profile if unclaimed
3. Complete every field: hours, phone, categories (primary + secondary), service
   list, attributes, business description (AI-drafted, owner-approved)
4. Photos: get 10–15 from the owner (or their Instagram/Facebook, with permission);
   AI-enhance if needed; upload with sensible names
5. Review system: generate their Google review link, print-ready QR card PDF,
   and a 2-line SMS template they send to past customers ("first push" = owner
   texts their last 20 happy customers, day one)
6. Seed 3–5 Q&A entries on the profile; publish 1 first post
7. AFTER snapshot: re-run audit → send before/after + the review kit

### Package B — Full Visibility Fix · $500–800 · 3–5 days
Everything in A, plus:
8. Listing consistency: correct name/address/phone/hours on the majors —
   Apple Maps, Bing Places, Yelp, Facebook, Nextdoor (manual; ~1 hr with logins)
9. One-page high-converting site or landing page (AI-built: Webild/Replit/Claude
   Code from a template) — tap-to-call, contact/booking form, hours, services,
   reviews embedded, photos. Connect their domain or provision one.
10. Basic local SEO on the page: title/meta, LocalBusiness schema, NAP match
11. AI-search visibility check: ask ChatGPT/Gemini/Google AI about the business
    before & after; the fixes above are what those engines read

**Upsell later, never bundled now:** review engine, missed-call text-back,
booking automation. That's the second sale, once trust exists.

## The delivery pipeline (every client, no exceptions)
| Day | Step | Tool |
|---|---|---|
| 0 | Sale on the phone → send intake form, collect 50% or full | script + payment link |
| 0 | Intake: GBP manager invite, photos, service list, hours | `config/clients/<name>.yaml` |
| 1 | BEFORE audit snapshot (save HTML + JSON) | `python -m src.audit.run --business "..." --json` |
| 1–2 | Work the checklist (A) / +3–5 (B) | checklist above |
| 2–5 | AFTER audit snapshot | same command |
| — | Send before/after report + review kit + invoice balance | email/SMS |
| +3 | Follow-up: "seen more calls yet?" → ask for a Google review + 1 referral | SMS |

**Definition of done (objective, non-negotiable):**
- GBP section grade **A** (≥90) in the AFTER audit
- 15+ photos live, hours set, description set, review link delivered
- Package B: Website section ≥ **B**, all listings matching, page live on their domain
- BEFORE and AFTER reports delivered to the client

## If you hand this to someone else (VA / Daniel / future hire)
This whole service is **a checklist + one command**, which means a careful
non-expert can run delivery end-to-end. The handoff kit is:

1. **This document** — the packages, pipeline, definition of done
2. **The intake config** — `config/clients/_template.yaml`, filled per client;
   it's the single source of truth for the engagement
3. **The audit tool** — they run BEFORE/AFTER; the report tells them what to fix
   and proves when they're done. They never need judgment about *what* to do,
   only execution of *how*.
4. **Access:** client adds `builtformainstreet@...` as GBP **Manager** (never
   owner-transfer); directory logins via the intake form; no client passwords
   stored anywhere except a shared password manager
5. **Escalation rule:** anything outside the checklist (suspended GBP, domain
   disputes, angry-review cleanup) goes to Miles — it's not in scope

**Quality bar for a delegated job:** the AFTER audit meets Definition of Done,
and the client got both reports. If the AFTER report isn't green, the job isn't
done — no exceptions, because the report is the product.

## Why this stays near-zero marginal cost
- Audit: automated (one command)
- Description/posts/Q&A/SMS templates: AI-drafted from the intake config
- Website: AI-built from a reusable template, config-swapped per client
- Human time per client: ~2–4 hrs (A) / ~4–8 hrs (B) — at $300–800 that's
  $75–150+/hr effective, and it drops as templates harden.
