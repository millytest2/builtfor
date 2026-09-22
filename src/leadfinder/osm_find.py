"""Find local-trade prospects with a phone and no website, from OpenStreetMap.

No API key. No billing. Uses two free public endpoints:
  Nominatim  - turns a place name into a bounding box
  Overpass   - queries OSM for businesses inside that box

OSM tags `website` and `phone` separately, which is exactly the filter we need:
a business with a phone and no website is a prospect, by definition.

  python -m src.leadfinder.osm_find --where "Sun Valley, Los Angeles, CA"
  python -m src.leadfinder.osm_find --where "San Fernando Valley, CA" --trades metal,fence
  python -m src.leadfinder.osm_find --bbox 34.15,-118.45,34.30,-118.25 --include-with-website

Output -> output/prospects_<slug>.csv, ready to paste into the call sheet.

Coverage caveat: OSM is volunteer-mapped, so it is thinner than Google and
skews toward businesses someone bothered to add. Treat a hit as a lead to
verify, never as gospel. Every row still needs eyes on the Google listing
before you dial. Data (c) OpenStreetMap contributors, ODbL.
"""
import argparse
import csv
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "BuiltForMainStreet/1.0 (prospect research; hello@builtformainstreet.com)"
NOMINATIM = "https://nominatim.openstreetmap.org/search"
OVERPASS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.osm.ch/api/interpreter",
]

# OSM craft/shop/office values worth calling: one job is worth real money and
# the owner typically still answers the phone.
TRADE_TAGS = {
    "metal":     ["craft=metal_construction", "craft=blacksmith", "craft=welder"],
    "fence":     ["craft=fence", "shop=fencing"],
    "carpenter": ["craft=carpenter", "craft=cabinet_maker", "craft=joiner"],
    "electric":  ["craft=electrician"],
    "plumb":     ["craft=plumber"],
    "hvac":      ["craft=hvac"],
    "roof":      ["craft=roofer"],
    "paint":     ["craft=painter"],
    "stone":     ["craft=stonemason", "craft=tiler"],
    "glass":     ["craft=glaziery", "craft=window_construction"],
    "landscape": ["craft=gardener", "shop=garden_centre", "landuse=plant_nursery"],
    "pool":      ["craft=pool_maintenance"],
    "floor":     ["craft=floorer", "craft=parquet_layer"],
    "builder":   ["craft=builder", "craft=scaffolder", "craft=insulation"],
    "auto":      ["shop=car_repair", "shop=tyres", "shop=car_parts"],
    "studio":    ["shop=hairdresser", "leisure=fitness_centre", "shop=beauty"],
}
DEFAULT_TRADES = ["metal", "fence", "carpenter", "roof", "stone",
                  "glass", "landscape", "pool", "builder", "hvac"]


