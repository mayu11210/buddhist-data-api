# 引き継ぎメモ 2026-06-13 瑜祇経 gabun 要否裁定完了（意図的未設定の継続）

**日付**：2026-06-13
**種別**：裁定記録セッション（retrofit 32 残課題①・データ変更なし・文書 only）
**起点 HEAD**：`1b5e322`（retrofit 32・push 済を着手前に巻き戻り検知全 pass で確認）
**ステータス**：裁定完了・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/motifs_index_design.md（補注 GG）・CLAUDE.md・
commit_message.txt・本メモ。**data/indices/motifs.json は不変**。corpus・索引・manifest も不変。
**commit_message.txt 更新確認**：済（冒頭行＝本裁定の内容と整合）

---

## ケンシン裁定（本セッション）

1. **最優先タスク**：①gabun 要否裁定を選択（②kaimyo-app 同期は残作業へ）
2. **gabun 裁定**：yugikyo 全 19 motifs（m2365-m2383）の gendai_gabun は
   **意図的未設定を継続**（hizoki 2026-06-11 裁定・W3 jujushinron と同運用・
   将来 retrofit 可能性は温存）

## 根拠（詳細は補注 GG）

- 非空海（伝・金剛智訳）の経典・全 motif 引用形式:典籍曰く＝書き下しのまま
  用いる文脈が強い（成句 sg の儀礼朗誦原則とも整合）
- kaimyo-app は gabun 不在時 text_kakikudashi にフォールバック（設計書 §3
  柔モード）のため利用側の欠落なし
- 「空海自筆（性霊集系）＝gabun あり／非空海・教学系 W3 以降＝意図的未設定」
  の運用線引きを維持

## データへの影響

- **motifs.json 不変**：total_motifs 2412・sg01-sg29・schema 0.2・
  schema_history 161 のまま。stats.motifs_without_gendai_gabun_intentional の
  yugikyo 2 キー（m2365-m2374／m2375-m2383・「将来 retrofit 可」）は
  retrofit 32 時点で記載済みのため温存（hizoki 裁定時と同様、裁定記録は文書側のみ）
- 補注 GG で「corpus 完走 → 連動軸 retrofit → gabun 要否裁定 → 利用側同期」の
  完走後残課題処理順を様式化（今後の新規 corpus に適用可能）

## 検証（着手時・全 pass）

巻き戻り検知：HEAD 1b5e322（push 済・origin/main..HEAD 差分なし）／
total_motifs=2412=len／m-id 連番 m1-m2383／sg01-sg29（29 件・famous 29）／
m506 引用形式:典籍曰く／m2375・m2378・m2381 一句性:核心／m2381 連動:sg28／
m2375 連動:sg29。
本セッションは motifs.json に触れないため適用後の JSON 再検証は不要
（不変であることをホスト側 Grep で確認）。

## 副次発見・要注意事項

- マウント同期不具合継続を実地確認：bash 側 motifs_index_design.md が
  1554 行で末尾欠損（補注 FF が見えない）。ホスト側 Grep では補注 FF 存在確認。
  **文書の読み書きはホスト側ツール（Read/Edit/Write/Grep）必須**の原則を再確認。
- bash 側 git status の幻影差分（M CLAUDE.md・M motifs_index_design.md）も継続。
  commit_push.bat の index リセットで解消される類。

## 残作業（次セッション）

- **kaimyo-app 側 motifs.json 同期**（単純コピー＋NUL 0／total 2412／
  引用形式タグ確認。典籍曰く冠生成ロジック対応要否・sg28/sg29 の扱い確認を含む。
  **着手前に kakikudashi-data スキル必読**）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2412・最終 m-id=m2383・sg01-sg29・
   m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心・m2381 連動:sg28・
   m2375 連動:sg29（巻き戻り検知・retrofit 32 と同一値のはず）
3. スクリプトの適用前 assert に m506 典籍曰く＋核心 3 チェックを継承すること
4. マウント同期不具合継続前提：文書はホスト側ツールで編集・motifs.json の
   正準形式は indent=1・末尾改行なし

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- 瑜祇経 gabun 要否裁定完了（commit <ハッシュ>）：yugikyo 19 motifs の gabun は
  意図的未設定を継続（hizoki/jujushinron 同運用・補注 GG・motifs.json 不変・
  total_motifs 2412・sg01-sg29 のまま）
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-13_gabun_saitei_complete.md
## 確認
git log --oneline -3 で HEAD・motifs.json total_motifs=2412・sg01-sg29・
m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心・m2381 連動:sg28（巻き戻り検知）
## 次の作業
kaimyo-app 側 motifs.json 同期（典籍曰く冠生成・sg28/sg29 対応確認含む・
着手前に kakikudashi-data スキル必読）
## 注意点
- マウント同期不具合継続前提。文書はホスト側ツールで編集
- motifs.json の正準形式は indent=1・末尾改行なし
- スクリプトの適用前 assert に m506 典籍曰く＋核心 3 チェックを継承
進める前に、最優先タスクを確認してください。
```
