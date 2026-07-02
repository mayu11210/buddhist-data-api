# 引き継ぎ：大智度論 Phase3 motif 抽出 第12ラウンド【判定表 draft・未承認・書込未実施】

日付：2026-07-02
状態：**R12 は判定表提示まで完了・ケンシン承認待ち・motifs.json への書込は一切していない**。
（Fable 5 の使用量逼迫のため中断。次セッションは Sonnet 5 で「承認から」再開。）
着手時 HEAD：ede9b95（Round11 完了コミット）＝本セッションでもコミット無し（本 handoff＋plan_round12.json＋commit_message.txt のみ追加）。

## 着手前チェック済（本セッションで検証済・再検証は軽く git log のみで可）
- HEAD=ede9b95・motifs.json total 4220・最終 m4189・from_corpus_daichidoron=148・schema_history 307＝handoff R11 と完全一致。
- k170-188（19段）corpus 確認済：全段 genten のみ・kakikudashi 空（Phase A 通り text_kakikudashi=genten）。
- citation.kukai_work：k170-183＝「吽字義・声字実相義（阿字本不生）／秘蔵記」／k184-188＝「吽字義・声字実相義／秘蔵記（陀羅尼・総持）」。
- 既存主題タグ Counter 確認済→新タグ値 0 で設計（下表の全値が既存軸内の既存値）。

## Phase A 合意（全ラウンド遵守・変更なし）
引用形式:典籍曰く 全件（伝・龍樹造/鳩摩羅什訳＝非空海）・大師系タグ非付与／category:密教教学・出典:大智度論／
text_kakikudashi＝genten・text_gendaigoyaku＝corpus verbatim／節=section_major（section）・引用元=citation.kukai_work／
gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）／文体は palette{問答/譬喩/偈/列挙}内。

## R12 判定表 draft（19段→19件・全段単独 motif・束ね無し・予定 id m4190-m4208）
**plan は outputs/plan_round12.json に作成済（この表と 1:1・承認後そのまま engine に渡せる）**

| 予定id | 段 | 節（要約） | 主題タグ | 文体 | 一句性 |
|---|---|---|---|---|---|
| m4190 | k170 | 四念処（経①）総説・循身観・以不可得故 | 四念処/観法/畢竟空 | 列挙 | － |
| m4191 | k171 | （経②）威儀と入出息・縄をなう師の譬 | 四念処/観法/一心 | 譬喩/列挙 | － |
| m4192 | k172 | （経③）四大（屠牛師）と三十六物（倉の譬） | 四念処/不浄/無我 | 譬喩/列挙 | － |
| m4193 | k173 | （経④）九相観・我身亦如是・未脱此法 | 四念処/九相/無常 | 列挙 | 候補どまり非付与 |
| m4194 | k174 | （論①）内外十二観・内空無主・猶如草木 | 四念処/無我/空 | 問答/譬喩 | － |
| m4195 | k175 | （論②）循身観と不生身覚・菩薩は身相を取らず | 四念処/観法/菩薩 | 列挙 | － |
| m4196 | k176 | （論③）自離其身易・離其心難・攢燧求火・破竹・魚楽水 | 精進/一心/煩悩 | 譬喩 | ★核心 |
| m4197 | k177 | （論④）不浄観の実際・身は草木瓦石の如し | 不浄/無我/観法 | 譬喩 | － |
| m4198 | k178 | （論⑤）死屍観・好色安在（幻法）・四観 | 不浄/無常/無我 | 譬喩/列挙 | － |
| m4199 | k179 | （論⑥）四聖行→四諦観→煖頂忍世第一 | 四諦/顛倒/修行 | 譬喩/列挙 | － |
| m4200 | k180 | （論⑦）菩薩の四念処・不可得空・柔順法忍/無生法忍 | 大悲/無生法忍/菩薩 | 譬喩 | － |
| m4201 | k181 | （論⑧）慧多念処・精進多正勤・定多如意足・根力道覚 | 三十七品/智慧/精進 | 問答/列挙 | － |
| m4202 | k182 | （論⑨）不取涅槃・七住地の夢筏・諸仏摩頂「念汝本願」 | 本願/大悲/諸法実相 | 問答/譬喩 | ★核心 |
| m4203 | k183 | 摩訶衍総枠・四念処〜字門を摩訶衍と名づけ以不可得故 | 大乗/三十七品/畢竟空/字門 | 列挙 | ★核心 |
| m4204 | k184 | 陀羅尼総論（1）能持能遮・完器盛水・須弥山 | 陀羅尼/功徳/菩薩 | 問答/譬喩 | － |
| m4205 | k185 | （2）聞持・分別知陀羅尼・諸物名一貴賤理殊の偈 | 陀羅尼/智慧/言語 | 問答/偈 | － |
| m4206 | k186 | （3）入音声・恒河沙劫の罵詈にも瞋らず・誰罵誰瞋 | 陀羅尼/忍辱/言語 | 問答/譬喩 | 候補どまり非付与 |
| m4207 | k187 | （4）讃歎にも不動・喜ぶべきは唯仏一人・五百門 | 陀羅尼/不動心/功徳 | 譬喩/列挙 | － |
| m4208 | k188 | （5）無礙陀羅尼＝最大・説法教化の根本 | 陀羅尼/教化/三昧 | 問答/譬喩/列挙 | － |

