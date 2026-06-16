# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 現代語訳バッチ4（六十心前半・訳済 35/106）

**日付**：2026-06-15／**種別**：kakikudashi-data Phase1 現代語訳バッチ（進行中）
**起点 HEAD**：`bee1c61`（batch3）／**ステータス**：batch4 完了・**訳済 35/106**・WIP・未 push

## 進捗
- 訳済 k001-k035（35/106）＝品題＋三十外道破＋世間八心＋六十心 第一〜第十二。残 71（k036-k106）。

## 残バッチ（順）
| batch | 区分 | k範囲 | 段 |
|---|---|---|---|
| 5 | 六十心 第十三〜第○ | k036-k047 目安 | ~12 |
| 6 | 六十心 続き | k048-k059 目安 | ~12 |
| 7 | 六十心 残＋第六十 | k060-k079 | ~20（短段多） |
| 8 | 百六十心・三妄執 | k080-k091 | 12 |
| 9 | 第一劫 五喩・法無我 | k092-k097 | 6 |
| 10 | 第二劫・第三劫・宝珠 | k098-k102 | 5 |
| 11 | 信解行地 | k103-k106 | 4 |
※六十心 k024-k079 は各心 ~100-300字。第十三諍心 k036 以降。区切りは適宜。

## ビルド手順
ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/`（paras.json・trans_1〜4.json・config_template.json）。
trans_5.json に {"36":"訳",...} → config_template の <REPO> 置換 → build_corpus.py → 半角括弧0/NUL0 確認。

## 文体
butten-yasashii-yaku：平易・割注〔 〕で原語温存・半角括弧禁止。六十心は各心の喩と対治を平易に。

## 残課題（全訳後）
manifest 登録 → 倉庫側 validate → genten 後送（T1796 vol.39 巻第二）→ Phase2 横断索引化 → Phase3 motif（著者=善無畏/一行＝非空海→引用形式:典籍曰く）。

## 留意：commit_push.bat 前に fix_index.bat。
## 次セッション：CLAUDE.md 冒頭→本メモ→git log。訳済 35/106。次 batch5 k036-。
