# 引き継ぎメモ 2026-06-13 理趣経開題 連動軸 retrofit（retrofit 33）完走（+10 連動タグ・total 2428 不変）

**日付**：2026-06-13
**種別**：retrofit セッション（完走後連動軸スキャン・補注 DD 様式・retrofit 7 型＝新規 sg 新設なし・既存軸被覆拡張）
**起点 HEAD**：`a0650ee`（理趣経開題 motif 抽出 第1ラウンド完走・着手前に巻き戻り検知全 pass で確認）
**ステータス**：作業完了・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json（+10 連動タグ・description 現況化・schema_history +2）・_dev_references/motifs_index_design.md（補注 HH）・CLAUDE.md（タイトル行・現在の進捗）・commit_message.txt・本メモ
**commit_message.txt 更新確認**：済（冒頭行＝retrofit 33 の内容と整合）

---

## Phase A/B 裁定（ケンシン 2026-06-13）

1. **着手順**：理趣経開題 完走後残課題（補注 GG 処理順）のうち①連動軸 retrofit を選択（②gabun 裁定・③kaimyo-app 同期は残作業へ）
2. **強候補 3 件**：全採用（+10 タグ）
3. **境界 2 件**：両件とも温存（m2385↔sg26・m2399↔sg08）
4. **新 sg 新設**：見送り（十六大菩薩/金剛薩埵は成句候補が弱い）
5. **R1 schema_history 誤追記**：top-level へ復元＋retrofit_33 追記（stats 側 R1 は温存）

## 成果（連動タグ +10・3 motif）

| motif | 連動先 | 根拠 |
|---|---|---|
| m2386（題目釈・大三法羯）三系統 | sg20/m534（六大無礙）＋sg03/m533（即身成仏）＋sg18/m571（顕密二教） | 能説の体は六大所成・四種曼茶帝網交映・三密智印互入／三大劫を経ず現生に位を証す／他受用⇄自受用・自証三摩地法門・余教成仏は方便引摂 |
| m2387（三門釈・核心） | sg08/m549（阿字本不生） | 般若波羅蜜多は阿字本不生の義・阿字は廓然不生不滅 |
| m2399（実相般若経答釈） | sg03/m533（即身成仏） | 現身に此の三昧を得・現身即得金剛身 |

- **m2386 は多系統連動 motif の第五例**（m524・m637・m2362・m2381 に続く）
- 新 sg なし・連動軸は二十五系統並立で不変・連動タグ総数 528→538

## 温存（境界裁定・全件温存＝補注 BB/DD adjacency 除外原則）

- m2385↔sg26 一切智智：「速かに一切智智の大覚を証す」一句のみ・核心は生死之河/涅槃之山の対句
- m2399↔sg08 阿字本不生：「三毒の本不生を観ず」＝阿字でなく三毒観への応用・即身成仏が主軸
- m2384（題号釈・報恩孝・五部定義）・m2388-m2397（科文/図像/儀軌/真言＝修法配当温存）・m2398（廻向偈・DD m2363 同型）

## メタデータ是正（本 retrofit で同時処理）

1. **top-level description 現況化**（補注 EE 現況系同期原則）：R1 完走時の同期漏れ（「2412 motifs＝m1〜m2383」「瑜祇経 13 著作目」「retrofit 32」のまま）→「2428 motifs＝m1〜m2399」「理趣経開題 R1 で 14 著作目」「retrofit 33」に更新。
2. **schema_history 整合是正**（ケンシン裁定）：R1（rishukyo-kaidai_round1）が canonical な top-level `schema_history` ではなく 5月レガシー stub の `stats.schema_history` 末尾に誤追記され、top-level から欠落していた（retrofit_32 handoff「160→161」と現状 top-level=161 の照合で判明）。R1 エントリを top-level 様式（summary）で復元し retrofit_33 を続けて追記（**161→163**）。stats 側 R1 元エントリは記録として温存（W3/jujushinron が両リストに併存する先例と整合）。

> ⚠ **schema_history は二系統併存**：top-level `schema_history`（canonical・詳細 summary・retrofit はここに追記）と `stats.schema_history`（2026-05 でフリーズしたレガシー・簡略 change）。今後の round/retrofit は **top-level のみ**に追記すること。着手時に top-level 末尾 origin と件数を handoff 記録値と照合して追記先誤りを検知する（補注 HH で Phase C チェック項目化）。

## stats 差分

- total_motifs 2428 不変・famous_phrases 29 不変・連動軸二十五系統並立（新軸なし）
- char 統計不変（text 不変）・schema 0.2 維持
- schema_history（top-level）161→163（R1 復元＋origin: retrofit_33:rishukyo-kaidai_rendou_scan）／stats.schema_history 13 不変
- 連動タグ総数 528→538（+10）

## 検証（全 pass）

