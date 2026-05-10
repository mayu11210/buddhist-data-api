# 引き継ぎメモ：W2 本体マージセッション完走

**日付**：2026-05-11
**フェーズ**：Phase 4 W2 本体マージセッション
**対象**：buddhist-doctrine-workshop〔W2〕9/9 著作完走形〔254 件 tw001-tw254〕を本体 buddhist-data-api に統合
**ステータス**：完走〔整合性検証 13 項目すべて pass・retrofit 採用 5 項目反映・schema_history 統合 + version 補完完了・CLAUDE.md 更新完了〕
**次フェーズ**：W1〔buddhist-shoryoshu-workshop・性霊集 残 55 篇〕継続抽出 or W2 retrofit セッション〔候補 4・5〕or kaimyo-app 教学系素材活用〔ケンシン裁定〕

---

## (a) 本セッションの位置づけ

W2〔buddhist-doctrine-workshop〕が 2026-05-11 に 9/9 著作完走〔254 件 tw001-tw254〕に到達し、W2 完走確認・予備マージ準備セッションでマージ方針策定が完了した状態を引き継いで、workshop_protocol §10 に従い**本体マージセッション**を実施した。

ケンシン裁定で以下三推奨案を採用：

- 最優先タスク A：本体マージ着手〔W2 先行マージ〕
- retrofit 取扱：本体マージ時に取捨選択
- schema_history 取扱：本体マージ時に version 補完

本セッションで Phase A〔機械的マージ〕・Phase B〔retrofit 採用〕・Phase C〔schema 整合化〕・Phase D〔CLAUDE.md 更新〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：機械的マージ

| 項目 | マージ前 | マージ後 | 差分 |
|---|---|---|---|
| motifs 配列件数 | 496 | 750 | +254 |
| total_motifs | 496 | 750 | +254 |
| kakikudashi_chars_total | 37,473 | 112,756 | +75,283 |
| gendai_gabun_chars_total | 73,889 | 154,931 | +81,042 |
| gendaigoyaku_chars_total | 127,485 | 305,726 | +178,241 |
| motifs_with_gendai_gabun | 489 | 743 | +254 |
| 篇別内訳 エントリ | 58 | 67 | +9 |
| schema_history 件数 | 33 | 61 | +28 |
| m-id 範囲 | m1-m490 + sg01-sg06 | m1-m744 + sg01-sg06 | +254 |

#### 再番号付け表

- tw001 → m491
- tw254 → m744
- W2 全 254 件を本体最終 m-id m490 の次から連番〔m491-m744〕に機械的再番号付け

#### 篇別内訳追加〔教学系 9 著作・本体形式 dict〕

| corpus | 著作名 | motifs 範囲 | 件数 |
|---|---|---|---|
| hannya-hiken | 般若心経秘鍵 | m491-m505 | 15 |
| bodaishinron | 菩提心論 | m506-m520 | 15 |
| shoji-jisso | 声字実相義 | m521-m532 | 12 |
| sokushin-jobutsu | 即身成仏義 | m533-m548 | 16 |
| ujiji | 吽字義 | m549-m566 | 18 |
| nikyo-ron | 弁顕密二教論 | m567-m593 | 27 |
| hizo-houyaku | 秘蔵宝鑰 | m594-m655 | 62 |
| sankyo-shiki | 三教指帰 | m656-m676 | 21 |
| dainichikyo-sho-vol1 | 大日経疏 巻第一 | m677-m744 | 68 |
| **合計** | | **m491-m744** | **254** |

各エントリは本体形式の dict〔著作名／corpus／章節別motifs／motifs／件数〕で `stats.篇別内訳` に追加。

#### from_corpus_* 追加〔stats トップレベル〕

- from_corpus_hannya-hiken: 15
- from_corpus_bodaishinron: 15
- from_corpus_shoji-jisso: 12
- from_corpus_sokushin-jobutsu: 16
- from_corpus_ujiji: 18
- from_corpus_nikyo-ron: 27
- from_corpus_hizo-houyaku: 62
- from_corpus_sankyo-shiki: 21
- from_corpus_dainichikyo-sho-vol1: 68

