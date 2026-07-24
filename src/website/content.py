"""Vertical-aware copy blocks for the website starter kit. Generic defaults with
per-vertical overrides for the primary categories. All strings support
{name} {city} {noun} {noun_plural} {region} formatting, applied in get_copy()."""

DEFAULTS = {
    "schema_type": "LocalBusiness",
    "noun": "{display}",
    "hero_headline": "{city}'s trusted {noun}",
    "hero_sub": "Fast, reliable service from a real local team. Call now — we pick up.",
    "primary_cta": "Call now",
    "secondary_cta": "Get a free quote",
    "services_title": "What we do",
    "services": ["Free estimates", "Fast, reliable service", "Fair, upfront pricing"],
    "why_title": "Why {city} calls us",
    "why": ["Local and dependable", "Upfront pricing, no surprises", "Fast response when you need us"],
    "faqs": [
        ("Do you serve {city}?", "Yes — {name} proudly serves {city} and the surrounding area."),
        ("How fast can you come out?", "Call us and we'll get you scheduled as soon as possible — often same week."),
        ("Do you give free estimates?", "Yes, estimates are free. Call or send a message and we'll take care of you."),
    ],
}

OVERRIDES = {
    "barbershop": {
        "schema_type": "HairSalon", "noun": "barbershop",
        "hero_headline": "The best cuts in {city}",
        "hero_sub": "Fresh fades, classic cuts, and hot-towel shaves. Walk in or book your chair at {name}.",
        "primary_cta": "Call the shop", "secondary_cta": "Book a chair",
        "services": ["Haircuts & fades", "Beard trims & lineups", "Hot-towel shaves", "Kids' cuts"],
        "why": ["Skilled local barbers", "Walk-ins & appointments welcome", "Clean, classic shop"],
        "faqs": [
            ("Do I need an appointment?", "Walk-ins are always welcome at {name}, and you can book ahead too."),
            ("Where are you located?", "{name} is right here in {city} — see the map below for directions."),
            ("What do you charge?", "Fair, straightforward pricing. Call the shop and we'll tell you exactly."),
        ],
    },
    "septic": {
        "schema_type": "LocalBusiness", "noun": "septic service",
        "hero_headline": "{city} septic service you can count on",
        "hero_sub": "Pumping, cleaning, repairs, and installs. Straight answers and honest pricing from a local crew.",
        "primary_cta": "Call now", "secondary_cta": "Request service",
        "services": ["Septic tank pumping", "Cleaning & maintenance", "Repairs & diagnostics", "New system installation"],
        "why": ["Licensed local crew", "Upfront pricing", "Fast emergency response"],
        "faqs": [
            ("How often should I pump my septic tank?", "Most homes need pumping every 3–5 years. Call {name} and we'll help you figure out your schedule."),
            ("Do you handle emergencies?", "Yes — backups don't wait, and neither do we. Call and we'll get to you fast."),
            ("Do you serve {city}?", "{name} serves {city} and the surrounding county. Give us a call."),
        ],
    },
    "fencing": {
        "schema_type": "GeneralContractor", "noun": "fence company",
        "hero_headline": "Quality fences, built to last in {city}",
        "hero_sub": "Wood, vinyl, chain link, and ornamental. Free estimates and clean, professional installs.",
        "primary_cta": "Call for a quote", "secondary_cta": "Get a free estimate",
        "services": ["Wood & privacy fences", "Vinyl fencing", "Chain link", "Ornamental & custom gates"],
        "why": ["Free on-site estimates", "Quality materials, clean installs", "Local and licensed"],
        "faqs": [
            ("Do you offer free estimates?", "Yes — {name} gives free, no-pressure estimates. Call to set one up."),
            ("What kinds of fence do you install?", "Wood, vinyl, chain link, and ornamental, plus custom gates."),
            ("How long does an install take?", "Most residential fences go in within a few days once materials arrive."),
        ],
    },
    "tree_service": {
        "schema_type": "LocalBusiness", "noun": "tree service",
        "hero_headline": "{city}'s go-to tree service",
        "hero_sub": "Removal, trimming, and stump grinding. Fully insured, free estimates, and we clean up after ourselves.",
        "primary_cta": "Call now", "secondary_cta": "Get a free estimate",
        "services": ["Tree removal", "Trimming & pruning", "Stump grinding", "Storm & emergency cleanup"],
        "why": ["Fully insured", "Free estimates", "We leave your yard clean"],
        "faqs": [
            ("Are you insured?", "Yes — {name} is fully insured, so you're covered. Call for a free estimate."),
            ("Do you handle emergency/storm work?", "We do. Call {name} and we'll get out to you as fast as we can."),
            ("Do you grind stumps too?", "Yes, we remove the tree and grind the stump so your yard is clean."),
        ],
    },
    "hvac": {
        "schema_type": "HVACBusiness", "noun": "heating & cooling company",
        "hero_headline": "{city} heating & air you can trust",
        "hero_sub": "Repairs, installs, and tune-ups. Fast service and honest pricing, when the weather won't wait.",
        "primary_cta": "Call now", "secondary_cta": "Schedule service",
        "services": ["AC repair & installation", "Heating repair & installation", "Tune-ups & maintenance", "Emergency service"],
        "why": ["Fast response", "Upfront pricing", "Licensed local techs"],
        "faqs": [
            ("Do you offer emergency service?", "Yes — call {name} and we'll get your system back up as fast as possible."),
            ("Do you serve {city}?", "{name} serves {city} and nearby areas. Give us a call."),
            ("Do you give free estimates on new systems?", "Yes, estimates on new installs are free. Call to schedule."),
        ],
    },
    "plumbing": {
        "schema_type": "Plumber", "noun": "plumbing company",
        "hero_headline": "{city} plumber, ready when you need one",
        "hero_sub": "Leaks, clogs, water heaters, and emergencies. Fast, clean, and fairly priced.",
        "primary_cta": "Call now", "secondary_cta": "Request service",
        "services": ["Leak & pipe repair", "Drain cleaning", "Water heaters", "Emergency plumbing"],
        "why": ["Fast emergency response", "Upfront pricing", "Licensed & local"],
        "faqs": [
            ("Do you handle emergencies?", "Yes — {name} answers emergency calls. Call and we'll get to you fast."),
            ("Do you give upfront pricing?", "Always. You'll know the price before we start the work."),
            ("Do you serve {city}?", "{name} serves {city} and the surrounding area."),
        ],
    },
    "restaurant": {
        "schema_type": "Restaurant", "noun": "restaurant",
        "hero_headline": "Good food, right here in {city}",
        "hero_sub": "Come hungry. {name} serves fresh, made-to-order food your neighbors already love.",
        "primary_cta": "Call to order", "secondary_cta": "Get directions",
        "services": ["Dine in", "Takeout", "Catering & large orders", "Daily specials"],
        "why": ["Made fresh to order", "Local favorite", "Friendly, fast service"],
        "faqs": [
            ("Where are you located?", "{name} is in {city} — see the map below for directions and hours."),
            ("Do you do takeout or catering?", "Yes — call {name} to place a takeout order or ask about catering."),
            ("What are your hours?", "See our hours below, and call ahead if you're not sure — we're happy to help."),
        ],
    },
    "cafe": {
        "schema_type": "CafeOrCoffeeShop", "noun": "coffee shop",
        "hero_headline": "{city}'s favorite coffee spot",
        "hero_sub": "Great coffee, fresh pastries, and a place to slow down. Stop by {name}.",
        "primary_cta": "Call us", "secondary_cta": "Get directions",
        "services": ["Espresso & specialty drinks", "Fresh pastries & bites", "Grab-and-go", "Cozy seating & wifi"],
        "why": ["Quality local coffee", "Friendly baristas", "A spot worth staying at"],
        "faqs": [
            ("Where are you located?", "{name} is in {city} — see the map below for directions and hours."),
            ("Do you have wifi and seating?", "Yes — come get comfortable, do some work, or catch up with a friend."),
            ("What are your hours?", "Our hours are listed below. Come see us."),
        ],
    },
    "equipment_repair": {
        "schema_type": "LocalBusiness", "noun": "repair shop",
        "hero_headline": "{city} small engine & equipment repair",
        "hero_sub": "Mowers, saws, trimmers, and more — diagnosed and fixed right by a local shop that knows the gear.",
        "primary_cta": "Call the shop", "secondary_cta": "Ask about a repair",
        "services": ["Small engine repair", "Mower & saw service", "Tune-ups & maintenance", "Parts & pickup"],
        "why": ["Experienced local techs", "Honest diagnostics", "Fast turnaround"],
        "faqs": [
            ("What do you repair?", "Mowers, chainsaws, trimmers, generators, and most small-engine equipment."),
            ("How long do repairs take?", "Most repairs turn around quickly — call {name} and we'll give you a timeline."),
            ("Do you serve {city}?", "{name} serves {city} and the surrounding area."),
        ],
    },
    "monument": {
        "schema_type": "LocalBusiness", "noun": "monument company",
        "hero_headline": "Memorials made with care in {city}",
        "hero_sub": "Custom headstones, markers, and monuments — crafted with patience and respect by a local family business.",
        "primary_cta": "Call us", "secondary_cta": "Start a design",
        "services": ["Custom headstones", "Grave markers & plaques", "Monument engraving", "Cleaning & restoration"],
        "why": ["Caring, patient guidance", "Quality craftsmanship", "Family-owned and local"],
        "faqs": [
            ("How does the process work?", "Call {name} and we'll walk you through design, materials, and timing with no pressure."),
            ("Do you do custom designs?", "Yes — we create custom memorials to honor your loved one exactly as you wish."),
            ("Do you serve {city}?", "{name} serves {city} and the surrounding communities."),
        ],
    },
}


def get_copy(vertical_name: str, display_name: str, facts: dict) -> dict:
    """Resolve copy for a vertical, formatted with the business's real facts."""
    base = dict(DEFAULTS)
    base.update(OVERRIDES.get(vertical_name, {}))

    noun = base["noun"].format(display=display_name.lower())
    ctx = {
        "name": facts.get("name", "we"),
        "city": facts.get("city") or "your area",
        "region": facts.get("region", ""),
        "noun": noun,
        "noun_plural": noun + "s",
        "display": display_name,
    }

    def fmt(s):
        try:
            return s.format(**ctx)
        except (KeyError, IndexError):
            return s

    services = facts.get("services") or base["services"]
    return {
        "schema_type": base["schema_type"],
        "noun": noun,
        "hero_headline": fmt(base["hero_headline"]),
        "hero_sub": fmt(base["hero_sub"]),
        "primary_cta": fmt(base["primary_cta"]),
        "secondary_cta": fmt(base["secondary_cta"]),
        "services_title": fmt(base["services_title"]),
        "services": [fmt(s) for s in services],
        "why_title": fmt(base["why_title"]),
        "why": [fmt(w) for w in base["why"]],
        "faqs": [(fmt(q), fmt(a)) for q, a in base["faqs"]],
    }
