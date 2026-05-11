# 引き継ぎメモ：retrofit 11 Phase A 途中（火宅三車軸）

**日付**：2026-05-11
**ステータス**：Phase A 設計合意の途中で中断（セッション切替）。**未 commit**。
**次セッションの最初の判断**：anchor 二重体制（m209/m636）と規模 4 件の組み合わせで、追加する強連動 motif を最終確定する一点だけ。

---

## 1. このセッションの結論（確定済）

ケンシン裁定で以下が確定済：

| 項目 | 確定値 |
|---|---|
| 連動軸 | 法華経 譬喩品 **火宅三車** 連動 |
| 新規 sg-id | **sg10** |
| 中心成句 | **「火宅三車」**（4字成句・retrofit 8 sg08「阿字本不生」、retrofit 10 sg09「諸法実相」と同型） |
| 書き下し anchor | **二重体制：m209（願文系 anchor）+ m636（教学系 anchor）** |
| 規模 | **4 件**（anchor を含めて計 4 件） |

m460 は当初候補だったが、Phase A 候補スキャンの結果、**化城喩品系で火宅 keywords 0 件**と判明したため、火宅三車軸 anchor からは除外。将来 retrofit 12 以降の化城喩品別軸候補へ温存。

---

## 2. 次セッションで最初に判断する一点

「anchor 2 件（m209/m636）に、追加する強連動 motif 2 件を何にするか」を確定すれば、Phase B 以降は機械的に進められます。候補は以下の 4 つ：

| m-id | 出典 | kakikudashi 中身（火宅 keyword） | 系統 |
|---|---|---|---|
| **m311** | 性霊集 第一巻 山に入る興 雑言 | 「三界火宅の裏に焼かるること莫れ」（**三界火宅** 直接含有） | 性霊集 詩系 |
| **m489** | 性霊集 第八巻 攘災願文 | 7 keywords 含有（火宅・三車・羊車・鹿車・白牛車・牛車・一仏乗） | 性霊集 願文系（追加） |
| **m615** | 秘蔵宝鑰 巻の中 第四住心 唯蘊無我心 | 「大覚世尊此の羊車を説いて」（**羊車** 教学） | 秘蔵宝鑰 教学系 |
| **m622** | 秘蔵宝鑰 巻の中 第五住心 抜業因種心 | 「縁覚の鹿車は、言説なし」（**鹿車** 教学） | 秘蔵宝鑰 教学系 |

推奨候補（claude 提案）：
- **m311 + m615**：性霊集 詩 + 秘蔵宝鑰 第四住心 の組み合わせで、anchor 2 件と合わせて願文・詩・教学第一段・教学第二段の 4 系統をカバー
- もしくは **m311 + m622**：詩 + 鹿車（縁覚）でやや教学を深める方向

次セッションで AskUserQuestion で確認 → 確定後 Phase B 着手の流れを想定。

---

## 3. このセッションで作成済のファイル（未 commit・新セッションで活用）

すべて outputs/ 配下。HEAD `9006ba1`（retrofit 10 commit）の後の未 commit ローカル変更：

| ファイル | サイズ | 用途 |
|---|---|---|
| `outputs/cleanup_git_state_pre_retrofit11.bat` | 2,709 bytes | ASCII bat・git 状態整理用・Phase D 直前に実行 |
| `outputs/cleanup_git_state_pre_retrofit11.py` | 6,577 bytes | UTF-8 helper・staged deletions/rename anomaly 解消 |
| `outputs/retrofit11_phaseA_scan.py` | 9,000+ bytes | Phase A 候補スキャン script・Linux/Windows 両対応 |
| `outputs/retrofit11_phaseA_candidates.txt` | 14,062 bytes | スキャン結果（判断材料） |

新セッションで `outputs/retrofit11_phaseA_candidates.txt` を読めば、火宅三車関連の全 24 motif の出典・既存タグ・kakikudashi 抜粋が即座に参照できる。

---

## 4. git 状態の異常（retrofit 9/10 §(d-1) 同型・継続中）

セッション開始時に `git status` で以下の異常が再発していた（未解消・新セッションでも同じ状態）：

- **誤ステージ済の削除**：package.json/render.yaml/start.bat/tsconfig.json/vercel.json/outputs/motifs_index_design_backup_pre_retrofit*.md/outputs/CLAUDE_md_backup_pre_retrofit9.md/outputs/CLAUDE_md_backup_pre_retrofit_workflow.md/引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md
- **異常 rename**：outputs/CLAUDE_md_backup_pre_retrofit8.md → outputs/CLAUDE_md_backup_pre_r（拡張子なしへの rename）

Phase D 直前にケンシン側で `outputs/cleanup_git_state_pre_retrofit11.bat` をダブルクリック実行して整理してから commit_push.bat へ進む方針。

---

## 5. 次セッションでの作業フロー

