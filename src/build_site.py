#!/usr/bin/env python3
"""
Render a complete client site from one JSON file.

    python3 src/build_site.py clients/jims-upholstery.json

Writes dist/<slug>/ — index.html, a page per service, a page per town.

The point of this file: the JSON-LD below is what makes an assistant able to
name the business. It has to be correct and identical on every site we ship.
That is exactly the part an AI site builder gets wrong or skips, so it lives
here in code and never in a prompt.
"""
import json, os, re, sys, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = open(os.path.join(ROOT, "templates", "base.html")).read()

DAYMAP = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday",
          "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}


def e(s):
    return html.escape(str(s), quote=True)


def digits(p):
    return "+1" + re.sub(r"\D", "", p)[-10:]


# ---------------------------------------------------------------- structured data

def opening_hours(c):
    """Schema.org openingHoursSpecification. Assistants read this to answer
    'are they open now' — one of the most common local questions there is."""
    out = []
    for day, h in c["hours"].items():
        if h.lower() == "closed":
            continue
        opens, closes = h.split("-")
        out.append({"@type": "OpeningHoursSpecification",
                    "dayOfWeek": f"https://schema.org/{DAYMAP[day]}",
                    "opens": opens.strip(), "closes": closes.strip()})
    return out


def local_business(c, url):
    d = {
        "@type": "LocalBusiness",
        "@id": f"{url}#business",
        "name": c["biz"],
        "url": url,
        "telephone": c["phone"],
        "description": c["about"],
        "address": {"@type": "PostalAddress", "streetAddress": c["street"],
                    "addressLocality": c["city"], "addressRegion": c["state"],
                    "postalCode": c["zip"], "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": t["name"]} for t in c["towns"]],
        "openingHoursSpecification": opening_hours(c),
    }
    if c.get("lat") and c.get("lon"):
        d["geo"] = {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lon"]}
    if c.get("email"):
        d["email"] = c["email"]
    if c.get("founded"):
        d["foundingDate"] = c["founded"]
    if c.get("reviews"):
        scores = [r["stars"] for r in c["reviews"]]
        d["aggregateRating"] = {"@type": "AggregateRating",
                                "ratingValue": round(sum(scores) / len(scores), 1),
                                "reviewCount": len(scores)}
        d["review"] = [{"@type": "Review",
                        "reviewRating": {"@type": "Rating", "ratingValue": r["stars"]},
                        "author": {"@type": "Person", "name": r["by"]},
                        "reviewBody": r["text"]} for r in c["reviews"]]
    d["hasOfferCatalog"] = {
        "@type": "OfferCatalog", "name": f'{c["biz"]} services',
        "itemListElement": [{"@type": "Offer",
                             "itemOffered": {"@type": "Service", "name": s["name"],
                                             "description": s["short"]}}
                            for s in c["services"]]}
    return d


def faq_block(pairs):
    if not pairs:
        return None
    return {"@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in pairs]}


def service_block(c, s, url, base):
    return {"@type": "Service", "name": s["name"], "description": s["body"],
            "serviceType": s["name"], "url": url,
            "provider": {"@id": f"{base}#business"},
            "areaServed": [{"@type": "City", "name": t["name"]} for t in c["towns"]]}


def jsonld(graph):
    body = json.dumps({"@context": "https://schema.org", "@graph": graph},
                      indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{body}\n</script>'


# ---------------------------------------------------------------- page assembly

def shell(c, *, title, desc, canonical, body, graph, depth):
    root = "../" * depth or "./"
    nav = "".join(f'<a href="{root}{h}">{e(l)}</a>'
                  for l, h in [("Services", "#services"), ("Areas", "#areas"),
                               ("Reviews", "#reviews"), ("Contact", "#contact")])
    addr = f'{e(c["street"])}<br>{e(c["city"])}, {e(c["state"])} {e(c["zip"])}<br>'
    hours = "<br>".join(f'{d} {h}' for d, h in c["hours"].items())
    serving = "Serving " + ", ".join(t["name"] for t in c["towns"])
    rep = {
        "TITLE": e(title), "META_DESC": e(desc), "CANONICAL": e(canonical),
        "BRAND": c.get("brand_color", "#1f4e79"), "BIZ": e(c["biz"]),
        "PHONE": e(c["phone"]), "PHONE_RAW": digits(c["phone"]),
        "CALLBAR": e(c.get("callbar", "Free estimates")), "ROOT": root,
        "NAV": nav, "BODY": body, "JSONLD": jsonld(graph),
        "ADDRESS_HTML": addr, "HOURS_HTML": hours,
        "SERVING": e(serving), "YEAR": str(date.today().year),
    }
    out = TPL
    for k, v in rep.items():
        out = out.replace("{{" + k + "}}", v)
    return out


def faq_html(pairs):
    if not pairs:
        return ""
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>"
                    for q, a in pairs)
    return f'<section id="faq"><div class="wrap"><h2>Questions we get asked</h2>{items}</div></section>'


def build_home(c, base):
    s_cards = "".join(
        f'<a class="card" href="services/{s["slug"]}.html"><h3>{e(s["name"])}</h3>'
        f'<p>{e(s["short"])}{" From " + e(s["price_from"]) + "." if s.get("price_from") else ""}</p></a>'
        for s in c["services"])
    t_links = "".join(f'<a href="areas/{t["slug"]}.html">{e(t["name"])}</a>' for t in c["towns"])
    revs = "".join(
        f'<div class="review"><div class="stars">{"★" * r["stars"]}</div>'
        f'<p>{e(r["text"])}</p><cite>{e(r["by"])} · {e(r["src"])}</cite></div>'
        for r in c.get("reviews", []))
    pics = "".join(f'<img src="{e(p["src"])}" alt="{e(p["alt"])}" loading="lazy" width="800" height="600">'
                   for p in c.get("photos", []))
    body = f"""
<section class="hero" style="border-top:none"><div class="wrap">
  <h1>{e(c["tagline"])}</h1>
  <p class="lede">{e(c["lede"])}</p>
  <div class="cta">
    <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
    <a class="btn ghost" href="#services">See what we do</a>
  </div>
  <div class="trust">
    <span>★ {len(c.get("reviews", []))} reviews</span>
    <span>In business since {e(c.get("founded", ""))}</span>
    <span>Free estimates</span>
  </div>
</div></section>

<section id="services"><div class="wrap">
  <h2>What we do</h2><p class="sub">{e(c["about"])}</p>
  <div class="grid">{s_cards}</div>
</div></section>

{f'<section id="work"><div class="wrap"><h2>Recent work</h2><div class="gallery">{pics}</div></div></section>' if pics else ''}

{f'<section id="reviews"><div class="wrap"><h2>What customers say</h2><div class="reviews">{revs}</div></div></section>' if revs else ''}

<section id="areas"><div class="wrap">
  <h2>Where we work</h2>
  <p class="sub">Based in {e(c["city"])}, serving the surrounding area.</p>
  <div class="towns">{t_links}</div>
</div></section>

{faq_html(c.get("faqs"))}

<section id="contact"><div class="wrap"><div class="band">
  <h2>Get a free estimate</h2>
  <p class="sub" style="margin:0 auto 18px">Call and tell us what you've got. We'll give you a firm price.</p>
  <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
</div></div></section>
"""
    graph = [local_business(c, base)]
    if c.get("faqs"):
        graph.append(faq_block(c["faqs"]))
    return shell(c, title=f'{c["biz"]} | {c["trade"].title()} in {c["city"]}, {c["state"]}',
                 desc=c["lede"][:155], canonical=base, body=body, graph=graph, depth=0)


def build_service(c, s, base):
    url = f'{base}services/{s["slug"]}.html'
    t_links = "".join(f'<a href="../areas/{t["slug"]}.html">{e(t["name"])}</a>' for t in c["towns"])
    body = f"""
<section class="hero" style="border-top:none"><div class="wrap">
  <h1>{e(s["name"])} in {e(c["city"])}, {e(c["state"])}</h1>
  <p class="lede">{e(s["body"])}</p>
  <div class="cta">
    <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
    <a class="btn ghost" href="../">All services</a>
  </div>
  {f'<div class="trust"><span>From {e(s["price_from"])}</span><span>Free estimates</span></div>' if s.get("price_from") else ''}
</div></section>

{faq_html(s.get("faqs"))}

<section><div class="wrap">
  <h2>Areas we cover</h2><div class="towns">{t_links}</div>
</div></section>

<section><div class="wrap"><div class="band">
  <h2>Get a price on your {e(s["name"].lower())}</h2>
  <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
</div></div></section>
"""
    graph = [local_business(c, base), service_block(c, s, url, base)]
    if s.get("faqs"):
        graph.append(faq_block(s["faqs"]))
    return shell(c, title=f'{s["name"]} in {c["city"]}, {c["state"]} | {c["biz"]}',
                 desc=s["body"][:155], canonical=url, body=body, graph=graph, depth=1)


def build_town(c, t, base):
    url = f'{base}areas/{t["slug"]}.html'
    s_cards = "".join(
        f'<a class="card" href="../services/{s["slug"]}.html"><h3>{e(s["name"])}</h3>'
        f'<p>{e(s["short"])}</p></a>' for s in c["services"])
    body = f"""
<section class="hero" style="border-top:none"><div class="wrap">
  <h1>{e(c["trade"].title())} serving {e(t["name"])}, {e(c["state"])}</h1>
  <p class="lede">{e(t["note"])} {e(c["about"])}</p>
  <div class="cta">
    <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
  </div>
</div></section>

<section><div class="wrap">
  <h2>What we do for {e(t["name"])} customers</h2>
  <div class="grid">{s_cards}</div>
</div></section>

<section><div class="wrap"><div class="band">
  <h2>Serving {e(t["name"])} from our shop in {e(c["city"])}</h2>
  <a class="btn primary" href="tel:{digits(c["phone"])}">Call {e(c["phone"])}</a>
</div></div></section>
"""
    lb = local_business(c, base)
    lb["areaServed"] = [{"@type": "City", "name": t["name"]}]
    return shell(c, title=f'{c["trade"].title()} in {t["name"]}, {c["state"]} | {c["biz"]}',
                 desc=f'{c["biz"]} serves {t["name"]}, {c["state"]}. {t["note"]}'[:155],
                 canonical=url, body=body, graph=[lb], depth=1)


# ---------------------------------------------------------------- driver

def build(path):
    c = json.load(open(path))
    base = f'https://{c["domain"]}/'
    out = os.path.join(ROOT, "dist", c["slug"])
    os.makedirs(os.path.join(out, "services"), exist_ok=True)
    os.makedirs(os.path.join(out, "areas"), exist_ok=True)

    pages = {"index.html": build_home(c, base)}
    for s in c["services"]:
        pages[f'services/{s["slug"]}.html'] = build_service(c, s, base)
    for t in c["towns"]:
        pages[f'areas/{t["slug"]}.html'] = build_town(c, t, base)

    for rel, content in pages.items():
        with open(os.path.join(out, rel), "w") as f:
            f.write(content)

    urls = "".join(f"<url><loc>{base}{r.replace('index.html','')}</loc></url>" for r in pages)
    open(os.path.join(out, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?>'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(out, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n")

    print(f'{c["biz"]} → dist/{c["slug"]}/  ({len(pages)} pages + sitemap + robots)')
    for r in pages:
        print("   ", r)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 src/build_site.py clients/<name>.json")
    for p in sys.argv[1:]:
        build(p)
