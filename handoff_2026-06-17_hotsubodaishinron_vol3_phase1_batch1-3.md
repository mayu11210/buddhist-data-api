# 引き継ぎメモ 2026-06-17 発菩提心論鈔 第三巻 Phase1 着手（段落化＋現代語訳バッチ1-3）

**日付**：2026-06-17／**種別**：kakikudashi-data Phase1（取込）着手
**起点 HEAD**：大日経疏 巻第二 完走後処理コミット（`2c9d184`）の後／**ステータス**：段落化完了・訳 36/70・**未 commit / 未 push**

## 対象
- ユーザー提供 doc『発菩提心論鈔 第三 宥快』。**宥快〔ゆうかい・1345-1416〕述**・『菩提心論』の注釈書（鈔）。至徳四年〔1387〕閏五月十日、宝性院にて談説。
- 第一巻（hotsubodaishinron-sho-vol1.json）と同じ著作シリーズの第三巻。**非空海（宥快）**＝Phase3 では 引用形式:典籍曰く。

## 成果（Phase1 着手）
- **docx 変換→70 段落 k001-k070 に段落化**（paras.json）。kakikudashi 19,645字。
- **outline 10 区分**：首題(k001)／目次(k002-k022)／奥書(k023)／菩提心の行相(k024-k028)／行相の三門と三摩地(k029-k036)／三種菩提心を戒とする義・三摩地の説黙(k037-k044)／三摩地の説黙〔顕密〕(k045-k048)／三門の列名と三種菩提心の分別(k049-k060)／行願の牒釈(k061-k068)／信の十義(k069-k070)。
- **現代語訳 batch1-3＝k001-k036 訳済**（butten-yasashii-yaku 文体）：
  - batch1 k001-k023（首題・目次・奥書）
  - batch2 k024-k028（菩提心の行相＝結前生後・四種の心・行相の解釈論）
  - batch3 k029-k036（行相の三門と三摩地・諸仏菩薩の因位の六義）
- **訳済 36/70・残 34**（最長 k043=4008字「三摩地の説黙・頓証」・k064=3184字「行願の牒釈」を含む）。
- ビルド素材を `_dev_references/hotsubodaishinron-sho-vol3_build/` に永続保存（source.docx・paras.json・outline.json・trans_1〜3.json）。
- 半角括弧0・NUL0（訳文は全角〔 〕割注のみ）。

## 取込方針（第一巻に準拠）
- ファイル名 `hotsubodaishinron-sho-vol3.json`、section「発菩提心論鈔 第三巻」、author「宥快」、source「宥快述・『菩提心論』の注釈書（鈔）」。
- base_text＝菩提心論（T1665）、base_text_ref relation:commentary_of（bodaishinron.json）。
- **genten（漢文原典）なし**（中世日本の鈔・大正蔵範疇外・第一巻と同じく書き下しのみ。genten=""・genten_source に理由）。
- **manifest 登録は全訳完了後**（未訳段落で validate を割らないため、corpus JSON は全訳まで WIP＝ビルド素材保持。data/kukai には未作成）。

## 残作業（順）
1. **現代語訳バッチ continue**：batch4 k037-k044〔三種菩提心を戒とする義・三摩地の説黙・k043 4008字〕→ batch5 k045-k060〔三摩地説黙顕密・三門の列名と三種菩提心の分別〕→ batch6 k061-k070〔行願の牒釈 k064 3184字・信の十義〕。各 trans_*.json に累積。
2. **全訳後**：scripts/build_corpus.py で hotsubodaishinron-sho-vol3.json をビルド（config に section/source/author/base_text_ref/outline/genten 空）→ skill validate＋倉庫 validate_corpus.py → register_manifest.py で登録（19 著作目）。
3. **Phase2 横断索引化**（extract 6本＋aggregate に追加・18 著作目）。
4. **Phase3 motif 抽出**（著者=宥快＝非空海→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit。第一巻 R1-R6 と同運用）。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. `_dev_references/hotsubodaishinron-sho-vol3_build/` の paras.json（k001-k070）・trans_1〜3.json（k001-k036 訳済）。
3. batch4（k037-〜）から現代語訳を継続。文体は butten-yasashii-yaku。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
