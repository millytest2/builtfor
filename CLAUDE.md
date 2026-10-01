# Built for Main Street

Sole proprietorship, Miles Tipton, Los Angeles. LLC filed on or after December 17
(the 15-day rule; filing earlier costs an extra $800). Target $10k/mo.

## What this business sells

> Built for Main Street helps local businesses get found, get contacted, and
> stop losing good leads.

Three steps, and we fix the one that is broken: (1) they cannot be found (Google
listing, what AI assistants know), (2) they have no website or it does not work,
(3) the people who find them slip away (follow-up, reviews; monthly, and later
tools behind the counter). Never open with "we build websites."

**Visibility Check** is free, and it is the door.

Setup is tiered. **Miles picks the tier before call two** from what he saw (crew
size, services, how far they travel), using the triggers below as his guide. The
owner is never asked to count anything; they hear one number, once, and it does
not move. This is scoping, not discounting.

| Tier | Trigger | Setup | Monthly | What the monthly adds |
|---|---|---|---|---|
| Small | ≤4 services, ≤3 towns, one location | **$600** | **$99** | Hosting, reasonable edits, Google listing kept current, a visibility check every quarter |
| Standard | ≤8 services, ≤6 towns | **$800** | **$199** | Small, plus a monthly report (search and ChatGPT, Gemini, Claude), review requests by counter QR card and email, review reply drafts the owner approves |
| Bigger | 9+ services, 7+ towns, or two locations | **$1,000** | **$300** | Standard, plus every lead routed to the owner and staff by email with a same-day follow-up draft, past-customer emails, a 15-minute monthly call |

Every tier gets the same build: a page per service and per town, the Google
listing claimed and completed, tap to call, a tested quote form, and the markup
search engines and AI assistants read.

**Never quote a range.** A range becomes its floor: say "$600 to $1,000" and the
client hears $600. Name one number for the tier they land in.

**Push Standard.** Two Small clients earn less a month than one Standard client
and take twice the work. Small exists for the one-truck owner who would otherwise
say no. The setup fee covers the build in every tier, so an early cancellation
does not lose money on the work.

Cancel with 30 days' notice. Buyout of the site at $2,000 after 12 months.
**We own the site; the client owns the domain.**

## Hard rules

- **No AI receptionists, no chatbots, nothing that replaces labour.** Enhance the
  business, do not replace the people in it.
- **No social media management, no ads, no SEO retainer, no "AI consulting."**
  Naming what we do not do is the fastest way to stop sounding like every other
  agency calling these businesses.
- **Nothing that sends an SMS before client #10.** TCPA is $500-1,500 per message
  uncapped, consent cannot be shared across brands since January 2026, and
  carriers block unregistered A2P 10DLC traffic outright.
- **Never promise rankings, leads or revenue.** Promise findable and reachable,
  and measure both.
- **Never re-measure rankings on day one.** They have not moved. Saying so is
  what makes the month-three number believable.
- **Never build on spec.** Money and photos first, then the two-week clock starts.
  The one exception is a **free one-page preview** used to sell: the homepage only,
  from public info, no photos taken from their listings, shared by private link and
  never on their domain. Say "I put one together" only when it exists.
- **Phone:** until Google Voice or a paid business line works, Miles calls from his
  cell by choice. His cell number never goes in emails or anything written;
  emails sign off with hello@ only.
- **Business money moves through the business account.** Never personal Venmo,
  Zelle or Cash App.
- **Edits are "reasonable", never "unlimited".** Text, photos, hours, prices,
  service details. Not new pages, not redesigns. Client-facing copy must match
  the agreement, because the client will quote whichever is more generous.
- **Photos have a deadline too.** 30 days from payment, or the build ships with
  what was supplied. Our 14-day clock cannot start on a date the client controls
  indefinitely.

## Where the work lives

| | |
|---|---|
| `docs/START_HERE.md` | every deliverable and link in one place, plus next steps |
| `docs/PLAYBOOK.md` | the whole business on one page: niche, offer, how it connects, path to $10k, scorecard |
| `docs/FOCUS.md` | who we call first and why: tree service crews, LA area (auto repair is the runner-up; pool service added Oct 1 as the third). The offer itself is general: any local small business |
| `docs/OFFER.md` | the offer, pricing reasoning, objection handling |
| `docs/BEFORE_AFTER.md` | the measurement spec, both halves |
| `docs/DELIVERY.md` | how a job gets done, and the two commands |
| `docs/SCRIPT.md` | call script |
| `site/launch.html` | the open-for-business checklist, tonight to the December LLC (published with saved ticks) |
| `output/master_call_list.csv` | 100 to call, 68 in California and 32 across the US: 1-30 tree crews with no website (23 LA area, 7 out of state), 31-50 auto shops, 51-69 tree crews whose site has a problem you can show (#3 Granada too; #63 James Luker OKC is on a free builder address), 70 Tree Rite Arborists, 71 Ahles Automotive (talked), 72-80 LA-area tree crews, 81-82 tree crews in FL and OK, 83-92 LA pool companies, 93-98 pool companies in NV, TX and FL, 99-100 tree crews in OH and SC. Talked: #3 Granada, #20 Menos, #71 Ahles. Weak leads swapped out Oct 1 are in `output/leads_parked.csv`. Owner, email, opener, your-time call window, status. Simple copy: `output/call_list_simple.csv`. All on the call sheet |
| `site/intake.html` | client intake sheet, one per signed client (published: https://claude.ai/artifact/S36dxQUuipm27aXPGoBvvP, db collection `intake`). The intake skill reads it |
| `src/build_site.py` | 11 pages + JSON-LD from one client JSON |
| `clients/_example.json` | the client data shape |

## House style for anything client-facing

Plain words an owner in their fifties reads without effort. No marketing
adjectives, no "leverage", no "solutions", no em dashes. Every claim carries a
screenshot or a number behind it. Short sentences.
