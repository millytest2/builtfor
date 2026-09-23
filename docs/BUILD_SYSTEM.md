# Building client sites without starting over every time

## The mistake to avoid

You are not selling a website. You are selling **being found** — and the thing
that actually makes an assistant able to name a business is the structured data
in the page: `LocalBusiness`, `Service`, `FAQPage`, hours, service area,
reviews, consistent name/address/phone.

That is precisely the part AI site builders do badly. Emergent, Lovable, v0 and
the rest will give you a good-looking page every time and schema that is
different every time, or wrong, or missing. Ship ten sites that way and you
have ten different products, none of which you can debug when a client asks why
ChatGPT still doesn't know them.

**So split it.** The structure and schema live in code and never change. The AI
writes copy only.

| Layer | Who does it | Changes per client? |
|---|---|---|
| HTML shell, CSS, JSON-LD generation | `templates/base.html` + `src/build_site.py` | Never |
| Business facts, services, towns, copy | one JSON file | Always |
| Photos | client sends them | Always |

## The whole workflow

```
clients/acme.json   →   python3 src/build_site.py clients/acme.json   →   dist/acme/
```

One JSON file in. Eleven pages out: home, a page per service, a page per town,
plus `sitemap.xml` and `robots.txt`. Every page carries valid JSON-LD. Took
about 40 milliseconds.

Try it now:

```bash
python3 src/build_site.py clients/_example.json
open dist/jims-upholstery/index.html
```

### Step 1 — Intake call, 15 minutes

Get these and nothing else:

- Legal business name, exactly as it appears on the Google listing
- Phone, street address, ZIP
- Year founded, owner's first name
- Four to six services they actually want more of
- Five to eight towns they'll drive to
- Three real reviews (copy from Google)
- Photos — ask for 8, expect 4

### Step 2 — Let AI fill the JSON

Copy `clients/_example.json`, then paste this into Claude or Emergent along
with your intake notes:

> Fill out this JSON for a client site. Copy the exact structure of the example
> — same keys, same shapes, no new fields, no removed fields.
>
> Rules for the copy:
> - Write how the owner talks, not how a marketer talks. Short sentences.
> - Never write "we pride ourselves" or "quality craftsmanship" or "your
>   satisfaction is our priority." If a sentence could belong to any business
>   in any trade, delete it.
> - Every service needs a `short` under 12 words and a `body` of 2-3 sentences
>   that says what actually happens to the item or the job.
> - FAQ questions must be phrased the way a customer would type them into a
>   phone. "How much does it cost to reupholster a sofa?" not "What are your
>   pricing options?"
> - Answer the price question with a real range. Refusing to answer it is the
>   single biggest reason these pages fail to get cited.
> - `town.note` must be one specific sentence per town. Distance, landmark,
>   whether you pick up. Never the same sentence with the name swapped.
>
> Output only the JSON.

Then read it. Fix the two or three sentences that sound like a robot. That
edit pass is 10 minutes and it is the whole difference between a site that
reads as real and one that reads as generated.

### Step 3 — Build, drop in photos, deploy

```bash
python3 src/build_site.py clients/acme.json
cp ~/Downloads/acme-photos/*.jpg dist/acme/photos/
```

Deploy to Cloudflare Pages — free, unlimited sites, free SSL, fast:

```bash
npx wrangler pages deploy dist/acme --project-name=acme
```

Point the domain (**registered in your entity's name** — that is the lease) at
the Pages project. Done.

### Step 4 — The parts that aren't the website

The site is maybe a third of the value. Do these or the site won't get cited:

1. Google Business Profile claimed, verified, 750-char description, all
   services listed, Q&A filled, the new domain linked
2. Name, address and phone **identical** on the site, the listing, Yelp, BBB
   and Facebook — down to "St" vs "Street"
3. Run the Visibility Check, save the result as the month-zero baseline

`src/delivery/pack.py` generates the listing content for you.

## Time per site

| | First one | By the fifth |
|---|---|---|
| Intake call | 15 min | 15 min |
| AI fills JSON | 5 min | 5 min |
| Your edit pass | 25 min | 10 min |
| Build + deploy | 10 min | 5 min |
| Listing + citations | 45 min | 30 min |
| **Total** | **~1h 40m** | **~65 min** |

At $1,000 setup that is roughly $900/hour on the build, before the $300/mo
starts. This is why the template matters more than the tool you use to write
copy.

## Where AI tools like Emergent actually fit

| Use it for | Don't use it for |
|---|---|
| Filling the client JSON from intake notes | Generating the HTML |
| Rewriting a service description that reads flat | Anything touching JSON-LD |
| Drafting the 750-char listing description | Deciding page structure |
| Turning a photo caption into alt text | The build step |

If you ever want a different visual style, change `templates/base.html` **once**
and rebuild every client. That is the payoff of doing it this way: your tenth
client and your first client get the same fix on the same afternoon.

## Adding a trade

Nothing in the code is upholstery-specific. A tree service JSON has
`services` like "Emergency Tree Removal" and `towns` around Fort Wayne. Same
build, same schema, same eleven pages.

Once you have sold two in a trade, save the second JSON as
`clients/_template_tree.json` with the copy genericized. The third one in that
trade is then a 20-minute job.

## What's deliberately not in here

No JavaScript framework, no build toolchain, no npm install, no CMS, no
database. Page weight is about 16KB and it loads instantly on a phone on rural
LTE, which is where half these customers actually are. Speed is one of the few
ranking inputs you fully control — don't spend it on a framework.
