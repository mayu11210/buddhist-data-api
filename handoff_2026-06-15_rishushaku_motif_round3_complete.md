# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）motif 抽出 第3ラウンド（巻下後半）完走＝全3ラウンド完走

**日付**：2026-06-15
**種別**：motif 抽出（kakikudashi-data Phase3・第3ラウンド／全3ラウンド中・最終）
**起点 HEAD**：`a394eab`（理趣釈 motif 第2ラウンド・push 済を着手前に確認）
**ステータス**：第3ラウンド完了・整合性検証 10 項目全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・CLAUDE.md・commit_message.txt・本メモ。corpus・manifest・索引は不変。

---

## Phase A 合意（全ラウンド遵守・第1ラウンドより継続）
- 書込方式：本体直接書込（並行書き手なし）。ID は最終 m-id の次から連番・配列末尾追記。
- 引用形式：伝・不空訳＝非空海 → 全件 `引用形式:典籍曰く`、大師系タグ非付与。source に著者「伝・不空訳」保持。
- 首尾題・訳者行（k001/k002/k022/k023/k024/k057）は motif 化せず。語中切れ段・短小真言句は直前に束ね。
- gabun（雅文体訳）：意図的未設定（理趣経本体・開題・yugikyo と同運用・将来 retrofit 可）。
- 連動軸：完走後 retrofit。
- タグ語彙：理趣経本体（rishikyo m2400-m2414）・開題・R1/R2 の値を再利用優先。

## 成果（第3ラウンド・m2453-m2465・13件）

| id | 段 | 節 | category | 核心 |
|---|---|---|---|---|
| m2453 | k044 | 第十段・摧一切魔＝能調伏持智拳如来・四種忿怒の三摩地 | 列挙 | |
| m2454 | k045 | 第十段・郝字の四義・二無我と金剛薬叉曼荼羅 | 語釈 | |
| m2455 | k046 | 第十一段・普賢＝一切平等建立如来・四部大曼荼羅 | 列挙 | |
| m2456 | k047 | 第十一段・吽字・三重輪曼荼羅と外金剛部教令（降三世教令輪品） | 語釈 | |
| m2457 | k048 | 第十二段・一切有情加持・四種蔵と四智四大菩薩 | 核心句 | ★ |
| m2458 | k049 | 第十二段・怛唎字（真如七種・塵垢）と摩醯首羅曼荼羅（外金剛会品） | 核心句 | ★ |
| m2459 | k050 | 第十三段・七母女天の鉤召摂入能殺能成・毘欲字（五乗） | 語釈 | |
| m2460 | k051 | 第十四段・麼度羯囉天三兄弟・薩嚩字・三宝三身 | 語釈 | |
| m2461 | k052 | 第十五段・四姉妹女天・都牟盧天・四波羅蜜・谽字 | 語釈 | |
| m2462 | k053 | 第十六段・無量無辺究竟如来・平等金剛出生の四部曼荼羅 | 列挙 | |
| m2463 | k054 | 第十七段・五種秘密の三摩地（五明妃菩薩） | 列挙 | |
| m2464 | k055 | 第十七段・百字偈の配釈（大慧・大静慮・大悲・大精進） | 核心句 | ★ |
| m2465 | k056 | 流通分・十六大菩薩生・五種善哉・囑累流通 | 語釈 | |

- **束ねなし**：全段 100 字超。k045／k047 末の「時婆伽梵」断片は各段 verbatim で保持（R2 の k036/k038 同方針）。
- **新タグ値 3**（判定表でケンシン承認・すべて密教軸）：
  - `密教:摧一切魔`（m2453/m2454）＝第十段主尊。R2 の段主尊立て（降三世/観自在/不空成就/虚空庫/文殊/虚空蔵）を継続。本体 m2409 は `金剛薬叉` を採用していたため k045 で `金剛薬叉` を併記。
  - `密教:外金剛部`（m2456/m2458/m2459/m2460/m2461）＝摩醯首羅等二十五類・七母天・三兄弟・四姉妹を束ねる外金剛部諸天の軸。R3 で5段に頻出のため新設。
  - `密教:五秘密`（m2463/m2464）＝第十七段 五種秘密三摩地（五明妃菩薩）。
