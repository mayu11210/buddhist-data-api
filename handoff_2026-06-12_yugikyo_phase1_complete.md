# 引き継ぎメモ 2026-06-12 瑜祇経 Phase 1 完了（corpus 取込・全訳・genten 付き）

**日付**：2026-06-12
**種別**：新規 corpus 取込（kakikudashi-data スキル Phase 1・13 著作目の主要 corpus）
**起点 HEAD**：`54cf8f8`（2026-06-11 未追跡素材処遇 handoff・push 済を着手前に確認）
**ステータス**：Phase 1 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/kukai/yugikyo.json（新規）・data/kukai/_corpus_manifest.json（エントリ追加）のみ。motifs.json・既存 corpus・索引は不変。

---

## 成果

- **data/kukai/yugikyo.json**：金剛峯楼閣一切瑜伽瑜祇経（瑜祇経）・伝・金剛智訳・全二巻十二品
  - 段落 58（k001-k058）・kakikudashi 24,123 字・gendaigoyaku 30,789 字（**全段落訳済**）
  - outline 16 区分（section_major＝巻上・巻下／section＝品名）
  - genten：CBETA T0867 全二巻 18,408 字（清掃標点本文）＋genten_source
  - 訳文体：butten-yasashii-yaku（半角括弧 0・割注〔 〕）
- manifest：dict_paragraphs・primary_corpus・role_complete: true・char_counts に genten 含む

## ケンシン裁定（2026-06-12・Phase 1）

1. ファイル名は「巻上.doc」だが実内容は全巻 → **全巻を 1 ファイル**に収録
2. 底本の品第二重複（段落 6-8 / 9-10・本文完全一致）→ **後者（連続版）を採用**し前者削除
3. author は **「伝・金剛智訳」**（訳経帰属に学術上の疑義。motif 抽出時は
   非空海・伝承 → **引用形式:典籍曰く** の根拠になる）
4. genten は **CBETA から取込**（T0867）

## 素材・経緯メモ

- 素材 .doc は 62 段落・約 24,953 字。品第二の表題＋本文が二度出現（前者は途中で
  段落割れした版、後者は連続版・本文同一）→ 裁定 2 で 3 段落削除し 59 段落
  （表題＋本文 58）に整理。
- genten 取得：workspace の web_fetch で CBETA XML（raw.githubusercontent.com の
  cbeta-org/xml-p5 T/T18/**T18n0867.xml**）を取得。結果ファイルが途中切断していたため
  subagent が Chrome 経由で全文 643,702 字を取得し DOM パースで抽出
  （note 78 件除去・app/lem なし・悉曇 gaiji 1,342 件はローマ字転写・チェックサム照合済）。
  巻末尾題は底本どおり「金剛峯樓閣一切瑜伽瑜祇經」（甲本増字「卷下」不採用）。
- 書き下し側の明らかな誤植（薄迦梵・著薩・三味耶・大剛金剛項 等）は kakikudashi では
  底本のまま保持し、現代語訳側で正しい語義により訳出。

## 検証（全 pass）

- スキル同梱 validate_corpus.py：JSON 再パース OK・NUL 0・段落 58／未訳 0・半角括弧 0・総合 OK
- 倉庫側 _dev_references/validate_corpus.py（引数なし）：manifest_files 25 = real_files 25 整合 OK
- ホスト側 Grep：yugikyo.json・_corpus_manifest.json の書込反映を確認（マウント同期問題なし）

## 残作業（次セッション以降）

- **Phase 2：横断索引化**（7 カテゴリ。_dev_references/ 抽出 6 本の DICT_CORPUS_LIST と
  aggregate_indices.py の ALL_CORPORA に yugikyo.json を追加 → 実行 → manifest index_status 付与）
- **Phase 3：motif 抽出**（Phase A 合意から。author 伝承につき 引用形式:典籍曰く 想定。
  巻下の短小真言段落 k032-k047 の束ね方針は Phase A で裁定）
- kaimyo-app 側 motifs.json 同期（既存残課題・本件とは独立）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. data/kukai/yugikyo.json：translation_status total 58／remaining 0・genten 18,408 字
3. motifs.json total_motifs=2391・m506 引用形式:典籍曰く（巻き戻り検知・本件では不変のはず）
