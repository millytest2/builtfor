---
name: visibility-check
description: Turn raw pasted answers from ChatGPT, Gemini and Claude into the client-facing Visibility Check, the before half of the before/after report. Use when the user pastes assistant answers about a prospect or asks for a Visibility Check.
---

# Visibility Check (the before report)

The free door, and the thing that sells this. Follow `docs/BEFORE_AFTER.md` — it
is the spec, this is the assembly.

## Input

Whatever the user pastes: assistant answers, search screenshots, a Google
Business Profile, a URL. Work from what is there. Name what is missing rather
than guessing it.

## Assemble the four sections

1. **Can they be found** — the two questions that matter are the shopping
   question ("who should I hire for <trade> in <town>") and the by-name question
   ("tell me about <business>"). The by-name answer is what sells. If an
   assistant returned something like "I don't have information about that
   business," quote it exactly and put it first.
2. **What Google knows** — claimed, categories, website link, hours, description
   length against 750, services, photos, reviews, Q&A.
3. **What the website communicates** — exists, mobile speed, trade in the title,
   towns, service pages, real photos, structured data present or not.
4. **Can they be contacted** — tap-to-call, working form, where it routes, hours,
   text option, taps to send a quote request. Most leaks are here and all of it
   is HTML.

## Rules

- **Every line is a fact with a screenshot or a number behind it.** No scores out
  of ten, no letter grades, no adjectives. The moment it reads as a sales
  document it stops working.
- Do not soften it and do not sharpen it. The facts are enough.
- If something is fine, say it is fine. A report where everything is broken reads
  as a pitch; one that credits what works reads as an inspection.
- House style from `CLAUDE.md`: plain words, short sentences, no marketing
  language.

## Output

A one-page report an owner reads without help, plus a separate short list of
**what the $1,000 fixes**, mapped line by line to what was found. Do not include
pricing inside the report itself — it is an inspection, not a proposal.

## Teach while doing it

Close with **What I would look at first if I were you** — two lines naming which
finding is the strongest lever on this specific business and why.
