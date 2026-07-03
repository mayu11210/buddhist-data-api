# handoff: sg05 諸法無我への anchor 設計 完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：ba9fcf9（sg01 anchor 設計・push 済確認済）／kaimyo-app 7bd8226（4269 同期済・SHA-256 一致）
**種別**：retrofit 7 型類例（既存 sg の anchor 化・新規 sg なし・補注 JJJ 副次発見〔sg05 は m4224 が anchor 候補・三軸化の是非〕解消）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg05 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-03）

1. **最優先タスク**：候補 (b) sg05 anchor 設計を採用（(c) 新著作取込より優先）
2. **anchor＝m4224 三軸化**（三法印 locus「一切法無我印」・核心既付与・既 sg09/m637＋sg01 連動→
   **三軸 anchor 初例**）。m4165 二軸化案（「諸法無我」verbatim 全 corpus 唯一だが空門定義文脈）・
   二重 anchor 案（m4224＋m4165）・m2847 案は不採用（教理 locus 性を優先）。
   **同一 anchor を二つの sg が共有する初例**：連動:m4224 は sg01/sg05 プールの合併を指し、
   弁別は 連動:sg01／連動:sg05 側で行う
3. **スコープ**：全 corpus 主題:無我 25 件フルスキャン＋「諸法無我」verbatim m4165
   （sg01 と異なり全件判定＝母数が小規模のため）
4. **Phase B**：○11＋△6 全件承認（境界例 m4194・m2454 含む）。△温存 7・×2

## 成果（motifs.json・タグのみ変更 +33）

**連動 +33**（18 motif・各件 連動:sg05＋連動:m4224・既 連動:m4224 保持の m4224/m4065/m4169 は
連動:sg05 のみ＝重複回避）：

| 区分 | motif | 内容 |
|---|---|---|
| anchor | m4224 | 三法印 locus・sg09/sg01 と三軸（連動:sg05 のみ追加） |
| ○ | m4052 | 法念処「求我不可得…無實我法」 |
| ○ | m4063 | 散空・車の譬「離散五眾人不可得」 |
| ○ | m4065 | 無我定義列挙「不自在故無我・無主故名為無我」（sg01 と二軸） |
| ○ | m4106 | 「身實無我、不自在故」身念処の結 |
| ○ | m4110 | 我使心破「無自性故無我」 |
| ○ | m4111 | 「我相皆不可得」法念処の結 |
| ○ | m4169 | 無我想の定義（核心既付与・sg01 と二軸） |
| ○ | m4165 | 空門定義「觀**諸法無我**我所空」＝**verbatim 全 corpus 唯一**（sg32 と二軸） |
| ○ | m513 | 菩提心論・涅槃経偈「無我の法の中に真我あり」（核心既付与） |
| ○ | m741 | 大日経疏巻一・我我所執破「何者かこれ我ならん」 |
| ○ | m2847 | 発菩提心論鈔巻十「無我とは人法二我を離るる義」 |
| △ | m4076 | 犍闥婆城「知無我無實法者是時顛倒願息」 |
| △ | m4077 | 如夢・二十身見 |
| △ | m4142 | 我空「解我空易解五衆空難」 |
| △ | m4194 | 内外十二観「內空無主亦無知者見者作者受者」（境界例） |
| △ | m2195 | 十住心論「人我の空を解らずして何ぞ法空の理を覚らん」（核心既付与・sg17 と二軸） |
| △ | m2454 | 理趣釈「二種の無我人空と法空を証す」（境界例・sg08 と二軸） |

**温存**：△7＝m4061（無常・畢竟空論＝sg01 既カバー）・m4072（如焰・譬喩中心・sg09 既連動）・
m4075（如響）・m4116（死屍観想）・m4197（不浄観の実際）・m4198（死屍観想・sg01 温存と同判定）・
m743（外道の真我計破が主）＝DD 原則。×＝m4192（四大三十六物・定型列挙）・m2210（七十五法頌）

## stats 差分

タグのみ +33（連動のみ・核心追加なし）・**total 4269 不変・famous 33 不変・字数不変**・
schema_history 317→**318**（origin: retrofit:sg05_shohomuga_anchor）・
top-level description 現況同期（連動軸**三十一系統**並立）・sg05 members 0→**18**（＋anchor）・
連動:m4224 15→**30**

