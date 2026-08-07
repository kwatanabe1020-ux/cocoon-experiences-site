#!/usr/bin/env python3
"""Static-generate the NEWS system (list page, per-post pages, homepage feed)
from news/data.json. Run this manually after editing news/data.json, then
commit the regenerated files. No build tooling / npm needed on purpose —
this site has no build step.
"""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "news", "data.json")
NEWS_DIR = os.path.join(ROOT, "news")
INDEX_PATH = os.path.join(ROOT, "index.html")

NAV_ICONS = """<nav class="nav nav--icons">
  <a class="nav-logo" href="/index.html">
    <img src="/assets/logo.png" alt="cocoon exs(cocoon experiences)">
  </a>
  <div class="icon-nav">
    <a class="icon-link" href="https://www.youtube.com/@cocoonexs" target="_blank" rel="noopener" aria-label="YouTube">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    </a>
    <a class="icon-link" href="https://cocoon-exs.bandcamp.com/" target="_blank" rel="noopener" aria-label="Bandcamp">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M0 18.75l7.437-13.5H24l-7.438 13.5H0z"/></svg>
    </a>
    <a class="icon-link" href="https://www.tunecore.co.jp/artists/cocoon-e" target="_blank" rel="noopener" aria-label="TuneCore">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h7M7.5 7v10"/><path d="M18 7.3A6 6 0 1 0 18 16.7"/></svg>
    </a>
    <a class="icon-link" href="https://instagram.com/cocoon.exs" target="_blank" rel="noopener" aria-label="Instagram">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"/></svg>
    </a>
    <a class="icon-link" href="https://www.facebook.com/profile.php?id=100063178571727" target="_blank" rel="noopener" aria-label="Facebook">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></svg>
    </a>
    <a class="icon-link" href="/stage-sim.html" aria-label="Stage Simulator">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12c0-4.5 4.5-8 10-8s10 3.5 10 8-4.5 8-10 8-10-3.5-10-8z"/><path d="M5 9c3 0 1 6 4 6s-1-6 2-6 1 6 4 6s-1-6 2-6"/></svg>
    </a>
  </div>
</nav>"""

FOOTER = """<footer class="footer-minimal">
  <div class="wrap">
    <p class="caption" lang="en">CINEMATIC EXPERIENCE INSTRUMENTAL JAM from Fussa, west Tokyo.</p>
    <p class="caption">contact: <a href="mailto:cocoon.exs@gmail.com">cocoon.exs@gmail.com</a></p>
  </div>
</footer>"""

HEAD_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Shippori+Mincho+B1:wght@600;800&family=Karla:wght@400;500&family=Zen+Kaku+Gothic+New:wght@400;500&family=IBM+Plex+Mono:wght@400&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Shippori+Mincho+B1:wght@600;800&family=Karla:wght@400;500&family=Zen+Kaku+Gothic+New:wght@400;500&family=IBM+Plex+Mono:wght@400&display=swap"></noscript>
<link rel="stylesheet" href="/styles/global.css">"""


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt_date(d):
    return d.replace("-", ".")


def load_posts():
    with open(DATA_PATH, encoding="utf-8") as f:
        posts = json.load(f)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def render_homepage_feed(posts):
    if not posts:
        return (
            '      <p class="news-empty" lang="ja">cocoon exs(cocoon experiences) webサイトオープンしました。</p>\n'
            '      <p class="news-empty caption" lang="en">The cocoon exs (cocoon experiences) website is now open.</p>'
        )
    rows = []
    for p in posts[:5]:
        rows.append(
            f'      <div class="news-row"><span class="date">{esc(fmt_date(p["date"]))}</span>'
            f'<a href="/news/{esc(p["slug"])}/">{esc(p["title_ja"])}</a></div>'
        )
    html = "\n".join(rows)
    if len(posts) > 5:
        html += '\n      <a class="news-all-link" href="/news/">all news &rarr;</a>'
    return html


def splice_homepage(posts):
    with open(INDEX_PATH, encoding="utf-8") as f:
        content = f.read()
    feed_html = render_homepage_feed(posts)
    new_content = re.sub(
        r"(<!-- NEWS:START -->\n).*?(\n\s*<!-- NEWS:END -->)",
        lambda m: m.group(1) + feed_html + m.group(2),
        content,
        flags=re.DOTALL,
    )
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def page_shell(title, description, body):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{HEAD_LINKS}
</head>
<body>

{NAV_ICONS}

{body}

{FOOTER}

<script src="/scripts/reveal.js"></script>
</body>
</html>
"""


