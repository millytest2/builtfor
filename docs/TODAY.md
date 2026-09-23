# Formation day — the exact sequence

You've decided on the LLC. Here's the cheapest secure path, in order, with the
real URLs and the real numbers. Total cash today: **$90 plus a domain.**

**One line on state:** file in the state you live and work in. If that's
California, file in California. Wyoming and Nevada do not avoid the $800 —
you'd register there *and* as a foreign LLC in California, paying both plus a
registered agent. If you are genuinely relocating within a few months, wait
and file where you land.

---

## Before you file — 15 minutes

### Name availability

Search the California business database:
**bizfileonline.sos.ca.gov/search/business**

Search `Built for Main Street` with no suffix. You're looking for anything
confusingly similar, not just exact matches. Rules that matter:

- The name must end in **LLC**, **L.L.C.**, or **Limited Liability Company**
- It cannot imply a bank, trust, or insurer
- California no longer does name reservations through a separate process for
  most filers — if it's clear, file the same day rather than sitting on it

### Domain — buy it before you file

I checked the DNS: **builtformainstreet.com** has no records, which usually
means it's unregistered. DNS absence isn't proof (a parked domain can have no
records), so confirm at checkout. `.net`, `.co`, and `mainstreetfound.com`
also look clear as backups.

Buy it at **Cloudflare Registrar** — sold at wholesale cost, about $10–11/yr
for `.com`, with free WHOIS privacy. Namecheap and Porkbun are fine too.
**Avoid GoDaddy** — the first year is cheap and the renewal is triple.

Register it in the **company's name** once the LLC exists. Today, register it
in yours and update the contact after; Section 6.3 of the operating agreement
assigns it to the company either way.

> Buy the domain first. If the name is taken as a domain you may want a
> different business name, and it's much cheaper to learn that before filing.

---

## Step 1 — File the LLC · $70 · ~20 minutes

**bizfileonline.sos.ca.gov** → Business Filings → Limited Liability Company →
Articles of Organization (**Form LLC-1**).

What it asks, and what to put:

| Field | Your answer |
|---|---|
| LLC name | `Built for Main Street LLC` |
| Business address | Your street address (no PO box) |
| Mailing address | Same, or a PO box if you prefer |
| Agent for service of process | See below |
| Management | **One Manager** is wrong — choose **All LLC Member(s)** |
| Purpose | California pre-fills this statutory sentence. Leave it. |
| Signature | Type your name as organizer |

**Do not pay for expedited processing.** Standard online filing is currently
clearing in about 1–3 business days. Expedite exists for people closing on
property, not for you. Note that California's queue stretches badly in
December — irrelevant today, relevant if you ever refile.

### The registered agent decision

| Option | Cost | Tradeoff |
|---|---|---|
| **Yourself** | $0 | Your home street address goes on the permanent public record, searchable by anyone. You must be there during business hours to receive service. |
| **Agent service** | $50–150/yr | Their address is public instead of yours. Mail is scanned to you. |

**Recommendation: use a service, ~$125/yr.** Two reasons specific to you.
First, the moat — your coach's whole point about privacy is undercut if your
home address is one search away from your business name. Second, you've moved
several times; an agent address doesn't change when you do, and a registered
agent address change is a filing every time.

Northwest Registered Agent (~$125/yr) is the usual pick and doesn't upsell.
If cash is genuinely tight today, be your own agent and switch later — it's a
$0 amendment in California.

**After filing:** you get a confirmation email. When it's approved you get
back the **stamped Articles of Organization with your entity number**. Save
that PDF. The bank wants it.

---

## Step 2 — Sign the operating agreement · $0 · 20 minutes

It's written: **`docs/legal/OPERATING_AGREEMENT.md`**

Fill every `[BRACKET]`, print or e-sign, date it. Nobody files this — you keep
it. Formation services charge $200–500 for this document.

You can do this today while the filing is pending, except for the entity
number and filing date in Section 1.1 — fill those in when approval lands.

**Read Section 4 twice.** That's the section that does the actual protecting.
Commingling is how single-member LLCs lose their shield, and it never happens
on purpose — it happens because one client Venmo'd you personally.

---

## Step 3 — EIN · **free** · 15 minutes · *after approval*

