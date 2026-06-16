# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 現代語訳バッチ5（六十心 第十三〜第二十四・訳済 47/106）

**日付**：2026-06-15／**種別**：kakikudashi-data Phase1 現代語訳バッチ（進行中）
**起点 HEAD**：`1066d9a`（batch4）／**ステータス**：batch5 完了・**訳済 47/106**・WIP・未 push

## 進捗
訳済 k001-k047（47/106）＝品題＋外道破＋八心＋六十心 第一〜第二十四。残 59（k048-k106）。

## 残バッチ（順）
| batch | 区分 | k範囲 | 段 |
|---|---|---|---|
| 6 | 六十心 第二十五〜 | k048-k059 | 12 |
| 7 | 六十心 〜第六十＋総括 | k060-k079 | 20 |
| 8 | 百六十心・三妄執 | k080-k091 | 12 |
| 9 | 第一劫 五喩・法無我 | k092-k097 | 6 |
| 10 | 第二劫・第三劫・宝珠 | k098-k102 | 5 |
| 11 | 信解行地 | k103-k106 | 4 |
※第二十五井心 k048 以降。第六十猨猴心 k079。

## ビルド手順
ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/`（paras.json・trans_1〜5.json・config_template.json）。
trans_6.json に {"48":"訳",...} → config_template の <REPO> 置換 → build_corpus.py → 半角括弧0/NUL0 確認。

## 文体：butten-yasashii-yaku（平易・割注〔 〕で原語温存・半角括弧禁止）。
## 残課題（全訳後）：manifest 登録→倉庫側 validate→genten 後送（T1796 vol.39 巻第二）→Phase2 横断索引化→Phase3 motif（著者=善無畏/一行＝非空海→引用形式:典籍曰く）。
## 留意：commit_push.bat 前に fix_index.bat。
## 次セッション：CLAUDE.md 冒頭→本メモ→git log。訳済 47/106。次 batch6 k048-。
