# handoff: sg06 我則金剛我則法界への anchor 設計 完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：1bcb310（sg04 anchor 設計・push 済確認済）／kaimyo-app 6ea0374（4269 同期済・SHA-256 一致 715cc2dc…d12155e7・橋プール 93→93）
**種別**：retrofit 7 型類例（既存 sg の anchor 化・新規 sg なし・補注 KKK 副次発見〔sg04・sg06 members 0〕の後半解消＝**両 sg 完全解消**）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg06 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-04）

1. **最優先タスク**：候補 (b) sg06 anchor 設計を採用（(c) 新著作取込より優先・★追記〔kaimyo-app
   同期完了記録〕は本 commit に同梱）
2. **anchor＝m371 単軸**（性霊集 idx=106 叡山の澄法師に答する書「若し無我の大我を求めば、
   則ち**遮那の三密即ち是れなり**。遮那の三密は何れの処にか遍ぜざらん。**汝が三密即ち是れ
   なり**」＝自己＝遮那三密の同一宣言の**教理 locus**・典故:涅槃経・核心既付与・既連動なし→
   自己参照 連動:sg06＋連動:m371 の 2 タグ＝sg33/m4183・sg04/m3081 先例）。
   案1 新規 motif 化案（idx=72 の未抽出段落「月鏡を心蓮に観じ、妄薪を智火に焼く。我則金剛、
   我則法界、三等の真言加持の故に五相成身し、妙観智力をもて即身成仏し、即心の曼荼なり」＝
   全 corpus 唯一の verbatim locus。ただし total 4269→4270 変動・retrofit 内新規 motif 先例なし）・
   案3 m303 案（詩 locus・教理密度で劣後→○強連動に）・案4 二重 anchor 案（sg04 不採用判例）
   より**教理 locus 性**（sg01/sg04/sg05 判例）で採用。成句が anchor 原文の部分文字列でない点は
   sg01/sg04 と同型
3. **スコープ＝A 狭域**：本文 入我我入 3＋五相成身 10＋即心 7＋個別 m371/m303＋タグ差分
   （密教:入我我入 m2289/m2293・密教:五相成身 m922/m2676）＝**26 件全件判定**。三平等 29 件・
   主題:即身成仏 78 件はスキャン外（軸拡散防止。**即身成仏軸は sg03 と弁別**＝sg06 の固有内容は
   「行者自身＝金剛＝法界の自己同一宣言〔入我我入・五相成身の行者側〕」）
4. **Phase B**：判定表（anchor＋○7＋△2＝10 件付与・温存 16・×0）全件承認

## 成果（motifs.json・タグのみ変更 +20）

**連動 +20**（10 motif・各件 連動:sg06＋連動:m371・既付与該当なしのため重複回避不要）：

| 区分 | motif | 内容 |
|---|---|---|
| anchor | m371 | 無我の大我＝遮那の三密＝汝が三密（性霊集 idx=106）・自己参照 2 タグ |
| ○ | m08 | 同篇 idx=72 成句直後の廻向「入我我入加持の故に、六大無碍瑜伽の故に」＝文脈連続 |
| ○ | m2293 | 秘蔵記 三平等の観「吾が身を以って諸仏の身に入るれば…」＝入我我入の正面観文 |
| ○ | m2299 | 秘蔵記 三平等観「吾が身は即ち印、語は即ち真言、心は即ち本尊」 |
| ○ | m2289 | 秘蔵記「諸仏を己体に引入」（大円鏡智・入我我入） |
| ○ | m303 | 「遮那は阿誰か号ぞ、本是れ我が心王なり」（handoff sg04 見込み候補） |
| ○ | m337 | 「即心の変化不思議なり、心仏之れを作す…万法は自心にして本より一体」 |
| ○ | m653 | 秘蔵宝鑰 五相成身の正面釈（三密行→通達心・成菩提心・金剛心・金剛身・金剛堅固身） |
| △ | m922 | 「五相入観して早く大悉地を証せよ」＝実修訓誡（sg32 と二軸） |
| △ | m678 | 大日経疏 巻一 大意「即心に万行を具し、心の正等覚を見て」 |

**温存 16**：m2270（経証・焦点は極無自性心＝sg08/sg17 既）・m2285（定義列挙）・m2384（釈名＝
m3289 判例）・m2469（教判言及）・m2485/m2491（語釈）・m2646（配釈列挙）・m2651/m2652
（引証・焦点は行願）・m2676（sg03 既）・m2773（sg22 既）・m2809（sg04 既）・m2869・m2890・
m3965・m646（言及のみ）＝DD 温存原則。**×0**（書名言及型なし）

## stats 差分

タグのみ +20（連動のみ・核心追加なし）・**total 4269 不変・famous 33 不変・字数不変**・
schema_history 319→**320**（origin: retrofit:sg06_gasokukongo_anchor）・
top-level description 現況同期（連動軸**三十三系統**並立）・sg06 members 0→**10**（anchor 込み）・
連動:m371 0→**10**

## 検証（全 pass）

