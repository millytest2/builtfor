# Focus: who we sell to, and why

The one-page answer. The models behind it are in `docs/niche_*.py` and
`docs/service_scorecard.py`. Rerun them when real call numbers replace the guesses.

## Update, October 4, 2026: what the deep check changed

A deep web search on Oct 1 found that most "no website" leads, tree crews above all,
had a real site the quick search missed. Of the first 100, 62 were parked. What is left
and what was added (97 leads on the call sheet):

| Group | Leads | Why they are on the list |
|---|---|---|
| Independent auto shops | 49 (#3, 22-38, 48-76, 81-82) | Owner at the counter, one repair pays the month, and most of the new ones have only a free page a directory made for them (edan.io). Easiest opener on the sheet |
| Tree crews | 33 | Still the best job size and the most search-driven need. Fewer layups than expected in LA, so many are out of state or have a free or broken page |
| Trades (upholstery, welding, masonry, concrete) | 14 (#77-78, 84-97) | Ruled out on interest Sept 28, pulled back Oct 1 because they pass the layup bar and owners answer their own phones. Called in the Central and Eastern slots |
| Pool | 1 (#39) | One-man route, answers his own phone |

The offer does not change by niche. Tree crews and auto shops stay first; trades fill
the out-of-state hours. Rerun this after 25 real conversations.

## Update, September 29, 2026: tree service first

Miles chose tree service crews as the niche to call first, LA area. Reasons: a tree
crew's phone is its lead line, one removal pays for months, and many already pay Angi,
HomeAdvisor or Thumbtack for leads. Auto repair is the runner-up and stays on the list.
**The offer is general**; the niche only decides who gets called first.

What the LA search showed: about 1 in 5 LA tree crews has no website (23 of about 120
checked). The no-website group is thinner in LA than in smaller cities, so plan on
adding crews whose site is broken or a free page. 30 tree leads are at the top of
`output/master_call_list.csv`: 23 LA area, 7 out of state.

Closed until 25 real owner conversations.

## The earlier decision (September 28, 2026)

Built for Main Street is the cash engine, not the identity. UPath is the mission.
So the niche is picked for speed to cash, owner reach, and leads already in hand.

**One niche for the coach: independent auto repair, San Fernando Valley first.** The
full reasoning, the offer and the scorecard are in `docs/PLAYBOOK.md`.

| # | Niche | Role | Usual tier | Channel |
|---|---|---|---|---|
| **1** | **Independent auto repair** | The niche. Owner at the counter, problem shown live on your phone, one brake job pays the month | Standard, $800 + $199 | Walk in to Valley shops 3:15 to 4:15pm and Saturday 9 to noon. Phone the rest. 23 checked leads in `output/leads_auto.csv`, 19 of them in the Valley |
| 2 | Tree service | Central and Eastern afternoons, when crews are off the job | Standard | Phone, 5 to 7pm their time. 8 checked leads in `output/leads_tree.csv` |
| 3 | Training studios, with recovery studios and physical therapy as referrals from them | Proof (client #1) and warm referrals | Small or Standard | Warm referrals first. 13 cold leads in `output/leads_training.csv`, best on Saturdays |
| 4 | Independent tutoring and test prep | Parked. Most independents already have a site | Standard | 6 checked leads in `output/leads_tutoring.csv` |

Why the switch from tree service to auto repair: the strict website check left 11 of
20 auto shops and 11 of 25 more Valley shops with no site. Every tree crew in Amarillo
and Lubbock now has one. Tree crews' best hours also fall during Miles's day job, while
Valley shops can be walked into after 3pm.

Locked September 28, 2026. Ruled out on interest: concrete, masonry, party rental,
mobile bartending, welding, upholstery. Do not reopen this list until 25 real
conversations are logged.

Lead files: all 48 clean leads in one dialing order in `output/master_call_list.csv` and on
the call sheet; clean leads per niche in `output/leads_*.csv`. Leads with a dead, rented
or doubtful site are in `output/leads_hooks_to_confirm.csv` (look at the Google
listing's Website button first). Leads with a real site are in
`output/leads_have_websites.csv` so they are never re-added. A name-only search missed
21 of 71 sites; always search the name plus "website".

The sections below are the history of how we got here.

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
