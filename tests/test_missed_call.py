from src.aisystems.missed_call.brain import TemplateBrain
from src.aisystems.missed_call.engine import Conversation

CONFIG = {
    "business_name": "Test Plumbing",
    "owner_first": "Mike",
    "services": ["leaks", "drains"],
}


def test_conversation_flow_and_lead_capture():
    convo = Conversation(CONFIG, brain=TemplateBrain())
    opener = convo.start()
    assert "Test Plumbing" in opener
    convo.customer_says("my water heater is leaking")
    convo.customer_says("it's Dave at 214 Oak St")
    convo.customer_says("asap please")

    lead = convo.lead_summary("(931) 555-0182")
    assert lead["customer_name"] == "Dave"
    assert "water heater" in lead["wants"]
    assert lead["caller_number"] == "(931) 555-0182"

    note = convo.owner_notification("(931) 555-0182")
    assert "New lead" in note and "Dave" in note


def test_template_brain_is_default_without_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    convo = Conversation(CONFIG)
    assert convo.brain.name == "template"
