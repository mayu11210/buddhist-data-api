# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 現代語訳バッチ2（外道破完訳・訳済 18/106）

**日付**：2026-06-15
**種別**：kakikudashi-data Phase1 現代語訳バッチ（進行中・複数セッション）
**起点 HEAD**：`c107aab`（巻第二 Phase1 着手・batch1）
**ステータス**：batch2 完了・**訳済 18/106**・WIP・未 commit / 未 push（commit_push.bat 実行待ち）

## 進捗
- **訳済 k001-k018（18/106）**＝品題＋三十外道の破 完訳。残 88（k019-k106）。
- batch1：k001-k006（品題＋外道破前半）。batch2：k007-k018（外道破後半）。

## 残バッチ（目安・順）
| batch | 区分 | k範囲 | 段数 |
|---|---|---|---|
| 3 | 世間八心・殊勝心決定心 | k019-k023 | 5 |
| 4-8 | 六十心（貪心〜猨猴心） | k024-k079 | 56（~12段ずつ5バッチ） |
| 9 | 百六十心・三妄執 | k080-k091 | 12 |
| 10 | 第一劫 五喩・法無我 | k092-k097 | 6 |
| 11 | 第二劫・第三劫・宝珠 | k098-k102 | 5 |
| 12 | 信解行地 | k103-k106 | 4 |

## ビルド手順（次セッション継続）
ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/`（paras.json・trans_1.json・trans_2.json・config_template.json・底本txt）。
1. `trans_3.json` に {"19":"訳",...}（キー＝k番号）を書く。
2. config_template の `<REPO>` を当セッション実パスに置換し config.json 化。
3. `python3 <skill>/scripts/build_corpus.py config.json` で再生成。
4. 半角括弧0・NUL0 確認。

## 文体（butten-yasashii-yaku）
平易な現代語に組み替え・原語/術語は割注〔 〕で多め温存・半角括弧禁止・対句保持。外道名/論師名/玄奘訳の誤り等は割注で補う。

## 残課題（全訳後）
manifest 登録（dict_paragraphs・role_complete）→ 倉庫側 validate → genten 後送（T1796 vol.39 巻第二）→ Phase2 横断索引化 → Phase3 motif 抽出（著者=善無畏/一行＝非空海→引用形式:典籍曰く）。

## 留意（git）
commit_push.bat 前に fix_index.bat。

## 次セッション確認
1. CLAUDE.md 冒頭 → 本メモ → git log
2. dainichikyo-sho-vol2.json：訳済 18/106
3. build 素材でバッチ継続（次 batch3 k019-k023）
