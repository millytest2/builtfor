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

## 4. The list: 86 prospects

`output/prospects_all.csv`. Open the call sheet, hit **Import**, paste the file.
(`prospects_san_fernando_valley.csv` is the LA-only subset if you want to work
that alone first.)

| | |
|---|---|
| Prospects | 86 |
| With a phone number | 85 |
| No own website found in search results | 78 |
| Los Angeles, drivable | 52 |
| National, phone only | 34 |

**LA metros:** Sun Valley 13, Van Nuys 10, Pacoima 10, Reseda 5, North Hollywood
4, Sylmar 3, Canoga Park 3, Northridge 2, Arleta 1.

**National metros:** Fort Wayne IN 7, Toledo OH 6, Lubbock TX 6, Knoxville TN 4,
Chattanooga TN 4, Tulsa OK 3, Wichita KS 2, Dayton OH 1, Springfield MO 1.

**Trades:** auto body 20, welding 9, metal fabrication 9, upholstery 4, sheet
metal 3, countertops 3, auto glass 3, flooring 3, cabinetry 4, tree 2, masonry
2, pool 2, appliance 2, garage doors 2, plus ironwork, radiator, transmission
and nursery.

### Why the split, and how to use it

**The 52 in LA are the ones that matter first.** You can drive to them, walk in
with the check on your phone, and collect a referral from the shop next door.
Thirteen are in Sun Valley alone, four auto body shops sit on the same block of
Branford Street. The first closes should come from here, because showing up
converts and a stranger on the phone does not, yet.

**The 34 national ones are dial volume**, and they exist because the offer is
100% deliverable remotely. Nothing in the build requires being there. What you
lose is the walk-in, the referral density and the local story, which is exactly
why they are second, not first.

Use them once the pitch is proven: after ten LA checks and five LA calls you
will know what lands, and then national is just more reps of a thing that works.
Calling Lubbock before you have said the pitch out loud ten times wastes the
one resource you cannot rebuild, which is your own conviction on the phone.

### What "verified" means here, exactly

**Verified:** the business name, phone and address appear in public listings
(Yelp, YellowPages, Nextdoor, TheBlueBook, HomeAdvisor), and a search for the
business surfaced no website of their own, only third-party directory pages.

That second part is the need signal and it is real. **78 of 86 show it.** A
business whose entire web presence is other people's directories almost
certainly has no site. It also means that when a customer searches them, the top
result is a Yelp page the business does not control and cannot fix.

**Not verified, and you check before dialling:**

- That the number still works and belongs to that business
- The state of their Google listing, claimed or not, filled in or not
- Whether any assistant names them

Those three are exactly what the call sheet walks you through, so the list is
built to be checked rather than called cold off the page.

**Flags carried in the notes:** Padilla's Masonry appears as CLOSED on one Yelp
listing. Special Touch Upholstery had a listed domain that looked mismatched.

The eight with websites are not mistakes. They are the better lead type: intent
already proven, and the question becomes whether the site they paid for is
getting read.

### A finding about national search

Searching nationally for "businesses with no website" mostly surfaces businesses
that **do** have websites, because search ranks sites and a shop with no site is
invisible to it. Broad queries returned SEO-optimised companies every time.

What works is querying a specific metro and trade the way a customer would, so
directory aggregators surface the small shops. That pattern produced every row
here. Use it if you expand further, or run the OSM finder, which filters on the
website tag directly and does not care about ranking.

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