1. CLAUDE.md と本メモを読む
2. `git log --oneline -3` で HEAD が `9006ba1` であることを確認
3. `outputs/retrofit11_phaseA_candidates.txt` を読んで判断材料を取り戻す
4. ケンシンに **強連動 2 件の最終確定**を AskUserQuestion で確認（m311 + m615 / m311 + m622 / その他）
5. Phase B：motif 判定表作成（4 件分の kakikudashi 抜粋・既存タグ確認・採否確定）
6. Phase C：本体 motifs.json 反映
   - sg10「火宅三車」motif 新規追加（sg09 の直後に追加）
   - 4 件（anchor 2 + 強連動 2）に `連動:sg10`・`連動:m209` または `連動:m636` を付与
   - **二重 anchor のタグ運用は要設計**：以下の二案いずれかをケンシン裁定
     - **案 A**：すべての motif に `連動:sg10`・`連動:m209`・`連動:m636` を付与（二重 anchor を全 motif に明示）
     - **案 B**：願文系 motif には `連動:sg10`・`連動:m209`、教学系 motif には `連動:sg10`・`連動:m636` を付与（系統別に anchor を切替）
   - schema_history に origin: retrofit_11:doctrine エントリ追加
   - 整合性検証 7 項目全 pass 確認
7. Phase D：補注 K 追加 + CLAUDE.md 更新 + commit_message.txt 書き換え + 完走 handoff 作成
8. 最終検証 → cleanup_git_state_pre_retrofit11.bat 実行 → commit_push.bat

---

## 6. 二重 anchor 運用の設計上の論点（次セッションで合意必要）

retrofit 5-10 は単一 anchor（書き下し anchor 1 件）だったため、本 retrofit 11 で初めて **二重 anchor 体制**が採用される。これに伴う運用ルールは新規。

主な論点：

| 論点 | 案 A（全 motif に二重 anchor タグ） | 案 B（系統別 anchor 切替） |
|---|---|---|
| タグ数 | 各 motif +3 タグ（sg10/m209/m636） | 各 motif +2 タグ（sg10/m209 or sg10/m636） |
| kaimyo-app 検索 | 「連動:m209」「連動:m636」のどちらでも 4 件取得 | anchor 別に 2 件ずつ取得 |
| 設計の単純性 | より単純 | やや複雑 |
| 既存 retrofit との整合 | sg09/m637 等の単一 anchor 運用と異なる二重 anchor | より既存運用と類似 |

claude 推奨：**案 A**（全 motif に二重 anchor を明示）。kaimyo-app での検索ロジックが単純化される。

---

## 7. 補注 K の予定内容（Phase D で追加・先行整理）

`_dev_references/motifs_index_design.md` §2 に追加予定。

主な記述項目（retrofit 10 補注 J を踏襲）：

1. anchor 構成表（sg10・m209・m636 の役割と関係）
2. 二重 anchor 体制の新規運用ルール（案 A または案 B に基づく）
3. 対象 4 motif 一覧
4. 除外 motif の理由（m460 化城喩品系の温存・将来 retrofit 12 候補）
5. 設計上の論点（連動軸六系統並立への到達／法華経内部の譬喩別軸との関係／kakikudashi 直接含有を客観基準とする継続）
6. 譬喩別軸の今後の展開（化城喩・良医喩・多宝塔等）

---

## 8. 完走時の到達点（予定）

- **連動軸六系統並立**：即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、**火宅三車 sg10/m209+m636**
- 法華経内部の軸が **諸法実相（抽象的核心）** と **火宅三車（具体的譬喩）** の二段構成に
- 二重 anchor 体制の初例（retrofit 11 設計上の最大の論点）

---

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 11 Phase A 途中再開版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に retrofit 11 着手。Phase A 設計合意の途中（anchor 二重体制 m209/m636、中心成句「火宅三車」、規模 4 件まで確定）でセッション切替。HEAD は retrofit 10 commit 9006ba1 のまま。未 commit のローカル変更は outputs/ 配下の準備ファイル 4 件のみ。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit11_phaseA_inprogress.md`（本メモ・必読）
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit10_complete.md`（前 retrofit 完走サマリ）
3. `C:\Users\user\buddhist-data-api\outputs\retrofit11_phaseA_candidates.txt`（候補スキャン結果）
4. `C:\Users\user\buddhist-data-api\CLAUDE.md`（必要に応じて）

着手前に `git log --oneline -3` で HEAD `9006ba1` を確認してください。

【最初に判断する一点】
anchor 2 件（m209/m636）に、追加する強連動 motif 2 件を以下から選ぶ：
- m311（性霊集 詩・三界火宅）
- m489（性霊集 願文・7 keywords）
- m615（秘蔵宝鑰 第四住心 唯蘊無我心・羊車）
- m622（秘蔵宝鑰 第五住心 抜業因種心・鹿車）

推奨：m311 + m615（願文/詩/教学第一段/教学第二段の 4 系統カバー）

【もう一つの判断項目】
二重 anchor のタグ運用：
- 案 A：全 motif に `連動:sg10`・`連動:m209`・`連動:m636` を付与（推奨）
- 案 B：願文系は m209、教学系は m636 を付与（系統別切替）

進める前に、上記 2 点を確認してください。
```

---

最終更新：2026-05-11（retrofit 11 Phase A 途中・anchor 二重体制 m209/m636 + 中心成句「火宅三車」+ 規模 4 件まで確定。残り：強連動 2 件最終確定 → Phase B → C → D。outputs/ 配下に cleanup bat/py + Phase A スキャン script + candidates txt の 4 ファイル準備済・未 commit。HEAD `9006ba1` 維持）
