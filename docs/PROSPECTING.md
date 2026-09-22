# PROSPECTING — finding people to call

Two tools and one rule. The rule: **never dial a number you have not seen on
the business's own Google listing.** Scraped and searched data goes stale, and
calling the wrong shop burns the one thing you cannot rebuild.

---

## 1. The finder

`src/leadfinder/osm_find.py` pulls local trade businesses from OpenStreetMap.
No API key, no billing, no Google Places quota. It uses two free public
endpoints: Nominatim to turn a place name into a bounding box, Overpass to
query businesses inside it.

```bash
# everything drivable in the valley, default trades
python -m src.leadfinder.osm_find --where "San Fernando Valley, Los Angeles, CA"

# one town, one trade
python -m src.leadfinder.osm_find --where "Sun Valley, Los Angeles, CA" --trades metal,fence

# also return businesses that already HAVE a site (often the better lead:
# they already paid for one and got let down, so intent is proven)
python -m src.leadfinder.osm_find --where "Pacoima, CA" --include-with-website

# a box you drew yourself: south,west,north,east
python -m src.leadfinder.osm_find --bbox 34.15,-118.45,34.30,-118.25
```

Output lands in `output/prospects_<area>.csv` with businesses that have a phone,
sorted so the ones with no website come first.

**Why OpenStreetMap works for this.** OSM tags `phone` and `website` as separate
fields, so "has a phone, has no website" is a query rather than a guess. That is
the exact filter, available free, which the dead Google Places key was never
needed for.

**What it will not do.** OSM is volunteer-mapped and thinner than Google,
especially for one-truck operations. A missing `website` tag is not proof there
is no website. Treat every row as a lead to verify, never as a vetted prospect.
Data © OpenStreetMap contributors, ODbL.

Available trades: metal, fence, carpenter, electric, plumb, hvac, roof, paint,
stone, glass, landscape, pool, floor, builder, auto, studio.

## 2. The call sheet

The widget where the work actually happens. Import the CSV, then for each lead
it walks the Visibility Check and records the answer:

- **Step 1** links straight to their Google Maps listing and to the search a
  customer would run. You record whether the listing is claimed, where they
  land in results, review count and rating.
- **Step 2** gives you the exact question to ask, a copy button, and direct
  links into ChatGPT and Claude with it pre-filled. You record named or not
  named for each assistant.
- **Step 3** is a tap-to-call button, a status, and notes.

It scores each lead as you go and tells you whether it is worth calling.

Everything saves, so you can stop mid-list and come back. Export gives you a
scored CSV for a spreadsheet.

### How the score works

| Signal | Points | Why |
|---|---|---|
| No website | +30 | Nothing to find, and the core of the offer |
| Google listing unclaimed | +25 | Never set up, easiest possible win |
| Named by no assistant | +20 | The gap you are selling |
| Draws a blank when asked by name | +15 | They do not exist to the assistant at all |
| Named by some but not all | +8 | Partial, weaker pitch |
| Outside the top three on Google | +15 | Losing the search too |
| 10 to 49 reviews | +10 | Established and still hungry |
| 50 to 99 reviews | +4 | Busy |
| 100+ reviews | **−10** | At capacity, and has declined this pitch before |
| Rating 4.5 or better | +5 | Good at the work, worth helping |

55 or above is worth calling. The negative on 100+ reviews is deliberate: a
business with 150 five-star reviews and no website has had money and been
pitched a dozen times. They did not do it. That is a revealed preference, not a
gap.

## 3. The check asks two questions

Both go in the widget, and the second is the one that closes.

**Shopping question:** *"Who are the best [trade] in [town]?"* Missing means
losing strangers who are comparing.

**Name question:** *"What can you tell me about [business] in [town]?"* Record
the reply word for word. "I don't have information about that business" is the
most uncomfortable sentence an owner can read about their own shop, and it is
the line you read back to them on the call. It is not about rankings or
competitors. It says they do not exist as far as the thing answering is
concerned.

Drawing a blank on the name question adds 15 to the score on its own.

## 4. The starter list: 52 San Fernando Valley prospects

`output/prospects_san_fernando_valley.csv` holds 52 businesses, 51 with a phone
number, all drivable. Open the call sheet, hit **Import**, paste the file.

| | |
|---|---|
| Prospects | 52 |
| With a phone number | 51 |
| No own website found in search results | 48 |
| Already have a website | 4 |
| With a street address | 43 |

**Towns:** Sun Valley 13, Van Nuys 10, Pacoima 10, Reseda 5, North Hollywood 4,
Sylmar 3, Canoga Park 3, Northridge 2, Arleta 1.

**Trades:** auto body 6, welding 5, metal fabrication 4, auto glass 3, flooring
3, cabinetry 4, countertop fabrication 2, tree service 2, masonry 2, pool 2,
appliance repair 2, garage doors 2, upholstery 3, plus radiator, transmission,
nursery and ironwork.

Heavy on metal, auto and stone on purpose. Those shops sit in industrial pockets
of Sun Valley and Pacoima, do work worth real money, are owner-run, and almost
none of them have a website. They are also clustered, so you can knock on six
doors on Branford Street in one trip.

### What "verified" means here, exactly

**Verified:** the business name, phone and address appear in public listings
(Yelp, YellowPages, Nextdoor, TheBlueBook, HomeAdvisor), and a search for the
business surfaced no website of their own, only third-party directory pages.

That second part is the need signal and it is a real one. A business whose entire
web presence is other people's directories almost certainly has no site. It also
means that when a customer searches them, the top results are Yelp pages the
business does not control.

**Not verified, and you must check before dialling:**

- That the number still works and belongs to that business
- The state of their Google listing, claimed or not, filled in or not
- Whether any assistant names them

Those three are exactly what the call sheet walks you through, so the list is
built to be checked, not called cold off the page.

One flag carried in the notes: **Padilla's Masonry and Landscaping** appears on
one Yelp listing as CLOSED. Verify before spending a call on it.

The four with websites (Mission Iron Works, Custom Furniture by WM, Van Nuys
Auto Glass, Blumer Auto Center) are not mistakes. They are the better lead type:
intent already proven, and the question becomes whether the site they paid for
is actually getting read.

## 5. About emails

Asked for phone numbers and emails. Here is the honest result of looking.

**These businesses do not publish email addresses.** Searched the seeded iron
and gate shops across directories, review sites and business profiles: phone
numbers everywhere, emails nowhere. That is not a gap in the research, it is
what this market looks like. A one-truck operation that never built a website
also never set up a business inbox, and the owner's personal address is not
listed anywhere public.

So for this segment:

| Channel | Reality |
|---|---|
| **Phone** | The channel. Trades answer 6:30-8am and 4-6pm local. Midday they are on a job. |
| **Walk-in** | Second best. They get fifteen calls a day and roughly zero visits. |
| **Email** | Only available for businesses that already have a website with a contact form, which is the "bad website" lead type. Use it as a follow-up after a call, never as the opener. |

The finder does pull an email when OpenStreetMap has one tagged, and the call
sheet has a field for it, so when you do collect one on a call it has a home.
Do not build a plan around emails you do not have.

## 6. The order of work

1. Run the finder over one town you can drive to.
2. Import into the call sheet.
3. Run checks until you have ten scoring 55 or above. About twenty minutes each
   at first, faster once you have the rhythm.
4. Call those ten. Lead with what you found, never with the offer.
5. Log what happened in the notes. After thirty checks you will know which
   trade and which town converts, and that answer picks the niche for you
   rather than you guessing it upfront.
