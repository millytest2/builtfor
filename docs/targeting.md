# Targeting strategy — the anti-guru, blue-ocean play

Geo: **United States, nationwide** — but deliberately *not* where the crowd is.
The whole edge is going where the YouTube/agency-guru herd isn't.

## The problem with the guru playbook
Every "make $10k/mo with local websites" guru teaches the same starter pack:
**HVAC, plumbing, roofing, dentists, med spas, chiropractors, real estate, gyms** —
in the **top 25 metros** (LA, NYC, Dallas, Houston, Phoenix, Miami, Atlanta, Austin…).

Result: those owners get 10+ identical cold calls a week. They're skeptical,
price-shopped, and burned out. You'd be competitor #11 saying the same script.

## Our edge: two axes the herd ignores

### Axis 1 — Category (unsexy, high-ticket, offline owner)
High job value + an owner who's 45–65 and not living on TikTok = high "no website" rate
and almost zero competing pitches:

- Septic / well & water systems / septic pumping
- Foundation repair & waterproofing, excavation / grading / land clearing
- Fencing, decks, gutters, chimney & masonry
- Tree service & stump removal
- Propane / fuel delivery, dumpster & portable-toilet rental, equipment rental
- Small-engine & equipment repair, machine shops, custom welding/fabrication
- Monument / headstone companies, funeral homes
- Farriers, large-animal vets, feed & farm supply
- Sign shops, upholstery, commercial/industrial cleaning, locksmiths

Avoid as *primary* targets (guru-saturated): HVAC, plumbing, roofing, dentists,
med spas, chiropractors, real estate, gyms, restaurants — *especially* in major metros.
(We keep hvac/plumbing configs around for flexibility, but they're not where we start.)

### Axis 2 — Geography (off the major-metro radar)
Secondary & tertiary markets: county seats and towns of **~10k–80k**, the kind that
sit an hour outside a metro. Heaviest opportunity in the **Midwest, South, Mountain West,
and rural-adjacent** areas. See `config/geos/secondary_towns.yaml` for a starter rotation.

## Why this works
- **Higher no-website rate** — these owners never got around to it.
- **High ticket** — $5k–$50k jobs, so a few extra calls a month easily covers your fee.
- **Almost no competing pitches** — the guru crowd only chases shiny metros/niches.
- **Trust fits us** — "me and my buddy Daniel, we're local-ish and real" lands far better
  with a 55-year-old septic owner than with a slick LA med-spa.

## The tactical insight (validated 2026-06, live search test)
Searching `septic / fence / monument` in small towns returned **only businesses that
already have websites** — because organic search *can't* surface the ones without sites.
The no-website businesses live on the **Google Maps pin + directory listings only**.

Therefore:
- **Web search ≠ lead source.** It finds the wrong half (the ones who don't need us).
- **Google Places (Maps) data IS the lead source.** It lists every business on the map
  regardless of website, and the `websiteUri` field tells us *definitively* who has none.
- Our `google_places` source already filters/scores exactly on this. It just needs a key.

## How we run it nationwide
Don't boil the ocean. Rotate **off-radar category × off-radar town**:
1. Pick 1–2 categories from Axis 1.
2. Pick a batch of towns from `secondary_towns.yaml` (or any list you want to work).
3. Run the lead-finder per (category × town); it dedupes, scores "most broken," and
   ranks. Work the high-priority "no website" rows first.
4. Move to the next batch of towns. The US is effectively unlimited supply at this filter.
