# 引き継ぎメモ 2026-06-15 理趣経 Phase 2 完了（横断索引化・7 カテゴリ）

**日付**：2026-06-15
**種別**：横断索引化（kakikudashi-data スキル Phase 2・14 著作目）
**起点 HEAD**：`0c5df0f`（理趣経 Phase 1 昇格・push 済を着手前に確認）
**ステータス**：Phase 2 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/ 抽出 6 本＋aggregate_indices.py・data/mikkyou/（per-corpus 7 本新規＋集約 7 本再生成）・data/kukai/_corpus_manifest.json・CLAUDE.md・commit_message.txt・本メモ。motifs.json・既存 corpus は不変。

---

## 成果

### スクリプト（_dev_references/）
- extract 6 本（terms／citations／sanskrit／kaimyo_jukugo／persons／places）の
  `DICT_CORPUS_LIST` に `rishikyo.json` 追加（13 著作目の dict 型）
- `aggregate_indices.py` の `ALL_CORPORA` に `rishikyo` 追加（性霊集含め 14 著作目）
- ※ マウント同期不具合でホスト編集後の bash 側が末尾欠損して見えたため、
  git HEAD の無傷版＋1 行挿入を bash から書き戻して復旧（7 本とも parse OK・各 +1 行 diff 確認済）。

### per-corpus 索引（data/mikkyou/・新規 7 本）

| カテゴリ | ファイル | unique | occ | 備考 |
|---|---|---|---|---|
| terms | index_rishikyo_terms.json | 19 | 16 | matched 6/19・kaimyo_suitable 11・top 真言 6 |
| citations | index_rishikyo_citations.json | 1 | 1 | 理趣経 自題のみ（経典本文ゆえ他者典故なし・妥当） |
| kukai_works | index_rishikyo_kukai_works.json | 0 | 0 | 不空訳ゆえ空海著作引用なし（妥当） |
| sanskrit | index_rishikyo_sanskrit.json | 8 | 12 | IAST 6・ASCII 2・top hūṃ 5 |
| kaimyo_jukugo | index_rishikyo_kaimyo.json | 11 | 11 | matched 3・needs_review 0 |
| persons | index_rishikyo_persons.json | 10 | 34 | subcat 4・top 不空 9/観音 7/大日如来 5 |
| places | index_rishikyo_places.json | 3 | 11 | subcat 2・top 安楽 9/欲界 1/大興善寺 1 |

### 集約索引（index_*_all.json 7 本再生成・14 著作）
- terms：occ 3,257→3,273（+16）・unique 19 不変・multi 17・max_cov 13→**14**
- citations：occ 2,360→2,361（+1）・unique 547→**548**（+1・理趣経自題）
- kukai_works：完全不変（occ 55・unique 13）
- sanskrit：occ 2,672→2,684（+12）・unique 1,743→**1,750**（+7）・multi 141→142
- kaimyo_jukugo：occ 5,380→5,391（+11）・unique 114 不変・max_cov 13→**14**
- persons：occ 2,975→3,009（+34）・unique 90 不変・max_cov 12→**13**
- places：occ 906→917（+11）・unique 73 不変・multi 37→38
- **集約増分＝per-corpus 件数の照合：全 7 カテゴリ一致**（by_corpus.rishikyo 合算・伝播スポット確認済：安楽 9／不空 9／hūṃ 5／理趣経自題 1）

### manifest（_corpus_manifest.json）
- rishikyo エントリに `index_status`（7 カテゴリ present・件数入り）付与
- `summary.indexed_corpora` 全カテゴリ 13→14
- `aggregate_indices`：source_corpora に rishikyo 追加・corpora_count 13→14・
  description に 2026-06-15 拡張文を追記
- 再 dump 時に indent=2 で全行差分化したため **indent=1（原本書式）に統一**し diff を意味差分のみ（84 ins / 31 del）に圧縮
- バックアップ：outputs/_corpus_manifest.json.bak_pre_rishikyo_index（未追跡・コミット対象外・スクラッチで次回消える）

## 検証（全 pass）

- 倉庫側 _dev_references/validate_corpus.py：manifest_files 25 = real_files 25 整合 ✅ OK
- manifest：JSON 再パース OK・NUL 0・意味論的 diff = 意図した 31 箇所のみ（HEAD と構造比較で確認）
- CLAUDE.md：タイトル行に 2026-06-15 理趣経 Phase 2 ★ エントリを冒頭追記（diff 1 行・末尾不変をバイト比較で確認・NUL 0）
- motifs.json：**完全不変**（本 Phase では非対象）

## 付随事項（要認識）

1. **理趣経 Phase 1（0c5df0f）は既に commit / push 済**だった（着手前に git log・origin/main..HEAD 空で確認）。引き継ぎメモの残課題 1（commit）は完了済のため再 commit 不要。
2. 着手時に `M CLAUDE.md` の幻影差分（bash 側が最終行末尾 442 字を欠損表示）を検出 → ホスト Grep で実体＝HEAD と一致を確認・実変更なしと判定。マウント同期不具合は継続前提。
3. CLAUDE.md・スクリプトは bash 書込でも問題が出るため、git HEAD 無傷版から再構成して書き戻す方式を採用。文書確認はホスト Grep で実施。
4. 未追跡の outputs/_dryrun_*.json・_dev_scripts/ 等は従来どおり残置（コミット対象外）。

## 残作業（次セッション以降）

- **Phase 3：motif 抽出**（Phase A 合意から。author 不空訳＝非空海につき
  引用形式:典籍曰く 想定・大師系タグ非付与。短小真言段（k015-k017 天部心真言）の束ね方針・
  gabun 要否・連動軸は完走後 retrofit を Phase A で裁定。
  着手前に skills/kakikudashi-data/references/motif-extraction.md 必読）
- 完走後：kaimyo-app への motifs.json 同期（理趣経 motif がプール入りする場合
  CORPUS_DISPLAY_NAME に rishikyo: '理趣経' 追加を要検討）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本 Phase2 コミットであること）
2. manifest：summary.indexed_corpora 全カテゴリ 14・rishikyo index_status 7 present・aggregate corpora_count 14
3. data/mikkyou/index_rishikyo_*.json 7 本存在
4. motifs.json total_motifs=2428（理趣経本体 motif は未抽出・Phase3 で追加予定）
