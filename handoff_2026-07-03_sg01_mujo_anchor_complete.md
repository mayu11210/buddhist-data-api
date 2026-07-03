# handoff: sg01 諸行無常への anchor 設計 完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：735a254（sg33 般若仏母・push 済確認済）／kaimyo-app 5e83534（4269 同期済・blob 一致）
**種別**：retrofit 7 型類例（既存 sg の anchor 化・新規 sg なし・補注 HHH の宿題〔無常 38 件スコープ外〕解消）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg01 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-03）

1. **最優先タスク**：候補 (a) sg01 anchor 設計を採用（(b) 新著作取込より優先）
2. **anchor＝m4224**（大智度論 巻第三十二・三法印 locus「一切有為法無常印」・核心既付与・
   既 sg09/m637 連動→**二軸 anchor**）。m3104 雪山偈案・二重 anchor 案・m243 案は不採用。
   **成句が anchor 原文の部分文字列でない初例**（教理 locus 性を優先）
3. **スコープ**：大智度論 未連動無常 38 件＋諸行無常 verbatim 4 件（全 corpus 主題:無常 109 件の
   全件スキャンはせず）
4. **Phase B**：○9 全件承認＋△8 のうち**教説系 5 のみ付与**（m4160・m4062・m4065・m4108・m4051）。
   △温存 3＝m4164・m4151・m4198（観想修法・布施文脈＝DD 原則）
5. **m3104 に 一句性:核心 追加付与**（雪山偈全四句 verbatim＝全 corpus 唯一）。
   anchor m4224 への核心は既付与のため追加なし

## 成果（motifs.json・タグのみ変更 +31）

**連動 +30**（15 motif・各件 連動:sg01＋連動:m4224・tags 末尾追加）：

| 区分 | motif | 内容 |
|---|---|---|
| anchor | m4224 | 三法印 locus・自己参照・sg09 と二軸 |
| ○ | m4061 | 七日喩経「一切有為法無常變異皆歸磨滅」＋「無常則是空之初門」（核心既付与） |
| ○ | m4169 | 十想「觀一切有為法無常智慧相應相是名無常想」（核心既付与） |
| ○ | m4102 | 四念処総説・四観定式 hub（核心既付与） |
| ○ | m4109 | 心念処「観是心無常生滅相一念不住」（核心既付与） |
| ○ | m4154 | 念死「不応於無常危脆命中而信望活」（核心既付与） |
| ○ | m4092 | 法忍・三法印定式（第二 locus） |
| ○ | m4148 | 念法・三法印定式（第三 locus） |
| ○ | m3104 | 大日経疏 巻七・**雪山偈全四句 verbatim**（＋核心 追加付与・典籍横断） |
| ○ | m243 | 性霊集 idx71・空海の雪山偈引用「諸行無常云云」（核心既付与・典籍横断） |
| △ | m4160 | 対治悉檀「観無常非第一義・空中無無常」 |
| △ | m4062 | 無始空「仏以是無常而度衆生」（核心既付与） |
| △ | m4065 | 「一切有為法皆是無常相」論証 |
| △ | m4108 | 「仏説無常即是苦」 |
| △ | m4051 | 心念処（十八空品側） |

**温存**：△3＝m4164（九相結語・核心既付与だが観想文脈）・m4151（布施主題）・m4198（死屍観想）。
×＝定型列挙 23（m4049/50/52/53/55/60/63/64/74/76/104/105/106/111/120/124/125/126/128/130/152/179/194/199 の系）・
例示 2（m2302 秘蔵記 名句文身文法例・m3107 大日経疏 声聞説法例）

## stats 差分

タグのみ +31（連動 30＋m3104 核心 1）・**total 4269 不変・famous 33 不変・字数不変**・
schema_history 316→**317**（origin: retrofit:sg01_shogyomujo_anchor）・
top-level description 現況同期（連動軸**三十系統**並立）・sg01 members 0→**14**（＋anchor）

## 検証（全 pass）

整合性 10 項目（NUL 0／再パース／total＝配列 4269／m-id 連番 m1〜m4236／sg 33 件／必須フィールド／
recompute drift 0＝字数不変／schema 0.2・history 317／連動:sg01 15・連動:m4224 15／本文 verbatim 不変）＋
巻き戻り assert（m506 典籍曰く／m4183 sg33＋核心・m4235 sg32・m4177/m566 二軸温存／retrofit4
m4098・m4045・m4175・m4143 系温存／anchor m630・m698・m719 自己参照／対象 15 件 snapshot 照合＝
追加のみ）＋backup 差分 +31 タグ一致＋ホスト側 Grep 反映確認（連動:sg01 16〔タグ 15＋history 1〕・
origin×1・三十系統×1）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（317）
- [x] motifs_index_design.md に**補注 JJJ**追加（ホスト側 Edit・Grep 確認済）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label sg01・+2529bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_sg01_mujo.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg01.json・
entry：outputs/entry_sg01.txt

## 副次発見（記録のみ・今回スコープ外）

- **sg04 一切衆生悉有仏性・sg05 諸法無我・sg06 我則金剛我則法界も members 0・anchor 無し**。
  特に sg05 諸法無我は三法印つながりで **m4224 が anchor 候補**（三軸化の是非を含め将来の
  Phase A 裁定事項）
- マウント同期不具合の新事例：前セッションでホスト側 Edit した motifs_index_design.md の
  補注 III が bash 側 grep で 0 件（ホスト側 Grep では 6 件・実体無傷）。**文書検証は必ず
  ホスト側 Grep** の運用を再確認

## 残課題

- **kaimyo-app への motifs.json 同期**：今回はタグのみ変更（total 4269 のまま）。連動タグは
  プール条件に影響しない見込みだが、同期時に NUL 0／total／SHA-256 一致を確認
- 新著作の取込（Phase 1 から）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集済みファイルが bash 側で欠損して見える事象あり
  （ホスト実体は無傷・検証はホスト側 Grep で）
- git phantom は cleanup_git_state_pre_*.bat で整理してから commit_push.bat
- bat は CRLF で作成（LF のみは即閉じの疑い）
- 1 リポジトリ 1 書き手

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api は sg01 諸行無常への anchor 設計（anchor m4224〔三法印 locus・sg09 と二軸〕・
連動 +30＋m3104 核心・total 4269 不変・famous 33・補注 JJJ・HEAD <push後のhash>）まで完了・push 済。
次の候補：(a) kaimyo-app への motifs.json 同期（タグのみ・total 4269 のまま・SHA-256 一致確認）／
(b) sg05 諸法無我への anchor 設計（m4224 三軸化の是非が Phase A 裁定事項・sg04/sg06 も anchor 無し）／
(c) 新著作の取込（Phase 1 から）。
まず CLAUDE.md 冒頭と handoff_2026-07-03_sg01_mujo_anchor_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4269・最終 m4236・sg01〜sg33・famous 33・schema_history 317・
kaimyo-app は 5e83534（4269 同期時点）のまま今回タグ未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。bat は CRLF で作成。k031 は genten 無しで保留。
1 リポジトリ 1 書き手。
```
