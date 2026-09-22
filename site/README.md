# Website

`index.html` is the whole site: six pages (home, what we do, pricing, why now,
about, free check) with client-side hash routing, so `#pricing` is a real
shareable link and the back button works. No build step, no dependencies. Fonts come from
Google Fonts, everything else is inline.

## Two ways to run it

**1. As a Claude Artifact (working now).** Published with the `db` capability,
so the waitlist form saves real signups and Miles can read them back. Limitation
worth knowing: an artifact that declares `db` cannot be shared publicly. Only
signed-in members of the owner's organization can open it and submit. That makes
it a working internal demo and a way to show the page to Daniel, not the public
site.

**2. On builtformainstreet.com (what customers see).** Drop `index.html` on any
static host. The form needs a real backend before it will capture anything from
a stranger. Two one-line options:

*Netlify:* add `data-netlify="true"` and `name="waitlist"` to the `<form>` tag,
add `<input type="hidden" name="form-name" value="waitlist">` inside it, and
delete the `ev.preventDefault()` line in the script. Submissions land in the
Netlify dashboard.

*Formspree:* set `action="https://formspree.io/f/<your-id>"` and `method="POST"`
on the `<form>`, then delete the `ev.preventDefault()` line. Submissions arrive
by email.

Either way the client-side validation above the submit keeps working, because it
runs before the network call.

## Reading the signups

Artifact version: the waitlist lives in the `waitlist` collection of the
artifact's database. Ask Claude to list it, or read it from the artifact tooling.
Each row holds business, city, contact, email, trade, status and submitted.

## Editing copy

Prices are in one table in the pricing section. The sample Leak Report in the
hero is marked `SAMPLE REPORT` on purpose and uses an invented company. Do not
put a real prospect's name on the public page saying they do not answer their
phone.