性霊集の `from_idx*` 形式と並行して教学系 9 著作分を保持。

### Phase B：retrofit 採用 5 項目

| # | retrofit 候補 | 対象 tw | 対象 m-id | 追加タグ | 採用判断 |
|---|---|---|---|---|---|
| 1 | 引用形式:問答 細分化〔§87-88 偈問偈答対話形式〕 | tw245, tw246 | m735, m736 | 引用形式:問答 | 採用〔タグ値追加のみ・新規軸ではない〕 |
| 2 | 密教:百六十心 軸新設〔§90 菩提心の発生と百六十心越〕 | tw248 | m738 | 密教:百六十心 | 採用〔密教軸内タグ値追加〕 |
| 3 | 典故:十二門論 軸新設〔§97 自在天破斥の典拠〕 | tw253 | m743 | 典故:十二門論 | 採用〔典故軸内タグ値追加・典故:中論 から分離〕 |
| 4 | category:大師御言葉 タグの戯曲形式運用 | tw166-tw186 | m656-m676 | （未付与） | **不採用**〔対象判定が複数 motif・別途 retrofit セッションに譲る〕 |
| 5 | 即身成仏義 sg06 連動 retrofit | tw208/234/243/239/250 | m698/m724/m733/m729/m740 | （未付与） | **不採用**〔連動タグ設計が未確定・別途 retrofit セッションに譲る〕 |
| 6 | 主題:三句法門〔秘蔵宝鑰 第八住心 一道無為心〕 | tw147 のみ | m637 | 主題:三句法門 | 採用〔代表 motif 限定付与・tw147-tw165 全件付与は過剰と判断〕 |
| 7 | 密教:初法明道〔§3 経証で既引用済〕 | tw147 | m637 | 密教:初法明道 | 採用〔密教軸内タグ値追加〕 |

採用 5 項目はいずれも既存軸〔引用形式・密教・典故・主題〕内のタグ値追加であり、workshop_protocol §3 §5 の「新規軸の発明は本体マージで合意」基準を満たさない〔軸新設ではないため自動採用可〕。

### Phase C：schema 整合化

- W2 schema_history 27 エントリのうち version 欠落 16 件〔エントリ 12-27 = 秘蔵宝鑰 巻の中 抜業因種心 完走以降〕を version=0.2 で補完
- 各 W2 エントリに `origin: W2:buddhist-doctrine-workshop` タグを付与〔本体既存エントリと区別〕
- マージ完走エントリ〔本セッション〕を末尾に追加
- 本体 schema_history 合計：33 + 27 + 1 = **61 エントリ**
- schema_version は 0.2 維持〔フィールド構造変更なし・データ拡張のみ〕
- W2 トップレベル `_workshop` セクション破棄〔本体に持ち込まない〕

### 整合性検証 13 項目〔すべて pass〕

| # | 項目 | 結果 |
|---|---|---|
| 1 | ファイルサイズ | 2,585,027 bytes |
| 2a | 半角括弧〔motif 本体〕 | open=0, close=0 ✓ |
| 2b | 半角括弧〔全体〕 | open=9, close=9〔本体既存メタのみ〕 ✓ |
| 3 | NUL バイト any/trailing | 0/0 ✓ |
| 4 | schema_version | 0.2 ✓ |
| 5 | schema_history 件数 | 61〔33+27+1〕 ✓ |
| 6 | total_motifs〔stats vs 配列〕 | 750 vs 750 ✓ |
| 7 | 必須フィールド完全性 | 750/750 ✓ |
| 8 | source 全 dict 形式 | 750/750 ✓ |
| 9 | tags 全 list[str] 形式 | 750/750 ✓ |
| 10 | stats vs recompute 差分〔全 5 項目〕 | (0, 0, 0, 0, 0) ✓ |
| 11 | 篇別内訳 全 dict 形式 | 67/67 ✓ |
| 12 | id 重複件数 | 0 ✓ |
| 13 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |

### Phase D：CLAUDE.md 更新

- タイトル行先頭〔最新エントリ位置〕に本マージセッション完走エントリを追加〔約 1,576 bytes〕
- 末尾の最終更新行に 2026-05-11 のマージセッション完走エントリを追加〔約 2,705 bytes〕
- 合計 +4,281 bytes 追加

