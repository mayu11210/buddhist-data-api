# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第五巻 完走後処理（連動軸 retrofit＋gabun 裁定＋kaimyo-app 同期）

**日付**：2026-06-18／**種別**：Phase3 完走後処理（retrofit＋gabun＋sync）＝**vol5 完結／発菩提心論鈔 全巻完結**
**起点 HEAD**：vol5 Phase3 motif 完走（`5b7f7b0`）／**ステータス**：完成・検証 pass・**倉庫は未 commit / kaimyo-app は別 commit**

## (1) 連動軸 retrofit（中心成句スキャン・第一/二/三/四巻 retrofit 同型）
- **新規 sg/anchor なし＝既存アンカー軸の被覆拡張**。直接連動〔核心・術語 verbatim〕の 4 motif に限定・連動タグ +12（タグのみ変更・total 2761 不変・famous 31 不変）：
  - m2708（勝義の菩提心の釈・行願に次いで勝義心・捨劣得勝）→ sg22 三種菩提心〔m506+m581〕
  - m2709（勝義の得名・般若の妙恵で九種住心を無自性と観じ捨劣得勝・核心）→ **多系統** sg22／sg17 十住心〔m599〕
  - m2711（相説旨陳の二段の十住心配当・核心）→ sg17 十住心〔m599〕
  - m2718（外道の行相・九種住心皆外道・核心）→ sg17 十住心〔m599〕
- 無自性結成〔m2728〕・生天を究竟と計す〔m2721〕・業力若尽未離三界の四義〔m2724〕・外道の原由〔m2730〕等はアンカー済みの中心成句に verbatim 直結しないため見送り（温存）。
- 巻き戻り assert（m506 典籍曰く／vol2 30件温存／vol5 motif text 不変）全 pass・recompute drift 0・NUL0・schema_history 206→207・補注 XX・origin: retrofit:hotsubodaishinron-sho-vol5_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol5_retrofit.json。

## (2) gabun 要否裁定
- vol5 全 23 motif（m2708-m2730）の text_gendai_gabun は **意図的未設定を継続**（宥快＝非空海・経典注釈系・全件 典籍曰く＝第一/二/三/四巻 同運用）。motifs.json は本裁定では不変。補注 YY。
- **発菩提心論鈔 第一〜第五巻 全巻の gabun 裁定が完了（全て意図的未設定）。**

## (3) kaimyo-app への motifs.json 同期【完了】
- 倉庫 data/indices/motifs.json（total 2761・retrofit 適用版）を kaimyo-app へコピー。**SHA-256 一致・NUL0・total 2738→2761（+23）**を確認。vol5 23件・全件 典籍曰く・連動タグ反映 OK。
- 冠は解決順(3) source.著作名「発菩提心論鈔 第五巻」で正しく合成（「発菩提心論鈔 第五巻に曰く、」）＝第一〜第四巻と同じフォールバック・**コード変更不要**。
- kaimyo-app 側は `commit_motifs_sync.bat`＋`commit_message_motifs_sync.txt`（更新済み）で別途 commit。

## ★ 発菩提心論鈔 第五巻 完結／発菩提心論鈔 全巻完結
Phase1 取込（全103段 全訳＋ビルド＋登録）→ Phase2 横断索引化（21 著作目）→ Phase3 motif 抽出（23件・R1-R5）→
連動軸 retrofit（+12）→ gabun 裁定 → kaimyo-app 同期、まで全工程完了。残課題なし。
**発菩提心論鈔 第一〜第五巻（vol1 60／vol2 30／vol3 25／vol4 22／vol5 23・計 160 motif）が全巻、取込→横断索引化→motif 抽出→retrofit→gabun→kaimyo-app 同期 まで完結。**

## 次セッション
- 別著作（例：大日経疏 巻第三 等）に進むときは同じ流れ（kakikudashi-data スキル Phase1-3）。

## 注意：phantom staged deletion（既知）
package.json 等は disk 実在の既知 stale index。commit_push.bat の index リセットで自動解消。