- **本体語彙への整合**：「大楽」は密教軸で再利用（`密教:大楽`。本体 m2400/m2413 と一致）＝`主題:大楽` は新設せず。大欲は `主題:大欲`。「二無我」→`主題:無我`、「即凡即聖/理事不礙」→`主題:不二`、「四部」→`密教:五部`、「五乗」→`主題:方便`＋`衆生救済`、「究竟」→`主題:涅槃` 等で表現（いずれも新設見送り）。吽字は R2 k040 同様 `密教:吽字`＋`密教:種子`（k047/k056）。
- **列挙段の category/文体**：R2 が「主尊＝如来・N種◯◯の三摩地/曼荼羅」の opening 段（k028/k031/k034/k037/k039/k041）に `category:列挙`＋`文体:列挙` を付与していたのに揃え、R3 の同型 opening 段 k044/k046/k053/k054 にも `category:列挙`＋`文体:列挙` を適用（判定表提示時は便宜上 `語釈` 表記だったが、著作内整合のため R2 規約に統一。content タグは承認どおり）。核心段は `category:核心句`＋`文体:長句`。
- 一句性:核心 3 件（m2457／m2458／m2464・ケンシン裁定で m2457 を核心に追加）。

## stats 差分
- total_motifs 2483→**2496**（+13）
- kakikudashi_chars_total +5,790（改行除き）／gendaigoyaku_chars_total +8,658
- from_corpus_rishushaku 38→**51**（+13・実数一致）
- 篇別内訳に `rishushaku_第十段〜第十七段＋流通分（巻下後半）` 追加（dict・節範囲・抽出_motif_数 13・id_範囲 m2453-m2465・属性 経典注釈〔伝・不空訳〕）
- motifs_without_gendai_gabun_intentional に `rishushaku_m2453-m2465` 追加
- schema_history +1（origin: rishushaku_round3・167 件）・schema_version 0.2 維持

## 検証（10 項目・全 pass）
NUL0／JSON 再パース／total==配列数 2496／m-id 連番 missing=[] dup=False（sg 31 不変・最大 m2465）／必須フィールド完全／新規 半角括弧 0／recompute drift kk0・gd0（from_corpus_rishushaku 51 実数一致）／schema 0.2・history 167／原文 verbatim 一致／ホスト Grep 反映（m2465・total 2496・rishushaku_round3）。＋ m506 引用形式:典籍曰く 巻き戻り assert pass。
- build script：outputs/build_rishushaku_r3.py（dry-run→--apply・新タグ allowed-new guard 付き）。バックアップ：outputs/motifs_backup_pre_rishushaku_r3.json・outputs/CLAUDE.md.bak_pre_rishushaku_r3。

## 残作業（次セッション以降）＝理趣釈 完走後の残課題
1. **連動軸 retrofit**（理趣釈 全 motif スキャン）：
   - 最有力＝**m2464（k055 百字偈配釈）↔ 理趣経 sg31「大欲得清浄、大安楽富饒」**（百字偈の配釈そのもの）。
   - 候補：十七清浄句 sg30（理趣釈 初段 R1 motif）／即身成仏 sg03（m2444・m2457 即身成仏）／阿字本不生 sg08（本不生系 m2454 等）／転識得智（R2 m2447・新規 sg 要否）。
   - retrofit は Phase A（軸設計合意）→B（判定表）→C（反映＋検証）→D（補注・文書）。リポジトリ CLAUDE.md「retrofit セッション運用」節参照。
2. **gabun 要否裁定**（理趣釈 全 motif・rishikyo/開題/yugikyo と同様 意図的未設定の継続裁定見込み）。
3. **kaimyo-app への motifs.json 同期**（倉庫 2496 → kaimyo-app・SHA-256 一致確認・新引用形式タグなし＝冠生成ロジック変更不要見込み）。

## 副次メモ（housekeeping）
- CLAUDE.md は**タイトル行（先頭の running log）**に R3 ★エントリを prepend 済。`## 現在の進捗` ヘッダは R1/R2 同様 rishushaku エントリ未反映のまま（先頭は rishikyo gabun verdict）＝R2 precedent 継承の既存ラグ。気になれば retrofit セッション時に再同期。

## 次セッション開始時の確認
1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本ラウンドコミット）
2. motifs.json：total_motifs 2496・最終 m-id m2465・schema 0.2・from_corpus_rishushaku 51
3. references/motif-extraction.md 必読（並行書き手・巻き戻り assert）

## ケンシン貼付用テンプレ（連動軸 retrofit 開始）
```
理趣釈（rishushaku.json）の連動軸 retrofit を始めてください。まず CLAUDE.md 冒頭と
handoff_2026-06-15_rishushaku_motif_round3_complete.md を読み、git log --oneline -3 で
HEAD が R3 コミットであることを確認してください。references/motif-extraction.md と
CLAUDE.md「retrofit セッション運用」節も必読です。理趣釈は motif 抽出 全3ラウンド完走済
（m2415-m2465・total 2496）。最有力は m2464（k055 百字偈配釈）↔ 理趣経 sg31「大欲得清浄、
大安楽富饒」の連動。Phase A（軸設計合意）→B（判定表）→C（反映＋整合性検証＋m506 assert）→
D（補注・CLAUDE.md・handoff・commit_message 更新）→commit_push.bat 依頼 の順で。
gabun 要否裁定・kaimyo-app への motifs.json 同期も残課題です。
```
