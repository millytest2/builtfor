# DELIVERY — how a job actually gets done

One build is about **six hours of your time**, not a week, if you run it in this
order. The bottleneck is never the work. It is waiting on photos.

---

## The two commands

```bash
# 1. blank intake, fill it in from the sales call
python -m src.delivery.pack --new alpine

# 2. everything you have to write, in one file
python -m src.delivery.pack --client config/clients/alpine.yaml
#    -> output/delivery/alpine/pack.md

# 3. site structure, schema and a sendable mockup
python -m src.website.build --client config/clients/alpine.yaml
#    -> output/websites/alpine/{mockup.html, build_brief.md, copy.md, schema.json}
```

The pack covers the half nobody tools: the Google Business Profile content, the
intake checklist, the page plan sized to the tier they bought, the ship
checklist and the day-45 re-check. The website builder covers structure.

---

## Where Claude does the work

| Step | You | Claude |
|---|---|---|
| **Visibility Check** | Run the four searches, paste what came back | Writes the one-page report in the owner's language |
| **Intake** | Ask the questions on the call | — |
| **GBP description** | Approve it | Writes it inside the 750-char limit |
| **Service descriptions** | Approve | Writes all 5-10 |
| **Q&A** | Approve | Writes 4 in the owner's voice |
| **Site copy** | Paste the block from section 3 of the pack | Writes every page, plus the JSON-LD |
| **Town pages** | — | Writes each one differently, which is the part people fake |
| **Day-45 report** | Re-run the searches, paste results | Writes the comparison |
| **Client emails** | Send | Drafts |

Section 3 of every pack carries the exact prompt with that client's intake
already filled in. Copy, paste, done.

**What Claude cannot do, so budget for it:** claiming the listing (your Google
account, sometimes a postcard), taking or choosing photos, the phone calls, and
deciding what is actually true about the business. That last one matters. Every
line Claude writes has to be checked against what the owner really does, or you
will ship a page claiming they do something they don't.

---

## The six hours

| | |
|---|---|
| Intake call and pack generation | 30 min |
| Listing claim started | 15 min |
| GBP content written and pasted in | 60 min |
| Site copy generated and edited | 90 min |
| Build and deploy | 90 min |
| Photos placed, NAP consistency swept | 45 min |
| Review round and fixes | 45 min |

Everything else in the two weeks is waiting. On them for photos, on Google for
verification. Start both on day one.

---

## Keeping the $79 low-touch

The monthly only works if it stays near-zero effort. Rules:

1. **One host, one stack, one template.** Every client the same. The moment you
   have two stacks you have a support desk.
2. **Batch the listing work.** One session a month across every client at once,
   not one client at a time.
3. **Script the re-check.** Same four searches, same format, generated.
4. **Target ten minutes per client per month.** At 40 clients that is under
   seven hours a month for roughly $3,200.
5. **Past 40 clients, hire it out rather than dropping it.** A VA can run the
   batch once the template is fixed.

If a client wants more than the hosting covers, that is a separate paid
conversation and you are allowed to say no.
