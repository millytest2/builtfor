"""Website starter kit — one command turns a client (or just a lead's name) into:
  1. copy.md         — tailored site copy
  2. schema.json     — JSON-LD LocalBusiness + FAQPage (SEO/AEO/GEO backbone)
  3. build_brief.md  — paste-into-Emergent (or any AI builder) prompt
  4. mockup.html     — a real, sendable single-page mockup (the "quick example")

    # From just a lead (pre-sale mockup to text them):
    python -m src.website.build --business "Ace Fence Company, Muncie IN" --vertical fencing

    # From a signed client's config file:
    python -m src.website.build --client config/clients/ace_fence.yaml

Live Google data (address, phone, hours, rating) is pulled when GOOGLE_PLACES_API_KEY
is set; otherwise it falls back to whatever's in the client file / placeholders.
"""
import argparse
import json
import re
from pathlib import Path

import yaml

from ..shared.config import CONFIG_DIR, load_vertical
from . import content


def digits(s: str | None) -> str:
    return re.sub(r"\D", "", s or "")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (name or "site").lower()).strip("_")[:60]


def good_reviews(facts: dict) -> bool:
    """Only surface a Google rating when it actually helps the sell."""
    return bool(facts.get("rating") and facts["rating"] >= 4.0
                and (facts.get("review_count") or 0) >= 5)


def parse_address(addr: str | None) -> dict:
    parts = [p.strip() for p in (addr or "").split(",")]
    out = {"street": "", "city": "", "region": "", "postal": "", "full": addr or ""}
    if parts:
        out["street"] = parts[0]
    if len(parts) >= 3:
        out["city"] = parts[1]
        m = re.match(r"([A-Za-z]{2})\s*(\d{5})?", parts[2])
        if m:
            out["region"], out["postal"] = m.group(1).upper(), (m.group(2) or "")
    elif len(parts) == 2:
        out["city"] = parts[1]
    return out


def gather_facts(args) -> dict:
    """Assemble business facts from the client file + live Google data."""
    client = {}
    query = args.business
    vertical_name = args.vertical
    if args.client:
        client = yaml.safe_load(Path(args.client).read_text()) or {}
        biz = client.get("business", {}) or {}
        query = query or biz.get("google_query") or biz.get("name")
        vertical_name = vertical_name or biz.get("vertical")

    live = {}
    if not args.no_live:
        try:
            from ..audit import checks
            data = checks.collect(query)
            if data:
                live = data
        except Exception as e:  # missing key, network, no match — degrade gracefully
            print(f"  (live lookup skipped: {type(e).__name__})")

    biz = client.get("business", {}) or {}
    intake = client.get("intake", {}) or {}
    web = client.get("website", {}) or {}

    addr = parse_address(live.get("address") or intake.get("address"))
    name = live.get("name") or biz.get("name") or (query or "Your Business").split(",")[0]
    facts = {
        "name": name,
        "phone": live.get("phone") or biz.get("owner_phone") or "",
        "email": biz.get("owner_email", ""),
        "address": addr["full"],
        "street": addr["street"],
        "city": intake.get("service_area") or addr["city"] or "",
        "region": addr["region"],
        "postal": addr["postal"],
        "rating": live.get("rating"),
        "review_count": live.get("review_count") or 0,
        "domain": web.get("domain") or "",
        "services": intake.get("services_list") or [],
        "hours": intake.get("hours") or "",
    }
    facts["vertical_name"] = vertical_name or "generic"
    return facts


def build_schema(facts: dict, copy: dict) -> list:
    local = {
        "@context": "https://schema.org",
        "@type": copy["schema_type"],
        "name": facts["name"],
    }
    if facts["phone"]:
        local["telephone"] = facts["phone"]
    if facts["domain"]:
        local["url"] = facts["domain"] if facts["domain"].startswith("http") else f"https://{facts['domain']}"
    if facts["street"] or facts["city"]:
        local["address"] = {
            "@type": "PostalAddress",
            "streetAddress": facts["street"],
            "addressLocality": facts["city"],
            "addressRegion": facts["region"],
            "postalCode": facts["postal"],
            "addressCountry": "US",
        }
    if facts["city"]:
        local["areaServed"] = facts["city"]
    if good_reviews(facts):
        local["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": facts["rating"],
            "reviewCount": facts["review_count"],
        }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in copy["faqs"]
        ],
    }
    return [local, faq]


def render_copy_md(facts, copy) -> str:
    services = "\n".join(f"- {s}" for s in copy["services"])
    why = "\n".join(f"- {w}" for w in copy["why"])
    faqs = "\n\n".join(f"**{q}**\n\n{a}" for q, a in copy["faqs"])
    return f"""# Website copy — {facts['name']}

## Hero
**{copy['hero_headline']}**

{copy['hero_sub']}

Primary button: **{copy['primary_cta']}** → tel:{digits(facts['phone'])}
Secondary button: **{copy['secondary_cta']}**

## {copy['services_title']}
{services}

## {copy['why_title']}
{why}

## Reviews
{"Rated " + str(facts['rating']) + "★ from " + str(facts['review_count']) + " Google reviews." if good_reviews(facts) else "Reviews are thin/low right now — a great upsell (Full Visibility Fix). Leave space and fill in as they grow."}

## FAQ (also used for AEO/GEO structured data)
{faqs}

## Contact
{facts['name']}
{facts['address']}
Phone: {facts['phone']}
{("Web: " + facts['domain']) if facts['domain'] else ""}
"""


