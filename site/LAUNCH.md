# Launching builtformainstreet.com

Everything that goes live is in `site/www`. Nothing in that folder needs editing
except one line in step 1.

## 1. Leads to your inbox (5 minutes)

Open `site/lead-to-email.gs` and follow the five steps at the top. You end up with a
URL like `https://script.google.com/macros/s/AKfy.../exec`.

In `site/www/index.html`, find `https://script.google.com/macros/s/PASTE_YOUR_SCRIPT_ID/exec`
and replace it with your URL. (Or send the URL to Claude and it will do it and rebuild.)

Every request is emailed to hello@builtformainstreet.com from your own Google account,
subject "Free check: <shop> (<town>)", and saved as a row in your Google Sheet.

## 2. Put the site online (2 minutes)

Go to app.netlify.com/drop and drag the `site/www` folder onto it. Sign up with your
email when it asks. You get a temporary address like `something.netlify.app`.

## 3. Point your domain at it (10 minutes, then up to a day to take effect)

In Netlify: Domain management > Add a domain > `www.builtformainstreet.com` > confirm.
Netlify will offer to add `builtformainstreet.com` too; say yes, so both work.

In Namecheap: Domain List > Manage > Advanced DNS. Remove any existing A record for
`@` and any CNAME for `www` (often a Namecheap parking page), then add:

| Type  | Host | Value                        |
|-------|------|------------------------------|
| A     | @    | 75.2.60.5                    |
| CNAME | www  | your-site-name.netlify.app   |

Leave MX and TXT records alone. Those carry your email.

Netlify issues the https certificate on its own once DNS has updated.

## 4. Test it (2 minutes)

1. Open https://www.builtformainstreet.com on your phone.
2. Fill in the free check form with your own details.
3. Confirm the email arrives at hello@builtformainstreet.com and a row appears in the Sheet.
   If the email is in spam, mark it "not spam".
4. Text the link to yourself and check the preview card shows the street image.
5. Visit https://www.builtformainstreet.com/anything and check you get the "This one's closed" page.

## What's in the folder

| File | What it does |
|---|---|
| `index.html` | The site |
| `privacy/index.html` | Privacy policy, required in California when a site collects contact details |
| `404.html` | Shown for any address that doesn't exist |
| `fonts/` | The three typefaces, served from your own site, with their open-font licences |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Browser tab and phone home-screen icons |
| `og.png` | The preview card when the link is shared by text, email or social |
| `robots.txt`, `sitemap.xml` | Tell search engines what to index |
| `_headers` | Security headers and font caching, read by Netlify |

## Changing the site later

Edit the files in `site/src`, then run:

    python3 site/src/build_site.py
    python3 site/src/render_images.py   # only if the icons or share image changed

The privacy page names Netlify and Google. If you move hosts or change how leads are
handled, update `site/src/privacy.body.html` and its effective date.
