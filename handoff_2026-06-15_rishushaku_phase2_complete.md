# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）Phase2 完了（横断索引化・7 カテゴリ）

**日付**：2026-06-15
**種別**：横断索引化（kakikudashi-data スキル Phase2・15 著作目）
**起点 HEAD**：`d440142`（理趣釈 genten retrofit・push 済を着手前に確認）
**ステータス**：Phase2 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/ 抽出 6 本＋aggregate_indices.py・data/mikkyou/（per-corpus 7 本新規＋集約 7 本再生成）・data/kukai/_corpus_manifest.json・CLAUDE.md・commit_message.txt・本メモ。motifs.json・既存 corpus は不変。

---

## 成果

### スクリプト（_dev_references/）
- extract 6 本（terms／citations／sanskrit／kaimyo_jukugo／persons／places）の `DICT_CORPUS_LIST` に `rishushaku.json` 追加（14 著作目の dict 型）
- `aggregate_indices.py` の `ALL_CORPORA` に `rishushaku` 追加（性霊集含め 15 著作目）
- 各スクリプトは git HEAD 無傷版＋1 行挿入で書き戻し、ast.parse で構文確認済

### per-corpus 索引（data/mikkyou/・新規 7 本）

| カテゴリ | unique | occ | 備考 |
|---|---|---|---|
| terms | 19 | 258 | matched 11/19・kaimyo_suitable 11・top 三摩地105/真言55/遮那41 |
| citations | 10 | 13 | top 指帰3・自題2 ほか（経典本文ゆえ他者典故少） |
| kukai_works | 0 | 0 | 不空訳ゆえ空海著作言及なし（妥当） |
| sanskrit | 0 | 0 | gendaigoyaku 側に IAST 表記なし（悉曇は genten 側にローマ字・抽出対象外） |
| kaimyo_jukugo | 11 | 142 | matched 7・needs_review 0・top 真言/遮那/法界 |
| persons | 11 | 140 | subcat 4・top 大日如来41/不空23/観音20 |
| places | 9 | 22 | subcat 4・top 安楽8/欲界4 |

### 集約索引（index_*_all.json 7 本再生成・15 著作）
- terms：occ 3,273→3,531（+258）・unique 19 不変・multi 17・max_cov 14→**15**
- citations：occ 2,361→2,374（+13）・unique 548→**555**（+7）
- kukai_works：完全不変（occ 55・unique 13）
- sanskrit：完全不変（occ 2,684・unique 1,750）
- kaimyo_jukugo：occ 5,391→5,533（+142）・unique 114 不変・max_cov **15**
- persons：occ 3,009→3,149（+140）・unique 90 不変・max_cov 14
- places：occ 917→939（+22）・unique 73 不変・multi 38
- **集約増分＝per-corpus 件数の照合：全 7 カテゴリ一致**（by_corpus.rishushaku 合算 = per-corpus occ：terms 258／citations 13／kaimyo 142／persons 140／places 22／sanskrit 0／kukai_works 0）

### manifest（_corpus_manifest.json）
- rishushaku エントリに `index_status`（7 カテゴリ present・件数入り・各 per-corpus 埋め込み summary と突合一致）付与
- `summary.indexed_corpora` 全カテゴリ 14→15
- `aggregate_indices`：source_corpora に rishushaku 追加・corpora_count 14→15・description に 2026-06-15 拡張文を追記・files.<cat> 統計を再生成値に更新
- indent=1（原本書式）統一で diff を意味差分のみ（81 ins / 28 del）に圧縮
- バックアップ：outputs/_corpus_manifest.json.bak_pre_rishushaku_index（未追跡・スクラッチ）

## 検証（全 pass）
- 倉庫 _dev_references/validate_corpus.py：manifest_files 26 = real_files 26 整合 ✅ OK
- 新規 per-corpus 7 本＋集約 7 本＋manifest：JSON 再パース OK・NUL 0
- index_status 全フィールド＝per-corpus 埋め込み summary と一致を機械照合
- CLAUDE.md：理趣釈 Phase 2 ★ エントリを冒頭追記（host Grep で反映確認・NUL 0）
- motifs.json：**完全不変**（本 Phase では非対象）

## 付随事項
1. 理趣釈 genten retrofit（d440142）は着手前に commit/push 済を確認（origin/main..HEAD 空）。
2. bash 側 git に既存の幻影差分（_dev_references/motifs_index_design.md の M 等）・実削除（package.json 等の旧 web 雛形整理・未 commit）が残存。本 Phase の変更とは無関係。commit_push.bat の Step4.5 削除ガードに留意。
3. マウント同期不具合継続前提：文書はホスト側ツールで確認、bash 書込 JSON はホスト Grep で反映確認。

## 残作業（次工程）
- **Phase3：motif 抽出**（references/motif-extraction.md 必読）。Phase A 合意から：
  - author=伝・不空訳＝**非空海** → 引用形式:典籍曰く 想定・大師系タグ非付与
  - 短小段（首題 k001／訳者 k002／尾題 k057・真言列挙段等）の motif 化要否・束ね方針
  - gabun 要否（hizoki/yugikyo/理趣経本体・開題と同じく意図的未設定が見込み）
  - 連動軸は完走後 retrofit
  - 理趣経本体（rishikyo m2400-m2414）・理趣経開題（rishukyo-kaidai m2384-m2399）との相互参照に留意
- 完走後：連動軸 retrofit・gabun 裁定・kaimyo-app への motifs.json 同期

## 次セッション開始時の確認
1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本 Phase2 コミットであること）
2. manifest：summary.indexed_corpora 全カテゴリ 15・rishushaku index_status 7 present・aggregate corpora_count 15
3. data/mikkyou/index_rishushaku_*.json 7 本存在
4. motifs.json total_motifs=2445（理趣釈 motif は未抽出・Phase3 で追加予定）