def render_build_brief(facts, copy, schema) -> str:
    services = ", ".join(copy["services"])
    return f"""# Build brief — {facts['name']}  (paste into Emergent / Webild / Replit)

Build a fast, mobile-first, high-converting **{copy['noun']}** website for a local
business. One page is fine to start; make it feel modern, trustworthy, and clean.

## Business facts
- Name: {facts['name']}
- Location / service area: {facts['city']} {facts['region']}
- Address: {facts['address']}
- Phone: {facts['phone']}  (every phone number must be a tap-to-call tel: link)
- Google rating: {facts['rating'] or "n/a"} from {facts['review_count']} reviews
- Domain: {facts['domain'] or "(to be connected)"}

## Sections (in order)
1. Sticky header: business name/logo + a prominent **{copy['primary_cta']}** call button
2. Hero: headline "{copy['hero_headline']}", subhead "{copy['hero_sub']}", two CTAs
   (call + {copy['secondary_cta'].lower()})
3. Services: {services}
4. Why choose us: {", ".join(copy['why'])}
5. Reviews: show the Google rating; leave room for pull-quotes
6. Service area + embedded map for {facts['city']}
7. Contact: tap-to-call, a short contact/quote form (name, phone, message), hours
8. Footer: name, address, phone (NAP must match Google exactly)

## Must-haves (SEO / AEO / GEO)
- Mobile-first, loads fast, HTTPS
- Tap-to-call on every phone number; a working contact/quote form
- Page <title> and meta description with "{copy['noun']}" + "{facts['city']}"
- Include this JSON-LD in the <head> (LocalBusiness + FAQPage — this is what gets you
  cited by Google AI Overviews, ChatGPT, and Perplexity):

```json
{json.dumps(schema, indent=2)}
```

- Add the FAQ section visibly on the page too (same Q&As as the schema).

## Style
Clean and confident. Big call button. Trustworthy local feel, not corporate.
Use real photos when the client provides them; tasteful stock until then.
"""


def render_mockup_html(facts, copy, schema) -> str:
    tel = digits(facts["phone"])
    services_html = "".join(
        f'<div class="svc"><h3>{s}</h3></div>' for s in copy["services"]
    )
    why_html = "".join(f"<li>{w}</li>" for w in copy["why"])
    faq_html = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in copy["faqs"]
    )
    rating_html = ""
    if good_reviews(facts):
        stars = "★" * int(round(facts["rating"]))
        rating_html = (f'<div class="rating"><span class="stars">{stars}</span> '
                       f'{facts["rating"]} · {facts["review_count"]} Google reviews</div>')
    call_btn = f'<a class="btn call" href="tel:{tel}">📞 {copy["primary_cta"]}</a>' if tel else ""

    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{facts['name']} — {copy['noun'].title()} in {facts['city']}</title>
