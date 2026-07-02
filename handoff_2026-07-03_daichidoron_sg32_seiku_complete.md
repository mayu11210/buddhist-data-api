# handoff: 大智度論 三昧定義の成句化（sg32 新設）完了

**状態**：Phase A〜D 完了・**push 待ち**（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：ae5e11c（gabun 裁定・push 済確認済）
**種別**：連動軸 retrofit 第三弾（retrofit 34 型＝新規 sg 新設）

## commit_message.txt 更新確認

- [x] commit_message.txt 書き換え済（sg32 用・冒頭行整合）

## 合意事項（ケンシン裁定・2026-07-03）

1. **Phase A**：sg32 新設承認・成句表記は**旧字 verbatim「善心一處住不動、是名三昧」**
   （anchor 本文と一字一致・部分文字列 assert 済）・スコープ**全 corpus 横断**・
   tags 9 種承認（category:密教教学／成句:famous／主題:三昧／主題:禅定／密教:三昧／
   出典:大智度論／引用形式:典籍曰く／一句性:核心／含意:全人生）
2. **Phase B**：○10 件承認＋△3 件中 **m922 のみ付与**（m1311・m1560 は除外）＝付与 11＋anchor

## 成果（motifs.json）

- **sg32 新設**：source {type:成句, 出典_ref:大智度論}・書き下し anchor m4235（k029・
  十住心論 巻第七 経由引用〔摩訶止観 経由〕）・挿入位置 sg31 直後（sg ブロック一体保持）・
  gabun 意図的未設定（成句方針・wg キー sg01-sg31→sg01-sg32）
- **連動タグ +24**（12 motif・各件 連動:sg32＋連動:m4235）：

| 区分 | motif | 内容 |
|---|---|---|
| anchor | m4235 | 三昧の定義（自己参照・sg31/m2413 先例） |
| 大智度論 | m4094 | 禅定の定義（思惟修・禅は王・燈と密宇の譬） |
| 大智度論 | m4119 | 四如意足・定摂心（塩の譬・智定力等） |
| 大智度論 | m4153 | 数息観・悪覚を滅す |
| 大智度論 | m4165 | 三解脱門はなぜ三昧か（住定中でなければ狂慧） |
| 大智度論 | m4172 | 八背捨 |
| 大智度論 | m4173 | 八勝処・十一切処 |
| 大智度論 | m4174 | 四禅 |
| 大智度論 | m4182 | 禅は般若波羅蜜の依止処（梯と船の譬） |
| 大日経疏16 | m3680 | 三昧の答（離想清浄＝密教側の三昧定義） |
| 性霊集 | m1104 | 「三昧の法仏は本より我が心に具せり」 |
| 性霊集 | m922 | 本尊三昧観・五相入観（△裁定付与） |

- **除外 21**（付与11/除外21・ケンシン Phase B 裁定）：m427/m859/m907〔sg09 系〕/m1149/
  m1311〔△除外〕/m1560〔△除外〕/m1664〔逆方向〕/m2373/m4082/m4083/m4208＋keyword 補完
  10 件（m4045/m4048〔sg09 済〕/m4053/m4056/m4086/m4132/m4146/m4203/m4214/m4218）

## stats 差分

total_motifs 4267→**4268**・famous_phrases 31→**32**・篇別内訳 成句_三十一件→**成句_三十二件**・
kk 字数 1066779→1066791（+12）・gd 字数 1866796→1867173（+377）・gabun 字数 238704 不変・
from_corpus_daichidoron 195 不変・top-level description **stale 是正**（retrofit 36 以降未更新
→現況反映・連動軸二十七→**二十八系統並立**）・schema_history 313→**314**
（origin: retrofit_daichidoron:sg32_seiku）

## 検証（全 pass）

整合性 10 項目（NUL 0／再パース／total＝配列／m-id 連番 m1〜m4236／sg01〜sg32 連続／
必須フィールド／新規文に半角括弧 0／recompute drift 0／schema 0.2／schema_history 314）＋
巻き戻り assert（m506 典籍曰く／m4185 sg08 タグ温存／m4042 sg09 タグ温存／gabun 裁定
16 エントリ温存）＋成句 verbatim（anchor 本文の部分文字列）＋ホスト側 Grep 反映確認
（total 4268 ×1・連動:sg32 ×12・famous 32 等）

## 文書更新（Phase D チェックリスト）

- [x] motifs.json 反映完了（検証全 pass）
- [x] schema_history 追記済（314）
- [x] motifs_index_design.md に**補注 GGG**追加（ホスト側 Edit）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label sg32_seiku・+1614bytes・
      行数 1395 不変・NUL 0・署名一意・ホスト側 Grep 確認済）
- [x] commit_message.txt 書き換え済（冒頭行整合）
- [x] 本 handoff 作成
- [ ] **commit_push.bat 実行（ケンシン）→ push 検証**

実装：outputs/retrofit_daichidoron_sg32_seiku.py（dry-run→--apply）・
backup：outputs/motifs_backup_pre_sg32.json

## 残課題

- **kaimyo-app への motifs.json 同期（4267→4268）**：⚠ sg32 は 12 字＋成句:famous＋
  引用形式:典籍曰く で isCandidateMotif（橋スロット候補）条件に該当しうる（大智度論として
  初のプール入り候補）。同期時に (a) app 側 picker の sg エントリ扱い（sg30/sg31 先例）、
  (b) source に 著作名 キーが無く 出典_ref のみである点の冠生成解決、(c) CORPUS_DISPLAY_NAME／
  CORPUS_AUTHOR_NAME 登録要否（瑜祇経先例「プール入りしたら登録」）を必ず検証すること
- 他の既存 anchor への大智度論 連動 retrofit 追加検討（残 約 160 件のうち強連動候補があれば）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- マウント同期不具合：ホスト側編集直後の .py が bash 側で末尾欠損して見える事象が本セッションでも
  発生（outputs/retrofit_daichidoron_sg32_seiku.py・ホスト実体は無傷）。/tmp ラッパで in-memory
  修復して実行した。bash 側で「壊れて見える」ときはホスト実体を確認してから判断
- git phantom は cleanup_git_state_pre_*.bat で整理してから commit_push.bat（今回は staged 空・
  実体全存在を確認済で整理不要だった。source.doc の M はサンドボックス幻影・staged 外）
- 1 リポジトリ 1 書き手

## ケンシン貼付用テンプレ（次セッション例）

```
buddhist-data-api の大智度論は sg32 成句化（「善心一處住不動、是名三昧」・anchor m4235・
連動 +24・total 4268・補注 GGG・HEAD <push後のhash>）まで完了・push 済。
次は kaimyo-app への motifs.json 同期（4267→4268・sg32 のプール入り検証つき）
または他 anchor への大智度論 連動 retrofit 追加検討を進めてください。
まず CLAUDE.md 冒頭と handoff_2026-07-03_daichidoron_sg32_seiku_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：motifs.json total 4268・最終 m4236・成句 sg01〜sg32・from_corpus_daichidoron 195・
schema_history 314・famous_phrases 32・補注 GGG まで記載・kaimyo-app は 4267 のまま未同期。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。文書はホスト側 Read/Write/Edit・
bash 書込 JSON はホスト側 Grep で反映確認。k031 は genten 無しで保留。
```