**irs.gov/ein** — Monday–Friday, 7am–10pm Eastern. Free. Instant.

**Wait for state approval.** Applying before the LLC exists creates an EIN
attached to an entity that doesn't, and unwinding that is a phone call to the
IRS you don't want.

| Question | Answer |
|---|---|
| Entity type | **Limited Liability Company** — not Sole Proprietor |
| Number of members | 1 |
| State where organized | California |
| Reason for applying | Started a new business |
| Principal activity | Other → `Website design and hosting services` |

At the end you get the **CP 575 confirmation letter** on screen. **Download the
PDF immediately.** The IRS issues CP 575 exactly once — a replacement (Letter
147C) means calling and waiting on hold. Save it in three places.

**Never pay for an EIN.** Any site charging $50–300 is filling in this same
free form.

---

## Step 4 — Bank account · $0 · 30 minutes · *after EIN*

**Novo**, **Mercury** or **Relay**. All free, all open online, no minimum.

Have ready:
- Stamped Articles of Organization (PDF)
- EIN letter, CP 575 (PDF)
- Signed operating agreement (PDF)
- Driver's license
- The business address you filed

**The same day the account opens:** transfer your initial capital contribution
from personal to business — whatever number you wrote in Section 2.2 of the
operating agreement, even $100 — and label the transfer
`initial capital contribution`. That single transaction is a documented fact
that the entity was funded, and it takes ten seconds.

### The rule that makes the $890 worth spending

**Every dollar of business money in and out of this account. No exceptions.**

- Client pays you → this account. Never personal Venmo, Zelle or Cash App.
- Domain, hosting, GHL, software → this card.
- You need money → transfer to personal and call it a distribution. Don't buy
  groceries on the business card and plan to sort it out later.

An LLC that's used like a personal account is an LLC a court can look straight
through. The paperwork doesn't protect you. The discipline does.

---

## Step 5 — Stripe · $0 · 15 minutes

Once the bank account exists: **stripe.com** → business type LLC → EIN →
connect the Novo account.

Build two things now so you're not scrambling on the first close:

1. **Payment link, $1,000** — "Build & fix." Text it on the second call.
2. **Subscription product, $199/mo** — so it bills itself. Chasing a tree
   service for a check every month will eat the margin this model exists for.

Add the **$1,990 annual** option as a second price on the same product.

---

## What you'll have spent

| | |
|---|---|
| LLC filing (Form LLC-1) | $70 |
| Domain, first year | ~$11 |
| Registered agent | $0 or ~$125/yr |
| Operating agreement | $0 |
| EIN | $0 |
| Bank account | $0 |
| Stripe | $0 until you're paid |
| **Today** | **~$81, or ~$206 with an agent** |

## Then, on the calendar

Put these in now, today, while you're thinking about it:

| When | What | Cost | Miss it and |
|---|---|---|---|
| **Within 90 days of approval** | Statement of Information, **Form LLC-12** | $20 | $250 penalty |
| **15th day of the 4th month** after formation | Franchise tax, **FTB Form 3522** | $800 | Penalties and interest |
| Every 2 years | Statement of Information again | $20 | $250 penalty |
| Annually | FTB Form 568 with your return | — | — |

The $800 is the one people forget because it arrives before any revenue does.
Set the reminder today.

## Explicitly not today

- **S-Corp election.** It's an IRS filing (Form 2553), not a state one, and it
  costs $1,000–2,000/yr in payroll and an 1120-S before it saves anything.
  It's worth it above roughly $50k of net profit. Your coach is right that it
  shouldn't slow the LLC down — it also shouldn't happen yet. Revisit it with
  a CPA the January after you clear that number; it can be made retroactive.
- **Go High Level.** $97/mo buys you nothing at zero clients. The call sheet
  handles the first ten.
- **Business insurance.** $300–600/yr, worth it around client five.

## The one thing that isn't on your coach's list

**Your client agreement.** You're leasing an asset you own — that's a
different contract from a normal build-and-hand-over, and it's the document
that decides what happens when a client stops paying and wants the site.

The LLC protects your personal assets. The client agreement protects the
business model. Say the word and I'll write it: scope, the $1,000 and $199
terms, who owns what, the 30-day cancel, the $2,000 buyout, and a liability
cap at fees paid.
