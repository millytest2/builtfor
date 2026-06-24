# Outreach — the "nothing to lose" conversation

Not a sales script. The frame is: **you're a real local person who looked them up,
noticed something genuinely broken, and is offering to just show them — they lose
nothing.** Problem-focused, chill, certain. You and Daniel, not a call center.

Personalization tokens map 1:1 to columns in the lead-finder CSV
(`output/leads_*.csv`), so these can be auto-filled per lead later:
`{{name}}` (owner/business), `{{business}}`, `{{trade}}`, `{{area}}`,
`{{top_problem_1}}`, `{{review_count}}`, `{{google_rating}}`.

---

## Tonality (read this before you dial)
- **Slow down.** Cold calls fail on speed, not words.
- **Drop your pitch at the end of sentences** — statements, not questions. Sound certain.
- **Smile on the opener.** They hear it.
- **Use their name twice, max.** More than that sounds like a script.
- **After you name the problem, shut up.** Let the silence sit. Don't rescue it.
- **Mean "you've got nothing to lose."** That's the whole frame. If you believe it, they will.

---

## A. The call — no-website angle (lead with this for `top_problem_1 = no website`)

**Open (pattern interrupt + honesty):**
> "Hey, is this {{name}}? ... Hey {{name}}, it's Miles — I'll be straight with you,
> this is kind of a cold call. [light, smiling] You can hang up if you want. ...
> Gimme 20 seconds to tell you why I called, then you can tell me to get lost?"

*(wait — let them say sure)*

**Reason + the observation:**
> "Appreciate it. So it's me and my buddy Daniel — we're local, we help {{trade}}
> businesses around {{area}} actually show up online. I looked you up before I called
> and... you don't really have a website. So if I'm a customer Googling
> '{{trade}} near me,' you're basically invisible — your competitors are the ones
> getting that call. Did you know it was like that, or...?"

*(genuine curiosity, NOT a gotcha — then stop talking)*

**If "I get everything by referral":**
> "Totally — referrals are the best customers you'll ever get, I'm not knocking it.
> But here's the thing: even your referrals Google you before they call, just to make
> sure you're legit. Right now when they do that there's nothing there. So you're
> losing the ones who weren't 100% sure yet."

**Soft transition (no pitch):**
> "Look, I'm not gonna do the whole sales thing on you. Here's all I'd suggest —
> let me build you a quick site, click-to-call, so when someone Googles you it actually
> rings your phone. You see it, you like it, we talk. You don't, no hard feelings —
> you've lost nothing. Fair?"

**Micro-close (a step, not the sale):**
> "Cool — best number or email to send you a quick mockup? ... And real quick, what's
> the work you actually want more of — {{trade}} jobs like [X], or [Y]?"

---

## B. The call — presence/reviews angle (for leads who HAVE a site but `top_problem` is reviews/listings)
*(This is offering #2 — what you already do at work.)*

> "...I looked you up before I called — you've actually got a solid setup, but a couple
> things are quietly costing you calls. Your Google listing's got [wrong hours / missing
> info / only {{review_count}} reviews while the guys ranking above you have 200+]. That's
> the stuff that decides who gets called first. It's fixable — not glamorous, just work.
> I can show you exactly what's off in like 2 minutes, no charge. Worth a look?"

---

## Objections (stay relaxed — you're not attached to the outcome)

- **"How much?"**
  > "Depends what you need, but way less than you'd think — AI does the heavy lifting so
  > it's cheap. Let me show you something first; if the price doesn't make sense we both
  > walk, no problem."

- **"I'm busy / not interested."**
  > "No worries, I'll be quick — want me to just text you what I found so you can look when
  > you've got a sec? Worst case, you delete it."

- **"I already have a website / a Wix thing."**
  > "Nice — is it actually bringing you calls? ... [if not] That's the difference. A site
  > that just sits there isn't the same as one built to make the phone ring. Lemme show you,
  > 2 minutes, no charge."

- **"Is this AI? Is this a scam?"**
  > "Ha — fair question. No, it's literally me and my friend, we're local. I'll text you my
  > number, you'll see we're real people."

---

## C. Voicemail (no answer)
> "Hey {{name}}, it's Miles — I help local {{trade}} folks around {{area}} get found online.
> Noticed you don't have a website and your competitors are scooping up the Google traffic.
> Not a sales thing — I'll just text you a quick example. Talk soon."

## D. SMS follow-up
> "Hey {{name}}, Miles here — made a quick example of what your site could look like: [link].
> Click-to-call so it rings your phone. No pressure, just lemme know what you think 👍"

## E. Email
> **Subject:** quick thing about {{business}} on Google
>
> Hey {{name}} — I'm local, me and my buddy help {{trade}} businesses around {{area}} get
> found online. Looked you up: you don't have a website, so when people search
> "{{trade}} near me" your competitors get the call instead of you. I put together a quick
> example of what yours could look like, click-to-call built in: [link]. Like it, we talk.
> Don't, no worries at all. — Miles
