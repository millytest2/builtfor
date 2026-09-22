"""Client delivery pack — everything you have to write for one job, in one file.

The website builder handles the site's structure. This handles the half nobody
tooled: the Google Business Profile content, the intake you need from the owner,
and the monthly re-check. It emits a single markdown pack you work straight down.

    python -m src.delivery.pack --client config/clients/alpine.yaml
    python -m src.delivery.pack --new alpine          # writes a blank intake

Output -> output/delivery/<slug>/pack.md

Fields are pre-shaped to Google's real limits (750-char description, 10
services, 4 Q&A) so nothing gets written twice. Where copy is needed, the pack
carries the exact prompt to hand Claude, with the intake already filled in.
"""
import argparse
import pathlib
import sys
import textwrap

import yaml

TEMPLATE = {
    "business": "", "slug": "", "owner": "", "phone": "", "email": "",
    "address": "", "city": "", "state": "", "zip": "",
    "trade": "", "tier": 800,
    "primary_category": "", "extra_categories": [],
    "services": [], "towns": [], "years": "", "hours": "",
    "what_they_want_more_of": "", "what_makes_them_different": "",
    "review_count": "", "rating": "", "listing_claimed": "",
    "check_google_position": "", "check_chatgpt": "", "check_gemini": "",
    "check_claude": "", "check_name_reply": "",
}

def blank(slug):
    d = dict(TEMPLATE); d["slug"] = slug
    d["services"] = ["", "", ""]; d["towns"] = ["", ""]
    d["extra_categories"] = ["", ""]
    return d

def need(c, *keys):
    missing = [k for k in keys if not c.get(k)]
    return missing