## 検証（全 pass）

整合性 11 項目（NUL 0／再パース／total＝配列 4269／m-id 連番 m1〜m4236・sg 33／必須フィールド／
recompute drift 0＝字数不変〔規約＝sg 含む全件・改行除き〕／schema 0.2・history 318／
連動:sg05 18・連動:m4224 30／タグ重複 0／backup 差分タグのみ +33／本文 verbatim 全件不変）＋
巻き戻り assert（m506 典籍曰く／m4183 sg33＋核心・m4235 sg32・m3104/m243 sg01＋核心温存／
sg01 △温存 3 件〔m4164・m4151・m4198〕の非付与維持／anchor m630・m698・m719 自己参照／
非対象 motif 完全一致 snapshot 照合）＋ホスト側 Grep 反映確認（連動:sg05 18・origin×1・
三十一系統×1・CLAUDE.md ★署名一意・補注 KKK×1）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（318）
- [x] motifs_index_design.md に**補注 KKK**追加（ホスト側 Edit・Grep 確認済）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label sg05・+3093bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_sg05_muga.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg05.json・
entry：outputs/entry_sg05.txt

## 要確認（ケンシン・commit_push.bat 実行前）

- **bash 側 git status で source.doc 2 件に M 表示**：
  `_dev_references/dainichikyo-sho-vol19_build/source.doc`（64 行差分）・
  `_dev_references/dainichikyo-sho-vol20_build/source.doc`（7118 行差分・挿入/削除等量 3591/3591）。
  改行変換系ノイズ or phantom の疑い（今回作業と無関係）。commit_push.bat は
  `git add _dev_references/` で stage するため、**意図しない変更ならホスト側で
  `git diff --stat` を確認**のこと（実変更が無ければ stage されず無害）
- 未追跡：`DST`・`ZoomInstallerFull.exe`・`_dev_scripts/`（root の *.md 以外は stage 対象外＝無害）

## 副次発見（記録のみ・今回スコープ外）

- **sg04 一切衆生悉有仏性・sg06 我則金剛我則法界が引き続き members 0・anchor 無し**。
  sg04（悉有仏性＝涅槃経系）は大智度論に直接 locus が乏しく、anchor 探索は
  発菩提心論鈔・十住心論など他 corpus からになる見込み。sg06 は性霊集 idx=72
  智泉達嚫の文の別系統成句（m2454 の二種無我とは別筋）
- bash 側マウント同期不具合の再現：motifs_index_design.md がホスト 2153 行に対し
  bash 側 2065 行（補注 III〜JJJ 欠損表示・ホスト実体無傷）。**文書検証は必ずホスト側 Grep** を再確認

## 残課題

- **kaimyo-app への motifs.json 同期**：今回もタグのみ変更（total 4269 のまま）。
  同期時に NUL 0／total／SHA-256 一致を確認
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
- 字数 recompute 規約＝**sg 含む全件・改行除き**（m のみで数えると drift 誤検知・本セッションで確認）

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api は sg05 諸法無我への anchor 設計（anchor m4224 三軸化〔三法印 locus・
sg09/sg01 と三軸 anchor 初例〕・連動 +33・total 4269 不変・famous 33・補注 KKK・
HEAD <push後のhash>）まで完了・push 済。
次の候補：(a) kaimyo-app への motifs.json 同期（タグのみ・total 4269 のまま・SHA-256 一致確認）／
(b) sg04 一切衆生悉有仏性／sg06 我則金剛我則法界への anchor 設計（いずれも members 0・
sg04 は他 corpus からの anchor 探索見込み）／(c) 新著作の取込（Phase 1 から）。
まず CLAUDE.md 冒頭と handoff_2026-07-03_sg05_muga_anchor_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4269・最終 m4236・sg01〜sg33・famous 33・schema_history 318・
kaimyo-app は 7bd8226（4269 同期時点）のまま今回タグ未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。bat は CRLF で作成。k031 は genten 無しで保留。
字数 recompute は sg 含む全件・改行除き。1 リポジトリ 1 書き手。
```
