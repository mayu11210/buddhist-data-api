# handoff: sg04 一切衆生悉有仏性への anchor 設計 完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：b5b7100（sg05 anchor 設計・push 済確認済）／kaimyo-app 2c78cc5（4269 同期済・SHA-256 一致）
**種別**：retrofit 7 型類例（既存 sg の anchor 化・新規 sg なし・補注 KKK 副次発見〔sg04・sg06 members 0〕の前半解消）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg04 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-04）

1. **最優先タスク**：候補 (b) sg04 anchor 設計を採用（sg06・(c) 新著作取込より優先）
2. **anchor＝m3081 単軸**（大日経疏 巻第六「一切の心有る者は悉く仏性有り。この仏性を、
   すなわち首楞厳定と名け、亦た金剛三昧と名け、亦た般若波羅蜜と名く」＝**涅槃経文の直接引用
   （経文 locus）**・核心既付与・既連動なし→自己参照 連動:sg04＋連動:m3081 の 2 タグ＝
   sg33/m4183 先例）。m2662 二軸化案（発菩提心論鈔 巻四・科段名「一切衆生悉有仏性」
   near-verbatim＋如来蔵十義＋自宗実義だが注釈 locus）・m2661 案（主題:一切衆生悉有仏性
   既付与だが釈文導入部）・二重 anchor 案は不採用（教理 locus 性を優先＝sg01/sg05 判例）。
   m3081 の段落 k031（dainichikyo-sho-vol6）は保留中の k031（大智度論・genten 無し）とは
   **別段落＝干渉なし**
3. **スコープ**：仏性/佛性 本文含有 38 件＋タグ追補 6 件（主題:如来蔵 m2808/m2809/m3907・
   主題:本覚 m449/m2707・主題:一切衆生悉有仏性 m2745）＝**44 件全件判定**（sg05 判例＝母数
   小規模）。主題:本来性 241 件のフルスキャンはしない（軸拡散防止＝sg33 スコープ判例）
4. **Phase B**：判定表（anchor＋○12＋△9＝22 件付与・温存 17・×5）全件承認

## 成果（motifs.json・タグのみ変更 +44）

**連動 +44**（22 motif・各件 連動:sg04＋連動:m3081・既付与該当なしのため重複回避不要）：

| 区分 | motif | 内容 |
|---|---|---|
| anchor | m3081 | 大日経疏 巻六「一切の心有る者は悉く仏性有り」＝涅槃経文引用・自己参照 2 タグ |
| ○ | m2661 | 「一切衆生皆本覚の仏性を具足して…堪任せり」主題:一切衆生悉有仏性 既付与 |
| ○ | m2662 | 悉有仏性の正面釈＋如来蔵十義＋自宗実義（sg20 と二軸） |
| ○ | m2673 | 「一切衆生畢竟成仏と知る故」不軽行 |
| ○ | m2654 | 「これ皆一切衆生悉有仏性の義を明かす」明示 |
| ○ | m2745 | 五性各別 対 一性皆成・主題:一切衆生悉有仏性 既付与 |
| ○ | m508 | 華厳経「一衆生として真如智慧を具足せずということなし」 |
| ○ | m2990 | 有余記「一切衆生に悉く仏性ありて…無上菩提に至るべし」 |
| ○ | m759 | 性霊集「有形有識は必ず仏性を具す」 |
| ○ | m856 | 「蠉飛蠕動仏性あらざること無し」典故:涅槃経 既付与 |
| ○ | m87 | 「蚑行蝡動何れか仏性無からん」 |
| ○ | m91 | 「鱗衫羽袍、蹄舃角冠、誰か仏性無からん」 |
| ○ | m116 | 「有情非情、動物植物、同じく平等の仏性を鑒みて」（草木成仏まで拡張） |
| △ | m2909 | 質多釈「無遷変は仏性・般若波羅蜜・首楞厳三昧」＝anchor と同系涅槃経文 |
| △ | m2987 | 「衆生仏性の乳」→五味→醍醐（涅槃経五味譬系統） |
| △ | m3647 | 「一切如来は皆仏性の種子、菩提心より生ず」 |
| △ | m2803 | 六大の異名＝自性清浄心真如仏性如来蔵法性 |
| △ | m2305 | 率都婆を「仏性とも如来蔵とも」観ず |
| △ | m2455 | 「一切有情に皆不壊にして金剛の仏性あり」 |
| △ | m2808 | 「一切有情如来蔵の心を含す」（sg22 と二軸） |
| △ | m2809 | 如来蔵性問答 |
| △ | m132 | 「法雷は永蟄の仏性を驚かし」 |

**温存 17**：m2996（歯木作法）・m2380（月輪観想譬）・m2504（惣持語釈）・m3907（性空文脈＝
sg21 既）・m449/m2707/m1949（本覚周辺・焦点別）・m1960（迷妄側）・m228/m238/m303（心性・
開顕メタファー）・m371（無我大我＝sg06 隣接）・m76（求法叙述）・m3289（釈名）・m2304
（三身釈の一語）・m2908（教目列挙）・m723（仏性は現代語訳の割注のみ・sg07 既）＝DD 原則。
**×5**：m633・m2623・m3823・m2627（『仏性論』書名）・m2212（吉蔵「仏性等の章」）

## stats 差分

