# 引き継ぎメモ 2026-06-13 kaimyo-app 同期完了の記録（理趣経開題 完走後残課題 全消化）

**日付**：2026-06-13
**種別**：同期完了記録セッション（理趣経開題 gabun 裁定 handoff 残作業の消込・データ変更なし・文書 only）
**起点 HEAD**：`ed26ebd`（理趣経開題 gabun 裁定・着手前に巻き戻り検知全 pass で確認）
**ステータス**：kaimyo-app 側 同期実施＋記録完了・**倉庫/kaimyo-app とも未 commit / 未 push**（各 bat 実行待ち）
**変更ファイル（倉庫側）**：CLAUDE.md（タイトル行・現在の進捗）・_dev_references/motifs_index_design.md（補注 II 残課題行）・commit_message.txt・本メモ。**data/indices/motifs.json は不変**。corpus・索引・manifest も不変。

---

## 実施内容（kaimyo-app 側・本セッション）

理趣経開題 完走後残課題の最後＝kaimyo-app 側 motifs.json 同期を実施した。

1. **motifs.json 同期（2412 → 2428 件）**：倉庫 `ed26ebd` 版を kaimyo-app/data/indices/motifs.json へ複写。
   - SHA-256 倉庫側と一致（`5f680459…`・5,857,488 bytes）・NUL 0・JSON 再パース OK・
     total_motifs=2428＝実数・m-id 連番 m1-m2399（欠番なし）・sg01-sg29・末尾改行なし・
     巻き戻り検知 assert（m506 典籍曰く＋核心・m2386 連動 3 軸・m2387 連動:sg08＋核心・
     m2399 連動:sg03・核心 6 件）全 pass・ホスト側 Grep 反映確認。
   - kaimyo-app commit：commit_motifs_sync.bat（motifs.json のみ stage）。

2. **CORPUS_DISPLAY_NAME 登録（ケンシン裁定）**：lib/daishi-kotoba-picker.ts に
   `rishukyo-kaidai: '理趣経開題'` を 1 行追加。
   - **橋プール 87→88 件**（大師 82→83・典籍 5 不変）。新規プール入りは **m2398「廻向偈」
     （46 字・大師曰く・核心）の 1 件のみ**。核心の m2385（624 字）・m2387（526 字）は
     80 字上限でプール外。脱落なし。
   - m2398 の冠（buildKan）は大師曰く系のため「弘法大師のたまわく、」で合成（CORPUS_DISPLAY_NAME 非依存）。
     出典明記（formatCitation）は未登録だと著作名フォールバックで「真実経文句」（理趣経開題の別題）に
     なるため、倉庫 corpus 名に揃えて「理趣経開題」を明示登録。データ実体で
     formatCitation(m2398)=「理趣経開題」・buildKan(m2398)=「弘法大師のたまわく、」を確認。
   - kaimyo-app commit：commit_picker_corpus_display_0613.bat（picker.ts のみ stage・
     実証済み commit_picker_shuffle.bat と機能同一）。

3. **kaimyo-app 側 引き継ぎメモ**：引き継ぎメモ_2026-06-13_倉庫2428同期_理趣経開題_CORPUS登録.md を作成（未 commit・次回 memo 系に同梱予定）。

## 瑜祇経との違い（要点）

瑜祇経（2412 同期・kaimyo `ee4046c`）は橋プール該当 motif 0 件で CORPUS_DISPLAY_NAME 追加を見送った。
理趣経開題は m2398 が**実際にプール入り**したため「プール入りしたら登録」条件が初めて発火し、
今回 CORPUS_DISPLAY_NAME 登録に至った。また理趣経開題は空海自筆＝**大師曰く**系のため、
瑜祇経（伝・金剛智訳＝典籍曰く・冠「瑜祇経に曰く、」）とは冠の系統が異なる。

## 倉庫側更新（文書 only・本セッション）

1. CLAUDE.md タイトル行・現在の進捗：新 ★ エントリ（kaimyo-app 側 motifs.json 同期完走）追加＋
   「残：kaimyo-app 同期のみ」の消込。
2. 補注 II「残課題」行：kaimyo-app 同期完了を追記（処理順が利用側同期まで一巡完了）。
3. commit_message.txt 差し替え・本メモ作成。

## 意義

理趣経開題の完走後残課題（連動軸 retrofit 33・gabun 要否裁定・利用側同期）を全消化。
瑜祇経に続き、補注 GG で様式化した処理順が利用側同期まで一巡した 2 例目（初の空海自筆教学注釈系 corpus）。

## 検証（着手時・全 pass）

巻き戻り検知：HEAD ed26ebd／total_motifs=2428=len／m-id 連番 m01-m2399／sg01-sg29（famous 29）／
m506 引用形式:典籍曰く／m2386 連動:sg20/sg03/sg18／m2387 連動:sg08／m2399 連動:sg03／
m2375・m2378・m2381・m2385・m2387・m2398 一句性:核心／schema_history top-level=163・末尾 retrofit_33。
本セッションは motifs.json に触れないため適用後の JSON 再検証は不要。

## 副次発見・要注意事項

- マウント同期不具合継続前提：bat・メモは bash heredoc で書き、ホスト側 Grep で反映確認した。
  CORPUS_DISPLAY_NAME 編集・commit_message はホスト側 Edit/Write。bash 側 git status の幻影差分
  （多数の .bat に M）は CRLF 由来で、各 one-shot bat の git reset → 単一ファイル stage で回避される。
- repo ルート直下の `python-3.14.6-amd64.exe`（30MB・untracked・6/11 迷い込み）は依然残存（要ケンシン確認）。

## 残作業（次セッション）

- **なし**（倉庫側・kaimyo-app 同期系とも完了）。
- 新規作業はケンシンの最新意向を確認してから着手：次期 corpus 候補
  （金剛頂経開題 47 段落・大日経開題 97 段落・菩提心論講要 146 段落・大日経本体 896 段落・長期）・retrofit 等。
- kaimyo-app 側の引き継ぎメモ commit は kaimyo-app 側の次回 memo 系 commit に同梱（倉庫側タスクではない）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2428・最終 m-id=m2399・sg01-sg29・m506 引用形式:典籍曰く・
   m2386 連動:sg20/sg03/sg18・m2387 連動:sg08・m2399 連動:sg03（巻き戻り検知・本記録は motifs.json 不変ゆえ ed26ebd と同一値）
3. schema_history（top-level）=163・末尾 origin retrofit_33:rishukyo-kaidai_rendou_scan
4. スクリプトの適用前 assert に m506 典籍曰く＋核心チェックを継承
5. マウント同期不具合継続前提：文書はホスト側ツールで編集・motifs.json の正準形式は indent=1・末尾改行なし

## kaimyo-app 側 push 手順（ケンシン操作）

1. `commit_motifs_sync.bat` をダブルクリック（motifs.json のみ・message=commit_message_motifs_sync.txt）
2. `commit_picker_corpus_display_0613.bat` をダブルクリック（picker.ts のみ・message=commit_message_picker_corpus_display.txt）
3. push 後 `git log --oneline -3` で 2 コミット確認

## 倉庫側 push 手順（ケンシン操作）

- `commit_push.bat` をダブルクリック（CLAUDE.md・motifs_index_design.md・commit_message.txt・本メモ等の文書差分）。
  motifs.json は不変。push 後 `git log --oneline -3`。
