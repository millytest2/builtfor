"""The 'brain' that writes each text-back message.

Two interchangeable backends behind one interface:
- TemplateBrain: rule-based, no API key. Runs the demo today.
- ClaudeBrain:   Claude-powered, natural conversation. Activates when
                 ANTHROPIC_API_KEY is set. This is what you deploy.

Both take the per-client config + the conversation so far and return the next
SMS the business should send. Keep replies short — it's a text message."""
import os

# History is a list of (speaker, text) where speaker is "business" or "customer".


class TemplateBrain:
    """Deterministic slot-filling flow. Believable for demos, zero cost,
    works with no API key. Good enough as a fallback if the API is down."""
    name = "template"

    def opener(self, config: dict) -> str:
        biz = config["business_name"]
        return (f"Hi, this is {biz} — sorry we missed your call! We're with a "
                f"customer but I can help right here. What do you need done?")

    def reply(self, config: dict, history: list) -> str:
        customer_turns = [t for t in history if t[0] == "customer"]
        n = len(customer_turns)
        biz = config["business_name"]
        owner = config.get("owner_first") or "the owner"
        if n == 1:
            return ("Got it — we can definitely help with that. What's the best "
                    "name and address (or cross streets) so we can get you scheduled?")
        if n == 2:
            return (f"Perfect, thank you! {owner} will text or call you shortly to "
                    f"lock in a time. Anything else we should know before then?")
        return f"Great — you're all set. Talk soon! — {biz}"


class ClaudeBrain:
    """Claude-powered receptionist. Natural, handles anything a customer says.
    Uses a cheap/fast model by default (SMS is high-volume) — override in config."""
    name = "claude"

    def __init__(self, config: dict):
        import anthropic  # imported lazily so the demo runs without the package
        self.client = anthropic.Anthropic()
        self.model = config.get("model", "claude-haiku-4-5")

    def _system(self, config: dict) -> str:
        biz = config["business_name"]
        services = ", ".join(config.get("services", [])) or "our services"
        return (
            f"You are the friendly SMS receptionist for {biz}, a local business. "
            f"A customer just CALLED and we missed it, so you're texting them back "
            f"automatically. Your job: help them by text and capture the lead.\n\n"
            f"What we do: {services}.\n"
            f"Hours: {config.get('hours', 'see below')}. "
            f"Service area: {config.get('service_area', 'local')}.\n\n"
            f"Rules:\n"
            f"- Keep every message SHORT — 1-2 sentences, like a real text.\n"
            f"- Ask ONE question at a time. Get: what they need, their name, "
            f"address/area, and preferred time.\n"
            f"- Be warm and human, never robotic. Never say you're an AI unless asked.\n"
            f"- NEVER invent prices, availability, or promises. If they ask price, say "
            f"the owner will confirm.\n"
            f"- If it sounds urgent/emergency, tell them to call back right now at "
            f"{config.get('owner_phone', 'our number')} and that we'll rush.\n"
            f"- Once you have what they need + a way to reach them, tell them "
            f"{config.get('owner_first', 'the owner')} will follow up shortly, and wrap up."
        )

    def opener(self, config: dict) -> str:
        return self._call(config, [
            {"role": "user", "content": "(A customer called and we missed it. "
                                        "Write the first friendly text-back to send.)"},
        ])

    def reply(self, config: dict, history: list) -> str:
        msgs = [{"role": "user", "content": "(Customer called and we missed it.)"}]
        for speaker, text in history:
            msgs.append({"role": "assistant" if speaker == "business" else "user",
                         "content": text})
        return self._call(config, msgs)

    def _call(self, config: dict, messages: list) -> str:
        resp = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            system=self._system(config),
            messages=messages,
        )
        return next((b.text for b in resp.content if b.type == "text"), "").strip()


def select_brain(config: dict, force_template: bool = False):
    """Claude if a key is present, else the template. One switch for the whole app."""
    if not force_template and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            return ClaudeBrain(config)
        except Exception:
            pass
    return TemplateBrain()
