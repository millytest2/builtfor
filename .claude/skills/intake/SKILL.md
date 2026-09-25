---
name: intake
description: Turn messy notes from an intake call into a complete client JSON, then build and check the site. Use after a client has paid and photos have arrived, or when the user pastes raw call notes for a signed client.
---

# Intake to built site

Target: 20 minutes of the user's time, not two hours. The user talks to the
client; everything downstream is this skill's job.

## Input

Raw notes, in any state. Bullet fragments, a transcript, a voice-memo
transcription. Do not ask for them to be tidied first.

## Steps

1. **Read `clients/_example.json`** for the exact shape. Top-level keys include
   slug, biz, domain, phone, street/city/state/zip, lat/lon, owner, trade,
   trade_plural, tagline, lede, callbar, about, hours, services[], towns[],
   reviews[], faqs[], photos[]. Service objects take slug, name, short, body,
   price_from and their own faqs; towns take slug, name, note.
2. **Write `clients/<slug>.json`.** Fill everything the notes support.
3. **List what is missing** as a short numbered set of questions the user can ask
   in one follow-up text. Do not invent a single fact — not an hour, not a year
   founded, not a service. An invented detail on a real business's website is the
   worst thing this system can produce.
4. **Write the copy.** Every service body, every town note, the about, the FAQs.
   Town pages must each be genuinely different; identical town pages with the
   name swapped are the thing that makes this category worthless, and an
   assistant reading them can tell.
5. **Build**: `python3 src/build_site.py clients/<slug>.json`
6. **Verify before saying it is done.** Confirm 11 pages emitted and that the
   JSON-LD parses on every one. Render it, do not assume.

## Rules

- **Structure and schema live in code, never in a prompt.** Write content into
  the JSON; never hand-write HTML. That separation is the whole build system.
- Use the owner's own words for what they do. Read their reviews and mirror the
  phrases customers already use.
- No marketing adjectives. An upholsterer does not say "premium bespoke
  solutions."
- Prices only where the client gave one.

## Teach while doing it

Report which fields came straight from the notes, which were inferred and from
what, and which are still blank. That list is the thing the user checks — and
after two or three clients it is the only part they still need to look at.