def pack(c):
    biz   = c.get("business") or "[BUSINESS]"
    city  = c.get("city") or "[CITY]"
    st    = c.get("state") or ""
    trade = c.get("trade") or "[TRADE]"
    svcs  = [s for s in (c.get("services") or []) if s]
    towns = [t for t in (c.get("towns") or []) if t]
    tier  = c.get("tier", 800)
    place = f"{city}, {st}".strip(", ")
    O = []
    W = O.append

    W(f"# Delivery pack — {biz}\n")
    W(f"`{place}` · {trade} · **${tier}** + $79/mo · owner: {c.get('owner') or '?'} "
      f"· {c.get('phone') or '?'}\n")

    gaps = need(c, "business", "city", "trade", "phone")
    if gaps:
        W(f"> **Intake incomplete.** Missing: {', '.join(gaps)}. "
          f"Fill those in the client yaml and re-run.\n")

    W("---\n\n## 0 · Before anything, get these from the owner\n")
    W("Day one starts when the photos land, not when they pay. Chase this first.\n")
    for item in [
        "10-15 photos of finished work, straight off their phone, not staged",
        "Confirmed business hours, including which days they're closed",
        "The services they actually want more of (not everything they can do)",
        "Google account access, or a time to do the listing claim together",
        "Anything already in progress: a half-built site, a domain they bought",
    ]:
        W(f"- [ ] {item}")
    W("")

    W("---\n\n## 1 · Google Business Profile\n")
    W(f"**Primary category:** `{c.get('primary_category') or 'PICK ONE — the single closest match'}`  ")
    extra = [x for x in (c.get("extra_categories") or []) if x]
    W(f"**Additional:** {', '.join(f'`{x}`' for x in extra) if extra else '_pick 2-4, no more_'}\n")

    W("### Description — 750 characters max, write it as the owner would talk\n")
    W("```text")
    W(textwrap.fill(
        f"{biz} has been doing {trade} in {place} "
        f"{'for ' + str(c.get('years')) + ' years' if c.get('years') else ''}. "
        f"{c.get('what_makes_them_different') or '[WHAT MAKES THEM DIFFERENT — one plain sentence]'} "
        f"We handle {', '.join(svcs[:4]) if svcs else '[SERVICES]'}"
        f"{' and serve ' + ', '.join(towns[:4]) if towns else ''}. "
        f"Call {c.get('phone') or '[PHONE]'} and you'll get a person.", 92))
    W("```")
    W("_Trim to 750. No keyword stuffing — Google reads it and so do the assistants._\n")

    W("### Services — up to 10, each with its own description\n")
    if svcs:
        for s_ in svcs[:10]:
            W(f"**{s_}**  ")
            W(f"`[1-2 sentences: what it is, who it's for, roughly what it runs. "
              f"Name {city} at least once across the set, not in every one.]`\n")
    else:
        W("_No services in the intake. Get 5-8 from the owner before writing this._\n")

    W("### Q&A — seed 4, answer them yourself from the owner's account\n")
    qs = [
        f"Do you serve {towns[0] if towns else city}?",
        f"How much does {svcs[0].lower() if svcs else '[main service]'} usually run?",
        "How soon can you come out?",
        "Are you licensed and insured?",
    ]
    for q in qs:
        W(f"- **{q}**  ")
        W(f"  `[answer in the owner's voice, 2-3 sentences, no marketing language]`")
    W("")

    W("### Opening post\n```text")
    W(textwrap.fill(f"[One recent job, 2-3 sentences, with a photo. What it was, where, "
                    f"what was tricky. No offers, no hashtags.]", 92))
    W("```\n")

    W("---\n\n## 2 · Website pages to build\n")
    W("| Page | Purpose | Must name |")
    W("|---|---|---|")
    W(f"| Home | Who they are, what they do, one tap to call | {trade}, {city} |")
    for s_ in svcs[:8]:
        W(f"| {s_} | The one job someone searched for | {s_}, {city} |")
    for t in towns[:6]:
        W(f"| {trade} in {t} | Catch the town-specific search | {trade}, {t} |")
    W("| About | Years, people, why they're different | owner name, years |")
    W("| Contact | Phone, hours, address, map | phone, hours |")
    W("")
    if tier >= 1000:
        W("_$1,000 tier: build every service and town page above._\n")
    elif tier >= 800:
        W("_$800 tier: home, contact, about, plus the top 3-4 service pages. "
          "Add towns only where they actually work._\n")
    else:
        W("_$500 tier: home, contact, about, one combined services page. "
          "No listing work in this tier._\n")

    W("---\n\n## 3 · Hand this to Claude\n")
    W("Paste the block below. It has the intake already in it.\n")
    W("```")
    W(f"Write website copy for {biz}, a {trade} business in {place}.")
    W(f"Owner: {c.get('owner') or '[owner]'}. {c.get('years') or '[?]'} years in business.")
    W(f"Services: {', '.join(svcs) if svcs else '[services]'}.")
    W(f"Towns served: {', '.join(towns) if towns else '[towns]'}.")
    W(f"What they want more of: {c.get('what_they_want_more_of') or '[?]'}.")
    W(f"What makes them different: {c.get('what_makes_them_different') or '[?]'}.")
    W(f"Reviews: {c.get('review_count') or '?'} at {c.get('rating') or '?'} stars.")
    W("")
    W("Write: a home page, one page per service above, one page per town above,")
    W("an about page, and 6 FAQ pairs. Plain language a tradesperson would use")
    W("out loud. No marketing voice, no 'unlock', no 'elevate', no em dashes.")
    W("Each page names the service and the town naturally, once or twice, never")
    W("stuffed. Include a JSON-LD LocalBusiness + Service + FAQPage block.")
    W("```\n")

    W("---\n\n## 4 · Ship checklist\n")
    for item in [
        "Listing claimed and verified (start this day one, the postcard is slow)",
        "Hours, categories, service areas, services, photos all filled in",
        "Website linked on the listing",
        "Name, address and phone identical on site, listing and anywhere else listed",
        "JSON-LD validates (Google Rich Results test)",
        "Loads under 2s on a phone, tap-to-call works",
        "Domain registered in THEIR business name",
        "Hosting billing set to $79/mo, first charge dated",
        "Re-check booked for day 45",
    ]:
        W(f"- [ ] {item}")
    W("")

    W("---\n\n## 5 · The day-45 re-check\n")
    W("Same searches as the original check. This is the retention mechanism, so "
      "send it even when the numbers are flat.\n")
    W("| | At sale | Day 45 |")
    W("|---|---|---|")
    W(f"| Google position | {c.get('check_google_position') or '—'} | |")
    W(f"| ChatGPT names them | {c.get('check_chatgpt') or '—'} | |")
    W(f"| Gemini names them | {c.get('check_gemini') or '—'} | |")
    W(f"| Claude names them | {c.get('check_claude') or '—'} | |")
    W(f"| Asked by name | {c.get('check_name_reply') or '—'} | |")
    W("")
    W("> Log every row in the master sheet across all clients too. After thirty "
      "businesses that dataset is worth more than the retainers.\n")
    return "\n".join(O)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--client", help="path to a client yaml")
    g.add_argument("--new", metavar="SLUG", help="write a blank intake and exit")
    args = ap.parse_args()

    if args.new:
        p = pathlib.Path(f"config/clients/{args.new}.yaml")
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.exists():
            sys.exit(f"{p} already exists.")
        p.write_text(yaml.safe_dump(blank(args.new), sort_keys=False, allow_unicode=True))
        print(f"-> {p}\nFill it in, then: python -m src.delivery.pack --client {p}")
        return

    cp = pathlib.Path(args.client)
    if not cp.exists():
        sys.exit(f"No such file: {cp}")
    c = yaml.safe_load(cp.read_text()) or {}
    slug = c.get("slug") or cp.stem
    out = pathlib.Path(f"output/delivery/{slug}/pack.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(pack(c))
    print(f"-> {out}")
    gaps = need(c, "business", "city", "trade", "phone")
    if gaps:
        print(f"   heads up, intake missing: {', '.join(gaps)}")


if __name__ == "__main__":
    main()
