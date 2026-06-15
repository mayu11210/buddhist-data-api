# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）gabun 要否裁定 完了（意図的未設定 継続）

**日付**：2026-06-15
**種別**：gabun 要否裁定（文書 only・補注 GG/KK と同型の記録セッション）
**起点 HEAD**：`1e13c7d`（発菩提心論鈔 Phase1）の上。理趣釈 retrofit 35 は `7546ab1` で push 済。
**ステータス**：裁定完了・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/motifs_index_design.md（補注 MM 追記）・CLAUDE.md（★ エントリ prepend）・commit_message.txt・本メモ。**motifs.json は不変**。

---

## 裁定（ケンシン 2026-06-15）

理趣釈（伝・不空訳）全 51 motif（m2415-m2465）の gabun（雅文体訳・text_gendai_gabun）は **意図的未設定を継続**。

- 理趣釈は『理趣経』を逐句注釈する釈論。非空海（伝・不空訳）・非文藝（経典注釈）・経典引用（全件 引用形式:典籍曰く）の三軸がいずれも未設定側に一致（補注 KK 理趣経本文と同型）。
- ジャンル基準（補注 II）でも教学注釈系＝未設定側。
- kaimyo-app は gabun 不在時 kakikudashi フォールバック（§3 柔モード）のため利用側欠落なし。

## データ確認

- motifs.json 不変（total 2496・連動タグ 566・schema 0.2）。
- 全 51 motif は R1-R3 抽出時点で gabun 未設定（gabun 既設 0 件）。
- without_gabun_intentional の rishushaku 3 キー（m2415-m2433／m2434-m2452／m2453-m2465）記載済を温存。

## 文書

- 補注 MM 追記（motifs_index_design.md）。gabun 意図的未設定の系譜：瑜祇経 GG → 理趣経開題 II → 理趣経本文 KK → 理趣釈 MM。
- CLAUDE.md 先頭 running-log に ★ エントリ prepend。

## 残課題

**kaimyo-app への motifs.json 同期**（理趣釈 完走後残課題の最後）：倉庫 2496 → kaimyo-app・SHA-256 一致確認。retrofit 35 は連動タグのみ＝新引用形式タグなしのため kaimyo-app 側 冠生成ロジック（daishi-kotoba-picker 等）の変更は不要見込み。これが済めば理趣釈の完走後残課題（連動軸 retrofit → gabun 裁定 → 利用側同期）が一巡完了。

## 次セッション確認

1. CLAUDE.md 冒頭 → 本メモ → `git log --oneline -3`
2. motifs.json：total 2496・連動タグ 566・schema 0.2
