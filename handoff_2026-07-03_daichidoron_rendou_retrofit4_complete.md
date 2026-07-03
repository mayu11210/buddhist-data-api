# handoff: 大智度論 連動軸 retrofit 第四弾（全軸横断スキャン）完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：73bf21c（sg32 成句化・push 済確認済）／kaimyo-app 97a02e0（4268 同期済）
**種別**：retrofit 7 型（新規 sg/anchor なし・既存軸被覆拡張）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（第四弾用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-03）

1. **最優先タスク**：未連動 157 件の全軸横断スキャン（handoff 記載の次タスク）を採用・
   並行セッション無し（本セッションが書き手）
2. **Phase A**：新規 sg・anchor の新設なし。**3 既存軸への被覆拡張のみ**承認
3. **Phase B**：判定表**全件付与**（○4＋△3＝7 件）
   ※当方の提示時「○5・8件」は数え違い（判定表実体は ○4＋△3＝7 件・+14 タグ）。
   裁定の実質＝判定表全件付与として 7 件で確定

## 成果（motifs.json・タグのみ変更）

**+14 連動タグ**（7 motif・各件 連動:sgXX＋連動:m主anchor・tags 配列末尾に追加）：

| 軸〔主 anchor〕 | motif | 内容 |
|---|---|---|
| sg02 色即是空〔m630〕 | m4098 | 「色即是空空即是色…空即是涅槃涅槃即是空」仏説明示引用＋世間即涅槃（一句性:核心 既付与・sg02 成句を含む大智度論唯一の段落） |
| sg26 一切智智〔m698〕 | m4045 | 一切智・一切種智の差別の定義的 locus（一切智＝声聞辟支仏事／道智＝菩薩事／一切種智＝仏事） |
| sg26 一切智智〔m698〕 | m4175 | 般若波羅蜜の定義＝初発心より一切種智を求む・仏心中に変名して一切種智 |
| sg27 自心本性清浄〔m719〕 | m4143 | 畢竟空即是畢竟清浄・人の空を畏るるを以て清浄と言う（一句性:核心 既付与） |
| sg27 自心本性清浄〔m719〕 | m4139 | 色性常浄乃至一切種智性常浄（△裁定付与） |
| sg27 自心本性清浄〔m719〕 | m4141 | 畢竟浄無所著・本末因果清浄（△裁定付与） |
| sg27 自心本性清浄〔m719〕 | m4127 | 法念処「諸法性浄不相污染」（△裁定付与） |

**主な除外（直接連動未満）**：供養校量群 m4209〜m4221（不離薩婆若心＝定型句・付随言及。
sg32 弾の keyword 補完除外と同基準）・m4047/m4086（五衆 付随）・m4060（畢竟清浄＝阿羅漢の
形容）・m4217（法華経は書名列挙）・m4163（涅槃城＝一般比喩）・m4220/m4221（帝釈非一切智人＝
付随）。**無常 38 件は sg01 諸行無常が連動軸未設定（anchor 無し）のためスコープ外**。

## stats 差分

タグのみ変更・**total 4268 不変・famous 32 不変・字数不変**・大智度論 連動済 38→**45**
（未連動 157→150）・sg02 members 9→**10**・sg26 28→**30**・sg27 20→**24**・
schema_history 314→**315**（origin: retrofit:daichidoron_rendou_scan3）

## 検証（全 pass）

整合性 10 項目（NUL 0／再パース／total＝配列 4268／m-id 連番 m1〜m4236／sg 32 件／
必須フィールド／recompute drift 0／schema 0.2／famous 32／from_corpus_daichidoron 195）＋
巻き戻り assert（m506 典籍曰く／m4185 sg08・m4042 sg09・m4235 sg32 タグ温存／anchor
m630・m698・m719 自己参照タグ確認／対象 7 件の元タグ snapshot 照合＝追加のみ）＋
backup 連動タグ差分 +14 一致（sg02+1/m630+1/sg26+2/m698+2/sg27+4/m719+4）＋
ホスト側 Grep 反映確認（origin ×1・連動:m719 25 行・連動:m630 12 行〔他軸 anchor 対
sg21/sg17 ぶんを含む値で backup 差分と整合〕）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（315）
- [x] motifs_index_design.md に**補注 HHH**追加（ホスト側 Edit）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label rendou3・+2523bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_daichidoron_rendou3.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_daichi_rendou3.json・
entry：outputs/entry_rendou3.txt

## 副次発見（記録のみ・今回スコープ外）

- **m4183「般若為之母…一切衆生之祖母」・m4184「言説為世俗、仮名説諸法」**＝般若仏母・
  仮名説の名句偈。対応軸なし。将来「般若仏母」軸新設（sg 新設 retrofit）の候補になり得る
- 無常 38 件（四念処の無常観が大半）：sg01 諸行無常への連動軸新設（anchor 設計）は
  将来の Phase A 裁定事項

## 残課題

- **kaimyo-app への motifs.json 同期**：今回はタグのみ変更（total 4268 のまま）。
  連動タグは picker のプール条件に影響しない見込みだが、同期時に NUL 0／total／
  SHA-256 一致を確認すること
- k031 は genten 無しで保留
- これで大智度論の連動軸 retrofit（sg08 字門群／sg09 実相群／sg32 成句化／全軸横断）は
  全消化。残る未連動 150 件は既存二十八軸に対する強連動候補なしと判定済

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集直後の .py が bash 側で末尾欠損して見える事象あり
  （ホスト実体は無傷・/tmp ラッパで回避可）
- git phantom は cleanup_git_state_pre_*.bat で整理してから commit_push.bat
- 1 リポジトリ 1 書き手

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api の大智度論は 連動軸 retrofit 第四弾（全軸横断スキャン・sg02/sg26/sg27 へ
7 motif・+14 タグ・total 4268 不変・補注 HHH・HEAD <push後のhash>）まで完了・push 済。
これで大智度論の連動軸 retrofit は全消化（sg08/sg09/sg32/全軸横断）。
次は kaimyo-app への motifs.json 同期（タグのみ変更ぶん・total 4268 のまま・SHA-256 一致確認）
を進めてください。
まず CLAUDE.md 冒頭と handoff_2026-07-03_daichidoron_rendou_retrofit4_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4268・最終 m4236・成句 sg01〜sg32・famous 32・schema_history 315・
大智度論 連動済 45／未連動 150（強連動候補なしと判定済）・kaimyo-app は sg32 同期時点
（97a02e0）のまま今回タグ未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。k031 は genten 無しで保留。1 リポジトリ 1 書き手。
```
