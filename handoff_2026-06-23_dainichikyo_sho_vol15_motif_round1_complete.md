# 引き継ぎメモ — 大日経疏 巻第十五 Phase3 motif 抽出 第1ラウンド 完了（2026-06-23）

Phase2 横断索引化（commit `e7b6b23`）に続けて Phase3 motif 抽出に着手。第1ラウンド（k004-k018・15件）を本体 motifs.json に追記した。

## Phase A 合意（巻第二〜十四 同運用・全ラウンド遵守）
1. 本体直接書込。ID は既存最終 m3600 の次から連番（m3601〜）。
2. 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に **`引用形式:典籍曰く`**・大師系タグ（category:大師御言葉／引用形式:大師曰く）**非付与**。source に 著者 保持。
3. 共通タグ：`category:密教教学`・`出典:大日経疏 巻第十五`・`引用形式:典籍曰く`。
4. gabun（雅文体訳）意図的未設定（完走後 retrofit 可）。
5. 連動軸タグは抽出時付与せず、完走後 retrofit。
6. 1段=1motif・束ねなし。首題k001/撰号k002/品題k003 は motif 化せず。

## ラウンド分割
| R | 段落 | 科段 | 状態 |
|---|---|---|---|
| R1 | k004-k018 | 金剛蔵の偈問／讃歎略説／大力明王／阿闍梨二種／弟子四種 | **完了（本件・15件）** |
| R2 | k019-k033 | 択地浄菩提心／結護／地加持／綖／蓮華座 | 未 |
| R3 | k034-k050 | 供養／護摩／色三部／形像色像／形量印 | 未 |
| R4 | k051-k064 | 潅頂／三昧耶五種／善住観覚／無縁観／見諦 | 未 |
| R5 | k065-k075 | 悉地／心続浄／空界昇身秘密／真言如意珠 | 未 |
| R6 | k076-k081 | 護摩再説／世間と出世の真言（巻末） | 未 |

## R1 成果（m3601-m3615・15件）
- 核心3件：m3606（秘密＝如来秘奥の蔵・優曇華）／m3607（菩提心は大悲を根本・調良の馬）／m3610（十二真言王＝金剛三昧で仏位）。
- 文体:問答4（m3601-m3604＝偈問の列挙）・譬喩2（m3606/m3607）・語釈9。
- 密教タグ：漫荼羅/真言/印契/大悲胎蔵/菩提心/金剛界/加持/灌頂/遮那（既存語彙のみ・新タグ値なし。潅頂は既存の `密教:灌頂` を再利用）。
- stats：total 3631→3646・kk +5,608／gd +8,058・from_corpus_dainichikyo-sho-vol15=15・篇別内訳に dainichikyo-sho-vol15 エントリ・motifs_without_gendai_gabun_intentional に _round1・schema_history +1（268→269・origin: dainichikyo-sho-vol15_round1）。

## 検証（整合性8項目＋追加2・全 pass）
NUL0／JSON再パースOK／total=配列 3646／m-id連番 m1-m3615 missing=[] dup=False／sg31 不変／必須フィールド完全／新規 motif 半角括弧0／kk・gd recompute drift 0／from_corpus一致／schema 0.2・schema_history +1／原文 verbatim 一致／ホスト側 Grep（CLAUDE.md R1 marker）。巻き戻り assert：m506 典籍曰く・anchor m549/m698 自己参照・vol14 52件 全件 典籍曰く 温存。バックアップ outputs/motifs_backup_pre_vol15_r1.json・build outputs/build_vol15_motif_r1.py。

## 次の作業
`commit_push.bat` で push → `git log` 先頭が本件・`origin/main..HEAD` 空を確認。次セッションは R2（k019-k033・択地浄菩提心〜蓮華座）。判定表を提示→承認→build（m3616〜）→検証→docs の流れ。完走後残課題＝連動軸 retrofit（阿字本不生 sg08/m549・一切智智 sg26/m698・浄菩提心 sg21・自心本性清浄 sg27 等とのスキャン）／gabun 要否裁定（意図的未設定継続見込み）／kaimyo-app 同期。