- **着手時巻き戻り検知**：HEAD a0650ee・total=2428・最終 m2399・sg01-sg29・m506 引用形式:典籍曰く＋一句性:核心・m2375/m2378/m2381 核心・m2381 連動:sg28＋sg03・m2375 連動:sg29＋sg19・m2385/m2387/m2398 核心・対象 3 motif 連動タグ未保有・採用アンカー（m534/m533/m571/m549）自己参照完全
- **適用後 整合性検証 12 項目**：serializer round-trip byte 一致／NUL 0／再パース OK／total=len=2428／m1〜m2399 連番（missing=[]・dup なし）／schema 0.2／必須フィールド完全／連動タグ +10／sg01-sg29 連番／char drift 0＋格納 char 不変／付与タグ反映／半角括弧 0／巻き戻りマーカー post 再確認／schema_history R1 復元＋retrofit_33・stats 不変
- **ホスト側 Grep 反映確認**：retrofit_33 origin 1・連動:sg18 6→7
- バックアップ：outputs/motifs_backup_pre_retrofit33.json（リポ outputs・untracked）
- build script：outputs/build_retrofit33_rishukyo_kaidai_rendou_scan.py（dry-run→--apply・コミット対象外）

## 副次発見・要注意事項

- **マウント同期不具合継続**：bash 側 CLAUDE.md 末尾欠損に加え、本セッションでは **bash 側 outputs にホスト Write したスクリプトが末尾 truncate**（194 行で切れ）する事象を確認。build script は bash ネイティブに heredoc で再生成して実行した。CLAUDE.md・motifs_index_design.md・commit_message.txt・本メモはホスト側ツール（Edit/Write）で編集。motifs.json は bash 側で書き、ホスト Grep で反映確認（正常）。
- **CLAUDE.md タイトル行（1 行目）巨大化継続**：ホスト Read（行単位）でも 1 行目だけでサイズ上限超過。Edit 前に 2 行目以降を小さく Read してファイル登録 → 部分文字列アンカーで Edit する手順を踏んだ。将来タイトル行短縮（過去 ★ の本文移設）の検討余地。
- 補注ラベルは **HH**（GG は瑜祇経 gabun 裁定で既使用）。

## 残作業（理趣経開題 完走後・補注 GG 処理順の残り 2 つ）

1. **gabun 要否裁定**：意図的未設定の継続可否（hizoki/jujushinron/yugikyo 継続中）。理趣経開題は空海自筆だが教学・注釈系で、W3 以降の「非性霊集系＝未設定」運用線引きとの整合を裁定。
2. **kaimyo-app 同期**：motifs.json 2428 版の単純コピー＋SHA-256 一致確認。m2398 廻向偈 43 字が橋プール入りする可能性 → 冠生成（理趣経開題系 CORPUS_DISPLAY_NAME 要否）をアプリ側で確認。
3. その後の次期 corpus 候補：金剛頂経開題（47 段落）・大日経開題（97 段落）・菩提心論講要（146 段落・典籍曰く）・大日経本体（896 段落・長期）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2428・最終 m-id=m2399・sg01-sg29・m506 引用形式:典籍曰く・m2375/m2378/m2381 核心・m2385/m2387/m2398 核心・**m2386 連動:sg20/sg03/sg18・m2387 連動:sg08・m2399 連動:sg03（本 retrofit 分・巻き戻り検知）**
3. schema_history（top-level）=163・末尾 origin=retrofit_33:rishukyo-kaidai_rendou_scan・直前=rishukyo-kaidai_round1（R1 復元分）
4. スクリプトの適用前 assert に m506 典籍曰く＋核心チェック（m2375/m2378/m2381 系・m2385/m2387/m2398 系）を継承
5. マウント同期不具合継続前提：文書はホスト側ツールで編集・motifs.json の正準形式は indent=1・末尾改行なし

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- retrofit 33 完走 commit 済（commit <ハッシュ>）：理趣経開題 連動軸 retrofit・
  強連動 3 motif に +10 連動タグ（m2386 三系統〔六大無礙 sg20/即身成仏 sg03/顕密二教 sg18〕＝
  多系統連動第5例・m2387 阿字本不生 sg08・m2399 即身成仏 sg03）・境界 2 件温存・新 sg なし・
  連動軸二十五系統・補注 HH・description 現況化・R1 schema_history を top-level へ復元（161→163）
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-13_rishukyo_kaidai_rendou_retrofit33_complete.md
## 確認
git log --oneline -3 で HEAD・motifs.json total_motifs=2428・最終 m2399・sg01-sg29・
m506 典籍曰く・m2386 連動:sg20/sg03/sg18・m2387 連動:sg08・m2399 連動:sg03（巻き戻り検知）・
schema_history top-level=163・末尾 retrofit_33
## 次の作業
理趣経開題 完走後残課題の残り：gabun 要否裁定 → kaimyo-app 同期。着手順はケンシンの意向を冒頭で確認
## 注意点
- マウント同期不具合継続前提。文書はホスト側ツールで編集（bash 側は CLAUDE.md・outputs とも末尾欠損あり）
- motifs.json の正準形式は indent=1・末尾改行なし
- schema_history は二系統併存。追記は top-level のみ。着手時に末尾 origin と件数を照合
- スクリプトの適用前 assert に m506 典籍曰く＋核心チェックを継承
進める前に、最優先タスクを確認してください。
```
