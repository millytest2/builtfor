"""Render favicon.svg, favicon-32.png, apple-touch-icon.png and og.png into site/www.

    python3 site/src/render_images.py

Uses the self-hosted fonts, so the share image is set in the same type as the site.
"""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from street import street
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
WWW, OUT = ROOT / 'site/www', ROOT / 'output/preview'
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

def mark(rounded=True):
    r = ' rx="13"' if rounded else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64"{r} fill="#1f3a32"/>
<rect x="10" y="17" width="44" height="9" fill="#f2ece0"/>
<path d="M10 17h9v9h-9zM28 17h9v9h-9zM46 17h8v9h-8z" fill="#c0392f"/>
<rect x="14" y="31" width="21" height="16" fill="#f0b429"/>
<rect x="40.5" y="31.5" width="9" height="18" fill="none" stroke="#f2ece0" stroke-width="2.6"/>
<path d="M8 50.5h48" stroke="#f2ece0" stroke-width="2.6"/>
</svg>'''

def og_html():
    fonts = (WWW / 'fonts').resolve().as_uri()
    art = street('og-street', '0 0 1000 196', False, 11.5, 'YOURS?')
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Fraunces';src:url({fonts}/fraunces.woff2) format('woff2');font-weight:100 900}}
@font-face{{font-family:'IBM Plex Mono';src:url({fonts}/plex-mono-500.woff2) format('woff2');font-weight:500}}
html,body{{margin:0}}
.card{{width:1200px;height:630px;box-sizing:border-box;background:#1f3a32;color:#f2ece0;
  padding:60px 72px 52px;display:flex;flex-direction:column;position:relative;overflow:hidden}}
.mark{{font-family:'Fraunces';font-weight:800;font-size:22px;letter-spacing:.04em;
  font-variation-settings:'SOFT' 40,'WONK' 1}}
.mark span{{color:#e2604f}}
h1{{font-family:'Fraunces';font-weight:800;font-size:66px;line-height:1.03;letter-spacing:-.02em;
  margin:34px 0 0;max-width:15ch;font-variation-settings:'SOFT' 50,'WONK' 1}}
h1 em{{font-style:normal;color:#f0b429}}
.og-street{{position:absolute;left:72px;right:72px;bottom:56px;width:auto}}
.lit{{opacity:1}}
.url{{position:absolute;right:72px;top:64px;font-family:'IBM Plex Mono';font-weight:500;font-size:18px;color:rgba(242,236,224,.62)}}
</style></head><body><div class="card">
<div class="mark">BUILT FOR MAIN <span>STREET</span></div>
<div class="url">builtformainstreet.com</div>
<h1>Your next customer is asking a machine who to <em>call</em>.</h1>
{art}
</div></body></html>'''

def main():
    (WWW / 'favicon.svg').write_text(mark(True), encoding='utf-8')
    tmp = ROOT / 'output/_render'; tmp.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME)
        for size, name, rounded in ((32, 'favicon-32.png', True), (180, 'apple-touch-icon.png', False)):
            page = b.new_page(viewport={'width': size, 'height': size})
            page.set_content(f'<html><body style="margin:0;background:transparent">'
                             f'<div style="width:{size}px;height:{size}px">{mark(rounded).replace("<svg ", f"<svg width={size} height={size} ")}</div></body></html>')
            page.screenshot(path=str(WWW / name), omit_background=True)
            page.close()
        (tmp / 'og.html').write_text(og_html(), encoding='utf-8')
        page = b.new_page(viewport={'width': 1200, 'height': 630})
        page.goto((tmp / 'og.html').as_uri()); page.wait_for_timeout(600)
        page.screenshot(path=str(WWW / 'og.png'))
        b.close()
    # the preview folder gets the same assets so it renders off disk
    for item in ('fonts', 'favicon.svg', 'favicon-32.png', 'apple-touch-icon.png', 'og.png'):
        src, dst = WWW / item, OUT / item
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
    for n in ('favicon.svg', 'favicon-32.png', 'apple-touch-icon.png', 'og.png'):
        print(n, (WWW / n).stat().st_size, 'bytes')

if __name__ == '__main__':
    main()
