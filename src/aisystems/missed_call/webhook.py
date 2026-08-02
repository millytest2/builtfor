"""Live Twilio webhook for missed-call-text-back (the CODE deployment option).

Two endpoints:
  POST /voice  -> Twilio hits this when the business number is called. We dial the
                  owner; if they don't answer, /voice-status sends the text-back.
  POST /sms    -> Twilio hits this on each inbound SMS from the customer. We run
                  the brain and reply. State is kept per caller number.

Config is loaded from a client YAML (env MISSED_CALL_CONFIG) so this is the same
clone-per-client pattern as everything else. Requires: flask, twilio,
GOOGLE-not-needed; ANTHROPIC_API_KEY for the Claude brain (else template).

Prefer n8n for no-code delivery (see docs/ai_systems.md). This file is here so the
logic is real, testable, and self-hostable when a client needs custom behavior.

    pip install flask twilio
    export MISSED_CALL_CONFIG=config/clients/fade_factory.yaml
    flask --app src.aisystems.missed_call.webhook run
"""
import os

import yaml

try:
    from flask import Flask, request, Response
    from twilio.twiml.voice_response import VoiceResponse
    from twilio.twiml.messaging_response import MessagingResponse
    from twilio.rest import Client as TwilioClient
except ImportError:  # keep the module importable for tests without the deps
    Flask = None

from .engine import Conversation


def _load_config() -> dict:
    path = os.environ.get("MISSED_CALL_CONFIG")
    if not path:
        raise RuntimeError("Set MISSED_CALL_CONFIG to a client YAML path.")
    data = yaml.safe_load(open(path)) or {}
    mc = data.get("ai_missed_call") or {}
    biz = data.get("business", {}) or {}
    intake = data.get("intake", {}) or {}
    cfg = {
        "business_name": biz.get("name", "Your Business"),
        "owner_first": (biz.get("owner_name", "") or "").split(" ")[0],
        "owner_phone": biz.get("owner_phone", ""),
        "services": intake.get("services_list", []),
        "hours": intake.get("hours", ""),
        "service_area": intake.get("service_area", ""),
        "twilio_number": mc.get("twilio_number", ""),
    }
    cfg.update({k: v for k, v in mc.items() if v})
    return cfg


# Per-caller conversation state. For production use Redis/DB; a dict is fine for
# a single client on one instance.
_conversations: dict = {}


def create_app():
    if Flask is None:
        raise RuntimeError("pip install flask twilio to run the webhook.")
    app = Flask(__name__)
    config = _load_config()

    def _twilio():
        return TwilioClient(os.environ["TWILIO_ACCOUNT_SID"],
                            os.environ["TWILIO_AUTH_TOKEN"])

    @app.post("/voice")
    def voice():
        """Ring the owner; if unanswered, /voice-status fires the text-back."""
        vr = VoiceResponse()
        dial = vr.dial(timeout=18, action="/voice-status", method="POST")
        dial.number(config["owner_phone"])
        return Response(str(vr), mimetype="text/xml")

    @app.post("/voice-status")
    def voice_status():
        """Called after the dial attempt. On no-answer, send the auto text-back."""
        if request.form.get("DialCallStatus") in ("no-answer", "busy", "failed"):
            caller = request.form.get("From", "")
            convo = Conversation(config)
            opener = convo.start()
            _conversations[caller] = convo
            _twilio().messages.create(
                to=caller, from_=config["twilio_number"], body=opener)
        return Response(str(VoiceResponse()), mimetype="text/xml")

    @app.post("/sms")
    def sms():
        """Inbound SMS from the customer -> brain reply -> owner alert when done."""
        caller = request.form.get("From", "")
        body = request.form.get("Body", "").strip()
        convo = _conversations.get(caller) or Conversation(config)
        _conversations[caller] = convo
        if not convo.history:
            convo.start()
        reply = convo.customer_says(body)

        # Notify the owner once we have enough to act on.
        if len([1 for s, _ in convo.history if s == "customer"]) == 2 and config.get("owner_phone"):
            _twilio().messages.create(
                to=config["owner_phone"], from_=config["twilio_number"],
                body=convo.owner_notification(caller))

        resp = MessagingResponse()
        resp.message(reply)
        return Response(str(resp), mimetype="text/xml")

    @app.get("/health")
    def health():
        return {"ok": True, "business": config["business_name"]}

    return app


app = create_app() if (Flask is not None and os.environ.get("MISSED_CALL_CONFIG")) else None
