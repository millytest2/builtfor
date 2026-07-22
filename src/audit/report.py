"""Render an audit into a clean single-file HTML report (print-to-PDF friendly).
Branding/CTA comes from config/audit.yaml — no code edits per client."""
import html as html_mod
from datetime import date
from pathlib import Path

GRADE_COLORS = {"A": "#1a9850", "B": "#66bd63", "C": "#fdae61", "D": "#f46d43", "F": "#d73027"}


def _esc(s) -> str:
    return html_mod.escape(str(s if s is not None else ""))


def render(data: dict, graded: dict, audit_cfg: dict, out_path: str) -> str:
    brand = audit_cfg.get("brand", {})
    cta = audit_cfg.get("cta", {})
    g = graded["overall_grade"]

    rows = []
    for s in graded["sections"]:
        checks_html = ""
        for ch in s["checks"]:
            icon, cls = ("✓", "ok") if ch["ok"] else (("?", "unk") if ch["ok"] is None else ("✕", "bad"))
            cost = ""
            if ch["ok"] is False:
                cost_line = next((f["cost"] for f in graded["fixes"]
                                  if f["label"] == ch["label"] and f["cost"]), "")
                if cost_line:
                    cost = f'<div class="cost">{_esc(cost_line)}</div>'
            checks_html += (f'<li class="{cls}"><span class="icon">{icon}</span>'
                            f'<div><strong>{_esc(ch["label"])}</strong>'
                            f'<div class="detail">{_esc(ch["detail"])}</div>{cost}</div></li>')
        color = GRADE_COLORS[s["grade"]]
        rows.append(f'''
        <section class="card">
          <div class="card-head">
            <h2>{_esc(s["title"])}</h2>
            <div class="badge" style="background:{color}">{s["grade"]}<span>{s["pct"]}%</span></div>
          </div>
          <ul class="checks">{checks_html}</ul>
        </section>''')

    fixes_html = "".join(
        f'<li><strong>{_esc(f["label"])}</strong> — {_esc(f["detail"])}'
        + (f'<div class="cost">{_esc(f["cost"])}</div>' if f["cost"] else "") + "</li>"
        for f in graded["fixes"][:6]
    ) or "<li>Nothing critical found — nice work.</li>"

    button = _esc(cta.get("button_text", "").format(
        contact_phone=brand.get("contact_phone", ""),
        contact_email=brand.get("contact_email", "")))

    page = f'''<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Online Presence Report — {_esc(data["name"])}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
         color:#1c2733; background:#f4f6f8; line-height:1.5; }}
  .wrap {{ max-width:760px; margin:0 auto; padding:32px 20px 60px; }}
  header {{ text-align:center; margin-bottom:28px; }}
  header .co {{ font-size:13px; letter-spacing:.12em; text-transform:uppercase; color:#5a6b7b; }}
  header h1 {{ font-size:26px; margin:6px 0 2px; }}
  header .addr {{ color:#5a6b7b; font-size:14px; }}
  .overall {{ display:flex; align-items:center; justify-content:center; gap:18px; margin:22px 0; }}
  .overall .big {{ width:92px; height:92px; border-radius:50%; color:#fff; font-size:44px;
                   font-weight:700; display:flex; align-items:center; justify-content:center; }}
  .overall .sub {{ font-size:15px; color:#41505e; max-width:330px; }}
  .card {{ background:#fff; border-radius:10px; padding:20px 22px; margin:14px 0;
           box-shadow:0 1px 3px rgba(20,40,60,.08); }}
  .card-head {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; }}
  .card h2 {{ font-size:17px; }}
  .badge {{ color:#fff; border-radius:8px; padding:6px 12px; font-weight:700; font-size:20px;
            display:flex; gap:8px; align-items:baseline; }}
  .badge span {{ font-size:12px; font-weight:500; opacity:.9; }}
  ul.checks {{ list-style:none; }}
  ul.checks li {{ display:flex; gap:10px; padding:8px 0; border-top:1px solid #eef1f4; }}
  ul.checks li:first-child {{ border-top:none; }}
  .icon {{ font-weight:700; width:22px; flex:none; text-align:center; border-radius:50%;
           height:22px; line-height:22px; font-size:13px; color:#fff; margin-top:2px; }}
  li.ok .icon {{ background:#1a9850; }} li.bad .icon {{ background:#d73027; }}
  li.unk .icon {{ background:#9aa7b3; }}
  .detail {{ color:#5a6b7b; font-size:13.5px; }}
  .cost {{ color:#b03a2e; font-size:13px; margin-top:3px; font-style:italic; }}
  .fixes h2 {{ font-size:17px; margin-bottom:10px; }}
  .fixes li {{ margin:0 0 10px 18px; }}
  .cta {{ background:#12324f; color:#fff; border-radius:10px; text-align:center;
          padding:28px 24px; margin-top:22px; }}
  .cta h2 {{ font-size:21px; margin-bottom:8px; }}
  .cta p {{ color:#c8d6e2; font-size:14.5px; max-width:520px; margin:0 auto 16px; }}
  .cta .btn {{ display:inline-block; background:#ff9f43; color:#12324f; font-weight:700;
               padding:12px 26px; border-radius:8px; font-size:15px; }}
  footer {{ text-align:center; color:#8a97a3; font-size:12.5px; margin-top:26px; }}
  @media print {{ body {{ background:#fff; }} .card {{ box-shadow:none; border:1px solid #e3e8ec; }} }}
</style></head><body><div class="wrap">
  <header>
    <div class="co">{_esc(brand.get("company", ""))} · Online Presence Report</div>
    <h1>{_esc(data["name"])}</h1>
    <div class="addr">{_esc(data["address"])} · {date.today().strftime("%B %d, %Y")}</div>
  </header>
  <div class="overall">
    <div class="big" style="background:{GRADE_COLORS[g]}">{g}</div>
    <div class="sub">Overall score <strong>{graded["overall_pct"]}/100</strong> across
      Google Business Profile, reviews, and website. Below is exactly what's
      costing you calls — and what it takes to fix it.</div>
  </div>
  {"".join(rows)}
  <section class="card fixes">
    <h2>Top fixes, in order of impact</h2>
    <ol>{fixes_html}</ol>
  </section>
  <section class="cta">
    <h2>{_esc(cta.get("headline", ""))}</h2>
    <p>{_esc(cta.get("body", ""))}</p>
    <div class="btn">{button}</div>
  </section>
  <footer>{_esc(brand.get("company", ""))} — {_esc(brand.get("tagline", ""))} · {_esc(brand.get("website", ""))}</footer>
</div></body></html>'''

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return str(out)
