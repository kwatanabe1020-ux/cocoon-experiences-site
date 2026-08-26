# cocoon exs — project notes

Static HTML/CSS/JS site (no build tooling), deployed to Cloudflare
Workers static assets. See `design/VLG.md` for the full visual
language guide.

## Schedule section: always pinned above the NEWS list

`index.html` has a `.schedule-section` block (`-2026 Schedule-`,
caption "Upcoming") as the **first** `.section` child inside
`<section class="stage-bleed">`, immediately followed by the regular
NEWS article `.section` blocks.

- When adding a new NEWS article, always insert it **after** the
  schedule block, never before it. The schedule stays pinned at the
  top no matter how many NEWS articles accumulate below it.
- The schedule is intentionally styled differently from a NEWS
  article (amber-accented date/caption, framing top/bottom rule,
  compact row-list instead of prose) — see `.schedule-section` and
  related rules in `styles/global.css`, right after `.section-tight`.
  Don't reuse `.news-date`/plain `.caption "News"` for schedule rows;
  keep using `.schedule-date`/`.schedule-caption` so the two stay
  visually distinct.
- Each row: `.schedule-date` (compact `M/D`, IBM Plex Mono, `datetime`
  attr in full ISO `YYYY-MM-DD`), then `.schedule-main` containing
  `.schedule-event` (event name, linked with `target="_blank"
  rel="noopener"` when a URL is known — plain text, no `<a>`, when
  it isn't) and `.schedule-region` (JA prefecture name + `<span
  lang="en">EN name</span>`, e.g. `埼玉 <span lang="en">Saitama</span>`).
- **Past dates are removed manually, not auto-hidden.** When a
  schedule date has passed, delete that `.schedule-row` outright the
  next time you're editing this section — there's no JS-driven
  expiry. This was a deliberate choice to keep the page fully static
  (no client-side date logic) and to keep the HTML source itself
  always accurate for crawlers/social-card scrapers that may not
  execute JS. If asked to add a new schedule entry, it's a good time
  to also check whether any existing rows are now in the past and
  flag them for removal.

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

### Member Instagram handles (reference, not currently displayed)

The site has no member-bio/credit format yet, so these aren't linked
anywhere on the live pages — kept here so a future "meet the band"
section or per-member credit line doesn't need to be re-sourced from
video descriptions. All at `https://www.instagram.com/{handle}/`.

| Role | Handle |
| --- | --- |
| Guitar | `mori.yoshitake` |
| Guitar | `yamanekorock8080` |
| Keyboards | `keyichro` |
| Bass | `yulian_groove` |
| Drums | `soiwst` |
| Filming & Editing | `elephantsho_` (already used as the NEWS photo/video credit) |

## Dev-reference material must never be publicly deployed

Screenshots, videos, and extracted frames used only as a reference
while implementing a feature (e.g. a target-behavior recording, a
mobile screenshot showing a layout bug) are **not** part of the site
and must never end up on the deployed site or in git history.

- Put this kind of file in `dev-reference/` at the project root. That
  directory is excluded via both `.assetsignore` (so `wrangler deploy`
  never uploads it) and `.gitignore` (so it never gets committed).
- `dev-reference/` is the default — don't invent a new location.
  Delete files from it once they're no longer needed; nothing in
  there needs to persist.
- As a safety net (in case a file lands loose at the project root
  instead), `.assetsignore`/`.gitignore` also exclude common ad-hoc
  patterns by name: `*.MOV`/`*.mov`, `IMG_*.{png,jpg,jpeg}` (the
  default iPhone camera-roll naming). Still prefer `dev-reference/`
  going forward — the pattern-based rules are a backstop, not a
  substitute.
- After adding or removing anything from `.assetsignore`, redeploy
  and verify the excluded file actually 404s on the live site —
  `wrangler deploy` only re-uploads *changed* files, so an
  already-published file needs a fresh deploy to be pulled down even
  after being excluded.
