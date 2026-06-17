# 引き継ぎメモ 2026-06-17 大日経疏 巻第二 完走後処理（連動軸 retrofit＋gabun 要否裁定）

**日付**：2026-06-17／**種別**：Phase3 完走後処理（retrofit＋gabun 裁定）
**起点 HEAD**：`c763848`（巻第二 motif R8 完走）／**ステータス**：完成・検証 pass・**未 commit / 未 push**

## (1) 連動軸 retrofit（中心成句スキャン）
- **新規 sg-id なし＝既存軸被覆拡張**（retrofit 7 型／hizoki retrofit 30 型）。巻第二は『大日経』住心品之余の注釈ゆえ既存中心成句軸と親子連動。
- **直接連動〔核心・術語 verbatim〕の 6 motif に限定**・連動タグ +27（タグのみ変更・total_motifs 2661 不変・famous_phrases 31 不変）：
  - m2546（k022 不生の生・阿字門入）→ sg08〔m549〕
  - m2622（k098 自心本不生・阿字門・心王池水本浄・浄菩提心一転）→ **三系統** sg08〔m549〕／sg21〔m638+m728〕／sg27〔m719〕
  - m2605（k081 浄菩提心＝出世間心・一生成仏）→ sg21〔m638+m728〕／sg03〔m533〕
  - m2624（k100 毘盧遮那具体法身・真言門乗超入）→ sg03〔m533〕
  - m2627（k103 因根究竟の三心・究竟一切智地・浄菩提心以上十住地）→ **三系統** sg07〔m713〕／sg26〔m698〕／sg21〔m638+m728〕
  - m2630（k106 前三句義・究竟一切智地）→ sg07〔m713〕／sg26〔m698〕
- 除外（直接連動未満ゆえ温存）：五蘊本不生の五喩 m2608-m2613・m2625（「蘊本不生」で阿字本不生 sg08 とは別義）・m2624 の阿字門（incidental）。
- 巻き戻り assert（m506 典籍曰く／対象 6 motif の元タグ温存／m2622・m2627 多系統連動）全 pass・recompute drift 0・NUL0・schema_history 183→184・補注 PP・origin: retrofit:dainichikyo-sho-vol2_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol2_rendou_retrofit.json。script：outputs/retrofit_vol2_rendou.py。

## (2) gabun 要否裁定
- 巻第二 全 105 motif（m2526-m2630）の text_gendai_gabun は **意図的未設定を継続**（ケンシン裁定）。
- 根拠：非空海（善無畏口述・一行筆受）・経典注釈系・全件 引用形式:典籍曰く＝hizoki/理趣経本文/理趣釈/発菩提心論鈔/大日経本文と同運用。将来 retrofit 可。
- motifs_without_gendai_gabun_intentional に dainichikyo-sho-vol2 の 8 ラウンド分キー記載済。motifs.json は本裁定では不変。補注 QQ。

## (3) 残課題：kaimyo-app への motifs.json 同期
- **kaimyo-app フォルダが本セッションに未接続のため未実施**。kaimyo-app 側 Cowork セッション、または本セッションに kaimyo-app フォルダを接続して実施する。
- 手順：倉庫 data/indices/motifs.json（total 2661）を kaimyo-app の data/indices/motifs.json へコピー → NUL0／total／引用形式タグ反映確認 → SHA-256 一致確認。
- **新しい引用形式タグの追加はない**（巻第二は全件 既存の 引用形式:典籍曰く）ため、kaimyo-app 側の冠生成ロジック（daishi-kotoba-picker 等）は既存「典籍曰く」運用でカバー＝コード変更不要見込み。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. motifs.json：total 2661・最終 m2630・連動タグ付与済 6 件・schema 0.2。
3. 残るは kaimyo-app 同期のみ（フォルダ接続要）。

## 注意：phantom staged deletion（既知）
package.json/render.yaml 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。
