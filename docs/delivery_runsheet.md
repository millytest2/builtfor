# Delivery run sheet — one client, start to finish

Print this. Tick the boxes. Do not improvise; every deviation is an hour you don't
get back and a precedent the next client inherits.

**Fourteen days. The clock starts when materials arrive, not when they pay.**

---

## Day 0 — the yes (same call, 10 minutes)

- [ ] Text the **Growth Plan — Setup $400** Stripe link while still on the phone
- [ ] Confirm the payment hit before you hang up
- [ ] Email the **client agreement** (`legal/client_agreement.md`) — e-sign via Dropbox
      Sign, Docusign free tier, or a typed name and date on a reply email
- [ ] Add a row to the **Clients** tab
- [ ] Copy `config/clients/_template.yaml` → `config/clients/<slug>.yaml`, fill it in
- [ ] Book the 20-minute intake call within 48 hours

**Do not start the subscription yet.** It starts at launch, with a 30-day trial, so
"first month included" is literally true.

## Day 0–1 — intake (20 minutes, one call, one form)

Everything you need, and nothing you don't:

- [ ] Exact business name, as it should appear on Google
- [ ] Services, in their words, in the order they want them sold
- [ ] Service area — towns, not a radius
- [ ] Phone, hours, address (or "service area only")
- [ ] **5–10 photos of real jobs.** This is the long pole. Ask on the call, then text
      a reminder the same day and again on day 3.
- [ ] 3 reviews they're proud of (you can lift these from Google)
- [ ] Logo if one exists; if not, say so plainly and set type instead
- [ ] Domain: do they own one? If not, you register it **in their name**
- [ ] GBP access: they add `hello@builtformainstreet.com` as **Manager**, never Owner

- [ ] Run the BEFORE audit and save it: `python -m src.audit.run --business "Name, City ST"`

**The clock starts when the photos land.** Say that out loud on the intake call so the
deadline is theirs to move, not yours to miss.

## Day 1–2 — generate (45 minutes, mostly automated)

- [ ] `python -m src.website.build --client config/clients/<slug>.yaml`
- [ ] Read the generated copy as the customer, not the builder. Fix the headline, the
      offer, and the proof. Leave the rest.
- [ ] Confirm the schema block has the right NAP, matching Google exactly

## Day 3–8 — build

**Clients 1–5: you build it.** You need to know this work before you can hand it over.
**Client 6 onward: the contractor builds it** off the brief. Agreement first.

- [ ] Build from the template. One page for $400, three to five for $600.
- [ ] Tap-to-call in the header, sticky on mobile
- [ ] Contact form, delivering to their email **and** yours
- [ ] Reviews embedded, photos in, hours, map, service area
- [ ] Mobile first, then desktop. Most of these visitors are on a phone in a driveway.

## Day 9 — preview (30 minutes, one round)

- [ ] Send the preview link with: *"Two things you'd change?"* Ask for two. You get two.
- [ ] **One revision round. One call. Time-boxed.** Then it goes live.
- [ ] A second round is a scope conversation, not a favour

## Day 12–14 — launch

- [ ] Domain pointed, HTTPS on, www redirect works
- [ ] **Buy the Twilio tracking number, put it on the site only.** Their real number
      stays primary on Google for NAP consistency.
- [ ] Forward the tracking number to their cell. Test it. Actually call it.
- [ ] Submit the form yourself. Confirm it arrives in both inboxes.
- [ ] Add the site URL to their Google Business Profile
- [ ] PageSpeed mobile check
- [ ] Run the AFTER audit. **If it isn't green, it isn't done.**
- [ ] **Start the Stripe subscription** — 30-day trial, so first charge is day 30

## Day 14 — handoff call (20 minutes, and this is the one people skip)

This call is worth more than the build. Do all five:

- [ ] Walk the before/after. Show the audit, red to green.
- [ ] Hand over access — domain in their name, site login, and say out loud:
      *"You own this. If you ever want to leave, you take it with you."*
- [ ] Explain the tracking number: *"Every call this site makes, I can show you. I'll
      send you the count monthly."*
- [ ] **Ask for the testimonial. Now, on this call, while they're happy.**
- [ ] **Ask for two referrals, by name.** Not "know anyone?" — *"Who else do you know
      who's good at this and has nothing online?"*

- [ ] Screenshot before and after for the case study
- [ ] Update the Clients tab: live URL, tracking number, launch date, next care day

---

## Every month after — care day, first Monday, every client at once

Budget: **under 20 minutes per client.** If it's more, the promise is wrong.

- [ ] Site loads, HTTPS valid, form still delivering (test one at random)
- [ ] Their one small edit, if they asked
- [ ] Pull the tracking-number call count
- [ ] Send one line: *"Your site brought in 11 calls last month. All good on my end."*

**That one line is the entire reason the $349 keeps clearing.** It is also the
`playbook.md` §8 gap: the monthly proof report doesn't exist yet. Build it before
client 10, not after.

## Day 60 — the diagnosis call (this is where the real money is)

- [ ] *"Now the foundation's handled — where do you actually lose jobs?"*
- [ ] Listen for exactly three things and nothing else:
      **missed calls** → missed-call text-back (+$200–400/mo)
      **unclosed estimates** → quote follow-up (+$200–300/mo)
      **dormant customers** → reactivation ($500 one-off or +$200/mo)
- [ ] Sell one. One only. And only when their own call log names it.

**Never invent a custom AI project.** Three products, in that order, forever.

---

## The rules that keep this from eating you

1. One platform. Three templates. Never negotiate the process.
2. One revision round.
3. Clock starts at materials, not at payment.
4. Care batched to one day a month.
5. Manager on their Google profile, never Owner.
6. Their domain, in their name, always.
7. Nothing is done until the AFTER audit is green and both reports were sent.