def _get(url, data=None, tries=3):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                url,
                data=urllib.parse.urlencode(data).encode() if data else None,
                headers={"User-Agent": UA, "Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read())
        except Exception as exc:                      # noqa: BLE001
            if attempt == tries - 1:
                raise
            wait = 2 ** (attempt + 1)
            print(f"  retry in {wait}s ({type(exc).__name__})", file=sys.stderr)
            time.sleep(wait)
    return None


def bbox_for(place):
    """Nominatim: place name -> (south, west, north, east)."""
    res = _get(f"{NOMINATIM}?" + urllib.parse.urlencode(
        {"q": place, "format": "json", "limit": 1}))
    if not res:
        sys.exit(f"Nominatim found nothing for {place!r}. Try a bigger area, "
                 f"or pass --bbox south,west,north,east yourself.")
    bb = res[0]["boundingbox"]                        # [south, north, west, east]
    return float(bb[0]), float(bb[2]), float(bb[1]), float(bb[3])


def build_query(bbox, trades):
    south, west, north, east = bbox
    box = f"({south},{west},{north},{east})"
    clauses = []
    for trade in trades:
        for tag in TRADE_TAGS.get(trade, []):
            key, _, val = tag.partition("=")
            clauses.append(f'  nwr["{key}"="{val}"]{box};')
    return "[out:json][timeout:180];\n(\n" + "\n".join(clauses) + "\n);\nout center tags;\n"


def fetch(query):
    last = None
    for endpoint in OVERPASS:
        try:
            print(f"  querying {urllib.parse.urlparse(endpoint).netloc} ...", file=sys.stderr)
            return _get(endpoint, {"data": query}, tries=2).get("elements", [])
        except Exception as exc:                      # noqa: BLE001
            last = exc
            print(f"  {type(exc).__name__}, trying next mirror", file=sys.stderr)
    sys.exit(f"Every Overpass mirror failed. Last error: {last}")


def tidy_phone(raw):
    if not raw:
        return ""
    digits = re.sub(r"\D", "", raw.split(";")[0])
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) != 10:
        return raw.split(";")[0].strip()
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def to_rows(elements, include_with_website):
    rows, seen = [], set()
    for el in elements:
        t = el.get("tags", {})
        name = (t.get("name") or "").strip()
        if not name:
            continue
        phone = tidy_phone(t.get("phone") or t.get("contact:phone") or "")
        site = (t.get("website") or t.get("contact:website") or t.get("url") or "").strip()
        if not phone:
            continue
        if site and not include_with_website:
            continue
        key = (name.lower(), re.sub(r"\D", "", phone))
        if key in seen:
            continue
        seen.add(key)

        street = " ".join(x for x in (t.get("addr:housenumber"), t.get("addr:street")) if x)
        trade = t.get("craft") or t.get("shop") or t.get("office") or t.get("landuse") or ""
        rows.append({
            "business": name,
            "trade": trade.replace("_", " "),
            "phone": phone,
            "city": t.get("addr:city", ""),
            "street": street,
            "website": site,
            "has_website": "yes" if site else "NO",
            "email": t.get("email") or t.get("contact:email") or "",
            "osm": f"https://www.openstreetmap.org/{el['type']}/{el['id']}",
            "maps": "https://www.google.com/maps/search/" + urllib.parse.quote(
                f"{name} {t.get('addr:city','')} CA"),
            # you fill these in while running the Visibility Check
            "gbp_claimed": "", "reviews": "", "rating": "",
            "google_position": "", "chatgpt": "", "gemini": "", "claude": "",
            "status": "new", "notes": "",
        })
    # no website first, then the ones with a site to audit
    rows.sort(key=lambda r: (r["has_website"] != "NO", r["business"].lower()))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--where", help='place name, e.g. "Sun Valley, Los Angeles, CA"')
    g.add_argument("--bbox", help="south,west,north,east")
    ap.add_argument("--trades", default=",".join(DEFAULT_TRADES),
                    help=f"comma list. available: {','.join(TRADE_TAGS)}")
    ap.add_argument("--include-with-website", action="store_true",
                    help="also return businesses that already have a site "
                         "(these are often the better leads: intent is proven)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.bbox:
        bbox = tuple(float(x) for x in args.bbox.split(","))
        label = "bbox"
    else:
        print(f"Looking up {args.where} ...", file=sys.stderr)
        bbox = bbox_for(args.where)
        label = args.where
        time.sleep(1)                                  # Nominatim asks for 1 req/sec

    trades = [t.strip() for t in args.trades.split(",") if t.strip()]
    unknown = [t for t in trades if t not in TRADE_TAGS]
    if unknown:
        sys.exit(f"Unknown trade(s): {', '.join(unknown)}. Available: {', '.join(TRADE_TAGS)}")

    print(f"Box: {bbox}\nTrades: {', '.join(trades)}", file=sys.stderr)
    rows = to_rows(fetch(build_query(bbox, trades)), args.include_with_website)

    slug = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")[:40] or "area"
    out = pathlib.Path(args.out or f"output/prospects_{slug}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with out.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    no_site = sum(1 for r in rows if r["has_website"] == "NO")
    print(f"\n{len(rows)} prospects with a phone ({no_site} with no website)")
    print(f"-> {out}")
    print("\nData (c) OpenStreetMap contributors, ODbL. Verify each on Google "
          "Maps before dialling: OSM can be stale, and a missing website tag is "
          "not proof there is no website.")
    for r in rows[:12]:
        print(f"  {r['business'][:34]:36} {r['phone']:16} {r['trade'][:18]:20} {r['city']}")


if __name__ == "__main__":
    main()
