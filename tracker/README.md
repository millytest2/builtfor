# The tracker — set it up once, in about fifteen minutes

Three CSVs, three tabs, one sheet. This replaces the Flip Doc. Everything that
happens to a lead lives here and nowhere else.

## Setup

1. sheets.new → name it **BFMS Pipeline**
2. File → Import → Upload → `01_call_queue.csv` → **Insert new sheet** → rename tab
   **Call Queue**
3. Repeat for `02_pipeline.csv` (tab: **Pipeline**) and `03_clients.csv` (tab:
   **Clients**)
4. On each tab: select row 1 → View → Freeze → 1 row. Then Data → Create a filter.
5. Share it with Daniel as **Editor**. One sheet, two people, no copies.

## The four colour rules (Format → Conditional formatting, on Call Queue)

Apply to the whole sheet, `Custom formula is`:

| Formula | Colour | Means |
|---|---|---|
| `=$R1="SOLD"` | green | closed |
| `=$R1="BOOKED"` | blue | appointment set, this is the real scoreboard |
| `=$R1="DQ"` | grey | disqualified, stop spending time |
| `=$T1<TODAY()` | red | **you owe someone a follow-up and you're late** |

That last one is the whole point. The Flip Doc had Ryan sitting in blue for ten weeks
because nothing ever turned red.

## Status values (column R) — use these exactly

`NEW` → `NO-ANSWER` → `VM-LEFT` → `CONVO` → `BOOKED` → `MOCKUP-SENT` → `SOLD`
Dead ends: `DQ` (told you no, or booked solid), `BURNT` (asked not to be called again)

A lead moves to the Pipeline tab the moment it hits **BOOKED**. It moves to Clients
the moment it hits **SOLD**. Call Queue stays a dialling list, not a CRM.

## The five formulas worth having

Put these in a blank block to the right on Call Queue:

```
Dials this week      =COUNTIFS('Call Queue'!L:L,">="&TODAY()-7)
Conversations        =COUNTIF('Call Queue'!Q:Q,"CONVO")+COUNTIF('Call Queue'!R:R,"BOOKED")+COUNTIF('Call Queue'!R:R,"SOLD")
Times price was said =COUNTIF('Call Queue'!Q:Q,"Y")
Booked               =COUNTIF('Call Queue'!R:R,"BOOKED")
Follow-ups overdue   =COUNTIF('Call Queue'!T:T,"<"&TODAY())
```

On the Clients tab:
```
MRR                  =SUM(G:G)
Clients to $5k       =ROUNDUP((5000-SUM(G:G))/349,0)
```

**"Times price was said" is the one to watch.** All-time count as of 16 Sep 2026: one.

## Before you dial any row: the 10-second Google check

**This matters more than anything else on this page.** The `google_website_button`
column starts as `CHECK ON MAPS` for every cold row, and it is not optional.

Open the business on Google Maps. Look at the listing panel. Fill in:

| Value | What you saw | What to do |
|---|---|---|
| `NONE` | No Website button at all | **This is the lead.** Dial it. |
| `FREE` | Button points at wixsite.com, godaddysites.com, business.site, or a facebook.com URL | **Still a great lead.** Different opener: "your front door has Wix's name on it." |
| `REAL` | Points at their own domain, with real pages behind it | **Drop the row.** Move on. |

**Why you have to do this yourself:** the research that built this list could not reach
google.com, Google Maps, or Google Business Profile — they're blocked from that
environment. Every "no website" call in this file is inferred from a name search
returning only directory listings. The GBP Website button is a **different field** and
the two can disagree. You're looking at the real one; the list is looking at a proxy.

**The permanent fix is restoring the Google Places API key.** `websiteUri` in that API
*is* the GBP Website field. That's why it's the only instrument that answers this at
scale, and why every workaround stays a workaround.

## Working it

- Dial in row order. The list is already sorted: warm first, then verified cold by
  time zone so you can work Pacific to Eastern in one sitting.
- Fill `ring_test` before you dial. It takes ninety seconds and it writes your opener.
- Every row you touch gets a `next_step` and a `next_date`. No exceptions. A row with
  no next date is how Ryan got lost.
- Friday: read the overdue count. If it's not zero, that's Monday morning.
- Monthly: roll the totals into `docs/vertical_scoreboard.csv`.

## Refilling the queue

Run the search operators in `HANDOFF.md` §5, verify each (Google review count, then
open their actual site), and paste new rows at the bottom. About 1 in 3 businesses
will have a real gap, so expect to check ~60 names to add 20 rows.
