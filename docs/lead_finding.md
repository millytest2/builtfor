# How to find leads (the repeatable way)

The wedge is **businesses with no website.** They're the easiest to find and the
easiest to pitch. Here's the whole loop — one command per batch.

## The 30-second version
```bash
export GOOGLE_PLACES_API_KEY=your_key

# 1) Pull a category across a batch of towns
python -m src.leadfinder.run --vertical barbershop --geo secondary_towns --source google_places --limit 120

# 2) Do that for a few categories, then merge into one ranked call-list,
#    keeping ONLY the no-website leads (your wedge):
python -m src.leadfinder.combine --min-score 50 --no-website-only

# -> output/master_call_list.csv  (sorted most-broken-first, with phone numbers)
```

## Why not just Google it yourself?
Because organic search only shows businesses that *already have websites* — the ones
who don't need you. The businesses you want live on the **Google Maps pin only**, and
the Places API is the one source that lists them *and* tells you definitively who has
no website (`websiteUri` is empty). Tested and confirmed — see `docs/targeting.md`.

## Where the supply comes from
- **Categories** (`config/verticals/`): barbershop, restaurant, cafe, septic, fencing,
  tree_service, equipment_repair, monument, hvac, plumbing. Add one by copying a yaml
  and changing `search_terms`.
- **Towns** (`config/geos/`): `secondary_towns.yaml` (batch 1) and
  `secondary_towns_2.yaml` (batch 2) — off-radar US markets the guru crowd ignores.
  Work a batch dry, then switch to the next. Add your own local metro anytime by
  copying a geo yaml and listing its cities under `areas:`.

At the "no website" filter the US is effectively unlimited. 10 categories × 40 towns is
thousands of qualified leads before you ever repeat.

## Working the list
1. Start at the top of `master_call_list.csv` (highest presence_score = most broken).
2. Skip rows with no phone (some cemeteries/holding listings).
3. Use script A in `outreach/cold_call_script.md` — every top row's problem is literally
   "no website," so the opener fits word-for-word.
4. When someone bites, run `python -m src.audit.run --business "Name, City ST"` and send
   the report — that's your proof and your close.

## Renewing / expanding supply
- New town batch: copy `secondary_towns_2.yaml`, swap in 20 new towns.
- New category: copy any vertical yaml.
- Your own backyard: make a geo yaml with your local city + suburbs under `areas:` and
  run any category against it — local jobs are the easiest first sales (in-person trust).

## Note on cost / limits
The finder caches every API response (`data/cache/`) and rate-limits itself, so re-runs
are free and you stay well inside Google's free tier at your volume.
