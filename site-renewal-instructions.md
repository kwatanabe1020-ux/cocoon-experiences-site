# Cocoon Experiences 公式サイト改修 — Claude Code 実装指示書

**準拠文書: /design/VLG.md (VLG v1.1) — 本指示書と矛盾する場合はVLGを優先し、作業を止めて報告すること**
**絶対制約: 月額コスト0円。有料サービス・有料フォント・有料アイコン導入禁止。既存VLGデザイントークン(--ce-*)の値変更禁止**

---

## STEP 0: 現状確認(実装前に必ず実施し、結果を報告)

1. リポジトリ構成・デプロイ設定(Cloudflare Pagesのビルド出力ディレクトリ)を確認
2. **現在のヘッダーリンクを実ファイルから特定**する。
   - 想定: YouTube / Instagram / Stage Simulator の3つ
   - 想定と異なる場合: 実際のリンク一覧を報告し、最終的に6つ(YouTube / Bandcamp / TuneCore / Instagram / Facebook / Stage Simulator)になるよう差分を調整
3. ロゴ素材の形式を確認(SVGが存在するか、PNG/JPGのみか)。SVGがなければその旨を報告し、PNG運用(srcset)で進める
4. 既存のOGP設定・meta・sitemapの有無を確認

## STEP 1: ABOUT / EPK の「非公開リンク」化(削除しない)

**方針確定: ABOUT・EPKはページとして公開を継続するが、サイト内のどこからもリンクせず、検索にも載せない「非公開リンク(unlisted)」とする。URLを知っている人(=アウトリーチ先)だけが到達できる状態にする。**

1. about・epkのファイルは現在の場所に維持し、デプロイ対象に**含めたまま**にする(`_archive/`への移動・301リダイレクトは行わない)
2. サイト内のABOUT/EPKへの導線を全削除: ヘッダー、フッター、本文リンク、sitemap、OGP、JSON-LD内の参照すべて。`grep`で `about` / `epk` を横断検索し、取り残しゼロを確認
3. 両ページの`<head>`に `<meta name="robots" content="noindex, nofollow">` を追加(検索結果からの流入を遮断。過去にインデックス済みでも順次除外される)
4. sitemapが存在する場合、両ページを必ず除外
5. 両ページ自体のデザイン・内容は今回変更しない(VLG適用等は別途依頼)
6. 完了後、直リンクでの表示確認を行い、**アウトリーチ用の正式URL2つ**を報告すること

## STEP 2: トップページの縮約と100vhヒーロー化

1. `sound & philosophy` セクション(見出し+配下の文章)を削除
2. `explore` セクション(見出し+サムネイルリンク3つ)を削除
3. レイアウトを `min-height: 100svh`(モバイルのアドレスバー対策でsvh使用、dvhフォールバック)基準に再設計。縦スクロールなしで完結
4. 構成(上から): ヘッダーアイコン列 → ヒーローロゴ → NEWS見出しリスト(STEP 5の確定仕様) → 最小フッター
5. 余白はVLGのスペーシング感覚(silk 20%の余白思想)で再調整。要素を詰めず、闇を残す

## STEP 3: ヒーローロゴ

1. テキスト「cocoon exs」をロゴ画像に置換
2. **白(--ce-silk)の縁取り**:
   - SVGの場合: 輪郭パスに `stroke: var(--ce-silk)` または白フチレイヤーを追加
   - PNGの場合: `filter: drop-shadow(0 0 1.5px var(--ce-silk)) drop-shadow(0 0 1.5px var(--ce-silk));` の重ねがけで擬似縁取り(ロゴに元々白フチがある場合はそのまま活かし、過剰な二重フチにしないこと)
3. サイズ制御(**最重要: スマホで左右見切れ禁止**):
   ```css
   .hero-logo {
     width: min(92vw, 720px);
     height: auto;
     object-fit: contain;
     margin-inline: auto;
   }
   ```
