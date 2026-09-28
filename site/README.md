# Website

The public site for builtformainstreet.com.

- **Source:** `site/src/` (`index.body.html`, `style.css`, `app.js`, `footer.html`, `nav.html`, `street.py`)
- **Build:** `python3 site/src/build_site.py` writes the static site to `site/www/` and a
  preview copy to `output/preview/` (including `artifact.html` for the published preview)
- **Deploy:** upload `site/www/` to any static host (Cloudflare Pages is free)

## The form

The free-check form posts to a Google Apps Script (`site/lead-to-email.gs`). Until the
script is deployed and its ID replaces `PASTE_YOUR_SCRIPT_ID` in
`site/src/index.body.html`, the form falls back to showing the email address.

## Other pages here

- `callsheet.html`: the call sheet. Leads, per-lead script, call windows, status log,
  weekly scorecard and pipeline. Published as an artifact with a database.
- `launch.html`: the LLC and launch checklist (file on or after December 17).
