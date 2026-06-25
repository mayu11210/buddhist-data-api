# handoff 2026-06-24 — 大日経疏 巻第十六 Phase3 motif 抽出 全6ラウンド＋retrofit＋gabun 完走（push2）

## 到達点
`data/indices/motifs.json` に巻第十六の motif を **m3679-m3744（66件）** 追記し、連動軸 retrofit と gabun 裁定まで完走。
新運用に従い **motif 全工程を1 push（push2）** に集約。**total 3709→3775**・schema_history **275→282**（R1-6 各＋retrofit 1）。`commit_message.txt` 更新済み・`commit_vol16_push2.bat` 実行待ち。

## Phase A 合意（巻第二〜十五 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全件 `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十六`／`引用形式:典籍曰く`。
- 1段=1motif（束ねなし）・gabun 意図的未設定・連動軸は完走後 retrofit。構造段 k001/k002/k003/k041/k051 は motif 化せず。

## 6ラウンド（核心15件）
| R | 範囲 | m-id | 件 | 核心 |
|---|---|---|---|---|
| R1 品11之余 答〜五事〜秘密漫荼羅の法と作法 | k004-k015 | m3679-m3690 | 12 | 3（五事 m3685／秘中の密＝大悲蔵 m3687／流出・四種造 m3690） |
| R2 三部曼荼羅〔仏・蓮華・金剛・不動・仏母〕 | k016-k026 | m3691-m3701 | 11 | 0 |
| R3 尊別印相〔仏頂・釈迦・諸天・文殊・除蓋障・地蔵・虚空蔵〕 | k027-k040 | m3702-m3715 | 14 | 0 |
| R4 入秘密漫荼羅品第十二 | k042-k050 | m3716-m3724 | 9 | 4（業煩悩を智火で焼く m3719／浄菩提心の仏種子 m3720／三昧耶＝我等仏仏等我 m3723／末代の戒め・明師 m3724） |
| R5 入秘密漫荼羅位品第十三 前半 | k052-k061 | m3725-m3734 | 10 | 5（毘盧遮那＝日 m3726／等至三昧 m3727／法界体性の蓮華王 m3732／無蔵性 m3733／無得偈・本不生＝阿字 m3734） |
| R6 同 後半 | k062-k071 | m3735-m3744 | 10 | 3（五大字観・阿字法界性 m3737／毘盧遮那無師智・一切衆生同性 m3740／証入 m3744） |

- 典故新値：金剛頂経（k043）。文体:偈（k060/k061）。本文 k004-k071 全網羅。

## 重要：判定表のずれを着手後に検知・修正（記録）
- 初版 motif_plan の section 節 ラベルが、品12 末（k047-k049）と品13（k052-k071）で実際の corpus 段落分割と**ずれていた**（テキストは corpus から verbatim で正しいが、節/タグ/核心 が別段に付く誤り）。
- 適用直後の retrofit 前スキャンで節と本文内容の不一致（例 m3734 が「十力」表示なのに本文は「無得偈・本不生」）を検知 → **適用済み66件を pre-vol16 バックアップから巻き戻し**、節を **corpus の section から直接取得**し、タグ・核心 を真の内容で再導出して**再 build**。`節 == corpus.section` を全66件 assert pass。push 前に是正済み（commit 未発生のため影響なし）。

## 連動軸 retrofit（タグのみ・total 不変）
- 新規 sg/anchor なし＝既存軸の被覆拡張。core verbatim に限定し 5 件に +13 連動タグ：
  - sg08 阿字本不生〔m549〕← m3734（k061 無得偈・本不生＝阿字の出入）／m3737（k064 五大字観・阿字＝法界性・一切法本不生）
  - sg21 浄菩提心〔m638+m728〕← m3720（k046 浄菩提心の仏種子）／m3728（k055 浄国地平＝浄菩提心）／m3740（k067 浄菩提心＝毘盧遮那悦心地）
- sg26 一切智智／sg27 自心本性清浄 は vol16 に core verbatim 直結なく見送り（温存）。origin: retrofit:dainichikyo-sho-vol16_rendou_scan。

## gabun 裁定
- vol16 全66 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十五 同運用）。`motifs_without_gendai_gabun_intentional` に round1-6 記載済。

## 検証（全 pass）
- NUL0／JSON再パースOK／m-id 連番 m1-m3744 missing=[] dup=False／total=配列 3775／sg31／vol16 66件 全件 典籍曰く・大師系0・半角括弧0（kk/gd とも）／kk・gd recompute drift 0／verbatim 一致（節=corpus section 一致）／from_corpus_vol16=66／核心15。
- 巻き戻り assert：m506 典籍曰く／vol15 retrofit m3623 連動:sg08／vol15 78件 温存。
- ホスト Grep：m3744 反映確認。バックアップ outputs/motifs_backup_pre_vol16_r1..r6.json／_pre_vol16_retrofit.json。build: outputs/vol16_build/build_vol16_motifs.py／motif_plan_v2.py／retrofit_vol16.py。

## push（push2）
- 変更ファイルは `data/indices/motifs.json`＋`CLAUDE.md`＋本 handoff＋commit_message.txt のみ。
- **`commit_vol16_push2.bat`**（専用・幻の削除回避）を用意：git reset HEAD → data/indices/motifs.json／CLAUDE.md／handoff_2026-06-24_*motif* を stage → ステージ済み削除のみ安全チェック → commit → push。標準 commit_push.bat は package.json 等の幻の staged 削除で Step4.5 中止するため使わない。

## 残（push3）
- kaimyo-app 同期：別リポジトリ。motifs.json を kaimyo-app/data/indices/motifs.json にコピー・NUL0／total 3775／引用形式:典籍曰く 反映確認・SHA-256 一致。冠は source.著作名 フォールバックで「大日経疏 巻第十六に曰く、」＝新引用形式タグなしのためコード変更なし見込み。要フォルダ接続。
