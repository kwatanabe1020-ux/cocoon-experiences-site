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

## NEWS section rule: credit the photographer/editor when known

When a NEWS article's photo or video has a credited photographer or
editor, append a credit line to the end of *both* the JA and EN
description paragraphs (not just one). Skip it entirely if there's no
one to credit — don't leave a placeholder.

### Markup pattern

```html
<p lang="ja">…description text.<br><span class="credit">撮影・編集：<a href="https://www.instagram.com/handle/" target="_blank" rel="noopener">Name</a></span></p>
<p class="caption" lang="en" style="margin-top:0.6rem;">…description text.<br><span class="credit">Filmed &amp; edited by <a href="https://www.instagram.com/handle/" target="_blank" rel="noopener">Name</a></span></p>
```

- JA phrasing: `撮影・編集：{name}` (adjust the role words — e.g. `撮影：`
  only — if only one credit applies).
- EN phrasing: a natural sentence, e.g. `Filmed & edited by {name}`.
- The credit link always opens in a new tab: `target="_blank"
  rel="noopener"`.
- Wrap the credit in `<span class="credit">…</span>`, appended after a
  `<br>` inside the same paragraph as the description it belongs to —
  don't make it a separate `<p>`.
- `.credit` (in `styles/global.css`, right after `.news-date`) renders
  it small/muted mono in natural case (not uppercased, even when
  nested inside a `.caption` paragraph) with a subtle underlined link
  that brightens to `--ce-amber` on hover/focus — reuse that class
  rather than inventing new styling per article.