### 設計上の新規ポイント

#### (i) 教学系 corpus の篇別内訳 dict 形式の確立

本体既存の性霊集 `性霊集_idx{n}_篇名` キー形式に対し、教学系は `教学系_{corpus}_{著作名}` 形式で命名。dict 内部は `著作名` `corpus` `章節別motifs` `motifs` `件数` の 5 フィールド構造。性霊集とは情報粒度が異なる〔性霊集は篇単位、教学系は著作単位〕が、いずれも本体 dict 形式の検証基準〔motifs_index_design.md §篇別内訳〕に準拠。

#### (ii) from_corpus_* と from_idx_* の並行運用

stats トップレベルに `from_idx*`〔性霊集〕と `from_corpus_*`〔教学系〕を並行配置。kaimyo-app 等の利用側で著作別件数を簡易取得可能。

#### (iii) schema_history の origin タグ

W2 由来エントリには `origin: W2:buddhist-doctrine-workshop` を付与し、本体側で workshop 由来エントリを識別可能に。今後の W1 マージでも同じ慣例を踏襲する〔origin: W1:buddhist-shoryoshu-workshop〕。

#### (iv) Edit tool truncate 事象の再現と対処

本セッションでも CLAUDE.md ルール記載の Edit tool 長文置換時の truncate 事象が再現発生〔Python script の Edit 後、ファイル末尾が `if __name__ == '__` で切断〕。Write tool 全文書直で対処。CLAUDE.md ルール「長文編集は Python script で in-memory 編集後 write back する代替手法」を本セッションで実証。

#### (v) 半角括弧の運用方針確立

motif 本体〔motifs 配列内〕は半角括弧 0 件達成。本体既存メタ情報〔schema_history・description〕の 9 件は本体運用上の許容範囲として温存。新規追加分〔本マージで追加した description・schema_history.changes〕は全角〔 〕で運用。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：W1 継続抽出〔buddhist-shoryoshu-workshop〕

W1 は性霊集 残 55 篇が並列進行中〔本体側で第 19 ラウンドまで完走済・W1 workshop に切替後の継続進捗は要確認〕。W1 完走時点で第 2 回本体マージセッションを実施。

利点：性霊集 motif の継続蓄積・kaimyo-app の性霊集系素材の拡充
欠点：W1 workshop 側の現況確認〔現在の状態・完走見込み〕が必要

### 選択肢 B：W2 retrofit セッション〔候補 4・5〕

本体マージ時に不採用とした以下 2 項目を別途実施：

- **retrofit 4** category:大師御言葉 タグの戯曲形式運用〔三教指帰 m656-m676 = tw166-tw186〕：三教指帰は戯曲形式〔対話劇〕で進行する著作のため、本体既存 category:大師御言葉 タグの運用を戯曲形式向けに拡張するか〔例：引用形式:対話 or 文体:戯曲 軸を新設〕の検討。各 motif の発言主体〔亀毛先生・兎角公・虚亡隠士〕を識別するタグ設計が必要。

- **retrofit 5** 即身成仏義 sg06「父母所生身、速証大覚位」連動 retrofit〔sg06 本体側 + tw208/234/239/243/250 = m698/m724/m729/m733/m740〕：sg06 は本体側で既存の成句として保持。これと連動する教学系 motif〔R23 §28 頓覚成仏／R27 §76 即時人法戯論浄／R27 §85 龍樹冶人譬／R27 §81 真言門行者一生成弁／R28 §92 五通仙人薬物錬冶譬〕に連動タグを付与する設計。連動タグの軸名〔連動 or 連動成句 等〕と運用ルール〔kaimyo-app での参照経路〕の合意が必要。

### 選択肢 C：kaimyo-app 教学系素材活用

本マージで kaimyo-app は教学系 9 著作 254 motif を即座に参照可能になった。kaimyo-app 側で：

