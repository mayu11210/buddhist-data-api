# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 現代語訳バッチ6（六十心 第二十五〜第三十七・訳済 59/106）

**日付**：2026-06-15／**種別**：kakikudashi-data Phase1 現代語訳バッチ（進行中）
**起点 HEAD**：`e8e6292`（batch5）／**ステータス**：batch6 完了・**訳済 59/106**（過半数）・WIP・未 push

## 進捗
訳済 k001-k059（59/106）＝品題＋外道破＋八心＋六十心 第一〜第三十七。残 47（k060-k106）。

## 残バッチ（順）
| batch | 区分 | k範囲 | 段 |
|---|---|---|---|
| 7 | 六十心 第三十八〜第六十＋百六十心総括 | k060-k079 | 20 |
| 8 | 百六十心・三妄執 | k080-k091 | 12 |
| 9 | 第一劫 五喩・法無我 | k092-k097 | 6 |
| 10 | 第二劫・第三劫・宝珠 | k098-k102 | 5 |
| 11 | 信解行地 | k103-k106 | 4 |
※第三十八烏心 k060〜。第六十猨猴心 k079。k060-k079 は短段多くまとめ訳可。

## ビルド手順
ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/`（paras.json・trans_1〜6.json・config_template.json）。
trans_7.json に {"60":"訳",...} → config_template の <REPO> 置換 → build_corpus.py → 半角括弧0/NUL0 確認。

## 文体：butten-yasashii-yaku（平易・割注〔 〕で原語温存・半角括弧禁止）。
## 残課題（全訳後）：manifest 登録→倉庫側 validate→genten 後送（T1796 vol.39 巻第二）→Phase2 横断索引化→Phase3 motif（著者=善無畏/一行＝非空海→引用形式:典籍曰く）。
## 留意：commit_push.bat 前に fix_index.bat。
## 次セッション：CLAUDE.md 冒頭→本メモ→git log。訳済 59/106。次 batch7 k060-。
