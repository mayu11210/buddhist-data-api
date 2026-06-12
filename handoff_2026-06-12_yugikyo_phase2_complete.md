# 引き継ぎメモ 2026-06-12 瑜祇経 Phase 2 完了（横断索引化・7 カテゴリ）

**日付**：2026-06-12
**種別**：横断索引化（kakikudashi-data スキル Phase 2・13 著作目）
**起点 HEAD**：`6595751`（瑜祇経 Phase 1 取込・push 済を着手前に確認）
**ステータス**：Phase 2 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/ 抽出 6 本＋aggregate_indices.py・data/mikkyou/（per-corpus 7 本新規＋集約 7 本再生成）・data/kukai/_corpus_manifest.json・CLAUDE.md。motifs.json・既存 corpus は不変。

---

## 成果

### スクリプト（_dev_references/）
- extract 6 本（terms／citations／sanskrit／kaimyo_jukugo／persons／places）の
  `DICT_CORPUS_LIST` に `yugikyo.json` 追加（12 著作目の dict 型）
- `aggregate_indices.py` の `ALL_CORPORA` に `yugikyo` 追加（性霊集含め 13 著作目）

### per-corpus 索引（data/mikkyou/・新規 7 本）

| カテゴリ | ファイル | unique | occ | 備考 |
|---|---|---|---|---|
| terms | index_yugikyo_terms.json | 19 | 151 | matched 7/19・kaimyo_suitable 6・top 真言 117 |
| citations | index_yugikyo_citations.json | 0 | 0 | 経典本文ゆえ典故引用なし（妥当） |
| kukai_works | index_yugikyo_kukai_works.json | 0 | 0 | 同上 |
| sanskrit | index_yugikyo_sanskrit.json | 0 | 0 | 訳文に IAST 表記なし |
| kaimyo_jukugo | index_yugikyo_kaimyo.json | 11 | 146 | matched 6・needs_review 0 |
| persons | index_yugikyo_persons.json | 14 | 63 | subcat 4・top 虚空蔵 15・普賢 14 |
| places | index_yugikyo_places.json | 9 | 11 | subcat 4・top 安楽 2・殷 2 |

### 集約索引（index_*_all.json 7 本再生成）
- terms：occ 3,106→3,257（+151）・multi 16→17・max_cov 13/13
- kaimyo_jukugo：occ 5,234→5,380（+146）・unique 114 不変・multi 76→77
- persons：occ 2,912→2,975（+63）・unique 90 不変・max_cov 11→12
- places：occ 895→906（+11）・unique 72→**73（+1・新規「南天竺」yugikyo 単独）**・max_cov 10→11
- citations／kukai_works／sanskrit：完全不変
- **集約増分＝per-corpus 件数の照合：全 7 カテゴリ一致**（by_corpus.yugikyo 合算で確認）

### manifest（_corpus_manifest.json）
- yugikyo エントリに `index_status`（7 カテゴリ present・件数入り）付与
- `summary.indexed_corpora` 全カテゴリ 12→13
- `aggregate_indices`：source_corpora に yugikyo 追加・corpora_count 13・
  description に 2026-06-12 拡張文を追記・generated_at 2026-06-12
- バックアップ：outputs/_corpus_manifest.json.bak_pre_yugikyo_index（未追跡・コミット対象外）

## 検証（全 pass）

- 倉庫側 _dev_references/validate_corpus.py：manifest_files 25 = real_files 25 整合 OK
- manifest：JSON 再パース OK・NUL 0・末尾改行なし維持・ホスト側 Grep で反映確認
- motifs.json：**完全不変**（git diff なし・total_motifs 2391・
  m506 引用形式:典籍曰く assert pass・巻き戻りなし）

## 付随事項（要認識）

1. **Phase 1 セッションは CLAUDE.md を更新していなかった**（commit 6595751 に
   CLAUDE.md 含まれず）。本セッションで Phase 1・Phase 2 両エントリを冒頭に追記済。
2. **commit 6595751 に _dev_references/shoryoshu_gendaigoyaku_input.txt の
   241 行変更が混入していた**（Phase 1 の対象外ファイル）。さらに作業樹で同ファイルが
   CRLF 化していたため、HEAD の LF 版に復元（内容同一・noise diff 解消）。
   bash 側 git status に stat キャッシュ由来の M 表示が残るが diff は空。
3. 未追跡の outputs/_dryrun_*.json・_dev_scripts/ 等は従来どおり残置（コミット対象外）。

## 残作業（次セッション以降）

- **Phase 3：motif 抽出**（Phase A 合意から。author 伝・金剛智訳につき
  引用形式:典籍曰く 想定。巻下の短小真言段落 k032-k047 の束ね方針を Phase A で裁定。
  着手前に skills/kakikudashi-data/references/motif-extraction.md 必読）
- kaimyo-app 側 motifs.json 同期（既存残課題・本件とは独立）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. manifest：indexed_corpora 全カテゴリ 13・yugikyo index_status 7 present
3. data/mikkyou/index_yugikyo_*.json 7 本存在
4. motifs.json total_motifs=2391・m506 引用形式:典籍曰く（巻き戻り検知・本件では不変のはず）
