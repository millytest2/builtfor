# Field Manual (PDF source)

`field_manual.html` is the print source for the Built for Main Street field manual —
what we sell, the 20 leads, the script, the close, and delivery.

Regenerate the PDF after editing:

```bash
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer \
  --print-to-pdf=output/Built_for_Main_Street_Field_Manual.pdf \
  docs/manual/field_manual.html
```

(Any Chrome/Chromium works — `--headless --print-to-pdf`. Letter size, 0.6in/0.7in margins
are set in the `@page` rule.)

Leads change: regenerate with `python -m src.leadfinder.shortlist --cluster --top 20`
and update section 2 of the HTML.
