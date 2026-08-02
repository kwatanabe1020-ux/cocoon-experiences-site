# Cocoon Experience Visual Language Guide (VLG)

**Version 1.1 — 実素材(ロゴ・写真)反映改訂版**
対象: Web (Astro + Sveltia CMS + Cloudflare Pages) / Instagram / YouTubeサムネイル / グッズ
形式: 本ガイドはCSS変数・JSON・SVGなど標準形式で記述されており、どのAIモデル・デザインツールに渡しても同一の解釈で再現可能。

**v1.0からの変更点:**
1. 既存ロゴ(水色バブルレター)を正式資産として承認。ロゴ由来の空色 `--ce-sky` を核パレットAccent 2に昇格
2. `--ce-haze`(渋紫)を核パレットから「滲みレイヤー」(§7)へ移設
3. `--ce-ink` を藍紫からわずかに青寄り(#1A1D2E)へ調整(ロゴの紺縁と夜空写真に整合)
4. §5(写真トーン)を一律規定からシーン別3規定に再構成
5. §7「アンビエント自然色パレット+極彩色の滲みレイヤー」を新設(二層構造の導入)

---

## 0. 核となる設計思想 — "120 BPM Design"

Cocoon Experiencesのライブ演出思想「反復と微変化によるトランス誘導(BPM 110–130)」を、
そのままデザインの数値体系に翻訳する。

1. **1拍 = 500ms (120 BPM)** を全モーションの基本単位とする
2. 環境アニメーションは **素数拍(7拍・11拍・13拍)** の周期を重ね、
   位相が永遠にずれ続ける「完全には繰り返さない反復」を作る(ポリリズムの視覚化)
3. 色はバンドの実世界から導出する: 繭=生成りの絹、Hammondトーンホイールの琥珀の灯、
   既存ロゴと野外フェスの空の水色、夜の会場の藍
4. **二層構造の原則(v1.1)**: 「くっきりした核パレット」(UI・文字・線)の背後に、
   「ぼやけた極彩色の光の滲み」(§7)が漂う。ステージ照明の極彩色は輪郭を持たせず、
   常にブラーされた光としてのみ存在する
5. くっきりした虹色グラデーション・多色の塗り分けは禁止。多色はブラーされた滲みとしてのみ許可

---

## 1. カラーパレット

### 1-1. 核パレット CSS変数(UI・文字・構造用/そのまま使用可)

```css
:root {
  /* === Core Palette v1.1 === */
  --ce-ink:    #1A1D2E;  /* Primary(地色): 夜空の藍。純黒ではなく、野外フェス夜の空 */
  --ce-silk:   #EDE4D3;  /* Secondary(文字・地色反転): 生成り。未晒しの絹=繭(Cocoon) */
  --ce-amber:  #E09A3E;  /* Accent 1: Hammondトーンホイール/真空管の灯/ロゴのオレンジ */
  --ce-sky:    #6FB0DF;  /* Accent 2: 既存ロゴの水色/野外フェスの昼の空(v1.1で昇格) */
  --ce-moss:   #3E5C4F;  /* Support: 深い苔緑。土着性・アース感の錨 */

  /* === Derived (透過・線) === */
  --ce-line:       rgba(237, 228, 211, 0.16);  /* silk 16%: 罫線・区切り */
  --ce-ink-soft:   #262B40;                    /* ink の一段浮き: カード背景 */
  --ce-silk-dim:   rgba(237, 228, 211, 0.64);  /* silk 64%: 補助テキスト */
  --ce-amber-glow: rgba(224, 154, 62, 0.24);   /* amber 24%: ホバー時の灯 */
  --ce-sky-glow:   rgba(111, 176, 223, 0.20);  /* sky 20%: リンク・フォーカス表示 */

  /* === Semantic Mapping === */
  --color-bg:        var(--ce-ink);
  --color-bg-raised: var(--ce-ink-soft);
  --color-text:      var(--ce-silk);
  --color-text-sub:  var(--ce-silk-dim);
  --color-accent:    var(--ce-amber);
  --color-accent-2:  var(--ce-sky);
  --color-border:    var(--ce-line);
}
```

### 1-2. JSON形式(デザインツール・他AI移植用)

```json
{
  "color": {
    "ink":   { "hex": "#1A1D2E", "role": "primary-bg",  "rationale": "night sky at outdoor fes, bridges logo navy outline" },
    "silk":  { "hex": "#EDE4D3", "role": "text/inverse", "rationale": "raw silk = cocoon" },
    "amber": { "hex": "#E09A3E", "role": "accent-1",     "rationale": "Hammond tonewheel / tube glow / logo orange" },
    "sky":   { "hex": "#6FB0DF", "role": "accent-2",     "rationale": "existing logo blue / daytime festival sky" },
    "moss":  { "hex": "#3E5C4F", "role": "support",      "rationale": "earthy grounding, 70s JP psych" }
  }
}
```

### 1-3. 各色の選定理由

| 色 | 理由 |
|---|---|
| ink `#1A1D2E` | 純黒ではなく夜空の藍。暗順応=没入を模しつつ、ロゴの紺縁・夜の野外フェス写真と地続きになる |
| silk `#EDE4D3` | バンド名Cocoonの物質的根拠(繭・未晒しの絹)。純白より刺激が弱く、長尺ジャムを聴き続ける体験と同型 |
| amber `#E09A3E` | SK-2内部のトーンホイールと真空管の灯。既存ロゴのオレンジとも一致(唯一最初から整合していた色) |
| sky `#6FB0DF` | 既存ロゴの水色に由来。タイ野外フェス・キャンプ写真が示す通り、昼の青空はこのバンドの実世界の色。amber(太陽)との暖冷対で「野外の一日」を成す |
| moss `#3E5C4F` | 浮遊しがちなサイケ表現を地面につなぎとめる土の色。森・山の写真とも整合 |

**使用比率の原則: ink 68% / silk 20% / amber 6% / sky 4% / moss 2%**
(アクセントは希少だから効く。amberとskyを同一要素で等量使わないこと)

### 1-4. ロゴ運用規定(v1.1新設)

- 既存ロゴ(水色バブルレター+繭のスクリブル)を**正式ロゴとして承認**。用途ごとの再配色は禁止(認知資産を守る)
- 使用背景は ink / silk / 白 の3種のみ。極彩色背景・写真の情報量が多い領域には直接置かず、余白を確保する
- 派生バリアントとして **silk単色版(線画)** を1種のみ作成してよい(小サイズ・刺繍・単色印刷用)。新規デザインではなく既存ロゴのトレース
- ロゴのバブルレター様式は70年代サイケポスターの正統であり、見出しフォント(Fraunces/しっぽり明朝)とは「ロゴ=声、見出し=文章」として役割分担する。見出しをバブルレター化しないこと

---

## 2. タイポグラフィ

### 2-1. フォントファミリー(すべてGoogle Fonts / 無料 / 商用可)

```css
:root {
  /* 見出し: 欧文=Fraunces(可変・有機的な70sソフトセリフ) / 和文=しっぽり明朝B1(重厚レトロ明朝) */
  --font-display: "Fraunces", "Shippori Mincho B1", serif;

  /* 本文: 欧文=Karla / 和文=Zen Kaku Gothic New(幾何学的でわずかにレトロ) */
  --font-body: "Karla", "Zen Kaku Gothic New", sans-serif;

  /* ユーティリティ(キャプション・日付・BPM表記・トラックリスト): テープラベル的モノスペース */
  --font-mono: "IBM Plex Mono", monospace;
}
```

Google Fonts読み込み(Astroでは§6の@fontsource自己ホストを推奨):

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Shippori+Mincho+B1:wght@600;800&family=Karla:wght@400;500&family=Zen+Kaku+Gothic+New:wght@400;500&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
```

選定理由:
- **Fraunces**: 可変フォントで"wonk"(歪み)軸を持つ、木版印刷的な柔らかいセリフ。丸みがロゴのバブルレターと質感的に橋渡しされる
- **Shippori Mincho B1**: 70年代日本の書籍装丁のような太い明朝。Guruguru Brain系アートワークとの親和性が高い
- **Karla / Zen Kaku Gothic New**: 見出しが強いぶん本文は静かに。両者とも幾何学的骨格で日英が並んでも質感が揃う
- **IBM Plex Mono**: カセットテープのラベル、セットリスト、機材リストの雰囲気。BPM・日付・型番表記に使う

### 2-2. サイズ規定

```css
:root {
  /* 基準: 1rem = 16px */
  --text-h1:      clamp(2.75rem, 7vw, 5rem);     /* 44px → 80px 可変 */
  --text-h2:      clamp(2rem, 4.5vw, 3rem);      /* 32px → 48px 可変 */
  --text-h3:      1.5rem;                        /* 24px */
  --text-body:    1.0625rem;                     /* 17px */
  --text-caption: 0.8125rem;                     /* 13px */

  --leading-display: 1.1;   /* 見出し行間 */
  --leading-body-ja: 1.9;   /* 和文本文: 広めが必須 */
  --leading-body-en: 1.65;  /* 欧文本文 */

  --tracking-caption: 0.08em;  /* モノスペースキャプションは字間を開ける */
}

h1 { font-family: var(--font-display); font-size: var(--text-h1); font-weight: 560; line-height: var(--leading-display); }
h2 { font-family: var(--font-display); font-size: var(--text-h2); font-weight: 520; line-height: var(--leading-display); }
h3 { font-family: var(--font-display); font-size: var(--text-h3); font-weight: 500; line-height: 1.3; }
body { font-family: var(--font-body); font-size: var(--text-body); line-height: var(--leading-body-ja); color: var(--color-text); background: var(--color-bg); }
:lang(en) { line-height: var(--leading-body-en); }
.caption { font-family: var(--font-mono); font-size: var(--text-caption); letter-spacing: var(--tracking-caption); color: var(--color-text-sub); text-transform: uppercase; }
```

バイリンガル運用ルール:
- `<html lang="ja">` を基本とし、英文ブロックには `lang="en"` を付与(行間が自動で切り替わる)
- 日英併記時は **日本語を上、英語をキャプション扱い(mono・小さめ)で下** に置く。逆でもよいが、ページ内で統一する

---

## 3. モーション原則 — 反復と微変化の実装

### 3-1. 基本単位: 1拍 = 500ms (120 BPM)

```css
:root {
  --beat: 500ms;                                  /* 120 BPM の四分音符 */
  --beat-half: 250ms;                             /* 八分音符: ホバー等の即応 */
  --beat-2: 1000ms;                               /* 2拍: スクロール出現 */
  --ease-drift: cubic-bezier(0.22, 1, 0.36, 1);   /* 立ち上がり速く、長い残響で減衰(ダブのディレイ的) */
  --ease-swell: cubic-bezier(0.4, 0, 0.2, 1);     /* 環境ループ用の滑らかな往復 */
}
```

### 3-2. スクロール演出(fade-up)

```css
.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity var(--beat-2) var(--ease-drift),
              transform var(--beat-2) var(--ease-drift);
}
.reveal.is-visible { opacity: 1; transform: translateY(0); }

