# cocoon exs — project notes

Static HTML/CSS/JS site (no build tooling), deployed to Cloudflare
Workers static assets. See `design/VLG.md` for the full visual
language guide.

## NEWS section rule: always include a date

Every NEWS item on the homepage (the `<section class="stage-bleed">`
items in `index.html`) must show a date between the `News` caption
label and the article headline. Never add a NEWS article without one
— if the exact day is unknown, use month precision (see below) rather
than omitting the date.

Order is always:

```
News (caption label)
↓
date
↓
headline
```

### Markup pattern

```html
<span class="caption">News</span>
<time class="news-date" datetime="2026-05">2026年5月 — MAY 2026</time>
<h2 style="margin-top:0.5rem; margin-bottom:1.2rem;">Article headline</h2>
```

- `datetime` uses ISO format: `"YYYY-MM"` when only the month is known,
  `"YYYY-MM-DD"` once the exact day is confirmed — update it in place
  when the day becomes available, no structural change needed.
- The visible text always pairs JA and EN, separated by an em dash:
  - Month-only: `2026年5月 — MAY 2026`
  - With day: `2026年5月15日 — MAY 15, 2026`
- Both the JA and EN parts of the date use **IBM Plex Mono**
  (`.news-date` / `var(--font-mono)`) — VLG treats dates as
  numeric/caption content regardless of language, unlike the JA
  body-font / EN mono-caption pairing used for headlines and prose.
- Date color is muted (`var(--color-text-sub)`, a translucent
  `--ce-silk`) so the headline stays the visual lead — do not use a
  bright/accent color for the date itself.

The `.news-date` CSS rule lives in `styles/global.css` right after
`.caption`.
