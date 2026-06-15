# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）連動軸 retrofit（retrofit 35）完走

**日付**：2026-06-15
**種別**：連動軸 retrofit（retrofit 7/30/33 型・新規 sg 新設なし・既存軸被覆拡張のみ）
**起点 HEAD**：`3d3f92e`（理趣釈 motif 第3ラウンド・全3ラウンド完走・push 済を着手前に確認）
**ステータス**：retrofit 35 完了・整合性検証 10 項目＋巻き戻り assert 全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・_dev_references/motifs_index_design.md・CLAUDE.md・commit_message.txt・本メモ。corpus・manifest・索引は不変。

---

## Phase A 合意（軸設計・ケンシン裁定 2026-06-15）

理趣釈は理趣経本文の逐段注釈であるため、独自の中心成句を立てず、理趣経由来・古典 anchor へ親子連動を張る方針。4 軸の被覆拡張のみ。

- sg30 十七清浄句（anchor m2400）／sg08 阿字本不生（anchor m549・吽字義）／sg03 即身成仏（anchor m533・即身成仏義）／sg31 大欲・百字偈（anchor m2413）。
- **転識得智（m2447・文殊段 四智剣）は新規 sg 見送り**：1 件のみ・「転識得智」は成句フレーズというより教学術語で成句性が弱い。sg28/29 の 1 件クラスタ先例があっても新設せず、主題:転識得智 タグのみ温存。
- sg30 範囲＝m2421/m2422＋m2423（第17句 般若波羅蜜多清浄も含む）。sg03 範囲＝核心 m2457 のみ（聞持功徳系は除外）。sg08 字釈＝3件すべて採用。

## Phase B 判定表（連動タグ +16／8 motif・確定）

| id | 段／節 | 連動先 | 付与タグ |
|---|---|---|---|
| m2421 | 初段・十七清浄句① | sg30 | 連動:sg30・連動:m2400 |
| m2422 | 初段・十七清浄句② | sg30 | 連動:sg30・連動:m2400 |
| m2423 | 初段・第17句 自性清浄 | sg30 | 連動:sg30・連動:m2400 |
| m2427 | 初段・吽字四字義 | sg08 | 連動:sg08・連動:m549 |
| m2454 | 第十段・郝字四義 | sg08 | 連動:sg08・連動:m549 |
| m2452 | 第九段・唵字 | sg08 | 連動:sg08・連動:m549 |
| m2457 | 第十二段・一切有情如来蔵 | sg03 | 連動:sg03・連動:m533 |
| m2464 | 第十七段・百字偈配釈 | sg31 | 連動:sg31・連動:m2413 |

除外：m2424/m2444（聞持功徳・経証的＝retrofit 5/7 の経証除外原則を継続）・m2438/m2458 等（連動先成句なし）。

## Phase C 反映（build script・dry-run→--apply）

- build script：`outputs/retrofit35_rishushaku_rendou.py`（既存連動タグ重複 guard 付き）。バックアップ：`outputs/motifs_backup_pre_retrofit35.json`。
- **タグのみ変更につき stats 不変**：total_motifs 2496・famous_phrases 31・字数3種（kk 280904／gd 768468／gabun 238704）・篇別内訳・without_gabun いずれも不変。連動タグ総数 **550→566（+16）**。
- schema_history(top-level) +1（origin: `retrofit_35:rishushaku_rendou_scan`）・stats.schema_history 不変・schema 0.2 維持。
- top-level description を現況同期（R1-R3 stale 是正）：2445 motifs/m1〜m2414/retrofit 34 → **2496 motifs/m1〜m2465・理趣釈 16 著作目・retrofit 35**。連動軸は二十七系統並立を維持（新規 sg なし）。

## 検証（10 項目・全 pass）

NUL0／JSON 再パース／total==配列数 2496（不変）／m-id 連番 missing=[] dup=False 最大 m2465／必須フィールド完全／連動タグ付与 missing=[]／stats recompute 全ゼロ（famous/kk/gd/gabun 不変）／連動タグ総数 +16／新規 motif 追加なし／schema 0.2・history +1。
＋**巻き戻り assert**：m506 引用形式:典籍曰く 温存／anchor m2400・m2413・m533・m549 の既存連動タグ温存／m2447 主題:転識得智 温存 — 適用前後で実施・全 pass。

## Phase D 必須チェックリスト（commit_push.bat 実行前）

- [x] motifs.json 反映完了（検証 全 pass）
- [x] schema_history(top) 追記済
- [x] motifs_index_design.md に **補注 LL** 追加済
- [x] 本体 CLAUDE.md 更新済（先頭 running-log 行に ★ retrofit 35 エントリ prepend）
- [x] **commit_message.txt 書き換え済**（冒頭行＝「理趣釈 連動軸 retrofit（retrofit 35）」で作業内容と整合）
- [x] 本 handoff 作成済
- [x] 全ファイル NUL 0／〔〕バランス（design 442=442）／半角括弧混入 0
- [x] サイズ差分が想定範囲内（motifs.json +16 タグ・design +34 行＝KK 復元 21＋LL 13）

## ⚠ 着手前に見つけた要確認事項（ケンシン裁定願い）

着手時、ワーキングツリーで **補注 KK（理趣経本文 gabun 要否裁定・HEAD=3d3f92e に存在）が誤って削除**されていた（設計ドキュメントの未コミット差分は当該 21 行削除のみ・他の編集なし）。次コミットでの欠落を防ぐため **HEAD から byte-identical に復元**のうえ補注 LL を追記した。意図的削除だった場合は再削除可。

なお git index に別件の未コミット状態あり（package.json/render.yaml/tsconfig.json/vercel.json 等の staged deletion・多数の outputs バックアップ）。これは本 retrofit と無関係の既存状態。commit_push.bat 実行前に `git status` で意図しないステージングが混ざっていないか目視確認を推奨。

## 残作業（次セッション以降）

1. **理趣釈 gabun 要否裁定**：理趣経本文（補注 KK）と同じく非空海・経典注釈系で意図的未設定の継続が見込み（補注 II ジャンル基準＝教学注釈系で未設定側）。文書 only セッション。
2. **kaimyo-app への motifs.json 同期**：倉庫 2496 → kaimyo-app・SHA-256 一致確認。新引用形式タグなし＝冠生成ロジック変更不要見込み。理趣釈の核心句がプール入りする場合 CORPUS_DISPLAY_NAME に rishushaku の表示名追加を要検討。

## 次セッション開始時の確認

1. CLAUDE.md 冒頭 → 本メモ → `git log --oneline -3`（HEAD が retrofit 35 コミット）
2. motifs.json：total_motifs 2496・最終 m-id m2465・schema 0.2・連動タグ 566
3. references/motif-extraction.md 必読（並行書き手・巻き戻り assert）

## ケンシン貼付用テンプレ（次＝理趣釈 gabun 要否裁定）

```
理趣釈（rishushaku.json）の gabun 要否裁定をしてください。まず CLAUDE.md 冒頭と
handoff_2026-06-15_rishushaku_retrofit35_rendou_complete.md を読み、git log で
HEAD が retrofit 35 コミットであることを確認。補注 KK（理趣経本文 gabun 裁定）・
補注 II（ジャンル基準）を踏襲し、理趣釈 全 motif（m2415-m2465）の gabun 要否を裁定。
理趣釈は非空海（伝・不空訳）・経典注釈系のため意図的未設定の継続が見込み。
補注 MM として記録（文書 only）。あわせて kaimyo-app への motifs.json 同期も残課題。
```