整合性 15 項目（NUL 0／再パース／total＝配列 4269／m-id 連番 m1〜m4236〔m01〜m09 はゼロ埋め
表記・数値ベース検証〕・sg 33／必須フィールド／recompute drift 0〔規約＝sg 含む全件・改行除き〕／
schema 0.2・history 320／連動:sg06 10・連動:m371 10／タグ重複 0／famous 33／anchor 自己参照／
温存 16 の非付与／先行軸維持 sg04 22・sg05 18・sg01 15／末尾改行なし）＋巻き戻り assert
（m506 典籍曰く／sg01 △温存 3 件〔m4164・m4151・m4198〕・sg05 温存 9 件・sg04 温存 17＋×5 の
非付与維持／anchor m630・m698・m719・m713・m4183・m3081・m4224 自己参照〔m698→sg26・
m719→sg27・sg07 anchor は m713 と実体確認済〕／非対象 motif 完全一致 snapshot 照合）全 pass・
backup 差分タグのみ +20 一致・ホスト側 Grep 反映確認（連動:sg06 10・origin×1・三十三系統×2
〔description＋history〕・CLAUDE.md ★署名 2 件とも一意・末尾「保全。）」無傷・補注 MMM×1）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（320）
- [x] motifs_index_design.md に**補注 MMM**追加（ホスト側 Edit・Grep 確認済）
- [x] CLAUDE.md ★entry **2 件**挿入（sg06 retrofit＋**kaimyo-app 同期完走記録の★追記同梱**。
      今回は bash 側 CLAUDE.md が末尾欠損表示だったため insert_claudemd_star.py ではなく
      **ホスト側 Edit で挿入**・タイトル行 anchor 一意確認→挿入→署名一意・末尾無傷を Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_sg06_gasoku.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg06.json

## 要確認（ケンシン・commit_push.bat 実行前）

- **注意1**：bash 側 git status で source.doc 2 件（vol19/vol20_build）に M 表示（sg04/sg05 時と
  同一事象・改行変換系ノイズ or phantom・今回作業と無関係。実変更が無ければ stage されず無害）
- **注意2（継続）**：git index に stale な **staged rename** が残存：
  `引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md →
  「引き継ぎメモ_202」`（切り詰め名・phantom・ホスト実体無傷）。commit_push.bat の
  SAFETY CHECK が「deleted: 引き継ぎメモ_202」で停止する場合は、ホスト側で
  `git restore --staged "引き継ぎメモ_202" "引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md"`
  を実行してから再実行のこと
- 未追跡：`DST`・`ZoomInstallerFull.exe`・`_dev_scripts/`・`outputs/CLAUDE.md.bak_*`
  （root の *.md 以外は stage 対象外＝無害）

## 副次発見（記録のみ・今回スコープ外）

- **idx=72 智泉達嚫の文に初期スライス（m01〜m08）の未抽出段落が残存**（「不生を一阿に証し、
  五智を鑁水に得…我則金剛、我則法界…即心の曼荼なり。故に経に云わく、我覚本不生云云」＝
  m07 と m08 の間）。sg06 成句の**唯一の verbatim locus** を含むため、将来の性霊集ミニ抽出
  （追補ラウンド）の第一候補。抽出時は sg06 anchor の再裁定（verbatim locus への交代または
  二重化）を検討可
- **マウント同期不具合の新事例**：ホスト側 Write 直後の outputs/*.py と CLAUDE.md が bash 側で
  末尾欠損表示（ホスト実体は無傷）。回避＝script は /tmp コピー＋欠損分追記で実行・CLAUDE.md は
  ホスト側 Edit で挿入。**検証は必ずホスト側 Grep で**
- 33 成句すべてに anchor または members が付いた状態を確認（members 0 の sg は解消）

## 残課題

- **kaimyo-app への motifs.json 同期**：今回もタグのみ変更（total 4269 のまま・+20 タグ）。
  同期時に NUL 0／total／SHA-256 一致を確認
- 新著作の取込（Phase 1 から）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可→insert_claudemd_star.py（ただし bash 側欠損表示時は
  ホスト側 Edit で代替可＝本セッション実績・挿入前後の anchor 一意・署名一意・末尾無傷を
  ホスト側 Grep で必ず確認）
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集済みファイルが bash 側で欠損して見える事象あり（双方向）
- git phantom は実体確認してから判断・commit_push.bat の SAFETY CHECK（deleted: 検出で中止）併用
- bat は CRLF で作成（LF のみは即閉じの疑い）
- 1 リポジトリ 1 書き手
- 字数 recompute 規約＝**sg 含む全件・改行除き**
- m01〜m09 はゼロ埋め表記（連番検証は数値ベースで）

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api は sg06 我則金剛我則法界への anchor 設計（anchor m371 単軸〔性霊集 idx=106
「無我の大我を求めば則ち遮那の三密即ち是れなり」＝教理 locus〕・連動 +20・total 4269 不変・
famous 33・補注 MMM・kaimyo-app 同期完走記録の★追記同梱・HEAD <push後のhash>）まで完了・push 済。
これで members 0 の sg は全解消（33 成句すべてに anchor/members あり）。
次の候補：(a) kaimyo-app への motifs.json 同期（+20 タグ・total 4269 のまま・SHA-256 一致確認）／
(b) 新著作の取込（Phase 1 から）／(c) 性霊集ミニ抽出（idx=72 未抽出段落「我則金剛、我則法界…
即心の曼荼なり」＝sg06 の verbatim locus を含む・抽出時は sg06 anchor 再裁定を検討）。
まず CLAUDE.md 冒頭と handoff_2026-07-04_sg06_gasoku_anchor_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4269・最終 m4236・sg01〜sg33・famous 33・schema_history 320・
kaimyo-app は 6ea0374（4269 同期時点）のまま今回 +20 タグ未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py（bash 側欠損表示時はホスト側 Edit 代替・
Grep 検証必須）。文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認。
bat は CRLF で作成。k031 は genten 無しで保留。字数 recompute は sg 含む全件・改行除き。
m01〜m09 はゼロ埋め表記。1 リポジトリ 1 書き手。
```
