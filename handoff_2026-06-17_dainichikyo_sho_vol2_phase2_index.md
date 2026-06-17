# 引き継ぎメモ 2026-06-17 大日経疏 巻第二 Phase2 横断索引化 完了（17 著作目）

**日付**：2026-06-17／**種別**：kakikudashi-data Phase2（横断索引化）完成
**起点 HEAD**：`3b48fcb`（巻第二 genten 後送）／**ステータス**：Phase2 完成・検証全 pass・**未 commit / 未 push**

## 成果（横断索引化 17 著作目）
- **extract 6 本の `DICT_CORPUS_LIST`＋`aggregate_indices.py` の `ALL_CORPORA` に `dainichikyo-sho-vol2` 追加**。
- **per-corpus 索引 7 本生成**（`data/mikkyou/index_dainichikyo-sho-vol2_*.json`）：
  - terms：辞書 19 語中 matched 10／occ 42（kaimyo_suitable 11）
  - citations：unique 13・occ 21／kukai_works 0・0（善無畏/一行の注釈で空海著作引用なし＝妥当）
  - sanskrit：0・0（現代語訳の割注に IAST/ASCII 梵語なし。理趣経/理趣釈と同じ 0）
  - kaimyo_jukugo：unique 11・occ 29（matched 6・review 0）
  - persons：unique 11・occ 24（subcat 4）／places：unique 4・occ 16（subcat 3）
- **集約 7 本再生成**（17 著作）：terms occ 3677→3719・citations occ 2584→2605/unique 616→624・
  kukai_works 不変 65・sanskrit 不変 2684・kaimyo occ 5642→5671・persons occ 3351→3375・places occ 964→980。
  **集約増分＝per-corpus 件数 全 7 カテゴリ一致**を照合済（terms by_corpus vol2=42 等）。
- **manifest 更新**：vol2 に `index_status`（7 カテゴリ present・各 file/件数）付与・`summary.indexed_corpora` 各 16→17・
  `aggregate_indices.corpora_count` 16→17・`source_corpora` に vol2 追加・description 追記。
- **検証 全 pass**：倉庫側 `validate_corpus.py` 28/28 メカニカル整合 OK。`motifs.json` 不変。

## 残課題
- **Phase3 motif 抽出**：Phase A 合意（著者=善無畏口述・一行筆受＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・
  gabun は経典注釈系ゆえ意図的未設定〔hizoki/理趣釈/発菩提心論鈔と同運用〕・連動軸は完走後 retrofit）→
  outline 10 区分でラウンド分割（外道破／世間八心／六十心／百六十心三妄執／三劫五喩／宝珠喩／信解行地 等）。
  着手前に `references/motif-extraction.md` を読むこと。

## 注意：phantom staged deletion（既知の stale index）
- 本セッション時点で git index に render.yaml・start.bat・tsconfig.json・vercel.json・引き継ぎメモ_2026-05-06_*.md の
  **staged deletion** が出ているが、いずれも disk 上に実在し HEAD にもある＝phantom（CLAUDE.md にも繰り返し記録あり、本作業由来ではない）。
- commit_push.bat は Step 1-2 で index を HEAD にリセットするため通常は自動解消される。
  もし SAFETY CHECK が「deleted:」で中止したら fix_index.bat を実行してから commit_push.bat を再実行。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`（HEAD が本 Phase2 コミット）。
2. data/mikkyou/index_dainichikyo-sho-vol2_*.json（7 本）・index_*_all.json（corpora_count 17）。
3. Phase3 motif 抽出 に着手するかケンシン意向を確認。
