# 引き継ぎメモ：★ Phase 4 W1 完走マージセッション完了 ★（W1 buddhist-shoryoshu-workshop → 本体統合）

**日付**：2026-05-25
**フェーズ**：Phase 4 W1 完走マージ（W1 性霊集 残篇 workshop の本体への移設マージ・第三回 workshop マージ）
**起点**：本体 retrofit 27 完走（2026-05-24・total_motifs 770）／W1 R66 完走（2026-05-25・sw001〜sw1553）
**終点**：本マージで本体 motifs.json は m1〜m2174 ＋ sg01〜sg26 ＝ **total_motifs 2200** に到達
**ステータス**：完走〔整合性検証 Phase B 全 pass ＋ 独立再検証 全 pass〕

---

## (a) 本セッションの位置づけ

W1〔buddhist-shoryoshu-workshop・性霊集 残篇 motif 抽出 workshop〕が 2026-05-25 第 66 ラウンド idx=0 真済序の消化をもって完走〔W1 motifs.json sw001〜sw1553・1553 件〕。CLAUDE.md §5・`_dev_references/workshop_protocol.md` §10 に従い、本体 repo の Cowork セッションで一回だけ実施するマージ移設を実施した。

過去の workshop マージ実績：

- **Phase 4 W1**〔2026-05-09〕：sw001〜sw123 を m282〜m404 に統合
- **Phase 4 W2**〔2026-05-11〕：tw001〜tw254 を m491〜m744 に統合
- **本セッション**〔2026-05-25〕：**W1 完走分 sw124〜sw1553 を m745〜m2174 に統合**（第三回）

着手前にケンシン裁定で以下 2 点を確定：

- **篇別内訳の形式**：案A〔bare「idxN」リッチ形式・2026-05-09 Phase 4 W1 マージと同形式〕を採用。
- **結界宣告 温存案件**：現状のまま verbatim 統合（schema 0.3 化マージで再検討する温存継続案件）。

---

## (b) 本セッションの主な成果

### Phase A：機械的マージ（schema 0.2 維持）

**実装**：`outputs/merge_w1_completion_to_main.py`（単独 Python build script・dry-run ＋ 本番適用の二段運用・in-memory 編集 ＋ write back）

**再番号付け表**：

- sw124 → m745
- sw1553 → m2174
- 採番式：m＝swN＋621（本体最終 m-id m744 の次から連番）
- W1 全 1430 件〔sw124〜sw1553〕を本体 motifs 配列末尾に追記

**マージ対象の確定**：W1 motifs.json は sw001〜sw1553〔1553 件〕。うち sw001〜sw123 は 2026-05-09 Phase 4 W1 マージで既に本体 m282〜m404 として統合済〔本文 text_kakikudashi 一致を sw001/sw002/sw003/sw123 で照合確認〕。本マージ対象は **sw124〜sw1553 の 1430 件**。

> **注**：マージ起動 paste メッセージは「W1 の性霊集 69 篇分を追加」と記載していたが、W1 from_idx_breakdown の 69 篇は既統合 14 篇を含む数。本マージで本体に新規追加するのは **55 篇分**〔idx=0,2〜5,8,9,11,13〜21,23〜33,35,36,38,40〜43,46,49,86,87,90〜101,103,104,107,111〕。既統合 14 篇〔idx=1,6,7,10,22,34,37,39,85,88,106,108,109,110〕とは重複なし。

**統計差分**：

| 項目 | マージ前 | マージ後 | 差分 |
|---|---|---|---|
| total_motifs | 770 | **2200** | +1430 |
| m-id 範囲 | m1〜m744 ＋ sg01〜sg26 | m1〜m2174 ＋ sg01〜sg26 | +1430 |
| kakikudashi_chars_total | 112,853 | **146,057** | +33,204 |
| gendai_gabun_chars_total | 154,931 | **238,704** | +83,773 |
| gendaigoyaku_chars_total | 326,255 | **549,031** | +222,776 |
| motifs_with_gendai_gabun | 743 | **2,173** | +1,430 |
| 篇別内訳 エントリ | 67 | **122** | +55 |
| flat from_idxN キー | 57 | **112** | +55 |
| schema_history 件数 | 85 | **147** | +62 |
| ファイルサイズ | 2,692,504 bytes | **5,094,815 bytes** | – |