- 即身成仏義 sg06 連動句〔本マージで m698/m724/m729/m733/m740〕の活用
- 吽字義 阿字本不生・声字実相義 五大皆有響〔密教教学核心句〕の戒名・諷誦文への組込
- 弁顕密二教論 顕密二教判・秘蔵宝鑰 十住心〔教学体系〕の法話素材化
- 大日経疏 三句法門・菩提心論 三摩地戒〔密教実践〕の引用句活用
- 般若心経秘鍵 文殊般若・三教指帰 儒道仏比較〔導入素材〕の教学解説活用

kaimyo-app 側の引き継ぎメモも参照しながら進める。

### 選択肢 D：W2 repo 凍結〔workshop_protocol §10(5)〕

W2 buddhist-doctrine-workshop は本マージで役割完了。workshop_protocol §10(5) 通り凍結：

- archive 化：GitHub.com 上で archive 化〔読み取り専用化〕
- ローカル：W2 フォルダの読み取り専用化 or `_archive/` 配下への移動

凍結タイミング・方式はケンシン判断。再開する場合は新 workshop を立ち上げる方針。

---

## (d) 副次発見・要注意事項

### (d-1) Edit tool 長文 truncate 事象の再現

CLAUDE.md ルール記載の「再現性のあるファイル truncate 事象〔Edit tool での長文置換時〕」が本セッションで再現発生：

- 状況：Python script `merge_w2_into_body.py` の長文（約 350 行）に対して、Edit tool で複数箇所を置換した結果、ファイル末尾の `if __name__ == '__main__':` 行が「if __name__ == '__」で切断
- 検知：bash 実行で SyntaxError: unterminated string literal が発生
- 対処：Write tool で全文書直〔今回のスクリプト全体を 1 回の Write で書き直す〕

教訓：

- 長文ファイル〔Python script・CLAUDE.md・motifs.json 等〕の編集は Python script による in-memory 編集 + write back を採用〔本セッションでも Python script でファイル更新を実施〕
- Edit tool は短文・1 箇所限定の置換に留める

### (d-2) 半角括弧の運用方針

本体側〔CLAUDE.md・motifs.json schema_history・description〕には半角括弧が運用上残存する〔英文表記・セクション番号 (1) (2) 等〕。motif 本体〔motifs 配列内〕の半角括弧 0 件達成を優先し、メタ情報の半角括弧は本体運用上の許容範囲。

本マージで新規追加した部分〔description・schema_history.changes〕は全角〔 〕運用に統一。本体既存の半角括弧 9 件はマージ前から存在するメタ情報の括弧として温存。

### (d-3) W2 schema_history version 欠落補完

W2 schema_history エントリ 12-27〔16 件・秘蔵宝鑰 巻の中 抜業因種心 完走以降〕は `"version"` フィールドが欠落していた。本マージで一律 `"version": "0.2"` を補完して統合。エントリ構造は `{version, round, date, summary, origin}` の 5 フィールド〔origin は本マージで追加〕。

将来 W1 マージでも version 欠落を確認し、同様の補完を実施する。

### (d-4) W2 _workshop セクション破棄

W2 motifs.json トップレベルの `_workshop` セクション〔workshop メタ情報・name/purpose/id_prefix/body_baseline_commit/target_corpora/last_round 等 11 フィールド〕は本マージで破棄。本体には持ち込まない方針。

将来 W1 マージでも同様の方針を踏襲する〔W1 側の `_workshop` セクションは本体に持ち込まない〕。

### (d-5) 本体側 schema_history と stats 内 schema_history の二重保持

本体 motifs.json には schema_history がトップレベル〔61 件〕と stats 内〔11 件〕の二重に存在する。stats 内の schema_history は古い形式の遺物と思われる〔最初の 11 エントリのみ・以後はトップレベルに集約された〕。本マージでは現状維持し、本体マージで触らない〔本体既存運用との互換性を優先〕。

整理は将来別セッションで判断〔stats 内を削除 or トップレベルへ統合〕。

### (d-6) ファイル容量

本体 motifs.json は 1,306,750 bytes → 2,585,027 bytes へ。約 2 倍に拡大。次回 W1 マージで再び拡大する見込み〔W1 残 55 篇分・約 1MB 想定〕。

巨大化対策：

