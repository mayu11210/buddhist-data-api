# 引き継ぎメモ 2026-06-15 発菩提心論鈔 第一巻（宥快）motif 抽出 第4ラウンド（副題釈）完了

**日付**：2026-06-15
**種別**：kakikudashi-data Phase3 第4ラウンド（副題釈のみ・造者釈は R5 へ分割）
**起点 HEAD**：`e8b0f80`（発菩提心論鈔 motif R3・題号釈②）
**ステータス**：R4 完了・整合性検証＋巻き戻り assert＋verbatim 照合 全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・CLAUDE.md・commit_message.txt・本メモ。corpus・manifest・索引は不変。

## Phase A 合意（R1 と同・継続）
著者=宥快（非空海・確定）→引用形式:典籍曰く 全件・大師系タグ非付与。論義見出し・牒文は後続本文に束ね。gabun 未設定・連動軸は完走後 retrofit。人名・地名は motif タグ軸になし。

## ラウンド分割の変更
当初 R4=副題釈+造者釈（k122-k161・40段）だったが、品質確保のため副題釈/造者釈で分割（ケンシン承認）。
- **R4＝副題釈 k122-k135（本メモ・m2501-m2507）**
- R5＝造者釈 龍猛菩薩造 k136-k161（13対想定・m2508-）
- R6＝訳者釈 k162-k171＋結 k172

## 成果（R4・m2501-m2507・7件）
副題釈「瑜伽惣持教門説菩提心観行修持義」の字義釈。各 見出し/牒を本文に束ね7対。
- m2501 副題の所依（発心修行・瑜伽惣持教門・両部分別）
- m2502 惣持＝陀羅尼（字母釈・惣摂任持・無尽蔵）／ m2503 四種惣持（法義呪忍）／ m2504 五種惣持（蔵持＝第九阿摩頼識＝仏性浄識）
- m2505 四種五種惣持＝四智五智 ／ m2506 教門の釈（ア字門教門即実証・門の四義）
- m2507 説菩提心観行修持の釈（説＝開演・観行修持を三種菩提心〔行願/勝義/第三〕に配当）
核心0件（語釈区分・無理に名句化しない）。新タグ値なし。

## stats 差分
total_motifs 2531→2538（+7）・kk +2,734・gd +3,929・from_corpus_hotsubodaishinron-sho-vol1=42。
篇別内訳に hotsubodaishinron-sho-vol1_副題釈（…）追加・without_gabun に m2501-m2507 追加。schema_history +1（origin: hotsubodaishinron-sho-vol1_round4）。

## 検証（全 pass）
整合性10項目／巻き戻り assert（m506 典籍曰く・retrofit35 連動:sg31・R3 核心 温存）／verbatim 照合 kk・gd 全7件。
build script：outputs/build_hotsubodai_r4.py。バックアップ：outputs/motifs_backup_pre_hotsubodai_r4.json。

## 残ラウンド
- R5 造者釈 龍猛菩薩造 k136-k161（26段・龍猛/龍樹の得名・六時出現・寿限・諸宗高祖・地位・部数・菩薩・造・撰号。想定13対 m2508-m2520）
- R6 訳者釈 大広智不空奉詔訳 k162-k171＋結 一段畢 k172
完走後：連動軸 retrofit（顕密二教 sg18／三種菩提心 sg22 候補・m2495/m2496/m2467/m2507 等）・gabun 要否裁定・kaimyo-app 同期。

## 留意（git）
- commit のたび .git/index 破損（末尾ゼロ SHA）が断続再発。commit_push.bat 前に fix_index.bat を流すこと（履歴に無害・push は健全）。

## 次セッション確認
1. CLAUDE.md 冒頭 → 本メモ → git log --oneline -3
2. motifs.json：total 2538・最終 m-id m2507・from_corpus_hotsubodaishinron-sho-vol1=42
3. references/motif-extraction.md 必読
