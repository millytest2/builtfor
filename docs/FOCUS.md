# Focus: who we sell to, and why

The one-page answer. The models behind it are in `docs/niche_*.py` and
`docs/service_scorecard.py`. Rerun them when real call numbers replace the guesses.

## The decision (September 28, 2026)

Built for Main Street is the cash engine, not the identity. UPath is the mission.
So the niche is picked for speed to cash, owner reach, and leads already in hand.

| # | Niche | Role | Usual tier | Channel |
|---|---|---|---|---|
| **1** | **Tree service** (owner-operated, no website) | Cash now. The one niche for the coach. | Standard, $800 + $199 | Cold call, 7 to 8am or 4 to 6pm their time. 20 verified leads in `output/tree_service_20.csv` |
| 2 | Independent auto repair and transmission | Steady buyers with lots of services | Bigger, $1,000 + $300 | Walk in locally, 10 to 11:30am. Phone elsewhere. 20 verified leads in `output/auto_repair_20.csv` |
| 3 | Training studios and sports performance, with recovery studios and physical therapy as referrals from them | Proof (client #1) and the world Miles lives in | Small or Standard | Warm referrals first. Ask every client for two intros. 20 cold leads in `output/training_studios_20.csv` |
| 4 | Independent tutoring and test prep | Education and careers, which feeds UPath | Standard | Email first, then morning calls, once mornings are free. 11 verified leads in `output/tutoring_11.csv` (about 1 in 5 independents has no site) |

Locked September 28, 2026. Ruled out on interest: concrete, masonry, party rental,
mobile bartending, welding, upholstery. Do not reopen this list until 25 real
conversations are logged.

**One niche for the coach: tree service.** The other four are where you go next or
work in parallel through a different channel, not a second pitch on the same day.

The sections below are the history of how we got here. The auto repair pick they
describe is superseded.

## Why auto repair

It is the only business type that came out on top in every test we ran:

| Test | Auto repair |
|---|---|
| Fundamentals (afford, reach, supply, pitch pressure, fit, retention, gap) | #1 of 60 |
| Random weights, 10,000 runs | Top 5 in 100% |
| Scores off by a point anywhere | Top 5 in 95% |
| Worst case, after fixes | #1 in 100% |
| Fit with the services owners value most | #1 (93) |
| Easy to sell, obvious need, will Miles understand it | #1 (87, tied) |
| All 11 criteria, 33 business types, 20,000 runs | #1 in 92%, top 5 in 100% |

In plain words:

- **The owner is at the counter all day.** You can walk in, and they pick up.
- **They can afford it.** One brake job or one collision repair pays the month.
- **The need is obvious.** "Who's an honest mechanic near me?" is one of the most asked local questions, to Google and to ChatGPT.
- **Customers come back for years,** so reviews and being found keep paying. That keeps the $199 alive.
- **Lots of them.** Every town has several. Filtering for the ones with a weak site still leaves plenty.
- **You already know the customer.** Every driver knows the fear of being ripped off. That fear is the pitch.
- **It is Main Street.** A storefront on the corner.

## Why not the others

| Group | Why it loses to auto repair |
|---|---|
| **Party / equipment rental** (close #2) | Seasonal, owners ask for Instagram, some are side hustles. Wins on insider knowledge (events), so it is the second list, not the first. |
| **Showrooms** (flooring, windows, countertops) | Good buyers, but few per town, and many flooring stores are buying-group dealers with a corporate site. Far from Miles's life. |
| **Field trades** (concrete, tree, fencing, welding) | The owner is on a job all day. Reach fails, and reach decides how many conversations happen. |
| **Cleaning and route services** (pool, window cleaning, pressure washing, gutters, detailing, junk removal) | Mostly solo operators with small jobs, so $1,000 plus $199 feels big. In the field all day. Many are side hustles that quit, and pressure washers and window cleaners are coached by YouTube marketers, so they build their own sites and hear agency pitches constantly. Best of the group is **mobile mechanic** (74), which is just auto repair without the counter. |
| **Restaurants, bars, gyms** | Miles knows them best, but they want social media, which we do not sell, and many already have sites or close. |
| **HVAC, plumbing, roofing** | Every agency is already calling them. |

## What we sell them

The website is the vehicle, not the headline. What owners value most, in order:

1. Their own AI visibility check, then a monthly AI report
2. A monthly report showing they are found and reachable
3. Review requests at the counter (QR card and email; ask everyone, no rewards, no texts)
4. Google listing claimed and cleaned up
5. Review reply drafts the owner approves

Never sold: chatbots, AI receptionists, texts before client #10, social media, ads, SEO retainers, logos.

**Pending decision:** add review requests, review reply drafts and listing upkeep to the $199 upkeep, and make and model pages to auto builds. Prices do not change. Nothing in the offer, agreement or site changes until this is approved.

## The math to $10k a month

About 30 clients on upkeep at $199 is roughly $6,000. Four new builds a month at $1,000 adds $4,000. That is one new shop a week.

## How it runs

| | Auto shops | Party rental |
|---|---|---|
| **Best time** | 10 to 11:30am, 1:30 to 3:30pm. Never at drop-off or pickup. | Evenings, when they prep orders |
| **How** | Walk in. Ask for the owner by name (state repair license lookup, signed review replies). | Phone, then visit the warehouse |
| **Opener** | "Who's an honest mechanic in [town]?" asked to ChatGPT, on your phone, in front of them | "Party rentals in [town]?" the same way |
| **Filter** | No site, a supplier template, a rented page, or a broken one | A real address, 3+ years, 50+ reviews |
| **Rule** | One shop per trade per town | Same |

## What would change this

The whole ranking rests on one guess: how many auto shops have a site we can beat.
Check 90 shops across three towns. Thirty percent or more with no site, a rented site
or a broken one: auto repair stays first. Under fifteen percent: party rental leads.

After 25 real conversations per list, replace the judgment scores in the models with
what actually happened, and rerun.

## Review: party rental vs auto shops (difficulty pass)

Party rental scored higher when Miles's edge (events, bartending) was weighted up.
The difficulty pass reversed it. The rule that settles it:

> **Choose the niche whose hard part is a skill, not a structure.**

| | Hard part | Kind | Gets easier with reps? |
|---|---|---|---|
| Auto repair, transmission | Getting past the counter, sounding credible | Skill | Yes, within 20 conversations |
| Party rental | Seasonal cash, rental-software sites, side hustles, Instagram asks | Structure | No |
| Mobile bartending | Small budgets, short-lived businesses | Structure | No |

Money per 100 dials (assumed rates, in `docs/niche_difficulty.py`): auto walk-in
about $6,400, transmission about $4,000, party rental about $3,100. Worst case,
same order.

**Practice plan before selling to auto shops:** 5 conversations with mobile
bartending owners (peers, low stakes), then 5 no-pitch talks with auto shop owners
("what is your biggest headache right now?") to learn whether their pain is
customers or technicians. Then sell.

## Evidence check (September 28, 2026)

What outside sources say about the assumptions behind the auto repair pick.

| Assumption | Verdict | Evidence |
|---|---|---|
| Auto shops feel customer pain, not only hiring pain | **Holds, stronger than assumed** | Transactions at independent shops fell 9.6% from Jan 2025 to Jan 2026, while they gained share from dealers on price. Tech shortage is cited by 31% of shops, parts prices by 46%. |
| People ask AI which local business to use | **Holds** | 45% of US consumers used AI for local recommendations in the past year, up from 6%; ChatGPT alone 31% (BrightLocal Local Consumer Review Survey 2026, 1,002 adults). Not broken out for auto repair. |
| Plenty of shops | **Holds** | Roughly 227,000 to 253,000 US auto repair shops, about three quarters single-owner. |
| Customers trust independents | **Holds** | Consumer Reports members rate independent shops highest for satisfaction and price. |
| Few agencies target auto shops | **Wrong** | Auto-specific platforms exist and partner with parts suppliers and shop networks (KUKUI with AutoZone and ACA; NAPA AutoCare). KUKUI is reported at $500 to $2,000+ a month. Established shops may already have a decent site. |
| Owner names from the California repair license lookup | **Unverified** | The BAR locator confirms a license. Owner names not confirmed. Use signed review replies, or ask. |
| Party rental sites come from rental software | **Holds** | Goodshuffle sells a website add-on ($79/mo); InflatableOffice sells site packages from $499. |
| How many auto shops have a site we can beat | **Still unknown** | No study found. Measure it: check 90 shops, and note any "Powered by KUKUI" or network template in the footer. |

**What changes:** the filter. Skip shops already on an auto marketing platform. Target shops with no site, a rented page, or a supplier template, and use the price contrast: $199 a month, no contract, against platforms reported at $500 and up.
