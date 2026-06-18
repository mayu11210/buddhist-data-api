# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第五巻 Phase2 横断索引化 完了（21 著作目）

**日付**：2026-06-18／**種別**：kakikudashi-data Phase2（横断索引化）完成
**起点 HEAD**：発菩提心論鈔 第五巻 Phase1 完成（`b9402d1`）／**ステータス**：Phase2 完成・検証全 pass・**未 commit / 未 push**

## 成果（横断索引化 21 著作目）
- extract 6本の `DICT_CORPUS_LIST`＋`aggregate_indices.py` の `ALL_CORPORA` に `hotsubodaishinron-sho-vol5` 追加。
- **per-corpus 索引 7本生成**（`data/mikkyou/index_hotsubodaishinron-sho-vol5_*.json`）：
  - terms：辞書 19 語中 matched 5／occ 32（kaimyo_suitable 11）
  - citations：unique 55・occ 85／kukai_works 5・occ 15
  - sanskrit：unique 0・occ 0（注釈書・割注に IAST なし）
  - kaimyo_jukugo：unique 11・occ 31（matched 4・review 0）
  - persons：unique 4・occ 12（subcat 3）／places：unique 4・occ 19（subcat 2）
- **集約 7本再生成（21 著作）**：corpora_count 20→21・全カテゴリで vol5 反映を確認。
  全 7 カテゴリ合計：unique_terms 2,807／occurrences 20,815。
- **manifest 更新**：vol5 に `index_status`（7 カテゴリ present・各 file/件数）付与・`summary.indexed_corpora` 各 20→21・
  `aggregate_indices.corpora_count` 20→21・`source_corpora` に vol5 追加。
- **検証 全 pass**：倉庫 `validate_corpus.py` 32/32 メカニカル整合 OK。`motifs.json` 不変。

## 残課題
- **Phase3 motif 抽出**：Phase A 合意は第一/二/三/四巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。outline の本文区分でラウンド分割。目次 k001-k035／尾題 k103 は motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる。
- 完走後：連動軸 retrofit（候補＝sg22 三種菩提心〔勝義菩提心〕／sg17 十住心〔九種住心無自性・嬰童無畏心〕／sg18 顕密二教 等）／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/mikkyou/index_hotsubodaishinron-sho-vol5_*.json（7本）・index_*_all.json（corpora_count 21）。
3. Phase3 motif 抽出 から着手。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