/* スタッガー: 16分音符(125ms)刻みで順に出現 = フレーズが遅れて入ってくる感覚 */
.reveal:nth-child(2) { transition-delay: 125ms; }
.reveal:nth-child(3) { transition-delay: 250ms; }
.reveal:nth-child(4) { transition-delay: 375ms; }
```

```js
// IntersectionObserver(Astroに1つ置くだけの最小実装)
const io = new IntersectionObserver(
  (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add("is-visible")),
  { threshold: 0.15 }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
```

### 3-3. 「反復と微変化」のマイクロインタラクション化 — 素数拍ループ

複数の環境アニメーションに **素数拍の周期(7拍=3.5s / 11拍=5.5s / 13拍=6.5s)** を与える。
各要素は単純な反復だが、周期が互いに割り切れないため、**組み合わせは143拍(約71.5秒)まで一度も同じ瞬間が来ない**。
ライブにおける「同じリフの反復なのに、毎小節どこかが違う」状態のWeb翻訳。

```css
@keyframes drift-y { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
@keyframes breathe { 0%,100% { opacity: 0.55; } 50% { opacity: 1; } }
@keyframes slow-spin { to { transform: rotate(360deg); } }

.loop-7  { animation: drift-y   3.5s var(--ease-swell) infinite; }  /* 7拍  */
.loop-11 { animation: breathe   5.5s var(--ease-swell) infinite; }  /* 11拍 */
.loop-13 { animation: slow-spin 6.5s linear infinite; }             /* 13拍: トーンホイールSVGに適用 */
```

### 3-4. ホバー・押下

```css
a, button {
  transition: color var(--beat-half) var(--ease-drift),
              background-color var(--beat-half) var(--ease-drift),
              box-shadow var(--beat-half) var(--ease-drift);
}
a:hover { color: var(--ce-amber); }
a:focus-visible { outline: 2px solid var(--ce-sky); outline-offset: 2px; }
.card:hover { box-shadow: 0 0 32px var(--ce-amber-glow); }  /* 真空管が灯る */
```

### 3-5. アクセシビリティ(必須)

```css
@media (prefers-reduced-motion: reduce) {
  .loop-7, .loop-11, .loop-13 { animation: none; }
  .reveal { opacity: 1; transform: none; transition: opacity var(--beat-half) ease; }
  .stage-bleed::before { animation: none; }
}
```

---

## 4. アイコン・図形モチーフ(SVG)

3種のモチーフを定義する。すべて `currentColor` で描画され、CSSの文字色を継承する。
線の太さは常に **1.5** で統一(モチーフ間の質感を揃える)。
既存ロゴの繭スクリブルとMotif B(同心楕円)は同じ「繭」の二表現であり、**ロゴがある画面にMotif Bを重ねない**こと。

### Motif A — Tonewheel(トーンホイール)

Hammondの音の発生源。`.loop-13` を付与すると6.5秒/周でゆっくり回転する。

```svg
<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tonewheel motif">
  <circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="32" cy="32" r="8" stroke="currentColor" stroke-width="1.5"/>
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="32" y1="4"  x2="32" y2="10"/>
    <line x1="32" y1="54" x2="32" y2="60"/>
    <line x1="4"  y1="32" x2="10" y2="32"/>
    <line x1="54" y1="32" x2="60" y2="32"/>
    <line x1="12.2" y1="12.2" x2="16.4" y2="16.4"/>
    <line x1="47.6" y1="47.6" x2="51.8" y2="51.8"/>
    <line x1="12.2" y1="51.8" x2="16.4" y2="47.6"/>
    <line x1="47.6" y1="16.4" x2="51.8" y2="12.2"/>
  </g>
</svg>
```

### Motif B — Cocoon(繭の同心楕円)

バンド名の中核。少しずつ軸の傾いた楕円の重なり=「反復と微変化」を静止画で表す。セクション区切り・About・アルバムフレームに使用。

```svg
<svg viewBox="0 0 64 80" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cocoon motif">
  <g stroke="currentColor" stroke-width="1.5">
    <ellipse cx="32" cy="40" rx="20" ry="32"/>
    <ellipse cx="32" cy="40" rx="15" ry="25" transform="rotate(4 32 40)"/>
    <ellipse cx="32" cy="40" rx="10.5" ry="18" transform="rotate(9 32 40)"/>
    <ellipse cx="32" cy="40" rx="6.5" ry="11.5" transform="rotate(15 32 40)"/>
    <ellipse cx="32" cy="40" rx="3" ry="6" transform="rotate(22 32 40)"/>
  </g>
</svg>
```

### Motif C — Drone(位相のずれた波)

同一の正弦波を3本、わずかに位相と透明度をずらして重ねる=ドローンのうねり・ダブのディレイ。フッター・見出し下・ローディング表示に使用。

```svg
<svg viewBox="0 0 240 48" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Drone wave motif">
  <g stroke="currentColor" stroke-width="1.5">
    <path d="M0 24 C 20 8, 40 8, 60 24 S 100 40, 120 24 S 160 8, 180 24 S 220 40, 240 24"/>
    <path d="M0 24 C 20 10, 40 10, 60 24 S 100 38, 120 24 S 160 10, 180 24 S 220 38, 240 24" opacity="0.55" transform="translate(7 0)"/>
    <path d="M0 24 C 20 12, 40 12, 60 24 S 100 36, 120 24 S 160 12, 180 24 S 220 36, 240 24" opacity="0.3" transform="translate(14 0)"/>
  </g>
</svg>
```

### 使用ルール

- モチーフは常に単色(silk / amber / sky のいずれか)。多色化・グラデーション禁止
- 1画面につきモチーフは1種類まで。同時に複数種を見せない(希少性が世界観を守る)
- 塗りつぶし(fill)は使わず、線(stroke)のみ。「煙で描いた線」の軽さを維持する

---

## 5. 写真・映像素材のトーン(v1.1 シーン別再構成)

実素材の検証により、一律の暖色補正規定を廃止し、**3シーン別規定+共通不変則**に再構成する。
原則: **会場照明・自然光の色はバンドの現実であり、色相を偽らない。VLGに揃えるのは暗部・粒子・構図であって、世界の色ではない。**

### 5-1. 共通不変則(全シーン適用)

| パラメータ | 規定 | 意図 |
|---|---|---|
| ブラックポイント | `#1A1D2E`(ink)付近まで持ち上げる。純黒禁止 | ページ背景と写真の影が地続きになる |
| 粒子(グレイン) | 15〜25%(屋外昼は10〜15%) | 70年代フィルムの質感。デジタルのツルツル感を消す |
| ハイライト | 白飛び回避。ただし照明のハレーション(にじみ)は歓迎 | 「光の滲み」は§7の二層構造と同じ思想 |
| 加工エフェクト | エコー/リピート/スタッター加工(コマ複製・ずらし)を公認とする | ダブのディレイの視覚化。既存アー写で実績あり。多用せずヒーロー画像限定 |

### 5-2. シーン別規定

**A. 暗所ライブ・スタジオ(タングステン/電球色)**
- WB +10〜+15(暖色方向)、コントラスト低〜中、彩度 -10(amber系光源は維持)、ビネット -5〜-10
- v1.0の規定をこのシーンに限定して継承。練習部屋・DISCO EDDIE'S等が該当

**B. 色照明ライブ(緑・赤・青等の演出照明)**
- **色相補正は行わない**。緑や赤の照明を暖色に強制すると肌と質感が破綻し、記録として嘘になる
- 揃えるのは共通不変則のみ(暗部をinkへ、グレイン、白飛び回避)
- 1枚の中で**支配的な照明色を1色に**。多色が混在するカットは補正ではなく「選ばない」ことで統制する(セレクトで解決し、レタッチで戦わない)

**C. 屋外昼(フェス設営・キャンプ・オフショット)**
- WBは自然のまま(±0〜+5)。青空・緑・原色の装飾は**skyとmossがパレット入りしたため、もはや敵ではない**
- 彩度は自然域を維持(-5〜±0)。グレイン10〜15%、暗部はinkまで持ち上げ
- フィルム風の既存オフショット(粒子+暖シャドウ)を基準見本とする

### 5-3. 構図・余白(2階層制に改訂)

**ヒーロー階層(サイトのファーストビュー、EPKトップ、リリースアートワーク):**
1. 被写体はフレームの60%以下。残りは闇・空・空間
2. 主要被写体は中央に置かず、左右どちらかに寄せて反対側に余白を残す(テキストを重ねる余地)
3. 動画サムネイルは「暗い画面+amberの一点光+mono書体の最小テキスト」を定型とする

**ドキュメンタリー階層(練習・設営・オフショット・SNS日常投稿):**
- 構図ルールは適用しない。雑然とした配線・機材の密度はジャムバンドの生活の記録であり、それ自体が世界観
- 適用するのは色の共通不変則のみ
- 機材のクローズアップ(ドローバー、真空管、ペダル)は常備素材として推奨。密度の高いドキュメンタリー写真からヒーロー用に切り出す場合は、機材の対角線(鍵盤の遠近等)を活かしてトリミングする

**Instagram共通**: 上下左右に10%のセーフマージン(UIに食われない+余白がフィードで目立つ)

補正数値はLightroom / Davinci Resolve / Snapseed(無料)いずれでも再現可能。
シーンA/B/C別に3つのプリセットを作成し全メンバーに配布すること(メンバー5の管轄)。

---

## 6. Astroプロジェクトへの実装アドバイス

### 6-1. ファイル配置

```
/design/
  VLG.md              ← 本ガイド(リポジトリの憲法。AIに渡す時はこのファイルを渡す)
  tokens.json         ← §1-2のJSON
  logo/
    cocoon-exs-full.png   ← 正式ロゴ(既存資産)
    cocoon-exs-silk.svg   ← silk単色版バリアント(§1-4)
/src/
  styles/
    tokens.css        ← §1・§3・§7のCSS変数のみを集約(1ファイル)
    global.css        ← tokens.cssをimportし、要素スタイルを定義
  components/
    motifs/
      Tonewheel.astro
      Cocoon.astro
      DroneWave.astro
    StageBleed.astro  ← §7の滲みレイヤーをコンポーネント化
  scripts/
    reveal.js         ← §3-2のIntersectionObserver
```

### 6-2. 実装方針

- **フォントは@fontsource(npm・無料)で自己ホスト**を推奨。CDN依存が消え、表示速度と長期安定性(方針8)が向上する。`npm install @fontsource-variable/fraunces @fontsource/shippori-mincho-b1 @fontsource/karla @fontsource/zen-kaku-gothic-new @fontsource/ibm-plex-mono`
- **色・フォント・時間の生値をコンポーネントに直書きしない**。必ず`var(--ce-*)`経由にする
- **Sveltia CMSの編集領域とスタイルを完全分離**する。メンバーが編集できるのはMarkdownの本文・画像・フロントマターのみ。tokens.css/コンポーネントは開発担当のみが触る
- ブロックパターン相当は**Astroコンポーネント+Sveltiaのカスタムフィールド**で実現
- Claude Codeへの依頼時は「`/design/VLG.md`に完全準拠すること」と一文添えるだけでよい

---

## 7. アンビエント自然色パレット+極彩色の滲みレイヤー(v1.1新設)

### 7-1. 二層構造の原則

**第1層(くっきり)**: UI要素(文字・ボタン・線・アイコン)は核パレット(ink/silk/amber/sky/moss)のみ。
**第2層(ぼやけ)**: 極彩色の照明・自然の色は、`blur`された輪郭のない光として**背景演出にのみ**使う。
文字・ボタン・線に滲みレイヤーの色を直接使うことを禁止する。

### 7-2. アンビエント自然色パレット(背景・イラスト・グラデーション用)

野外フェスの一日(昼→夕→夜)と自然物から導出。UIには使用しない。

```css
:root {
  /* === Ambient: 時間帯 === */
  --amb-noon-sky: #A8CFEA;               /* 昼の空(skyの淡色展開) */
  --amb-sun:      var(--ce-amber);       /* 太陽(核パレット流用) */
  --amb-dusk:     #33427A;               /* 夕暮れの群青 */
  --amb-night:    var(--ce-ink);         /* 夜(核パレット流用) */

  /* === Ambient: 自然物 === */
  --amb-mountain: #5C7A5E;               /* 山の緑(mossより明るい展開色) */
  --amb-forest:   var(--ce-moss);        /* 森(核パレット流用) */
  --amb-river:    #4A8C8C;               /* 川の青緑 */
  --amb-earth:    #8A6B4F;               /* 土・キャンプの地面 */
}
```

用途例: 時間帯に応じたセクション背景のグラデーション(昼→夕→夜のスクロール演出)、
イラスト・Instagramテンプレートの背景色。**必ず核パレットの文字色(silk/ink)と組み合わせ、
アンビエント色の上にアンビエント色の文字を置かない。**

### 7-3. 極彩色の滲みレイヤー(Stage Bleed)

ステージ照明の緑・赤・紫は「はっきりした色」としては使わず、多重radial-gradient+blurで
「輪郭のない光の滲み」として背景に漂わせる。

```css
:root {
  /* === Bleed: ブラー専用色(不透明度込み。UIでの単独使用禁止) === */
  --bleed-red:   rgba(216, 74, 58, 0.32);   /* ステージの赤 */
  --bleed-green: rgba(72, 196, 138, 0.28);  /* ステージの緑 */
  --bleed-haze:  rgba(139, 127, 199, 0.32); /* 紫煙・リバーブテール(v1.0のhazeはここに移設) */
}

.stage-bleed {
  position: relative;
  isolation: isolate;
}
.stage-bleed::before {
  content: "";
  position: absolute;
  inset: -10%;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(40% 35% at 20% 30%, var(--bleed-green), transparent 70%),
    radial-gradient(35% 40% at 78% 62%, var(--bleed-red),   transparent 70%),
    radial-gradient(50% 45% at 55% 15%, var(--bleed-haze),  transparent 70%);
  filter: blur(64px);
}

/* 滲みも素数拍で漂わせる(§3-3と同一思想): 各光源が別周期でずれ続ける */
@keyframes bleed-drift-a { 0%,100% { transform: translate(0,0); }   50% { transform: translate(3%, -2%); } }
@keyframes bleed-drift-b { 0%,100% { transform: translate(0,0); }   50% { transform: translate(-2%, 3%); } }
.stage-bleed--live::before { animation: bleed-drift-a 5.5s var(--ease-swell) infinite; }  /* 11拍 */
.stage-bleed--deep::before { animation: bleed-drift-b 6.5s var(--ease-swell) infinite; }  /* 13拍 */
```

### 7-4. 滲みレイヤーの制約(違反禁止)

1. `filter: blur()` は **48px以上**。輪郭が認識できる状態で極彩色を置かない
2. 1つの滲みに使う色は **最大3色**
3. 不透明度は各色 **0.35以下**。滲みの上の文字は必ずsilkで、コントラスト比4.5:1を維持する
4. 文字・ボタン・線・アイコン・罫線には bleed変数を使用しない(背景専用)
5. ヒーロー・セクション見出し背景など**1ページに滲み領域は2箇所まで**。全面に敷き詰めない

---

*Cocoon Experience Visual Language Guide v1.1 — この文書自体がポータブルな成果物です。他のAI・デザイナー・将来のメンバーに、このファイル1つを渡してください。*
