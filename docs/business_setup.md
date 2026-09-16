# Making it legit — the setup checklist

Everything here is a one-time task. Total cost to be fully legitimate is roughly
**$700–1,500 in year one**, most of it California's franchise tax. Total time is about
a weekend.

**This is a practical checklist assembled from standard small-business practice, not
legal or tax advice.** Three things below are genuinely worth paying a professional
for, and they're marked. Everything else you can do yourself in an afternoon.

---

## 0. Read this first: the Social Hog conflict

You currently work at Social Hog doing local marketing and Google Business Profile
work, and BFMS sells local marketing and Google Business Profile work. Before this has
real revenue, pull your employment agreement and look for three things:

1. **Non-compete.** California generally does not enforce these (Bus. & Prof. Code
   §16600), and since 2024 California employers have had to notify employees that such
   clauses are void. So this is probably the least of the three.
2. **Non-solicitation.** Different animal. Do not approach Social Hog's clients,
   prospects, or lead lists. Not one. Every lead in this repo was sourced
   independently and that needs to stay true.
3. **IP assignment / invention clauses.** Many employment agreements claim work
   product created during employment. Build BFMS on your own time, own equipment, own
   accounts. Never on their laptop, their hours, or their tools.

None of that is a reason to stop. It is a reason to keep the two completely separate
and to have read the document rather than assumed.

---

## 1. Entity — pick one of two shapes, this week

### Recommended for now: single-member LLC owned by Miles, Daniel paid as a contractor

Simpler in every way that matters at $0 MRR: one Schedule C instead of a partnership
return, one $800 franchise tax, one bank account, and no dissolution mess if Daniel's
involvement changes. Daniel gets a **written revenue-share agreement** (a percentage of
collected revenue, paid monthly on an invoice) and a 1099-NEC at year end.

**The tradeoff, stated plainly:** Daniel owns nothing. If the deal you two actually
shook on is 50/50 ownership, don't paper it as a contractor arrangement to save
paperwork. Do the multi-member version below instead.

### If Daniel is a true 50/50 owner: multi-member LLC

Same formation, but it files **Form 1065** and issues **K-1s**, which means a CPA every
year (~$600–1,200). And it needs a real **operating agreement** — see §5.

### California formation steps

| Step | Where | Cost | Time |
|---|---|---|---|
| Articles of Organization (Form LLC-1) | bizfileOnline.sos.ca.gov | $70 | 20 min |
| Statement of Information (LLC-12) | same, **within 90 days**, then every 2 years | $20 | 10 min |
| EIN | irs.gov, apply online, free — **never pay a service for this** | $0 | 10 min |
| Annual franchise tax | FTB, **$800/yr minimum**, due the 15th day of the 4th month | $800 | — |
| City business license | your city's finance dept (LA: Business Tax Registration Certificate) | varies | 30 min |
| Fictitious Business Name (DBA) | **only if** the LLC isn't named "Built for Main Street" — county clerk, and California requires newspaper publication | ~$50–100 | 1 hr |

⚠️ **The $800 is the one that surprises people.** It is owed whether or not you make
money. A first-year exemption existed for LLCs formed in 2021–2023; confirm the current
rule before you assume it applies to you.

---

## 2. Bank and books

- **Separate business checking account.** Do this the day the EIN arrives. Mercury,
  Novo and Bluevine are free and open online; your existing bank works too.
- **Never** run a client payment through a personal account. Commingling is the single
  fastest way to lose the liability protection you just paid $70 and $800 for, and it
  is the thing that most damages a sale price later.
- **Bookkeeping:** Wave is free and enough at this size. Move to QuickBooks or Xero at
  ~15 clients. Categorise weekly, not annually.
- **Set aside 30% of profit for taxes** in a second account. You are self-employed now
  and nobody is withholding anything for you.
- Quarterly estimated taxes (federal 1040-ES and CA 540-ES) once you're profitable.

---

## 3. Payments — Stripe, three links, twenty minutes

Create three **Payment Links** (Stripe dashboard → Payment links → New):

| Link name | Type | Amount | Notes |
|---|---|---|---|
| `Growth Plan — Setup` | One-time | **$400** | Sent at the sale |
| `Growth Plan — Care` | Recurring monthly | **$349/mo** | Set a **30-day free trial** — that *is* "first month included" |
| `Website Only` | One-time | **$600** | The deliberately worse option |