- motifs.json の分割保持〔性霊集 motifs.json・教学系 motifs.json 等〕
- データベース化〔SQLite 等への移行・aggregate_indices.py 系列と連動〕

設計上の判断は本マージ後の別セッションで議論。

### (d-7) retrofit 4・5 の対象判定の複雑性

retrofit 4〔category:大師御言葉 戯曲形式運用〕は三教指帰 21 motif すべての発言主体識別が必要。retrofit 5〔即身成仏義 sg06 連動〕は連動タグの軸設計〔軸名・運用ルール〕が必要。いずれも複数 motif への一括判断ができないため、別途 retrofit セッションで 1 件ずつ検討する方針。

retrofit セッションでは Phase A〔軸設計合意〕・Phase B〔対象 motif の判定〕・Phase C〔本体 motifs.json 反映〕の三段で進める。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔750 件・m1-m744 + sg01-sg06・2,585,027 bytes〕
- W2〔凍結予定〕：`C:\Users\user\buddhist-doctrine-workshop\`
- W2 motifs.json：`data/indices/motifs.json`〔254 件 tw001-tw254・1,264,123 bytes・凍結予定〕
- 前セッション handoff〔W2 完走確認・予備マージ準備〕：`C:\Users\user\buddhist-doctrine-workshop\handoff_2026-05-11_w2_completion_summary.md`
- 本セッション build script：`outputs/merge_w2_into_body.py`〔本体マージ用 Python script・dry-run + 本番適用の二段運用〕
- 本セッション CLAUDE.md 更新 script：`outputs/update_claude_md.py`
- バックアップ：`outputs/motifs_backup_pre_w2_merge.json`〔マージ前 motifs.json〕／`outputs/CLAUDE_md_backup_pre_w2_merge.md`〔マージ前 CLAUDE.md〕
- workshop_protocol：`_dev_references/workshop_protocol.md`〔§10 移設マージセッション手順〕
- schema 仕様：`_dev_references/motifs_index_design.md`〔schema 0.2 真値〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（W2 マージ完了後・W1 継続抽出 or W2 retrofit 着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。W1 継続抽出の場合は同時に W1 側 `C:\Users\user\buddhist-shoryoshu-workshop` も接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
W2〔buddhist-doctrine-workshop〕は 2026-05-11 に 9/9 著作完走〔254 件 tw001-tw254〕→ 同日 Phase 4 W2 本体マージセッション完走で本体 motifs.json に統合済。本体は 750 motif〔m1-m744 + sg01-sg06〕・kakikudashi 112,756 字・gendai_gabun 154,931 字・gendaigoyaku 305,726 字に到達。次フェーズは以下から選択：(A) W1 継続抽出／(B) W2 retrofit セッション〔候補 4・5〕／(C) kaimyo-app 教学系素材活用／(D) W2 repo 凍結手続。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_w2_merge_complete.md`〔本マージセッション完走サマリ・本ファイル〕
2. `C:\Users\user\buddhist-data-api\_dev_references\workshop_protocol.md`〔W1 継続抽出の場合〕
3. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様〕
4. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・750 件〕
5. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕

【本セッションの選択肢】
(A) W1 継続抽出〔buddhist-shoryoshu-workshop〕：性霊集 残 55 篇から motif 抽出
(B) W2 retrofit セッション〔候補 4・5〕：category:大師御言葉 戯曲形式運用 + 即身成仏義 sg06 連動 retrofit
(C) kaimyo-app 教学系素材活用：即身成仏義 sg06 連動句・吽字義 阿字本不生 等の戒名・諷誦文への組込
(D) W2 repo 凍結手続：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避〕
- 本体 motifs.json は 2,585,027 bytes〔本マージ後〕・W1 マージで再拡大見込み〔将来分割設計検討〕
```

---

最終更新：2026-05-11〔Phase 4 W2 本体マージセッション完走・整合性検証 13 項目すべて pass・本体 750 件 m1-m744 + sg01-sg06・kakikudashi 112,756 字／gendai_gabun 154,931 字／gendaigoyaku 305,726 字・schema_history 61 件統合・retrofit 採用 5 項目反映・CLAUDE.md 更新完了〕
