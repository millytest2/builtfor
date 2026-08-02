"""Simulate a missed-call-text-back conversation and render it as a phone
mockup, so you can SEE what the customer experiences.

    # Runs on the built-in demo (no API key needed):
    python -m src.aisystems.missed_call.simulate

    # For a specific client config:
    python -m src.aisystems.missed_call.simulate --client config/clients/fade_factory.yaml

    # Talk to it yourself in the terminal:
    python -m src.aisystems.missed_call.simulate --interactive

Output: output/missed_call/<slug>.html (an iMessage-style thread) + the owner
notification text, printed.
"""
import argparse
import html as html_mod
import re
from pathlib import Path

import yaml

from .engine import Conversation

DEMO_CONFIG = {
    "business_name": "Blue Sky Plumbing",
    "owner_first": "Mike",
    "owner_phone": "(555) 123-4567",
    "services": ["drain cleaning", "water heaters", "leaks & repairs", "emergencies"],
    "hours": "Mon-Sat 7am-7pm",
    "service_area": "Cookeville, TN",
    "caller_number": "(931) 555-0182",
    "demo_customer": [
        "hey my water heater is leaking pretty bad in the garage",
        "it's Dave, I'm at 214 Oak St",
        "asap if you can, there's water everywhere",
    ],
}


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:50]


def load_config(args) -> dict:
    if args.client:
        data = yaml.safe_load(Path(args.client).read_text()) or {}
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
            "caller_number": "(555) 555-0100",
            "demo_customer": DEMO_CONFIG["demo_customer"],
        }
        cfg.update({k: v for k, v in mc.items() if v})
        return cfg
    return dict(DEMO_CONFIG)


def render_html(config: dict, history: list, owner_note: str, out_path: str) -> str:
    biz = html_mod.escape(config["business_name"])
    caller = html_mod.escape(config.get("caller_number", ""))
    bubbles = []
    for speaker, text in history:
        side = "in" if speaker == "business" else "out"
        bubbles.append(f'<div class="row {side}"><div class="bubble {side}">'
                       f'{html_mod.escape(text)}</div></div>')
    owner_html = html_mod.escape(owner_note).replace("\n", "<br>")

    page = f'''<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Missed-Call Text-Back — {biz}</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    background:#e9edf2;padding:28px 14px;color:#111}}
  .wrap{{max-width:430px;margin:0 auto}}
  .lead{{text-align:center;color:#51606e;font-size:14px;margin-bottom:16px}}
  .phone{{background:#fff;border-radius:34px;box-shadow:0 12px 40px rgba(20,40,60,.18);
    overflow:hidden;border:1px solid #dfe5ec}}
  .status{{height:24px}}
  .contact{{text-align:center;padding:10px 0 12px;border-bottom:1px solid #eef1f4}}
  .contact .avatar{{width:46px;height:46px;border-radius:50%;background:#12324f;color:#fff;
    display:flex;align-items:center;justify-content:center;font-weight:700;margin:0 auto 5px;font-size:18px}}
  .contact .name{{font-weight:600;font-size:15px}}
  .contact .sub{{font-size:12px;color:#8a97a3}}
  .callbanner{{background:#fdeee0;color:#8a4b12;font-size:12.5px;text-align:center;padding:7px 12px}}
  .thread{{padding:14px 12px 20px;display:flex;flex-direction:column;gap:3px;
    background:#fff;min-height:360px}}
  .row{{display:flex;margin-top:7px}}
  .row.in{{justify-content:flex-start}}
  .row.out{{justify-content:flex-end}}
  .bubble{{max-width:78%;padding:9px 13px;border-radius:19px;font-size:14.5px;line-height:1.35}}
  .bubble.in{{background:#e9e9eb;color:#111;border-bottom-left-radius:5px}}
  .bubble.out{{background:#0a84ff;color:#fff;border-bottom-right-radius:5px}}
  .label{{text-align:center;font-size:11px;color:#9aa7b3;margin:8px 0 2px}}
  .owner{{max-width:430px;margin:18px auto 0;background:#12324f;color:#dce7f0;border-radius:14px;
    padding:16px 18px;font-size:13.5px}}
  .owner h3{{color:#fff;font-size:13px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}}
  .owner .n{{font-family:ui-monospace,Menlo,monospace;background:#0d2438;padding:10px 12px;
    border-radius:8px;line-height:1.5}}
  .foot{{text-align:center;color:#8a97a3;font-size:12px;margin:16px auto 0;max-width:430px}}
</style></head><body><div class="wrap">
  <div class="lead">What your customer sees after they call and you can't pick up</div>
  <div class="phone">
    <div class="status"></div>
    <div class="contact">
      <div class="avatar">{biz[:1]}</div>
      <div class="name">{biz}</div>
      <div class="sub">Text Message</div>
    </div>
    <div class="callbanner">📞 Missed call from you — auto-text sent 18 seconds later</div>
    <div class="thread">
      <div class="label">Today</div>
      {"".join(bubbles)}
    </div>
  </div>
  <div class="owner">
    <h3>🔔 And the owner instantly gets this</h3>
    <div class="n">{owner_html}</div>
  </div>
  <div class="foot">Built for Main Street · missed-call-text-back · every missed call becomes a captured lead</div>
</div></body></html>'''
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return str(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Simulate + visualize missed-call text-back.")
    ap.add_argument("--client", help="config/clients/<slug>.yaml")
    ap.add_argument("--interactive", action="store_true", help="type replies yourself")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    config = load_config(args)
    convo = Conversation(config)
    print(f"[brain: {convo.brain.name}]  Missed call to {config['business_name']}...\n")

    opener = convo.start()
    print(f"  {config['business_name']}: {opener}")

    if args.interactive:
        print("\n(Type as the customer. Blank line to finish.)")
        while True:
            try:
                line = input("  You: ").strip()
            except EOFError:
                break
            if not line:
                break
            print(f"  {config['business_name']}: {convo.customer_says(line)}")
    else:
        for line in config.get("demo_customer", []):
            print(f"  Customer: {line}")
            print(f"  {config['business_name']}: {convo.customer_says(line)}")

    note = convo.owner_notification(config.get("caller_number", ""))
    print("\n--- Owner gets this text ---")
    print(note)

    out = args.out or f"output/missed_call/{slugify(config['business_name'])}.html"
    render_html(config, convo.history, note, out)
    print(f"\nPhone mockup -> {out}")


if __name__ == "__main__":
    main()