stats 全項目を本体 motifs 配列から recompute して整合化（増分加算ではなく全件再計算）。

### 篇別内訳の追加〔案A bare「idxN」リッチ形式・55 篇〕

性霊集 55 篇分を `stats.篇別内訳` に bare「idxN」キー・リッチ形式 dict で追加。フィールド構成は 2026-05-09 Phase 4 W1 マージの 14 篇と同一：`idx`／`巻番号`／`篇名`／`字数_kakikudashi_本文`／`字数_gendai_gabun`／`字数_gendaigoyaku`／`抽出_motif_数`／`id_範囲`／`属性`／`ラウンド`／`完走日`／`出典_workshop`。

- `字数_*`・`巻番号`・`篇名`・`抽出_motif_数` は W1 `from_idx_breakdown` から取得。
- `id_範囲` は再番号付け後の m-id 先頭〜末尾〔例：idx0 真済序 → `m2161〜m2174`〕。
- `属性` は各篇の支配的ジャンル `出典:*` タグから導出〔詩／碑／序／書／啓／状／表／願文／知識文／式／奏状／勅答／啓白文 等・全 55 篇 判定済・未判定 0〕。
- `ラウンド`・`完走日` は W1 schema_history の session フィールド〔`w1-round-NN-idxNN`〕から導出〔W1 第 12〜66 ラウンド〕。

flat `from_idxN` 整数キーも 55 件追加〔値＝当該 idx の motif 数・合計 1430〕。

### 結界宣告 温存案件〔ケンシン裁定：verbatim 統合〕

W1 内に温存継続案件として保持されていた結界宣告核心句 3 motif を、タグ含めそのまま統合：

- 旧 sw148〔idx=98〕→ **m769**（一句性:核心 付与済）
- 旧 sw154〔idx=99〕→ **m775**（一句性:核心 付与済）
- 旧 sw158〔idx=99〕→ **m779**（結界宣告反復・一句性:核心 未付与）

sw158 の核心句整合性〔sw148/sw154 と揃えるか否か〕は schema 0.3 化マージで再検討する温存継続案件として引き続き保持。

### schema_history 統合

- W1 schema_history 61 件を本体 top-level schema_history に統合。各エントリに `origin: W1:buddhist-shoryoshu-workshop` タグを付与〔2026-05-11 W2 マージの origin タグ慣例を踏襲〕。W1 側は version 欠落ゼロのため version 補完は不要。
- マージ完走エントリ 1 件を末尾に追加〔`session: w1-completion-merge`／`merged_from: W1:buddhist-shoryoshu-workshop`〕。
- 本体 schema_history 合計：85 ＋ 61 ＋ 1 ＝ **147 件**。

### schema 整合

- `schema_version` 0.2 維持〔フィールド構造変更なし・データ統合のみ〕。
- W1 motif 1430 件は全件 `id`／`source`(dict)／`text_kakikudashi`／`text_gendaigoyaku`／`text_gendai_gabun`／`tags`(list) 完備・余分フィールドなし・本体 schema 0.2 に完全準拠。
- W1 tags 内に sw/sg/m-id 参照（連動タグ等）は皆無のため、再番号付けに伴うタグ参照の追随変換は不要〔点検済〕。
- W1 motif text の半角括弧は 0 件〔W1 側で全角徹底済〕。
- 新規タグ軸・新規 含意の射程 区分の導入なし → `_dev_references/motifs_index_design.md` は無改変。
- W1 トップレベル `_workshop` セクションは本体に持ち込まず破棄〔2026-05-11 W2 マージの方針踏襲〕。W1 トップレベル `famous_phrases` は空配列のため処理なし。

### 整合性検証〔Phase B 全 pass ＋ 独立再検証 全 pass〕

