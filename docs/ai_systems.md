# AI Systems — the "Get Paid" expansion (+$300–700/mo)

This is package 3: the sticky, high-margin recurring layer you sell to existing,
happy clients. It's operationally embedded — the client can't turn it off without
losing leads — which is exactly why it retains and why a buyer pays a premium for it.

## Built: Missed-Call Text-Back

When a customer calls a local business and no one picks up, that lead is usually gone.
This turns every missed call into a captured lead:

1. Customer calls the business number.
2. It rings the owner. If unanswered in ~18 seconds...
3. The customer instantly gets a friendly text back ("sorry we missed you — what do
   you need?").
4. An AI receptionist texts with them, captures the job + name + timing, and never
   invents prices or promises.
5. The owner gets an instant text with the lead summary and can take over anytime.

**See it:** `python -m src.aisystems.missed_call.simulate` → opens a phone mockup of the
whole thread. That mockup is also your sales demo — text it to a prospect.

### Two ways to deliver it

**Option A — n8n (no-code, recommended for most clients).**
Fastest to deploy and clone. The flow:
- Twilio number (per client) → forwards to owner's cell.
- Twilio "call status" webhook → n8n: if `no-answer`/`busy`, send the opener SMS.
- Twilio inbound-SMS webhook → n8n: call an LLM (Claude) node with the business
  context + conversation, send the reply, and after 2 customer messages fire the
  owner-alert SMS.
- Clone per client by swapping the config values (business name, services, owner
  number) in one n8n "Set" node.

**Option B — the code webhook (`src/aisystems/missed_call/webhook.py`).**
Same logic as a self-hostable Flask app for clients who need custom behavior
(booking integration, CRM push, special routing). Deploy on Render/Fly/Railway,
point the Twilio number's voice + messaging webhooks at it.
```bash
pip install flask twilio
export MISSED_CALL_CONFIG=config/clients/<slug>.yaml
export TWILIO_ACCOUNT_SID=...  TWILIO_AUTH_TOKEN=...  ANTHROPIC_API_KEY=...
flask --app src.aisystems.missed_call.webhook run
```

Both share the same `Conversation`/brain code in `src/aisystems/missed_call/`, so the
"brain" (the actual texting behavior) is identical whichever transport you pick.

### The brain
- **No API key:** a template brain runs a believable slot-filling flow (used for the
  demo, and a safe fallback).
- **With `ANTHROPIC_API_KEY`:** a Claude brain handles natural conversation. Defaults
  to `claude-haiku-4-5` — cheap and fast, which matters for high-volume SMS. Bump the
  `model` in the client config to Sonnet/Opus if a client wants more finesse.

### Cost / margin
Twilio: ~$1–2/mo per number + ~$0.01/SMS. Claude Haiku: fractions of a cent per
reply. So delivery cost is a few dollars a month against a $300–700/mo price — this is
the highest-margin thing you sell, and it runs itself.

### Config (clone-per-client)
Everything lives in the client's `config/clients/<slug>.yaml` under `ai_missed_call:`
(see `_template.yaml`). Onboarding = fill the config, provision a Twilio number, point
the webhooks. Done.

## The other four expansion problems (same pattern, build when a client needs one)
Missed calls ✅ (built) · lead follow-up nurture · review-request engine · booking
automation · repetitive-admin workflow. Each is a config-driven module under
`src/aisystems/`, sold as its own +$300–700/mo add-on. Build the next one the first
time a paying client needs it — don't pre-build speculatively.
