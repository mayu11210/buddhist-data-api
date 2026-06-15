# 引き継ぎメモ 2026-06-15 理趣経本文 gabun 要否裁定（意図的未設定を継続・文書 only 記録セッション）

**日付**：2026-06-15
**種別**：gabun 要否裁定（補注 GG／II 様式）・文書 only（motifs.json 不変・整合性保守型ですらない記録セッション）
**起点 HEAD**：`8440a0c`（理趣経 連動軸 retrofit 34 完走・push 済を着手前に確認）
**ステータス**：裁定確定（ケンシン裁定 2026-06-15）・補注 KK／CLAUDE.md／本メモに記録・**未 commit / 未 push**
**変更ファイル**：`_dev_references/motifs_index_design.md`（補注 KK 追加）・`CLAUDE.md`（タイトル行＋現在の進捗に gabun 裁定 ★ エントリ先頭追加）・本メモ。**motifs.json は不変**（実データは R1 時点で既に未設定側に整合）。

---

## 裁定（ケンシン裁定・2026-06-15）

理趣経本文（不空訳・T0243）全 15 motifs（m2400-m2414）の gabun（雅文体訳・text_gendai_gabun）要否について、**意図的未設定を継続**（hizoki／jujushinron／yugikyo／理趣経開題と同運用・将来 retrofit 可能性は温存）。

## 根拠（三軸収束の平明例）

理趣経開題（補注 II）は「空海自筆かつ教学注釈系」で著者帰属軸とジャンル軸が衝突した難件だったが、理趣経本文は判定軸が全て収束する最も平明なケース：

1. **著者帰属軸（旧線引き）**：不空訳＝非空海 →「非空海・教学系＝未設定」に直接該当。
2. **ジャンル軸（補注 II 精緻化）**：経典本文＝非文藝（性霊集系の願文・表白・詩文ではない）→ 未設定側。
3. **経典引用原則（補注 GG）**：全 15 motif が 引用形式:典籍曰く。経典引用は書き下しのまま用いる文脈が強く、雅文体に開く必然が薄い（成句 sg の儀礼朗誦の伝統・新設 sg30/sg31 の gabun 未設定運用とも整合）。

加えて、kaimyo-app 側は gabun 不在時 text_kakikudashi にフォールバックする設計（§3 柔モード）のため、未設定でも利用側の欠落は生じない。

## データ確認（着手時点）

- m2400-m2414 全 15 motif とも gabun 未設定。
- `stats.motifs_without_gendai_gabun_intentional` に `rishikyo_m2400-m2414`（「理趣経 motif は gabun 未設定〔hizoki/jujushinron/yugikyo と同運用・将来 retrofit 可〕」）が R1 時点で記載済み。実データは既に未設定側に整合。
- したがって本裁定による motifs.json の変更は不要（文書 only）。

## 記録先

- `_dev_references/motifs_index_design.md` 末尾に **補注 KK**「理趣経本文 gabun 要否裁定（2026-06-15・意図的未設定の継続＝三軸収束の平明例）」を追加（補注 JJ の次・letter 連番 KK）。
- `CLAUDE.md` タイトル行・現在の進捗セクションに gabun 裁定の ★ エントリを先頭追加。
- 本メモ。

## 検証

- motifs.json は git diff で変更なし（不変）を確認。
- without_gabun キー `rishikyo_m2400-m2414` 据置（不変）。
- 補注 KK present・design doc 半角括弧 0。

## 残課題（次セッション以降）

1. **kaimyo-app への motifs.json 同期**（倉庫 2445→kaimyo-app・SHA-256 一致確認・橋プール更新・理趣経 motif〔80 字以下の核心句〕がプール入りする場合 CORPUS_DISPLAY_NAME に `rishikyo: '理趣経'` 追加を要検討＝理趣経開題で発火した「プール入りしたら登録」条件の踏襲）。これが消化されれば理趣経本文の完走後残課題（連動軸 retrofit → gabun 要否裁定 → 利用側同期）が一巡完了＝瑜祇経・理趣経開題に続く 3 例目。

## git state 注意（要対処・本作業と無関係）

着手時の `git status` に、過去 cleanup セッション由来の既存ステージ済の削除（`package.json`・`render.yaml`・`tsconfig.json`・`vercel.json`・`start.bat`・`引き継ぎメモ_2026-05-06...idx48...md`・`outputs/motifs_index_design_backup_pre_retrofit6-9.md` 等）と多数の未追跡ファイル（`outputs/` 配下の retrofit スクリプト・backup json・dryrun・`_dev_scripts/` 等、ルートの `package.json`/`render.yaml`/`tsconfig.json`/`vercel.json` の未追跡コピー）が残存。8440a0c（retrofit 34＝4 ファイルのみ）には未混入だが、**次回 commit_push.bat 実行時にこれらを巻き込む懸念がある**。本 gabun 裁定の commit を行う際は、`motifs_index_design.md`・`CLAUDE.md`・本メモの 3 ファイルのみを明示的に add する運用（commit_push.bat が `git add -A` 系なら要注意）を推奨。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`
2. motifs.json：total_motifs 2445・famous_phrases 31・最終 m-id m2414・最終 sg sg31・連動:sg 系統数 27（retrofit 34 から不変）
3. m506 引用形式:典籍曰く（巻き戻り検知・不変のはず）
4. 理趣経（rishikyo）：Phase1 取込（0c5df0f）・Phase2 横断索引化（a0bba39）・Phase3 motif R1（e420e0a）・retrofit 34 連動軸（8440a0c）・gabun 要否裁定（本セッション・文書 only）。残＝kaimyo-app 同期のみ。
