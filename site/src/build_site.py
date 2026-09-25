"""Build builtformainstreet.com from site/src into site/www.

    python3 site/src/build_site.py

Writes index.html, privacy/index.html, 404.html, robots.txt and sitemap.xml
into site/www, and a relative-path preview copy into output/preview for
checking the site before it is deployed. Images are rendered separately by
site/src/render_images.py.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from street import street

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC, WWW, OUT = ROOT / 'site/src', ROOT / 'site/www', ROOT / 'output/preview'
SITE = 'https://www.builtformainstreet.com'
UPDATED = '2026-09-25'

read = lambda name: (SRC / name).read_text(encoding='utf-8')
CSS, JS = read('style.css'), read('app.js')
NAV, FOOT = read('nav.html'), read('footer.html')

STREETS = {
    '@@TOP_DESK@@': street('st-desk', '0 0 1000 196', False, 11.5, 'YOURS?'),
    '@@TOP_MOB@@':  street('st-mob',  '578 14 384 182', False, 13, 'YOURS?'),
    '@@END_DESK@@': street('st-desk', '0 0 1000 196', True, 11.5, 'YOURS'),
    '@@END_MOB@@':  street('st-mob',  '578 14 384 182', True, 13, 'YOURS'),
}

def fonts(a):
    face = "@font-face{{font-family:'{f}';src:url({a}fonts/{file}) format('woff2');font-weight:{w};font-style:{s};font-display:swap}}"
    return '\n'.join([
        face.format(f='Fraunces', a=a, file='fraunces.woff2', w='100 900', s='normal'),
        face.format(f='Libre Franklin', a=a, file='libre-franklin.woff2', w='100 900', s='normal'),
        face.format(f='Libre Franklin', a=a, file='libre-franklin-italic.woff2', w='100 900', s='italic'),
        face.format(f='IBM Plex Mono', a=a, file='plex-mono-400.woff2', w='400', s='normal'),
        face.format(f='IBM Plex Mono', a=a, file='plex-mono-500.woff2', w='500', s='normal'),
    ])

def head(title, desc, path, a, social=True):
    url = SITE + path
    tags = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{desc}">',
        f'<link rel="canonical" href="{url}">',
        '<meta name="theme-color" content="#1f3a32">',
        f'<link rel="icon" href="{a}favicon.svg" type="image/svg+xml">',
        f'<link rel="icon" href="{a}favicon-32.png" sizes="32x32" type="image/png">',
        f'<link rel="apple-touch-icon" href="{a}apple-touch-icon.png">',
        f'<link rel="preload" href="{a}fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>',
        f'<link rel="preload" href="{a}fonts/libre-franklin.woff2" as="font" type="font/woff2" crossorigin>',
    ]
    if social:
        tags += [
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Built for Main Street">',
            f'<meta property="og:title" content="{title}">',
            f'<meta property="og:description" content="{desc}">',
            f'<meta property="og:url" content="{url}">',
            f'<meta property="og:image" content="{SITE}/og.png">',
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            '<meta property="og:image:alt" content="A row of shops on a main street. Four are lit; the fifth is dark.">',
            '<meta name="twitter:card" content="summary_large_image">',
        ]
    return '\n'.join(tags) + f'\n<style>\n{fonts(a)}\n{CSS}</style>\n'

def fill(tpl, a, here, priv):
    nav = NAV.replace('@@H@@', here).replace('@@P@@', a or './')
    foot = FOOT.replace('@@P@@privacy/', priv).replace('@@P@@', a or './')
    out = tpl.replace('@@NAV@@', nav).replace('@@FOOT@@', foot).replace('@@JS@@', JS)
    out = out.replace('@@P@@privacy/', priv).replace('@@P@@', a or './')
    for k, v in STREETS.items():
        out = out.replace(k, v)
    return out

def doc(h, body):
    return f'<!doctype html>\n<html lang="en">\n<head>\n{h}</head>\n<body>\n{body}\n</body>\n</html>\n'

HOME_T = 'Built for Main Street'
HOME_D = ('Your next customer is asking Google or an AI assistant who to call. We fix what '
          'keeps local trade shops off that list, and make sure customers can reach you in one tap.')
PRIV_T = 'Privacy | Built for Main Street'
PRIV_D = 'What Built for Main Street collects through this website, what we do with it, and how to reach us about it.'
LOST_T = 'Page not found | Built for Main Street'

def build():
    pages = {
        # live site: absolute paths, served from the domain root
        WWW / 'index.html': doc(head(HOME_T, HOME_D, '/', '/'), fill(read('index.body.html'), '/', '', '/privacy/')),
        WWW / 'privacy/index.html': doc(head(PRIV_T, PRIV_D, '/privacy/', '/'), fill(read('privacy.body.html'), '/', '/', '/privacy/')),
        WWW / '404.html': doc(head(LOST_T, HOME_D, '/404', '/', social=False).replace('<link rel="canonical" href="https://www.builtformainstreet.com/404">\n', '')
                              + '<meta name="robots" content="noindex">\n',
                              fill(read('404.body.html'), '/', '/', '/privacy/')),
        # preview: relative paths so the files can be opened straight off disk
        OUT / 'index.html': doc(head(HOME_T, HOME_D, '/', ''), fill(read('index.body.html'), '', '', 'privacy/index.html')),
        OUT / 'privacy/index.html': doc(head(PRIV_T, PRIV_D, '/privacy/', '../'), fill(read('privacy.body.html'), '../', '../index.html', 'index.html')),
    }
    for path, html in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding='utf-8')

    (WWW / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    urls = ''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod></url>\n' for p in ('/', '/privacy/'))
    (WWW / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    (WWW / '_headers').write_text(
        '/*\n'
        '  X-Content-Type-Options: nosniff\n'
        '  X-Frame-Options: DENY\n'
        '  Referrer-Policy: strict-origin-when-cross-origin\n'
        '  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()\n'
        '  Strict-Transport-Security: max-age=31536000\n'
        '/fonts/*\n'
        '  Cache-Control: public, max-age=31536000, immutable\n')
    # the Artifact preview wants the page without its own html/head/body wrapper
    idx = pages[OUT / 'index.html']
    art = idx[idx.index('<title>'):idx.index('</head>')] + idx[idx.index('<body>') + 6:idx.rindex('</body>')]
    (OUT / 'artifact.html').write_text(art, encoding='utf-8')
    for p in pages: print('wrote', p.relative_to(ROOT))

if __name__ == '__main__':
    build()