4. PNGの場合は `srcset` で1x/2xを用意
5. アクセシビリティ: `alt="Cocoon Experiences"`。加えて `<h1 class="sr-only">Cocoon Experiences (cocoon exs)</h1>` を維持(sr-onlyユーティリティがなければ標準パターンで追加)
6. 出現アニメーション: VLG §3-2の `.reveal`(opacity+translateY 28px、1000ms、--ease-drift)を適用

## STEP 4: ヘッダーリンク6つのアイコン化

**並び順: YouTube → Bandcamp → TuneCore → Instagram → Facebook → Stage Simulator**

正規化済みURL(トラッキングパラメータ付与禁止):
- Bandcamp: `https://cocoon-exs.bandcamp.com/`
- TuneCore Japan: `https://www.tunecore.co.jp/artists/cocoon-e`
- Facebook: `https://www.facebook.com/profile.php?id=100063178571727`
- (YouTube / Instagram / Stage Simulator は既存URLを継続。全6リンクの疎通確認を実施し、結果を報告)

**アイコン実装:**
1. YouTube / Bandcamp / Instagram / Facebook: [Simple Icons](https://simpleicons.org/)のSVGパスを**インライン**で使用(CC0。npmパッケージ `simple-icons` からパス取得可)
2. TuneCore: Simple Iconsに存在するか確認。なければ独自生成(下記ルール)
3. Stage Simulator: 繭スクリブルの**簡略版アイコン**を独自生成。元データの絡まりをそのまま縮小すると潰れるため、レンズ形の輪郭内に3〜4回の自己交差ループを持つ一筆書き線として再設計する(24pxで判読できること)
4. **統一ルール**: 全アイコン 24×24 viewBox、視覚的重量を揃える(Simple Iconsは塗りベースなので、独自アイコンは線幅を太め=2.0前後にして重量を合わせる)。**単色 `currentColor`、通常時 silk、ホバー/フォーカス時 amber**(VLG §3-4のトランジション --beat-half / --ease-drift)

**アクセシビリティ(必須):**
- 各リンクに `aria-label`(例: `aria-label="YouTube"`)
- ホバー/フォーカスでラベル表示(CSSツールチップで可。mono書体・caption規定に準拠)
- `:focus-visible { outline: 2px solid var(--ce-sky); outline-offset: 2px; }`(VLG既定)
- タップターゲット44×44px以上。**320px幅で6個+間隔が収まる計算を先に行うこと**(44×6=264px、残り56pxを間隔配分。gap 8px×5=40pxで304px+左右padding=320px内に収まる想定。収まらなければアイコン部を40pxにしてpadding込み44pxを確保)

## STEP 5: NEWSページ新設

**URL設計: `/news/`(一覧) と `/news/{slug}/`(個別)**

1. **データ分離(必須)**: 記事データはHTMLに直書きせず `news/data.js`(または`.json`)で管理:
   ```js
   // 将来のSveltia CMSフロントマターと同一スキーマにすること
   const NEWS_POSTS = [
     // {
     //   slug: "example-post",
     //   date: "2026-07-26",
     //   title_ja: "タイトル",
     //   title_en: "Title",
     //   excerpt_ja: "抜粋…",
     //   excerpt_en: "Excerpt…",
     //   body_ja: "本文…",
     //   body_en: "Body…"
     // }
   ];
   ```
2. **一覧ページ**(phish.com/news/ の構造を参照、見た目はVLG準拠):
   - 日付(IBM Plex Mono・caption規定)+タイトル(Fraunces/しっぽり明朝)+抜粋数行+「read more」リンクのカードが縦に並ぶ
   - 情報密度は低く、余白広く。カード背景 `--ce-ink-soft`、罫線 `--ce-line`
   - スクロール出現に `.reveal` +16分音符スタッガー(VLG §3-2)
3. **個別記事テンプレート**: 上部に「NEWS ・ 日付」ラベル(mono)、本文、下部に「Latest Headlines」(他記事の日付付きリンク一覧)
4. **空状態(記事0件)**: 日英併記のプレースホルダ:
   > まだお知らせはありません。最初の便りをお待ちください。
   > No news yet — the first dispatch is on its way.
5. **トップページへのNEWS列挙(確定仕様)**: NEWSはヘッダーアイコン群には入れない。アイコン群の下(ページフロー上はヒーローロゴの下)に、ニュース記事の見出しを直接列挙する:
   - 各行 = 日付(IBM Plex Mono・caption規定)+記事タイトル(リンク。通常silk、ホバー/フォーカスでamber)。クリックで `/news/{slug}/` へ遷移
   - 表示は最新5件まで。6件以上になったら末尾に「all news →」で `/news/` 一覧へ誘導
   - 記事0件の現在は、この位置に上記の日英併記の空状態文言を表示
   - データ源はSTEP 5-1の `NEWS_POSTS` を共用し、トップと`/news/`で二重管理しないこと
   - リストが増えてもロゴの主役性を損なわないよう、リスト領域はヒーロー(100svh)の下に配置。初期表示ではロゴが画面の主役であること

## STEP 6: フッター(最小限のEPK的受け皿)

トップ下部に最小フッターを新設:
- 英語一行バイオ: `Instrumental psych from Fussa, west Tokyo.`
- 連絡先: `contact: <mailto リンク>`(メールアドレスは発注者に確認すること。未確定なら `TODO` コメントで仮置きし報告)
- 表記: caption規定(mono・13px・silk-dim)。視覚的に主張しないこと

## STEP 7: SEO・メタ整合

1. `<title>` / meta description をシングルページ構成に合わせ更新
2. OGP画像をロゴベースに更新(1200×630、ink背景+ロゴ+白縁取り。生成して`/og.png`等に配置)
3. JSON-LD追加(構造化データ、コスト0のSEO補完):
   ```json
   {
     "@context": "https://schema.org",
     "@type": "MusicGroup",
     "name": "Cocoon Experiences",
     "alternateName": "cocoon exs",
     "genre": "Psychedelic / Jam / Instrumental",
     "foundingLocation": "Fussa, Tokyo, Japan",
     "sameAs": [ /* 6リンクのURL */ ]
   }
   ```
4. VLG準拠の最小404ページを作成(ink背景・silk文字・トップへのリンク1つ)

## STEP 8: 検証(受け入れ条件)

以下すべてを満たすこと。スクリーンショットを添えて報告:
- [ ] 320 / 375 / 390 / 428 / 768 / 1024 / 1440px でロゴの左右見切れなし
- [ ] 320pxでヘッダーアイコン6つが折返し・はみ出しなし、各タップ領域44px以上
- [ ] `/about` `/epk` が直リンクで表示でき、かつサイト内リンク・sitemapに一切現れない(grepで確認)
- [ ] 両ページに `noindex, nofollow` メタが入っている
- [ ] トップのNEWS列挙が空状態文言を表示し、ダミー記事を1件入れると日付+タイトル行が正しく描画される(確認後ダミーは削除)
- [ ] NEWS一覧・個別テンプレート・空状態の表示確認
- [ ] キーボードTab移動でフォーカスリング(sky)が全リンクに出る
- [ ] Lighthouse(モバイル)で Accessibility 90+ / Performance 90+
- [ ] 既存VLGトークン(--ce-*)の値が変更されていないこと(diffで確認)

## STEP 9: 報告事項(完了時)

1. STEP 0の確認結果(現状ヘッダーリンク・ロゴ形式・ビルド設定)
2. 新規追加したCSS変数の一覧(追加した場合のみ。命名は `--ce-` 接頭辞を避け `--site-` 等で区別)
3. 6リンクの疎通確認結果
4. アイコンSVG一式の出所(Simple Icons由来 or 独自生成の別)
5. 変更ファイル一覧と変更点サマリ
6. TODO残(連絡先メールアドレス等、発注者確認待ちの項目)