Settings to turn on once:
- **Collect customer name, email, phone** on every link
- **Automatic receipts** (Settings → Emails)
- **Smart retries and dunning** (Settings → Revenue recovery) — this is how you stop
  losing MRR to expired cards, and it is free
- **Card updater** (on by default on most accounts, confirm it)
- Turn on **Apple Pay / Google Pay** — trades owners buy from a phone in a truck

**Fees: 2.9% + $0.30 per charge.** So $400 nets ~$388 and $349/mo nets ~$338.
Price with that in mind; don't discount on top of it.

**The mechanic on a call:** they say yes, you text the setup link while still on the
phone, and you start the subscription link at launch so the trial clock begins when
the site goes live. **Card on file from day one, every client, no exceptions.** A buyer
of this business is buying that card file, not your charm.

---

## 4. Insurance — do it before the first stranger pays

| Cover | Why | Rough cost |
|---|---|---|
| **General liability** | Commercial clients and any chamber/BNI will ask for a certificate of insurance before they refer you | $350–600/yr |
| **Professional liability (E&O)** | The one that actually matters for this work. Covers "the site went down and I lost jobs" and "you used a photo I didn't own" | $400–800/yr |

Hiscox, Next and Thimble all quote and bind online in about fifteen minutes. Get both;
they're usually bundled. **And never use a photo you didn't take or license** — stock
photo demand letters are a real and common way small web shops lose $2,000.

---

## 5. The paperwork that actually matters

In order of how much pain it saves you:

1. **Miles ↔ Daniel agreement** — drafts in `legal/`. The split, who owns the client
   relationships, what happens to the accounts if one of you stops, who decides what.
   **Write this while you still like each other.** Every partnership horror story is
   two friends who never wrote it down.
2. **Client service agreement** — `legal/client_agreement.md`. One page. Scope, what
   the monthly includes, cancel-any-time, who owns the domain and the site, payment
   terms.
3. **Contractor agreement** — `legal/contractor_agreement.md`. Needed *before* you hire
   the site builder at client 6. Without a work-for-hire and IP assignment clause, your
   contractor owns the code you just sold to a client.
4. **W-9 from anyone you pay**, before the first payment. **1099-NEC** in January to
   anyone paid $600+ in the year, Daniel included if he's a contractor.

### Worth paying a professional for (about $800–1,500 total, once)

- **A lawyer, one hour, to read the client agreement and the Miles/Daniel agreement.**
  ~$300–500. The templates in `legal/` are a starting draft written to be
  lawyer-reviewed, not lawyer-replacing.
- **A CPA, one hour, before year end.** Entity election, quarterly estimates, and
  whether an S-corp election makes sense (usually only above ~$50k of profit).
- **Confirm sales tax treatment.** California generally doesn't tax services, and a
  site delivered electronically is generally not taxable, but "generally" is doing work
  in that sentence. Ask the CPA once and be done.

---

## 6. Accounts to open in the company's name, not yours

This is the difference between a business you can sell and a job you can't leave.

- [ ] Domain registrar (Cloudflare or Porkbun) — **client domains registered to the
      client, with you as technical contact.** Never hold a client's domain hostage;
      it's also the promise that closes deals.
- [ ] Hosting (Cloudflare Pages or Netlify), company account
- [ ] Twilio (tracking numbers + missed-call text-back)
- [ ] Google Workspace on builtformainstreet.com — `hello@`, not a personal Gmail
- [ ] Stripe, company account
- [ ] A shared password manager (1Password or Bitwarden) — client logins live there,
      never in this repo, never in a text thread

**Rule: you are a Manager on a client's Google Business Profile, never the Owner.**
Taking ownership of someone's GBP is how you become the villain in their story.

---

## The order to do it in

**Weekend 1:** LLC filing, EIN, bank account, Stripe links. You can sell legally on
Monday.
**Weekend 2:** Insurance, client agreement, Miles/Daniel agreement, password manager.
**Before client 6:** contractor agreement, W-9s.
**Before year end:** the CPA hour.

Do not wait for any of this to make calls. **You can call tomorrow and paper it before
anyone pays.** The only thing that must exist before you take money is the Stripe link
and the client agreement.