- 新タグ値 0（四念処21/観法7/畢竟空8/一心1/不浄12/無我21/九相2/無常106/空29/菩薩20/精進31/煩悩16/四諦7/顛倒4/修行55/大悲54/無生法忍2/三十七品5/智慧137/本願1/諸法実相31/大乗5/字門55/陀羅尼3/功徳6/言語27/忍辱4/不動心1/教化42/三昧6 全て既存値再利用）。
- m4203 のみ主題 4 タグ（m4169 の 4 タグ前例・摩訶衍総枠→字門接続が本アンソロジーの主旨のため）。
- 核心 3 提案：m4196（離其心難）・m4202（夢筏・念汝本願）・m4203（以不可得故の総枠）。
  k173（我身亦如是）は R10 の九相核心 m4164 既付与のため見送り・k186（誰罵誰瞋）は候補どまり。
- m4203 は完走後 retrofit で sg08（阿字本不生）連動候補に追加（m4185・m4165 系と併せて）。

## 次セッション（Sonnet 5）開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md（kakikudashi-data スキル同梱）を読む。
2. `git log --oneline -3` で HEAD 確認（本 handoff の push 後は本コミットが HEAD・motifs.json は 4220/m4189 のまま）。
3. **上の判定表をケンシンに提示して承認を得る**（修正指示があれば plan_round12.json の該当 items を修正）。
4. 承認後：`python3 outputs/daichidoron_round_builder.py --plan outputs/plan_round12.json`（dry-run）
   → `--apply`（backup: outputs/motifs_backup_pre_daichidoron_round12.json 自動）→ `--verify`（10項目＋巻き戻り assert）。
   期待値：total 4220→4239・m4190-m4208・from_corpus_daichidoron 148→167・schema_history 307→308。
5. claudemd_entry_round12.txt を書き（「★ 」開始・「〕」終端・末尾に「・」を付けない）、
   `python3 outputs/insert_claudemd_star.py --entry-file outputs/claudemd_entry_round12.txt --label round12`。
6. handoff_2026-07-02_daichidoron_motif_round12_complete.md 作成・commit_message.txt 更新・git status 確認→push 依頼。

## 残ラウンド（R12 の後）
- R13＝寶塔校量品＋述誠品＋如法性実際 k189-209（21段）。
- 説話 k218-222（5段）＝小ラウンドまたは併合。孤立段 k029/k030＝引用抜粋ラウンド・k031＝保留。
- 完走後：連動軸 retrofit（sg08←m4185/m4165系/m4203 候補等・handoff R11 のリスト参照）・gabun 裁定・kaimyo-app 同期。

## 落とし穴（継続）
- CLAUDE.md は単一行巨大ファイル・Edit 不可→insert_claudemd_star.py 必須。entry 終端「〕」・冪等 sig=entry[:90]。
- 長文は bash ヒアドキュメントで書き wc -l／tail で末尾検証。全角括弧のみ・割注〔 〕。
- commit_push.bat は _dev_references/ も staging（作業前からの M 2件が巻き込まれ得る）。
  リポジトリ直下の未追跡 DST・ZoomInstallerFull.exe は対象外→push 前に git status 確認。
- 1リポジトリ1書き手。既存 motif・他 corpus に触れない（追記のみ）。
