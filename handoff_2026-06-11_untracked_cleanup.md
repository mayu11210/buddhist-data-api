# handoff 2026-06-11（後続）未追跡素材の処遇裁定

**日付**：2026-06-11（retrofit 31 の後続セッション）
**ステータス**：裁定済・cleanup_untracked_0611.bat 実行済（移動完了をホスト側で検証済）
**変更なし**：motifs.json・corpus・索引は一切触っていない（検証のみ）

## 開始時検証（全 pass）

- 倉庫 `git log --oneline -1` = `5093e88`（retrofit 31）
- motifs.json：total_motifs=2391（ホスト側 Grep）・m506 `引用形式:典籍曰く`（巻き戻りなし）
- kaimyo-app：`3cc51a1`・total_motifs=2391・m506 典籍曰く

## ケンシン裁定（2026-06-11）

1. **遍照発揮性霊集.docx** → **リポジトリ外へ退避**
   - 根拠：shoryoshu_miyasaka.json（primary_corpus・全 112 篇）と重複、
     巻六途中切れの不完全素材、CLAUDE.md 上も本来「リポジトリ外」参照、
     Kindle 本コピペのため commit は著作権上不適
   - 実施：`C:\Users\user\shoryoshu_seireishu_kindle.docx` へ move
     （bat の ASCII 制約によるリネーム。必要なら手動で旧名に戻してよい）
2. **dainichikyo_genten.txt** → **outputs/ へ移動**
   - 用途判明：CBETA T0848 大日経・全 7 巻（@@@JUANn|字数@@@ 区切り・計約 88,466 字）の
     **genten 取込用中間ファイル**。取込は 2026-06-10 完了済
     （dainichikyo.json に genten 64,901 字＋genten_source 記録あり）。再取得可

## 実施手段

- `cleanup_untracked_0611.bat`（ASCII・git 操作なし・上書き禁止ガード付き）
- 実行後確認：ルートに *.docx と dainichikyo_genten.txt が無いこと、
  `git status` のルート untracked が `_dev_scripts/`・本メモ・bat 類のみになること

## kaimyo-app 側（同セッション）

- 引き継ぎメモ 2026-06-11 を `commit_push_memo_0611.bat` で commit（`d39170e`・D 完了）
- **縦割り経路（fusonmon-vertical）の典籍曰く対応を実装・commit**（`210e091`・B 完了）：
  橋候補に origin='motif_tenseki'（菩提心論 m516/m519/m520 の 3 件）・冠
  「龍猛菩薩、菩提心論に曰く、」合成・typecheck OK。詳細は kaimyo-app
  引き継ぎメモ_2026-06-11_縦割り典籍曰く対応.md

## (C) gabun 要否のケンシン裁定（2026-06-11・本セッションで確定）

- **秘蔵記 90 件・十住心論 100 件の text_gendai_gabun は「意図的未設定」を正式継続**
- 根拠：未設定時は kaimyo-app 側が書き下しにフォールバックするため実害なし。
  秘蔵記の核心句は全件 80 字超で橋プールにも入らない
- motifs_without_gendai_gabun_intentional（retrofit 31 で被覆 218/218 完備）の
  運用をそのまま恒久化。将来必要になったら gabun retrofit として再開可
- これをもって温存継続案件 (C) はクローズ

## 残課題（継続）
- kaimyo-app の commit_push 系 .bat 多数の M 表示（CRLF 差分とみられる・未裁定）
- `_dev_scripts/`・outputs/ 配下の retrofit 系作業ファイル整理（別タスクのまま）
- kaimyo-app 実機検証：縦割り生成で観測ログ `motif_tenseki=3` と
  冠「龍猛菩薩、菩提心論に曰く、」＋終止「と。」の出力確認
- ※「典籍曰く」冠生成ロジックは横割り 6/10（efbebe3）・縦割り本日（210e091）で
  実装完了済（CLAUDE.md retrofit 29 記載の残課題は解消）

## 注意

- 本メモのみ commit_push_memo_0611_souko.bat で commit。one-shot bat 類と
  commit_message_memo_0611.txt は .gitignore の方針（作業用ツールは untracked 運用）
  に従い commit しない
- CLAUDE.md の git status M 表示は phantom 差分（ホスト実体は HEAD 一致）の継続前提