def render_list_page(posts):
    if not posts:
        body_inner = (
            '<p class="news-empty" lang="ja">cocoon exs(cocoon experiences) webサイトオープンしました。</p>\n'
            '  <p class="news-empty caption" lang="en">The cocoon exs (cocoon experiences) website is now open.</p>'
        )
    else:
        cards = []
        for p in posts:
            cards.append(f"""    <article class="news-card reveal">
      <span class="date caption">{esc(fmt_date(p["date"]))}</span>
      <h2>{esc(p["title_ja"])}</h2>
      <p>{esc(p["excerpt_ja"])}</p>
      <a class="read-more" href="/news/{esc(p["slug"])}/">read more &rarr;</a>
    </article>""")
        body_inner = '<div class="news-card-list reveal-group">\n' + "\n".join(cards) + "\n  </div>"

    body = f"""<header class="section-tight wrap reveal">
  <span class="caption">News</span>
  <h1 style="font-size:var(--text-h2); margin-top:0.6rem;">News</h1>
</header>

<section class="wrap section-tight">
  {body_inner}
</section>"""
    return page_shell("News — cocoon exs(cocoon experiences)", "cocoon exs(cocoon experiences)からのお知らせ一覧。", body)


def render_post_page(post, all_posts):
    others = [p for p in all_posts if p["slug"] != post["slug"]]
    headline_rows = "\n".join(
        f'    <div class="news-row"><span class="date">{esc(fmt_date(p["date"]))}</span>'
        f'<a href="/news/{esc(p["slug"])}/">{esc(p["title_ja"])}</a></div>'
        for p in others
    )
    headlines_block = ""
    if others:
        headlines_block = f"""<div class="wrap news-headlines reveal">
  <span class="caption">Latest headlines</span>
  <div style="margin-top:1rem;">
{headline_rows}
  </div>
</div>"""

    body = f"""<header class="section-tight wrap reveal">
  <span class="caption">News &middot; {esc(fmt_date(post["date"]))}</span>
  <h1 style="font-size:var(--text-h2); margin-top:0.6rem; max-width:20ch;">{esc(post["title_ja"])}</h1>
  <p class="caption" lang="en" style="margin-top:0.4rem; text-transform:none; letter-spacing:normal;">{esc(post["title_en"])}</p>
</header>

<section class="wrap section-tight reveal news-detail-body">
  <p lang="ja">{esc(post["body_ja"])}</p>
  <p class="en" lang="en">{esc(post["body_en"])}</p>
</section>

{headlines_block}"""
    return page_shell(
        f'{post["title_ja"]} — cocoon exs(cocoon experiences)',
        post["excerpt_ja"],
        body,
    )


def main():
    posts = load_posts()

    splice_homepage(posts)

    os.makedirs(NEWS_DIR, exist_ok=True)
    with open(os.path.join(NEWS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_list_page(posts))

    valid_slugs = {p["slug"] for p in posts}
    for entry in os.listdir(NEWS_DIR):
        full = os.path.join(NEWS_DIR, entry)
        if os.path.isdir(full) and entry not in valid_slugs:
            shutil.rmtree(full)

    for p in posts:
        post_dir = os.path.join(NEWS_DIR, p["slug"])
        os.makedirs(post_dir, exist_ok=True)
        with open(os.path.join(post_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render_post_page(p, posts))

    print(f"Built {len(posts)} post(s). news/index.html + homepage feed regenerated.")


if __name__ == "__main__":
    main()
