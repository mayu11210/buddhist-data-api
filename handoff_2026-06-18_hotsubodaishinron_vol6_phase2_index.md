# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第六巻 Phase2 横断索引化 完了（22 著作目）

**日付**：2026-06-18／**種別**：kakikudashi-data Phase2（横断索引化）完成
**起点 HEAD**：発菩提心論鈔 第六巻 Phase1 完成（`f1d85cc`）／**ステータス**：Phase2 完成・検証全 pass・**未 commit / 未 push**

## 成果（横断索引化 22 著作目）
- extract 6本の `DICT_CORPUS_LIST`＋`aggregate_indices.py` の `ALL_CORPORA` に `hotsubodaishinron-sho-vol6` 追加。
- **per-corpus 索引 7本生成**（`data/mikkyou/index_hotsubodaishinron-sho-vol6_*.json`）：
  - terms：辞書 19 語中 matched 4／occ 15（kaimyo_suitable 11）
  - citations：unique 49・occ 96／kukai_works 5・occ 11
  - sanskrit：unique 0・occ 0（注釈書・割注に IAST なし）
  - kaimyo_jukugo：unique 11・occ 15（matched 4・review 0）
  - persons：unique 5・occ 25（subcat 2）／places：unique 1・occ 1（subcat 1）
- **集約 7本再生成（22 著作）**：corpora_count 21→22・全カテゴリで vol6 反映を確認。
  全 7 カテゴリ合計：unique_terms 2,832／occurrences 20,978。
- **manifest 更新**：vol6 に `index_status`（7 カテゴリ present・各 file/件数）付与・`summary.indexed_corpora` 各 21→22・
  `aggregate_indices.corpora_count` 21→22・`source_corpora` に vol6 追加。
- **検証 全 pass**：倉庫 `validate_corpus.py` 33/33 メカニカル整合 OK。`motifs.json` 不変。

## 残課題
- **Phase3 motif 抽出**：Phase A 合意は第一〜五巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。目次 k001-k036／尾題 k106 は motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる。
- 完走後：連動軸 retrofit（候補＝sg17 十住心／sg22 三種菩提心／sg12 化城宝処／sg11 良医病子 等）／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/mikkyou/index_hotsubodaishinron-sho-vol6_*.json（7本）・index_*_all.json（corpora_count 22）。
3. Phase3 motif 抽出 から着手。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