| # | 項目 | 結果 |
|---|---|---|
| 1 | NUL 末尾バイト | 0 ✓ |
| 2 | schema_version | 0.2 ✓ |
| 3 | total_motifs〔stats vs 配列〕 | 2200 vs 2200 ✓ |
| 4 | m-id 連番性〔m1-m2174〕 | missing=[] extra=[] dups=0 ✓ |
| 5 | sg-id 件数 | 26 ✓ |
| 6 | 必須フィールド完全性 | 不備 0 ✓ |
| 7 | motif text 半角括弧 | 0 ✓ |
| 8 | stats vs recompute 差分〔5 項目〕 | 全ゼロ ✓ |
| 9 | 篇別内訳 全 dict 形式 | 122/122 ✓ |
| 10 | schema_history 件数 | 147 ✓ |
| 独 | content fidelity〔12 サンプル・sw124/sw1553 含む〕 | 本文・タグ・source 全一致 ✓ |
| 独 | 結界 温存案件 verbatim〔m769/m775/m779〕 | タグ・本文一致 ✓ |
| 独 | id 全体重複 | 0 ✓ |
| 独 | 既存 m1-m744〔744〕／sg〔26〕不変 | ✓ |

### 本体 CLAUDE.md 更新

- タイトル行（line 1）先頭〔最新エントリ位置・`2026-04-25〜・` の直後〕に本マージ完走エントリを追加。
- 最終更新行（retrofit 27 の行）先頭に本マージ完走エントリを追加・日付を 2026-05-25 に更新。
- `## 現在の進捗` ヘッダ先頭に本マージの短縮エントリを追加。
- 実装：`outputs/update_claude_md_w1_completion_merge.py`（in-memory 編集 ＋ write back・anchor 各 1 件一致を assert・NUL 0 確認）。CLAUDE.md 357,626 bytes。

---

## (c) 残作業〔次セッション以降〕

### 選択肢 A：W1 buddhist-shoryoshu-workshop repo の凍結 ★最優先

workshop_protocol §10(5) に従い、本マージで役割を完了した W1 repo を凍結する：

