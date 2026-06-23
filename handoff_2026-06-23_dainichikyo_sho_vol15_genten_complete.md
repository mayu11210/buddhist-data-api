# 引き継ぎメモ — 大日経疏 巻第十五 genten 後送 完了（2026-06-23）

Phase1 取込（commit `b3dffa8`）に続けて、漢文原典（genten）を後送した。巻第十三・十四と同手順。

## 取得・清掃
- **取得**：CBETA 線上閱讀 `https://cbetaonline.dila.edu.tw/zh/T1796_015` を Chrome 経由で取得（JS レンダリング）。`#body` の DOM 構造から `.juan`（首題）・`.byline`（撰号）・`.div-pin > p.head`（品題）＋本文 `.div-pin > p`（20 段）を抽出。CBETA の自然段落構造（本文20段）をそのまま genten のブロック構造に採用。
- **清掃**（DOM clone 上で実施）：
  - 夾註 `.inline-note.doube-line-note` 62 組を ( ) → 〔 〕 に変換。
  - 校勘アンカー・マーカー除去：`.noteAnchor`／`.note-link`／`.note-link-cbeta`／`.star`。
  - 行番号・UI 除去：`.lb`（T39n1796_p… の行頭ラベル）／`.lb_br`（BR）／`.scan-image-display-btn`／`.label`／`.glyphicon`。
  - gaiji 1字 `𨷂`（U+28DC2・`.gaijiAnchor`）は Unicode 保持。
  - **半月形の図 1 件**（`.graphic` img `T39p0735_01.gif`・Unicode 無し）は、本文「方□…圓○…三角△…半月◗其中雜色」の幾何記号列の文脈に合わせ **半月記号 ◗（U+25D7）で代替**。原典は CBETA の図版で、Unicode 字が存在しないための代替。
  - 悉曇 IAST 2 組（`ram`・`.siddam`）は半角括弧 `(ram)` のまま温存。

## 検証（バイト一致）
- 構成した genten をブラウザで Blob ダウンロード（`genten_T1796_015.txt`）→ Downloads マウントで読込。
- 全文 SHA-256 **`56ef036666bd166fb1d5203529fbeddaaa76d751ed17029e88afbbd8d56901ae`** をブラウザ側・Python 側で照合しバイト一致を確認（UTF-8 **52,750 bytes**）。
- 注意：JS の `string.length` は 17,642、Python `len()` は 17,641 で +1 差があるが、これは astral gaiji `𨷂`（U+28DC2）が UTF-16 では 2 単位・code point では 1 のため。UTF-8 バイト数と SHA-256 が一致しているので本文は同一。
- 字数：17,641字cp（改行45含む）・改行除外 **17,596字**。夾註〔〕62組・半角括弧2組（IAST のみ）・残存校勘 `[n]` 0・NUL 0。

## 更新
- corpus `data/kukai/dainichikyo-sho-vol15.json`：`genten` 充填・`genten_source` を CBETA 出典に更新・`genten_unavailable_reason` 削除。
- `_corpus_manifest.json`：vol15 の `data_status.genten=true`・`genten_unavailable_reason` 削除・`char_counts.genten=17596`・notes に genten 後送の経緯追記・`summary.genten_present 23→24`。
- ビルド素材 `_dev_references/dainichikyo-sho-vol15_build/genten_T1796_015_clean.txt` に永続保存。
- CLAUDE.md 冒頭に ★ genten 後送 完了 エントリ追記。
- 倉庫 `validate_corpus.py` 全 50 件メカニカル整合 OK（ERROR/WARNING 0）。

## Phase1 段落化の重複除去との関係（重要・要確認事項の決着）
Phase1 で原 doc（書き下し）に検出した「35文ぶんの重複ブロック」（三昧耶五種・秘密漫荼羅五種・善住観覚の段）について、**今回の CBETA genten（原典）側には重複は存在しない**ことを確認した（genten 本文20段は重複なしで連続）。すなわち Phase1 で後出の重複を除去した判断は正しく、書き下し側の重複は doc 作成時のコピー由来であったと確定。

## 残課題
1. **Phase2 横断索引化**（39 著作目）：extract 6本＋aggregate に dainichikyo-sho-vol15 追加 → per-corpus 7本生成 → 集約 7本再生成 → manifest index_status 7カテゴリ present・summary.indexed_corpora 各 38→39。
2. **Phase3 motif 抽出**（ラウンド制）：著者＝善無畏口述/一行筆受＝非空海 → `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十四 同運用）。
3. **kaimyo-app 同期**（Phase3 後・別リポジトリ）。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝genten 後送 に更新済み）。push 後 `git log` 先頭が本件・`origin/main..HEAD` 空を確認。その後 Phase2 横断索引化へ。
