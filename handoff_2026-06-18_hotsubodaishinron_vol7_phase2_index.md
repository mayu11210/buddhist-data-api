# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第七巻 Phase2 横断索引化 完了（23 著作目）

**日付**：2026-06-18／**種別**：kakikudashi-data Phase2（横断索引化）完成
**起点 HEAD**：発菩提心論鈔 第七巻 Phase1 完成（`0ff9453`）／**ステータス**：Phase2 完成・検証全 pass・**未 commit / 未 push**

## 成果（横断索引化 23 著作目）
- extract 6本の `DICT_CORPUS_LIST`＋`aggregate_indices.py` の `ALL_CORPORA` に `hotsubodaishinron-sho-vol7` 追加。
- **per-corpus 索引 7本生成**（`data/mikkyou/index_hotsubodaishinron-sho-vol7_*.json`）：
  - terms：辞書 19 語中 matched 8／occ 83（kaimyo_suitable 11）
  - citations：unique 37・occ 60／kukai_works 6・occ 18
  - sanskrit：unique 0・occ 0（注釈書・割注に IAST なし）
  - kaimyo_jukugo：unique 11・occ 63（matched 7・review 0）
  - persons：unique 6・occ 23（subcat 3）／places：unique 3・occ 21（subcat 3）
- **集約 7本再生成（23 著作）**：corpora_count 22→23・全カテゴリで vol7 反映を確認。
  全 7 カテゴリ合計：unique_terms 2,845／occurrences 21,246。
- **manifest 更新**：vol7 に `index_status`（7 カテゴリ present・各 file/件数）付与・`summary.indexed_corpora` 各 22→23・
  `aggregate_indices.corpora_count` 22→23・`source_corpora` に vol7 追加。
- **検証 全 pass**：倉庫 `validate_corpus.py` 34/34 メカニカル整合 OK。`motifs.json` 不変。

## 残課題
- **Phase3 motif 抽出**：Phase A 合意は第一〜六巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。目次 k001-k035／尾題 k097 は motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる。
- 完走後：連動軸 retrofit（候補＝sg17 十住心〔第六住心・超十地〕／sg22 三種菩提心〔勝義行願三摩地〕／sg03 即身成仏〔従凡入仏位・父母所生身速証大覚位〕／sg12 化城宝処 等）／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/mikkyou/index_hotsubodaishinron-sho-vol7_*.json（7本）・index_*_all.json（corpora_count 23）。
3. Phase3 motif 抽出 から着手。

## 注意：bash マウント stale（既知）／phantom staged deletion（既知）
bash マウント経由の grep/wc は古い版を表示することがある（virtiofs）。検証は Read/Edit ツールと git を真値とする。package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