<meta name="description" content="{copy['hero_sub']}">
<script type="application/ld+json">{json.dumps(schema)}</script>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  :root{{--ink:#16202b;--accent:#ff8f2b;--deep:#12324f}}
  body{{font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--ink);line-height:1.55}}
  a{{color:inherit;text-decoration:none}}
  .btn{{display:inline-block;font-weight:700;padding:14px 26px;border-radius:9px;font-size:16px}}
  .btn.call{{background:var(--accent);color:#12324f}}
  .btn.ghost{{border:2px solid #fff;color:#fff}}
  header{{position:sticky;top:0;background:#fff;box-shadow:0 1px 8px rgba(0,0,0,.08);
    display:flex;justify-content:space-between;align-items:center;padding:12px 20px;z-index:9}}
  header .name{{font-weight:800;font-size:18px}}
  header a.tel{{background:var(--accent);color:#12324f;font-weight:700;padding:9px 16px;border-radius:8px;font-size:14px}}
  .hero{{background:linear-gradient(135deg,#12324f,#1c4c74);color:#fff;text-align:center;padding:64px 20px}}
  .hero h1{{font-size:34px;max-width:640px;margin:0 auto 14px;line-height:1.15}}
  .hero p{{font-size:18px;color:#cfe0ee;max-width:560px;margin:0 auto 26px}}
  .hero .cta{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
  .rating{{margin-top:20px;color:#ffe3c2;font-size:15px}}.stars{{color:var(--accent);letter-spacing:2px}}
  section{{max-width:820px;margin:0 auto;padding:44px 20px}}
  h2{{font-size:24px;text-align:center;margin-bottom:22px}}
  .svcs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px}}
  .svc{{background:#f5f7f9;border-radius:10px;padding:20px;text-align:center}}
  .svc h3{{font-size:17px}}
  .why{{background:#f5f7f9}}
  .why ul{{list-style:none;max-width:520px;margin:0 auto;display:grid;gap:12px}}
  .why li{{padding-left:30px;position:relative;font-size:17px}}
  .why li:before{{content:"✓";position:absolute;left:0;color:#1a9850;font-weight:800}}
  details{{border-top:1px solid #e6ebee;padding:14px 0}}
  summary{{font-weight:600;cursor:pointer}}
  details p{{margin-top:8px;color:#4a5b6b}}
  .contact{{background:var(--deep);color:#fff;text-align:center}}
  .contact h2{{color:#fff}} .contact p{{color:#cfe0ee;margin-bottom:8px}}
  form{{max-width:420px;margin:20px auto 0;display:grid;gap:10px}}
  input,textarea{{padding:12px;border-radius:8px;border:none;font-size:15px;font-family:inherit}}
  .banner{{background:#fff3e6;color:#8a4b12;text-align:center;font-size:13px;padding:8px}}
  footer{{background:#0d2438;color:#8fa6ba;text-align:center;font-size:13px;padding:22px}}
  @media(max-width:600px){{.hero h1{{font-size:27px}}}}
</style></head><body>
<div class="banner">Sample mockup by Built for Main Street · {copy['noun'].title()} · not yet live</div>
<header>
  <div class="name">{facts['name']}</div>
  {f'<a class="tel" href="tel:{tel}">📞 Call</a>' if tel else ''}
</header>
<div class="hero">
  <h1>{copy['hero_headline']}</h1>
  <p>{copy['hero_sub']}</p>
  <div class="cta">
    {call_btn}
    <a class="btn ghost" href="#contact">{copy['secondary_cta']}</a>
  </div>
  {rating_html}
</div>
<section>
  <h2>{copy['services_title']}</h2>
  <div class="svcs">{services_html}</div>
</section>
<section class="why"><h2>{copy['why_title']}</h2><ul>{why_html}</ul></section>
<section><h2>Questions</h2>{faq_html}</section>
<section class="contact" id="contact">
  <h2>{copy['primary_cta']}</h2>
  <p>{facts['name']}</p>
  <p>{facts['address']}</p>
  {f'<p><a class="btn call" href="tel:{tel}">📞 {facts["phone"]}</a></p>' if tel else ''}
  <form onsubmit="alert('This is a mockup — the real form will email you.');return false">
    <input placeholder="Your name" required>
    <input placeholder="Your phone" required>
    <textarea placeholder="How can we help?" rows="3"></textarea>
    <button class="btn call" type="submit">Send</button>
  </form>
</section>
<footer>{facts['name']} · {facts['address']} · {facts['phone']}<br>
Mockup by Built for Main Street — builtformainstreet.com</footer>
</body></html>'''


def main(argv=None):
    ap = argparse.ArgumentParser(description="Generate a website starter kit for a business.")
    ap.add_argument("--business", help='Name + area, e.g. "Ace Fence, Muncie IN"')
    ap.add_argument("--client", help="Path to a config/clients/<slug>.yaml")
    ap.add_argument("--vertical", help="Vertical name (overrides client file)")
    ap.add_argument("--no-live", action="store_true", help="Skip the live Google lookup")
    ap.add_argument("--outdir", default=None)
    args = ap.parse_args(argv)

    if not args.business and not args.client:
        raise SystemExit("Provide --business \"Name, City ST\" or --client <file>.")

    print(f"Building website kit for: {args.business or args.client}")
    facts = gather_facts(args)

    display = facts["vertical_name"]
    try:
        display = load_vertical(facts["vertical_name"]).get("display_name", display)
    except Exception:
        pass
    copy = content.get_copy(facts["vertical_name"], display, facts)
    schema = build_schema(facts, copy)

    slug = slugify(facts["name"])
    outdir = Path(args.outdir or f"output/websites/{slug}")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "copy.md").write_text(render_copy_md(facts, copy))
    (outdir / "schema.json").write_text(json.dumps(schema, indent=2))
    (outdir / "build_brief.md").write_text(render_build_brief(facts, copy, schema))
    (outdir / "mockup.html").write_text(render_mockup_html(facts, copy, schema))

    print(f"\n{facts['name']}  ({display}, {facts['city'] or 'area unknown'})")
    if facts["rating"]:
        print(f"  Google: {facts['rating']}★ / {facts['review_count']} reviews")
    print(f"  Headline: {copy['hero_headline']}")
    print(f"\nKit -> {outdir}/")
    for f in ("mockup.html", "build_brief.md", "copy.md", "schema.json"):
        print(f"    {f}")
    print("\nText the mockup.html to the prospect. Paste build_brief.md into Emergent to build for real.")


if __name__ == "__main__":
    main()
