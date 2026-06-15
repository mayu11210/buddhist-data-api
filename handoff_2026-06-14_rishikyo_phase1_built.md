# 引き継ぎメモ 2026-06-14 理趣経（T0243・不空訳）Phase1 取込（生成・検証済・未 commit）

**日付**：2026-06-14
**種別**：新規 corpus 取込（kakikudashi-data Phase1）／**Phase1 完了・commit_push.bat 実行待ち**
**起点 HEAD**：`89e1ee9`（kaimyo-app 同期完了の記録）
**ステータス**：rishikyo.json 生成＋スキル validate＋倉庫全件 validate 済・manifest 昇格済（type dict_paragraphs 是正）・CLAUDE.md 反映済・**未 commit / 未 push**（commit_push.bat 実行で完了）
**変更ファイル**：data/kukai/rishikyo.json（昇格・本文新規）・data/kukai/_corpus_manifest.json（rishikyo 昇格）・commit_message.txt・本メモ。**data/indices/motifs.json は不変**。

---

## 今セッションでやったこと

1. **素材**：ユーザー提供 `理趣経 書き下し.doc`（理趣経本体＝大楽金剛不空真実三摩耶経 般若波羅蜜多理趣品・不空訳）。
2. **段落抽出**：extract_paragraphs.py → 20 段落（表題＋経題＋訳者＋本文17段）。
3. **genten 取得（ケンシン裁定：CBETA T0243 取込）**：web_fetch は CBETA reader が JS レンダリングで本文取れず（API/GitHub raw もタイムアウト）。**Chrome MCP（Browser 1・ローカル）で reader をレンダリングし get_page_text で全文取得**。校勘記号 \[n\]/\[An\] を除去、真言音写は漢字のまま、雙行夾註（引・二合・短 等）は温存。genten 3,466 字（outputs/rishikyo_genten.txt → corpus に格納）。
4. **現代語訳（butten-yasashii-yaku）**：本文17段＋経題・訳者を全訳。割注〔〕で原語温存・全角括弧厳守・真言は読み＋教義的意味を注記。現代語訳 8,355 字。
5. **build_corpus.py**：config_rishikyo.json（title_is_first・sections 16・meta に genten/genten_source/text 温存）→ `data/kukai/rishikyo.json`（19 段落 k001-k019・99,862 bytes・NUL 0）。
6. **manifest 昇格**（手動 Edit）：excerpt_stub→primary_corpus・data_status 3 種 true・char_counts（書き下し5394/訳8355/genten3466/text326）・role_complete=true・taisho_ref「T0243 / vol.8（不空訳）」。

## ケンシン裁定（本セッション）

- 作業範囲：**Phase1 取込まで**（Phase2 横断索引化・Phase3 motif 抽出は別セッション）。
- genten：**CBETA T0243 を取込**（書き下しのみ案ではなく原典取込を選択）。
- 取込先：既存スタブ rishikyo.json を昇格（新規 rishukyo.json は作らない）。section 名は「理趣経（大楽金剛不空真実三摩耶経 般若波羅蜜多理趣品）」。

## 検証（済）

- スキル validate_corpus.py：JSON 再パース OK・NUL 0・段落19/未訳0・現代語訳 半角括弧 0・**総合 OK**。
- 段落構成：k001 経題／k002 訳者／k003 序分（十七清浄句＋大楽不空三摩耶心）／k004-k014 正宗分 各如来段／k015-k017 天部心真言（七母女天・末度迦羅天・四姉妹女天）／k018 究竟段＋深秘百字偈／k019 流通分。

## 完了済（2026-06-14 再開セッション）

- 倉庫側 _dev_references/validate_corpus.py 全件横断：manifest 25／実 25 一致・✅ OK。
  初回 type 不一致（manifest 'dict' vs 実体 'dict_paragraphs'）を是正（dict_paragraphs・schema_ref null・hizoki/yugikyo 同形式）。
  manifest の bash ミラー末尾 NUL（マウント同期不具合）を除去済。
- CLAUDE.md タイトル行・現在の進捗に理趣経 Phase1 を反映（進捗テーブルに rishikyo 専用行はなし）。
- commit_push.bat は `git add data/kukai/`・`CLAUDE.md`・`*.md` を含むため rishikyo.json／_corpus_manifest.json／CLAUDE.md／本メモが staged される。Step 4.5 deleted ガードあり・削除なしで安全。

## 残課題（次セッション・この順で）

1. **commit**：commit_push.bat ダブルクリック（commit_message.txt 更新済）。push 後 `git log --oneline -2`。
2. **Phase2 横断索引化**：extract_terms/citations/sanskrit/kaimyo_jukugo/persons/places_dict.py の DICT_CORPUS_LIST と aggregate_indices.py の ALL_CORPORA に `rishikyo.json` を追加 → per-corpus 7 本生成 → 集約再生成 → manifest に index_status 付与・summary 更新。
4. **Phase3 motif 抽出**：references/motif-extraction.md 必読。Phase A 合意（不空訳＝非空海ゆえ **引用形式:典籍曰く** 想定・大師系タグ非付与・短小真言段の束ね方針・gabun 要否・連動軸は完走後 retrofit）。ラウンド制。
5. **CLAUDE.md** タイトル行・現在の進捗・進捗テーブルへ理趣経 Phase1 反映。
6. 完走後：kaimyo-app への motifs.json 同期（理趣経 motif がプール入りする場合 CORPUS_DISPLAY_NAME に rishikyo: '理趣経' 追加を要検討）。

## 注意点

- **作業中間ファイルはスクラッチパッド（outputs）にあり、次セッションで消える**：rishikyo_paras.json・trans_batch1.json・config_rishikyo.json・rishikyo_genten.txt。ただし内容はすべて rishikyo.json に格納済みのため再取得不要（Phase2/3 は corpus json から作業）。
- マウント同期不具合継続前提：文書はホスト側ツール（Read/Edit/Write/Grep）で編集・確認。bash 側 git status の幻影差分は commit_push.bat の index リセットで解消。
- 既存 motifs.json（total 2428）は不変。理趣経開題（rishukyo-kaidai）とは別 corpus（こちらは理趣経本体＝rishikyo）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD=89e1ee9・本 Phase1 は未 commit）
2. data/kukai/rishikyo.json：section「理趣経（…）」・paragraphs 19・translation_status remaining 0・genten 3466 字（ホスト側 Grep / python で確認）
3. _corpus_manifest.json：rishikyo エントリ role=primary_corpus・data_status 3 種 true
