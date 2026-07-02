# handoff: 大智度論 gabun 要否裁定（完了）＋ kaimyo-app motifs.json 同期（実施）

**状態**：(b) gabun 裁定＝完了・文書反映済・**push 待ち**／(c) kaimyo-app 同期＝bat 準備済・**ユーザー実行待ち**
**着手時 HEAD**：1292c5f（sg09 retrofit 第二弾）
**種別**：裁定記録のみ（motifs.json 不変）＋利用側アプリ同期

## (b) gabun 要否裁定（ケンシン裁定・確定）

**裁定**：大智度論 全 195 motif（m4042-m4236）の text_gendai_gabun は**意図的未設定を継続**。

- 根拠：非空海（伝・龍樹菩薩造/鳩摩羅什訳）の経典引用集・全件 引用形式:典籍曰く・非文藝。
  gabun 付与は文藝系（性霊集 miyasaka 1919 件）限定の現行運用に一致。hizoki／理趣釈／
  大日経疏／発菩提心論鈔 第一〜第七巻（補注 QQ・SS・UU・WW・YY・AAA・CCC）と同運用。将来 retrofit 可。
- 検証：motifs_without_gendai_gabun_intentional に daichidoron_round1（m4042-m4045）〜
  round15（m4235-m4236）の全 16 エントリ・計 195 件 記載済。
  合計 4+13+11+11+16+15+12+8+15+16+12+15+19+21+5+2＝195＝from_corpus_daichidoron（漏れなし）。
- **motifs.json は不変**（total 4267・最終 m4236・schema_history 313 のまま。stats 全項目不変）。

### 文書反映（Phase D 相当）

- [x] motifs_index_design.md に**補注 FFF**追加（ホスト側 Edit・「補注 FFF」1 件 Grep 確認済）
- [x] CLAUDE.md ★entry 挿入（insert_claudemd_star.py・label gabun_saitei・+939bytes・行数1395不変・
      NUL0・署名一意。ホスト側 Grep で反映確認済）
- [x] commit_message.txt 書き換え済（gabun 裁定用・冒頭行整合）
- [x] 本 handoff 作成
- [ ] commit_push.bat 実行（ケンシン）→ push 検証

## (c) kaimyo-app motifs.json 同期（4072→4267）

**着手時 app 状態**：total 4072・最終 m4041（大日経疏 巻第二十 同期版・app HEAD 20ba869）

### 事前検証（実施済・すべて倉庫側 HEAD 1292c5f の motifs.json に対して）

- 新引用形式タグ導入なし：daichidoron 195 件 全件 引用形式:典籍曰く（既存タグ値）
- **プール入り 0 件**：橋スロット候補条件（isCandidateMotif＝典籍曰く/大師系 AND
  一句性:核心 or 成句:famous AND ≦80字）に対し、daichidoron の 一句性:核心 44 件は
  すべて 80 字超（最小 m4145 の 90 字）・成句:famous 0 件
- → **CORPUS_DISPLAY_NAME／CORPUS_AUTHOR_NAME 登録不要・冠生成ロジック
  （lib/daishi-kotoba-picker.ts）改修不要**（瑜祇経先例「プール入りしたら登録」条件未発火。
  仮に将来プール入りしても source.著作名='大智度論' フォールバックで冠「大智度論に曰く、」・
  出典明記「大智度論」に正しく解決。著者は伝承ゆえ著者名未登録＝hizoki 同運用の安全側）

### 実行手順（ケンシン・順番厳守）

1. `outputs\cleanup_git_state_pre_retrofit15.bat`（汎用実装）ダブルクリック → git status に
   「deleted:」「phantom renamed:」が無いことを確認（phantom 6 件はホスト実体全存在の index 幻影・
   stale index.lock も Step 1 で退避される）
2. 倉庫 `commit_push.bat` → (b) gabun 裁定コミット（CLAUDE.md・補注 FFF・本 handoff）
   ※ `_dev_references/*/source.doc` の M はサンドボックス側幻影の可能性大（過去コミットに
   source.doc 変更履歴なし）。Windows 側 git status に出た場合は commit 前に報告を
3. `outputs\push3_sync_kaimyo_4267.bat` → 倉庫 motifs.json を kaimyo-app にコピー
   （HEAD コミット済ガード＋total 4267 ガード＋SHA-256/fc バイナリ一致検証つき）
4. kaimyo-app の `commit_motifs_sync.bat` → app 側 commit＋push
   （commit_message_motifs_sync.txt は同期用に書き換え済・motifs.json のみ stage する安全設計）

### 同期後検証（Claude が実施）

- kaimyo-app 側 motifs.json：NUL 0／total 4267／最終 m4236／引用形式:典籍曰く 反映（daichidoron 195 件）
- 両リポジトリ git log で push 反映確認

## 現状 stats（不変）

total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 313・sg 31・
sg08 members 83・sg09 members 29・famous_phrases 31・補注 FFF まで記載。

## 残課題

- (a) m4235 三昧定義「善心一処住不動、是名三昧」の成句化＝sg32 新設（見送り継続。
  着手なら Phase A 軸設計合意から）
- (d) 他の既存 anchor への大智度論 連動 retrofit 追加検討（残 約 166 件のうち強連動候補があれば）
- k031 は genten 無しで保留

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → insert_claudemd_star.py（★開始・〕終端・冪等・行数不変）
- 文書はホスト側 Read/Write/Edit・bash 書込 JSON はホスト側 Grep で反映確認
- git phantom は cleanup_git_state_pre_*.bat で整理してから commit_push.bat
- 1 リポジトリ 1 書き手（本セッションは倉庫＝文書のみ・app＝motifs.json コピーのみ）

## ケンシン貼付用テンプレ（次セッション例・sg32 成句化）

```
buddhist-data-api の大智度論（daichidoron.json）は gabun 裁定（意図的未設定・補注 FFF）と
kaimyo-app への motifs.json 同期（4072→4267）まで完了・push 済。
次は m4235 三昧定義「善心一処住不動、是名三昧」の成句化（sg32 新設・Phase A 軸設計合意から）
または他 anchor への大智度論 連動 retrofit 追加検討を進めてください。

まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_gabun_saitei_kaimyo_sync.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。

現状：motifs.json total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 313・
sg08 members 83・sg09 members 29・補注 FFF まで記載・kaimyo-app 同期済（total 4267）。

落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。git phantom は
cleanup_git_state_pre_*.bat で整理。k031 は genten 無しで保留。
```
