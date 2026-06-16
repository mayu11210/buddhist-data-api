# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 現代語訳バッチ3（世間八心区分・訳済 23/106）

**日付**：2026-06-15
**種別**：kakikudashi-data Phase1 現代語訳バッチ（進行中・複数セッション）
**起点 HEAD**：`833c0c0`（batch2・外道破完訳）
**ステータス**：batch3 完了・**訳済 23/106**・WIP・未 commit / 未 push（commit_push.bat 実行待ち）

## 進捗
- 訳済 k001-k023（23/106）＝品題＋三十外道破＋世間八心・殊勝心決定心。残 83（k024-k106）。
- batch1 k001-k006／batch2 k007-k018／batch3 k019-k023。

## 残バッチ（順）
| batch | 区分 | k範囲 | 段 |
|---|---|---|---|
| 4-8 | 六十心（貪心〜猨猴心） | k024-k079 | 56（~12段ずつ） |
| 9 | 百六十心・三妄執 | k080-k091 | 12 |
| 10 | 第一劫 五喩・法無我 | k092-k097 | 6 |
| 11 | 第二劫・第三劫・宝珠 | k098-k102 | 5 |
| 12 | 信解行地 | k103-k106 | 4 |
※六十心 k024-k079 は 第二無貪心 k025 から番号付き・第一貪心は k024（秘密主よ彼云何が貪心）。各心は ~100-200字 の短段が多く、~12段ずつでバッチ化。

## ビルド手順（次セッション継続）
ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/`（paras.json・trans_1〜3.json・config_template.json・底本）。
1. `trans_4.json` に {"24":"訳",...}（キー＝k番号）。
2. config_template の `<REPO>` を実パス置換し config.json 化。
3. `python3 <skill>/scripts/build_corpus.py config.json`。
4. 半角括弧0・NUL0 確認。

## 文体（butten-yasashii-yaku）
平易・割注〔 〕で原語温存・半角括弧禁止・対句保持。六十心は各心の喩（牛羊/河/井/猫狸/狗/迦樓羅/鼠 等）と対治法を平易に。

## 残課題（全訳後）
manifest 登録 → 倉庫側 validate → genten 後送（T1796 vol.39 巻第二）→ Phase2 横断索引化 → Phase3 motif 抽出（著者=善無畏/一行＝非空海→引用形式:典籍曰く）。

## 留意（git）
commit_push.bat 前に fix_index.bat。

## 次セッション確認
1. CLAUDE.md 冒頭 → 本メモ → git log
2. dainichikyo-sho-vol2.json：訳済 23/106
3. build 素材でバッチ継続（次 batch4 六十心 k024-）
