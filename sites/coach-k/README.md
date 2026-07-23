# Beyond Limits — Coach K (static site)

Single-file static site (`index.html`) for Coach K / Beyond Limits — personal training,
nutrition, and mindset coaching, NYC + online. No build step, no dependencies.

## Deploy (pick one, all free)

- **Vercel**: `npx vercel sites/coach-k` — instant `*.vercel.app` URL.
- **Netlify**: drag the `sites/coach-k` folder onto https://app.netlify.com/drop — instant `*.netlify.app` URL.
- **GitHub Pages**: repo Settings → Pages → deploy from branch, folder `sites/coach-k`.
- **Hostinger**: upload `index.html` via file manager to `public_html/`.

## Before launch (placeholders to replace)

- Hero + portrait + before/after image slots (`.duo` blocks) — swap for real photos/video of Coach K.
- Stats (10+ years, 500+ clients, 97%, 5.0★) — replace with real, defensible numbers.
- Testimonials + transformation names — replace with real, permissioned client stories.
- CTA links (`#book`) — point at a real booking link (Calendly etc.).
- Popup form — wire to an email service (currently front-end demo only).

## Placeholder AI imagery (interim)

The hero and portrait slots currently reference Higgsfield-generated concept
shots (dark, ember-lit gym photography) hosted on Higgsfield's CDN. These are
for the PITCH only. Before launch: download them into `assets/`, repoint the
`<img src>` to the local files, and ultimately replace with real photos/video
of Coach K (the #1 conversion factor per the research).
