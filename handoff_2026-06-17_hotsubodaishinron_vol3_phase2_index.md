# 引き継ぎメモ 2026-06-17 発菩提心論鈔 第三巻 Phase2 横断索引化 完了（18 著作目）

**日付**：2026-06-17／**種別**：kakikudashi-data Phase2（横断索引化）完成
**起点 HEAD**：発菩提心論鈔 第三巻 Phase1 完成（`61abe0e`）／**ステータス**：Phase2 完成・検証全 pass・**未 commit / 未 push**

> ※ 本作業の途中で PC が突然再起動したが、push 済みの Phase1（`61abe0e`）は GitHub 上に安全。commit 前だった Phase2 の working 変更も全ファイルがディスクに残存し、再パース／NUL0／スクリプト構文／倉庫 validate 29/29 で**無損を確認済み**。

## 成果（横断索引化 18 著作目）
- extract 6本の `DICT_CORPUS_LIST`＋`aggregate_indices.py` の `ALL_CORPORA` に `hotsubodaishinron-sho-vol3` 追加。
- **per-corpus 索引 7本生成**（`data/mikkyou/index_hotsubodaishinron-sho-vol3_*.json`）：
  - terms：辞書 19 語中 matched 12／occ 300（kaimyo_suitable 11）
  - citations：unique 51・occ 106／kukai_works 6・occ 13
  - sanskrit：unique 1・occ 1（IAST 1）
  - kaimyo_jukugo：unique 11・occ 183（matched 8・review 0）
  - persons：unique 14・occ 65（subcat 4）／places：unique 2・occ 29（subcat 2）
- **集約 7本再生成（18 著作）**：terms occ 3719→4019・citations occ 2605→2711/unique 624→650・kukai_works occ 65→78・
  sanskrit occ 2684→2685・kaimyo occ 5671→5854・persons occ 3375→3440・places occ 980→1009。
  **集約増分＝per-corpus 件数 全 7 カテゴリ一致**を照合済。
- **manifest 更新**：vol3 に `index_status`（7 カテゴリ present・各 file/件数）付与・`summary.indexed_corpora` 各 17→18・
  `aggregate_indices.corpora_count` 17→18・`source_corpora` に vol3 追加・description 追記。
- **検証 全 pass**：倉庫 `validate_corpus.py` 29/29 メカニカル整合 OK。`motifs.json` 不変。
- CLAUDE.md は Phase2 エントリ追記済み（再起動前に完了）。

## 残課題
- **Phase3 motif 抽出**：Phase A 合意は第一巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。outline の本文区分でラウンド分割。目次 k001-k023 は首題・目次ゆえ motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる（第一巻 R1-R6 同運用）。
- 完走後：連動軸 retrofit／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/mikkyou/index_hotsubodaishinron-sho-vol3_*.json（7本）・index_*_all.json（corpora_count 18）。
3. Phase3 motif 抽出 から着手。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
