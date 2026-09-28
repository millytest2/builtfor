# Website

The public site for builtformainstreet.com.

- **Source:** `site/src/` (`index.body.html`, `style.css`, `app.js`, `footer.html`, `nav.html`, `street.py`)
- **Build:** `python3 site/src/build_site.py` writes the static site to `site/www/` and a
  preview copy to `output/preview/` (including `artifact.html` for the published preview)
- **Deploy:** drag `site/www/` onto Netlify Drop and point the domain at it, as in `site/LAUNCH.md`.
  The privacy page names Netlify, so change it if you host elsewhere.

## The form

The free-check form posts to a Google Apps Script (`site/lead-to-email.gs`). Until the
script is deployed and its ID replaces `PASTE_YOUR_SCRIPT_ID` in
`site/src/index.body.html`, the form falls back to showing the email address.

## Other pages here

- `callsheet.html`: the call sheet. Leads, per-lead script, call windows, status log,
  weekly scorecard and pipeline. Published as an artifact with a database.
- `launch.html`: the open-for-business checklist, from tonight's setup to the December LLC.
  Published as an artifact with a database, so ticks save.
