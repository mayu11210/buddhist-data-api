# handoff 2026-06-24 — 大日経疏 巻第十六 取込（Phase1＋genten＋Phase2）完了

## 到達点
大日経疏 巻第十六（`data/kukai/dainichikyo-sho-vol16.json`・善無畏口述/一行筆受＝**非空海**）の
**取込ひとまとめ（Phase1＋genten＋Phase2 横断索引化＝40著作目）が完了**。新運用に従い、この3工程は
**1 push に集約（push1＝取込）**する。`commit_message.txt` を更新済み。`commit_push.bat` 実行待ち。

- 40 著作目。motif は次フェーズで **m3679 から連番**（現 motifs.json total 3709・最終 m3678・不変）。
- 倉庫 `validate_corpus.py` **51/51 OK**。

## ★新運用ルール（2026-06-23 ケンシン決定・巻第十六から適用）
- push は1巻あたり **3回に集約**：①取込（Phase1＋genten＋Phase2）／②motif（全ラウンド＋retrofit＋gabun）／③kaimyo-app 同期（別リポジトリ・単独）。
- Phase3 の motif 判定表は **全ラウンド分をまとめて提示→確認後 止めずに一気に処理**。各ラウンドの build は個別に dry-run＋assert＋backup・schema_history／handoff／CLAUDE.md 追記も**ラウンドごとに個別**に残す（検証粒度は従来どおり）。
- 本ルールは CLAUDE.md タイトル行に一文記録済（取込コミットに同梱・単独 push しない）。

## 巻第十六の内容（3品）
1. 秘密漫荼羅品 第十一之余（金剛手の偈問への答＝果数寿量三昧悉地・心の無自性／五事＝印色尊位住三昧／秘密中の秘たる秘密漫荼羅の法と作法〔四方漫荼羅・十字金剛印・九点・十二字真言王・四菩薩〕／三部〔仏部・蓮華部・金剛部〕＋釈迦部・菩薩部の尊別印相）
2. 入秘密漫荼羅品 第十二（唯仏与仏・持金剛智印／阿闍梨の遍学資格／弟子の業煩悩を方便智火で焼く字観〔阿・囉・嚩〕／十二字真言王の身布／三昧耶＝我等仏仏等我／末代の妄師への戒め）
3. 入秘密漫荼羅位品 第十三（等至三昧／毘盧遮那＝日／大悲胎蔵荘厳／内心の秘密漫荼羅〔五大字観・八葉の諸仏配置・暗字潅頂・花投〕・証入）

## Phase1（corpus）
- 段落化：元 doc 12ブロック（本文7ブロック・最大10,404字）を科文・話題境界で**本文66段**に分割＋構造5段（k001 首題／k002 撰号／k003・k041・k051 品題3品）＝**全71段 k001-k071**。
- **重複ブロックなし**（vol15 のような重複は無し。全文連結＝段落化前の科文連結と完全一致 assert pass・kk 27,575字）。
- 現代語訳 butten-yasashii-yaku **43,111字**（6バッチ・共通 GLOSSARY・半角括弧0・全71段訳済）。
- corpus 構造は vol15 同型（section/source/base_text/genten/genten_source/text/format_note/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs〔id・section_major・section・kakikudashi・gendaigoyaku〕）。
- manifest：vol16 entry を vol15 直後に登録・summary（total_files 50→51・primary 36→37・kk/gd present 37→38）。

## genten（CBETA T1796_016）
- Chrome で `https://cbetaonline.dila.edu.tw/zh/T1796_016` を取得（#body の `.juan/.byline/.div-pin>.head/.div-pin>p` 構造）。
- 夾註96（`.inline-note.doube-line-note`）を ( )→〔 〕化／`.lb`(行番号 T39n1796_p…)・`.lb_br`・`.noteAnchor`・`.note-link`・`.scan-image-display-btn`・`.glyphicon`・`.label`・`.lineInfo` 除去。
- gaiji 2種 Unicode 保持：𤙖 U+24656×1・𭄍 U+2D10D×2（悉曇なし）。
- **content 図版4点**（`.div-figure>img.graphic`）：T39p0742_01/02/03＝曼荼羅形・T39p0743_01＝仏頂印。Unicode 等価字なきため **〔図 ID〕で位置保持**（ケンシン裁定）。
- バイト一致：blob download が Downloads 既存ファイルと衝突したため、図版なし版 download（SHA d946587d…）に4図版ブロックを規定位置へ挿入し再構成。全文 **SHA-256 `5334c95c5dc8a812140fe0719ceb948cd6e8243e11f351e563599fb7eac44355`** をブラウザ側計算値とバイト一致照合（UTF-8 47,379 bytes・cp 15,906・改行75・excl-nl 15,831）。
- corpus.genten 投入・genten_unavailable_reason 削除・char_counts.genten=15831・manifest genten_present 24→25。
- clean txt 保存：`_dev_references/dainichikyo-sho-vol16_build/genten_T1796_016_clean.txt`。

## Phase2（横断索引化・40著作目）
- `_dev_references/extract_{terms,citations,sanskrit,kaimyo_jukugo,persons,places}_dict.py` の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に vol16 追加。
- per-corpus 7本生成（`data/mikkyou/index_dainichikyo-sho-vol16_*.json`）：terms 9/19 occ141・citations 2（法華経・金剛頂経）・kukai_works 0・sanskrit 1（citta）・kaimyo unique11 occ116・persons 16 occ96・places 2 occ10。
- aggregate 7本再生成（**40著作**・corpora_count 39→40・summary.indexed_corpora 各39→40・aggregate 合計 unique 3,264／occ 27,869）。
- **注意（既存挙動の踏襲）**：places の「殷（商）」9件は本文「商佉〔法螺貝〕」の「商」の**誤検出**。seed辞書が商を殷/Shang の別名とするため。vol11-14 も同型に誤検出済み。**vol16 のみ是正せず既存と同挙動を踏襲**（seed の全体見直しは別課題）。

## 次フェーズ（push2＝motif）— Phase A 合意（巻第二〜十五 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に「引用形式:典籍曰く」・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十六`／`引用形式:典籍曰く`。
- gabun（雅文体訳）は意図的未設定・連動軸は完走後 retrofit・1段=1motif（束ねは語中切れ等のみ）。
- 首題/撰号/品題（k001/k002/k003/k041/k051）は motif 化しない → **motif 対象は本文66段**。
- m3679 から連番。判定表は全ラウンドまとめて提示→一気に処理（新運用）。着手前に `references/motif-extraction.md` を再読。

## 次フェーズ（push3＝kaimyo-app 同期）
- 要フォルダ接続（kaimyo-app）。motifs.json コピー・SHA-256 一致確認。motif 完走後。

## 検証ログ（pass）
- Phase1：JSON再パースOK・NUL0・全71段訳済・半角括弧0・段落連結 assert pass・validate 51/51。
- genten：SHA-256 バイト一致（ブラウザ⇔Python）・夾註/校勘/gaiji 検査・validate 51/51。
- Phase2：per-corpus 7本＋aggregate 7本生成・indexed_corpora 各40・validate 51/51。

## commit_push 注意
- `commit_push.bat` は data/kukai/・data/mikkyou/・_dev_references/・CLAUDE.md・root *.md をディレクトリ単位で stage（vol16 追加分を網羅）。
- Step4.5 の SAFETY CHECK で `deleted:` を検出したら phantom deletion の疑い → 中断・ホスト実体確認。今回は追加・修正のみで削除なしの想定。
