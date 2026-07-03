# handoff: 般若仏母軸の新設（sg33）完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：5ea31e2（retrofit 第四弾・push 済確認済）／kaimyo-app 8f59ffc（タグ同期済・blob 一致）
**種別**：retrofit 34 型（新規 sg 新設・retrofit 第四弾〔補注 HHH〕の副次発見 m4183 からの Phase A 起動）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg33 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-03）

1. **最優先タスク**：候補 (a) 般若仏母軸の新設 retrofit を採用（(b) sg01 anchor 設計・(c) 新著作取込より優先）
2. **成句**：案 2「般若能生佛、是則為一切眾生之祖母」（旧字 verbatim・m4183 原文の部分文字列）
3. **スコープ**：教理系のみ（般若＝諸仏を生む母）。尊格系仏母（仏眼仏母・虚空眼・金剛吉祥・
   仏母印・仏母漫荼羅等 約 20 件）は除外＝軸の拡散防止
4. **Phase B**：○6 全承認＋△4 のうち **m4184 のみ付与**（m3028・m491・m4086 は除外）
5. **m4183 に 一句性:核心 追加付与**（sg32 anchor〔m4235 核心既付与〕先例と整合・タグ計 +15）

## 成果（motifs.json）

**sg33 新設**（sg32 直後挿入＝sg ブロック一体保持・total 4268→4269）：

- text_kakikudashi：「般若能生佛、是則為一切眾生之祖母」（16 字）
- tags 10 種：category:密教教学／成句:famous／**主題:般若仏母（新規値）**／主題:般若波羅蜜／
  主題:智慧／密教:般若／出典:大智度論／引用形式:典籍曰く／一句性:核心／含意:全人生
- gendaigoyaku 442 字（解説文体・sg32 様式・anchor 明記）・gabun 意図的未設定
  （wg キー sg01-sg32→sg01-sg33）

**+14 連動タグ**（7 motif・各件 連動:sg33＋連動:m4183・tags 配列末尾に追加）：

| motif | 著作 | 内容 |
|---|---|---|
| m4183 | 大智度論 巻十八 | anchor 自己参照（讃般若波羅蜜偈 上・k163）。＋一句性:核心 追加付与 |
| m4177 | 大智度論 巻十八 | 同偈句「般若為之母能出生養育佛為衆生父般若能生佛」verbatim（sg09 既連動→**二軸**） |
| m4184 | 大智度論 巻十八 | 同偈下半「解脱涅槃道皆従般若得」＝般若→諸仏の出生方向（△裁定付与） |
| m4213 | 大智度論 巻五十七 | 「般若波羅蜜是諸仏之母」＝宝塔校量品 書写供養功徳論の根拠句 |
| m2794 | 発菩提心論鈔 | 「仏母般若の船栰に乗じて…彼岸に到る」＝大師御釈引用 |
| m3242 | 大日経疏 巻九 | 「大空を証するを名けて般若仏母と為す。正しくこれ明妃の義」＝定義的 locus |
| m566 | 吽字義 | 「大空の義＝般若仏母明妃の義」（sg24 既連動→**二軸**） |

**主な除外**：△裁定＝m3028（虚空眼＝毘盧遮那の母・尊格側）・m491（覚母の梵文＝般若菩薩は
sg23 主担）・m4086（大悲是般若波羅蜜之母諸仏之祖母＝**系譜の方向が逆**・祖母語の共有のみ）。
その他＝尊格系約 20 件（m2275・m2353・m2371・m2375〜77・m2970/71・m3038/39・m3215・
m3544/45・m3697・m3701/02・m3741・m4040）・覚母＝文殊発心場面（m644/m2200・華厳叙述）・
白住処＝観音の母（m3292）・蓮華坐能生諸仏（m3509・座喩）・世俗の母（m630・m671・m2385・
m4062）・仏母明王経＝経名（m1248）。

## stats 差分

total 4268→**4269**・famous_phrases 32→**33**・篇別内訳 成句_三十二件→**三十三件**・
kakikudashi +16 字・gendaigoyaku +442 字・schema_history 315→**316**
（origin: retrofit:sg33_hannya_butsumo）・top-level description 現況同期（連動軸**二十九系統**並立）・
sg33 members 7（anchor 含む）。

## 検証（全 pass）

整合性 10 項目（NUL 0／再パース／total＝配列 4269／m-id 連番 m1〜m4236／sg 33 件 連番／
必須フィールド／recompute drift 0／schema 0.2／famous 33／from_corpus_daichidoron 195）＋
巻き戻り assert（m506 典籍曰く／m4185 sg08・m4042 sg09・m4235 sg32 タグ温存／retrofit4 anchor
m630・m698・m719 自己参照＋m4098 温存／対象 7 件 snapshot 照合＝追加のみ）＋
backup 差分 +15 タグ一致（連動 +14＋m4183 核心 +1・本文不変）＋
ホスト側 Grep 反映確認（origin×1・成句_三十三件×1・total 4269×1・連動:m4183 7 行）＋
成句 verbatim 照合（sg33 本文＝m4183 原文の部分文字列）。

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（316）
- [x] motifs_index_design.md に**補注 III**追加（ホスト側 Edit）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label sg33・+2786bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_sg33_hannya_butsumo.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg33.json・
entry：outputs/entry_sg33.txt

## 残課題

- **kaimyo-app への motifs.json 同期**：本体 4268→4269（sg33 新設＋タグ +15）。sg33 は
  16 字＋成句:famous＋引用形式:典籍曰くで**プール入り条件該当しうる→同期時に
  isCandidateMotif 検証要**（sg32 同期時と同様）。同期時に NUL 0／total／SHA-256 一致を確認
- sg01 諸行無常への anchor 設計（Phase A 裁定事項・大智度論 無常 38 件が対象候補）
- 新著作の取込（Phase 1 から）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集直後の .py が bash 側で末尾欠損して見える事象あり
  （ホスト実体は無傷・/tmp ラッパで回避可）
- git phantom は cleanup_git_state_pre_*.bat で整理してから commit_push.bat
- bat は CRLF で作成（LF のみは即閉じの疑い）
- 1 リポジトリ 1 書き手

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api は 般若仏母軸の新設（sg33「般若能生佛、是則為一切眾生之祖母」・anchor m4183・
+14 連動タグ＋m4183 核心・total 4269・famous 33・HEAD <push後のhash>）まで完了・push 済。
次は kaimyo-app への motifs.json 同期（4268→4269・sg33 の isCandidateMotif 検証・SHA-256 一致確認）
を進めてください。
まず CLAUDE.md 冒頭と handoff_2026-07-03_sg33_hannya_butsumo_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4269・最終 m4236・sg01〜sg33・famous 33・schema_history 316・
kaimyo-app は 8f59ffc（4268 タグ同期時点）のまま今回未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。bat は CRLF で作成。k031 は genten 無しで保留。
1 リポジトリ 1 書き手。
```
