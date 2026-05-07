# 引き継ぎメモ 2026-05-08 Phase 1 完了（workshop 方式移行・本体プロトコル整備）

## 本セッションの位置づけ

前セッション（候補 B 第 12 ラウンド完走・commit `3e261b3`）を起点に、**workshop 方式への移行合意**（前々セッション B10 5/7 最終で確立）に基づく **Phase 1：本体プロトコル整備**を実施。本体での motif 抽出は commit `3e261b3` を**最終地点**として完全停止し、以後は W1〔buddhist-shoryoshu-workshop〕・W2〔buddhist-doctrine-workshop〕の独立 GitHub repo で並列に motif 抽出を進める方針を本体側のプロトコルとして明文化した。

## 本セッションの主な成果

### 作成ファイル（4 ファイル）

| ファイル | 内容 | 字数 |
|---|---|---|
| `_dev_references/workshop_protocol.md` | 標準仕様書（12 章構成） | 約 5,500 字 |
| `_dev_references/workshop_CLAUDE_template.md` | workshop 用 CLAUDE.md テンプレ（7 章構成） | 約 1,500 字 |
| `_dev_references/workshop_commit_push_template.bat` | commit_push.bat テンプレ（path 引数化版） | 約 130 行 |
| `CLAUDE.md`（更新） | 本体 CLAUDE.md 更新〔進捗ヘッダ・次の作業セクション・並行候補テーブル・最終更新行〕 | – |

### workshop_protocol.md（12 章構成）

1. 概要（workshop 方式の目的・倉庫設計原則との関係）
2. 構成（W1 性霊集 / W2 教学系 9 著作）
3. スキーマ準拠（schema 0.2 凍結期間中の運用ルール）
4. ID 体系（staging プレフィックス：W1=sw001〜・W2=tw001〜・移設時に本体連番 m288 以降に再番号付け）
5. タグ軸の遵守（標準 9 軸 + 特殊 6 軸 + 成句例外）
6. 文体規定 7 項目（雅文体訳の執筆ガイド・再掲）
7. 必須検証項目（半角括弧予防的全角徹底・stats と recompute 差分ゼロ・篇別内訳 dict 形式・NUL 0 件）
8. 引き継ぎメモ運用（ASCII 名）
9. commit_push.bat 運用（path 設定方法・bash 経由 git 禁止）
10. 移設マージセッション手順（本体側で実施・各 workshop 完走時 1 回・1 セッション目安）
11. スキーマ更新プロトコル（本体で先に決定 → 全 workshop に通達 → 同時追従）
12. kaimyo-app との連携（移設後にすぐ参照可能）

### 本体 CLAUDE.md 更新内容

- **進捗ヘッダ**：「workshop 方式移行・本体での motif 抽出は commit `3e261b3` を最終地点に停止」を冒頭に追加。Phase 1 完了内容と全体ロードマップ Phase 1 → 2a → 2b → 3 → 4 を反映。
- **次の作業セクション**：全文書き換え。Phase 1 完了状態を明示し、Phase 2a（W1 性霊集 workshop 立ち上げ）の手順・全体ロードマップ・workshop 方式の全体像・段階的並列化選択肢・合意根拠を記載。
- **並行候補テーブル**：候補 L の状態を「★ 2026-05-08 commit `3e261b3` で本体最終地点・以後 motif 抽出は workshop 方式（候補 M）に移行 ★」に更新。**候補 M：workshop 立ち上げ・運用**を新規追加（状態：Phase 1 完了・次フェーズ Phase 2a）。
- **最終更新行**：(ξ) Phase 1 完了エントリを冒頭に追加。本セッション経緯（workshop 移行合意の経緯・前セッション引き継ぎメモへの反映漏れ・選択肢 (2) 採用）と Phase 2a 着手手順を記載。

## 全体ロードマップ

| Phase | 内容 | セッション数 | 並列可否 |
|---|---|---|---|
| **Phase 1** | **本体プロトコル整備（本セッション完了）** | **1（完了）** | **–** |
| Phase 2a | W1 性霊集 workshop 立ち上げ | 1 | Phase 2b と並列可 |
| Phase 2b | W2 教学系 workshop 立ち上げ | 1 | Phase 2a と並列可 |
| Phase 3 W1 | W1 で性霊集 第 13 ラウンド以降（残 77 篇） | 5〜10 | W2 と完全並列 |
| Phase 3 W2 | W2 で教学系 9 著作の motif 抽出 | 5〜8 | W1 と完全並列 |
| Phase 4 W1 | 移設マージ（本体に統合） | 1 | – |
| Phase 4 W2 | 移設マージ（本体に統合） | 1 | – |
| 合計 | – | 15〜23 | 並列で実時間 9〜13 程度 |

## 残作業：次セッション（Phase 2a：W1 性霊集 workshop 立ち上げ）

### ケンシン側操作