タグのみ +44（連動のみ・核心追加なし）・**total 4269 不変・famous 33 不変・字数不変**・
schema_history 318→**319**（origin: retrofit:sg04_shitsuubussho_anchor）・
top-level description 現況同期（連動軸**三十二系統**並立）・sg04 members 0→**22**（anchor 込み）・
連動:m3081 0→**22**

## 検証（全 pass）

整合性 11 項目（NUL 0／再パース／total＝配列 4269／m-id 連番 m1〜m4236〔m01〜m09 は
ゼロ埋め表記〕・sg 33／必須フィールド／recompute drift 0〔規約＝sg 含む全件・改行除き〕／
schema 0.2・history 319／連動:sg04 22・連動:m3081 22／タグ重複 0／backup 差分タグのみ +44／
本文 verbatim 全件不変）＋巻き戻り assert（m506 典籍曰く／sg01 △温存 3 件〔m4164・m4151・
m4198〕の非付与維持／sg05 温存 9 件〔m4061・m4072・m4075・m4116・m4197・m4198・m743・
m4192・m2210〕の非付与維持／anchor m630・m698・m719 自己参照／m4183 sg33＋自己参照／
m4224 sg01＋sg05／m4235 sg32／m3104・m243 sg01＋核心温存／非対象 motif 完全一致 snapshot
照合）＋ホスト側 Grep 反映確認（連動:sg04 22・origin×1・三十二系統×1・CLAUDE.md ★署名一意・
補注 LLL×1）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（319）
- [x] motifs_index_design.md に**補注 LLL**追加（ホスト側 Edit・Grep 確認済）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label sg04・+3368bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_sg04_bussho.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg04.json・
entry：outputs/entry_sg04.txt

## 要確認（ケンシン・commit_push.bat 実行前）

- **注意1**：bash 側 git status で source.doc 2 件に M 表示
  （`_dev_references/dainichikyo-sho-vol19_build/source.doc` 64 行差分・
  `_dev_references/dainichikyo-sho-vol20_build/source.doc` 7118 行差分・挿入/削除等量
  3591/3591）。sg05 時と同一事象（改行変換系ノイズ or phantom・今回作業と無関係）。
  実変更が無ければ stage されず無害
- **注意2（新規発見）**：git index に stale な **staged rename** が残存：
  `引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md →
  「引き継ぎメモ_202」`（切り詰め名）。**ホスト実体確認済＝元ファイル無傷・切り詰め名は
  不存在＝phantom**。commit_push.bat の SAFETY CHECK が「deleted: 引き継ぎメモ_202」で
  停止する場合は、ホスト側で
  `git restore --staged "引き継ぎメモ_202" "引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md"`
  を実行してから再実行のこと
- 未追跡：`DST`・`ZoomInstallerFull.exe`・`_dev_scripts/`（root の *.md 以外は stage 対象外＝無害）

## 副次発見（記録のみ・今回スコープ外）

- **sg06 我則金剛我則法界が引き続き members 0・anchor 無し**（性霊集 idx=72 智泉達嚫の文の
  別系統成句・m2454 の二種無我とは別筋）。今回温存の m371（「無我の大我」＝遮那三密・
  典故:涅槃経）・m303（「遮那は中央に坐す」）は sg06 設計時の候補になりうる
- m-id は m01〜m09 がゼロ埋め表記（連番検証は数値ベースで行うこと・本セッションで確認）

## 残課題

- **kaimyo-app への motifs.json 同期**：今回もタグのみ変更（total 4269 のまま・+44 タグ）。
  同期時に NUL 0／total／SHA-256 一致を確認
- sg06 我則金剛我則法界への anchor 設計（Phase A から）
- 新著作の取込（Phase 1 から）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集済みファイルが bash 側で欠損して見える事象あり
  （ホスト実体は無傷・検証はホスト側 Grep で）
- git phantom は実体確認してから判断・commit_push.bat の SAFETY CHECK（deleted: 検出で中止）併用
- bat は CRLF で作成（LF のみは即閉じの疑い）
- 1 リポジトリ 1 書き手
- 字数 recompute 規約＝**sg 含む全件・改行除き**

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api は sg04 一切衆生悉有仏性への anchor 設計（anchor m3081 単軸〔大日経疏 巻六
「一切の心有る者は悉く仏性有り」＝涅槃経文引用・経文 locus〕・連動 +44・total 4269 不変・
famous 33・補注 LLL・HEAD <push後のhash>）まで完了・push 済。
次の候補：(a) kaimyo-app への motifs.json 同期（+44 タグ・total 4269 のまま・SHA-256 一致確認）／
(b) sg06 我則金剛我則法界への anchor 設計（members 0・性霊集 idx=72 智泉達嚫の別系統成句・
候補見込み＝m371 無我大我・m303 遮那中央坐）／(c) 新著作の取込（Phase 1 から）。
まず CLAUDE.md 冒頭と handoff_2026-07-04_sg04_bussho_anchor_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4269・最終 m4236・sg01〜sg33・famous 33・schema_history 319・
kaimyo-app は 2c78cc5（4269 同期時点）のまま今回 +44 タグ未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。bat は CRLF で作成。k031 は genten 無しで保留。
字数 recompute は sg 含む全件・改行除き。m01〜m09 はゼロ埋め表記。1 リポジトリ 1 書き手。
```