- (a) GitHub.com 上で `mayu11210/buddhist-shoryoshu-workshop` を archive（read-only）化。
- (b) ローカル `C:\Users\user\buddhist-shoryoshu-workshop\` は保全（消去しない）。R12〜R66 のラウンド履歴・引き継ぎメモ群は参照可能なまま残す。
- (c) 再開する場合は新 workshop を立ち上げる方針〔§10(5)〕。

### 選択肢 B：本体側 retrofit セッションの継続

性霊集 全 112 篇の motif が本体に揃ったため、retrofit 28 以降の連動軸 retrofit〔般若心経秘鍵 仏法不外求軸・三教指帰軸 等の温存候補〕を本体側で継続可能。

### 選択肢 C：kaimyo-app での新 motif 活用

本マージで kaimyo-app は性霊集 全 112 篇 2174 motif〔＋教学系・成句〕を即座に参照可能になった。kaimyo-app 側のテーマ駆動辞書設計への統合作業余地あり。

---

## (d) 副次発見・要注意事項

### (d-1) paste メッセージの「69 篇」記載

マージ起動 paste メッセージは「W1 の性霊集 69 篇分を本体に追加」と記載していたが、W1 `from_idx_breakdown` の 69 篇は既統合 14 篇を含む総数。本体に新規追加されたのは **55 篇**。CLAUDE.md 原則 11「ラベルより内容を信頼」に従い、着手前に JSON 解析で実状を確認し 55 篇と確定してから Phase A に着手した。

### (d-2) 篇別内訳の 2 形式混在（本体既存）

本体 `stats.篇別内訳` は形式が混在している：

- `性霊集_idxN_篇名` キー・簡易形式〔42 件・本体ネイティブ抽出分・値は {巻番号, motifs:[m-id配列], 件数}〕
- bare `idxN` キー・リッチ形式〔2026-05-09 Phase 4 W1 マージの 14 件 ＋ idx105 ＋ 本マージの 55 件〕
- `教学系_corpus_著作名` キー〔9 件・W2 由来〕
- `成句_七件`〔1 件〕

本マージは案A〔bare「idxN」リッチ形式〕を採用し、W1 由来 性霊集 69 篇〔14＋55〕が同一形式に統一された。本体ネイティブ 42 篇との形式統一は将来の整理候補。

### (d-3) 本体 stats の既存レガシーフィールド（無改変）

以下は本マージで触れていない〔データ統合のみの原則・2026-05-11 W2 マージの「本体既存運用との互換性優先」を踏襲〕：

- `stats.schema_history`〔stats 内・11 件・古い形式の遺物。top-level schema_history とは別物〕。
- `stats.motifs_without_gendai_gabun_intentional` のキー `"sg01-sg07"`：本体は現在 sg01〜sg26 まで存在するためラベルが古い。本マージ対象 1430 件は全件 text_gendai_gabun 完備のため新規の intentional 除外は発生せず、ラベル是正は将来の整理候補。

### (d-4) bash 経由 git 書き込み禁止

commit / push は本体 repo 直下の `commit_push.bat` をケンシンがダブルクリック実行する。`commit_push.bat` は `data/indices/`・`CLAUDE.md`・`*.md`（repo 直下）を stage するため、`data/indices/motifs.json`・`CLAUDE.md`・本引き継ぎメモが commit に含まれる。`outputs/` 配下（build script・バックアップ）は stage 対象外。Step 4.5 SAFETY CHECK で `deleted:` が出ないことを確認すること。

---

## 関連ファイル

- 本体 motifs.json：`data/indices/motifs.json`〔2200 件・m1-m2174 ＋ sg01-sg26・5,094,815 bytes〕
- 本マージ build script：`outputs/merge_w1_completion_to_main.py`（dry-run ＋ 本番適用）
- CLAUDE.md 更新 script：`outputs/update_claude_md_w1_completion_merge.py`
- バックアップ：`outputs/motifs_backup_pre_w1_completion_merge.json`／`outputs/CLAUDE_md_backup_pre_w1_completion_merge.md`
- W1 完走サマリ：`C:\Users\user\buddhist-shoryoshu-workshop\handoff_2026-05-25_w1_completion_summary.md`
- workshop_protocol：`_dev_references/workshop_protocol.md`〔§10 移設マージ手順〕
- 前回 workshop マージ handoff：`handoff_2026-05-09_w1_merge_complete.md`／`handoff_2026-05-11_w2_merge_complete.md`

---

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（Phase 4 W1 完走マージ完了後）===

【最初にやること】
作業フォルダ C:\Users\user\buddhist-data-api を mcp__cowork__request_cowork_directory で接続してください。

【セッション概要】
Phase 4 W1 完走マージ（2026-05-25）で W1 buddhist-shoryoshu-workshop の完走分
sw124〜sw1553（1430 件）を本体 m745〜m2174 として統合。本体は total_motifs 2200
（m1-m2174 ＋ sg01-sg26）に到達し、性霊集 全 112 篇の motif 抽出が完了した。

【最初に読むファイル】
1. handoff_2026-05-25_w1_completion_merge_complete.md（本マージ完走サマリ）
2. CLAUDE.md（本体ルール・進捗ヘッダ）
3. _dev_references/motifs_index_design.md（schema 0.2 仕様）
4. data/indices/motifs.json（本体現況・2200 件）

【次フェーズの選択肢】
(A) W1 buddhist-shoryoshu-workshop repo の凍結（archive 化・最優先）
(B) 本体 retrofit セッション継続（retrofit 28 以降）
(C) kaimyo-app での新 motif 活用

【注意点】
- bash 経由 git 書き込み禁止（commit_push.bat 経由でケンシン側ダブルクリック）
- 長文編集は Python script で in-memory 編集 ＋ write back（Edit tool truncate 回避）
- 本体 motifs.json は 5,094,815 bytes（将来の分割設計は検討課題）
```

---

最終更新：2026-05-25〔Phase 4 W1 完走マージセッション完了・W1 buddhist-shoryoshu-workshop（性霊集 残篇）の sw124〜sw1553 1430 件を本体 m745〜m2174 に統合・本体 total_motifs 2200 達成・整合性検証 Phase B 全 pass ＋ 独立再検証 全 pass・schema 0.2 維持・性霊集 全 112 篇 motif 抽出完了〕
