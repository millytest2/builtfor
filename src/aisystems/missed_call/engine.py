"""Runs a missed-call-text-back conversation and captures the lead.

The engine is transport-agnostic: the same logic drives the terminal simulator
and the live Twilio webhook. It holds the conversation, calls the brain for each
reply, and extracts a lead summary for the owner."""
import re

from .brain import select_brain


class Conversation:
    def __init__(self, config: dict, brain=None):
        self.config = config
        self.brain = brain or select_brain(config)
        self.history: list = []   # list of (speaker, text)

    def start(self) -> str:
        """Fire the auto text-back after a missed call. Returns the message."""
        msg = self.brain.opener(self.config)
        self.history.append(("business", msg))
        return msg

    def customer_says(self, text: str) -> str:
        """Record a customer reply and return the business's next message."""
        self.history.append(("customer", text))
        msg = self.brain.reply(self.config, self.history)
        self.history.append(("business", msg))
        return msg

    def lead_summary(self, caller_number: str = "") -> dict:
        """Best-effort structured lead for the owner notification."""
        customer_msgs = [text for speaker, text in self.history if speaker == "customer"]
        joined = " ".join(customer_msgs)
        name = None
        m = re.search(r"\b(?:i'?m|it'?s|name'?s|this is)\s+([A-Z][a-z]+)", joined)
        if m:
            name = m.group(1)
        return {
            "business": self.config["business_name"],
            "caller_number": caller_number,
            "customer_name": name or "(unknown)",
            "wants": customer_msgs[0] if customer_msgs else "(no reply yet)",
            "details": customer_msgs[1:] if len(customer_msgs) > 1 else [],
            "messages": len(customer_msgs),
        }

    def owner_notification(self, caller_number: str = "") -> str:
        lead = self.lead_summary(caller_number)
        lines = [
            f"New lead - missed call at {lead['business']}",
            f"From: {lead['customer_name']}  {caller_number}".rstrip(),
            f"Wants: {lead['wants']}",
        ]
        if lead["details"]:
            lines.append("More: " + " / ".join(lead["details"]))
        lines.append("Reply here or open the thread to take over.")
        return "\n".join(lines)