1. GitHub.com で `mayu11210/buddhist-shoryoshu-workshop` 作成（Private 推奨）
2. ローカルでクローン：`C:\Users\user\buddhist-shoryoshu-workshop\`
3. 本体から workshop_protocol.md・CLAUDE_template.md・commit_push_template.bat をコピー（path 書換え）
4. `data/kukai/shoryoshu_miyasaka.json` をコピー（参照用）
5. 初期 `data/indices/motifs.json` を作成（schema 0.2・空 motifs 配列）
6. Cowork 起動 → このフォルダ（`C:\Users\user\buddhist-shoryoshu-workshop`）を選択

### Phase 2a セッションでの Cowork 側作業

- workshop CLAUDE.md を本体テンプレから具体化（W1 用に対象著作・ID プレフィックス sw・対象範囲を書き込み）
- workshop commit_push.bat の `cd /d` パスを `C:\Users\user\buddhist-shoryoshu-workshop` に書換え
- 初期 motifs.json の schema 0.2 構造を整える（tag_axes・field_rules セクションは本体参照で省略可・stats は空集計で初期化）
- 初期 commit & push
- 立ち上げ完了の引き継ぎメモを作成

Phase 2a 完走後、Phase 3 W1（性霊集 第 13 ラウンド以降）で実際の motif 抽出を開始する。

## 副次発見・要注意事項

### workshop 方式移行合意の経緯と反映漏れの教訓

- **前々セッション（B10 5/7 最終）末尾**でケンシンと workshop 移行合意済（kaimyo-app と同じ並列パターン）。
- **前セッション（commit `3e261b3`）の引き継ぎメモ**にはこの合意が**反映されておらず**、Cowork 側で誤って第 12 ラウンド motif 抽出（idx=105・m272〜m281）を実施してしまった。
- 本セッションでケンシン確認の結果、**選択肢 (2) を採用**：commit `3e261b3` を本体最終地点として再定義し、抽出物（m272〜m281）を保全したまま Phase 1 に着手。
- **教訓**：合意事項は引き継ぎメモの本文（特に「次の作業」「最優先タスク」）に明記する。タイトル・進捗ヘッダだけでは新セッションが見落とす可能性がある。

### 本体での motif 抽出禁止の徹底（次セッション以降の Cowork 全般に適用）

commit `3e261b3` 以降、本体 `data/indices/motifs.json` への motif 追加は**禁止**。motif 抽出は W1/W2 workshop で行う。本体 CLAUDE.md の進捗ヘッダで「workshop 方式移行・motif 抽出停止」を明記し、将来の Cowork セッションが再び本体で motif 抽出を始めないようにする予防措置を講じた。

ただし以下は本体側の作業として継続：
- workshop 完走時のマージセッション（本体に motif を統合する作業）
- schema 更新（本体で先に決定 → 全 workshop に通達）
- 横断索引化（aggregate 等）
- 他著作の書き下し+現代語訳取込（御請来目録・十住心論 等）

### bash workspace 健在

本セッションで bash workspace は健在で、Read/Write/Edit/Grep/Glob と Python による検証も問題なく運用可能だった。ただし新規ファイルの commit / push は次のステップで commit_push.bat 経由で実施する（bash 経由 git 禁止）。

### git status 確認による検証

本セッション完走前に `git status` で以下を確認すること：
- `_dev_references/workshop_protocol.md`（新規）
- `_dev_references/workshop_CLAUDE_template.md`（新規）
- `_dev_references/workshop_commit_push_template.bat`（新規）
- `CLAUDE.md`（更新）
- `handoff_2026-05-08_phase1_workshop_protocol.md`（新規・本メモ）

合計 5 ファイルが staged / modified に出ることを確認してから commit_push.bat を実行する。

## 次セッション開始時の流れ

1. CLAUDE.md と本メモを読む
2. `git log --oneline -5` で HEAD を確認（本セッション完走 commit が頭）
3. ケンシンに **Phase 2a 着手で良いか** 確認
4. 上記「ケンシン側操作」が完了していたら、新 Cowork セッションを `C:\Users\user\buddhist-shoryoshu-workshop` で起動
5. workshop の CLAUDE.md・commit_push.bat 具体化 → 初期 motifs.json → 初期 push を実施

## 注意点（次セッション以降の遵守事項）

- **本体 motifs.json への motif 追加は禁止**（workshop 移行合意済）
- **本体 CLAUDE.md「現在の進捗」が「workshop 方式移行・motif 抽出停止」を明記**していることを確認
- **引き継ぎメモは ASCII 名で作成**（日本語名は git 認識不能リスク）
- **bash 経由 git は禁止・commit_push.bat 経由のみ**
- **半角括弧予防的全角徹底**（fix_parens 関数を Python 内に実装）
- **巻番号は shoryoshu_miyasaka.json を真値とする**

## 関連ファイル

- 本メモ：`handoff_2026-05-08_phase1_workshop_protocol.md`（ASCII 名）
- 前セッション：`handoff_2026-05-08_round12_idx105_complete.md`（本体最終地点記録・commit `3e261b3`）
- 第 11 ラウンド：`handoff_2026-05-07_round11_idx89_complete.md`（履歴用）
- 標準仕様書：`_dev_references/workshop_protocol.md`（本セッション作成・12 章構成）
- workshop CLAUDE.md テンプレ：`_dev_references/workshop_CLAUDE_template.md`（本セッション作成）
- workshop commit_push.bat テンプレ：`_dev_references/workshop_commit_push_template.bat`（本セッション作成）
- schema 仕様書：`_dev_references/motifs_index_design.md`（schema 0.2 真値・本セッション参照のみ）
- 本体 motifs.json：`data/indices/motifs.json`（287 motifs・以後 motif は本体に追加しない・読込のみ）

---

最終更新：2026-05-08（**Phase 1 完了：本体プロトコル整備・workshop 方式移行・本体での motif 抽出は commit `3e261b3` を最終地点に停止・workshop_protocol.md（12 章）/workshop_CLAUDE_template.md（7 章）/workshop_commit_push_template.bat 作成・本体 CLAUDE.md 4 箇所更新（進捗ヘッダ・次の作業・並行候補テーブル候補 M 追加・最終更新行）・次フェーズは Phase 2a：W1 性霊集 workshop 立ち上げ**）
