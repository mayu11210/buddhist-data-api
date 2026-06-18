# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第七巻 完走後処理（連動軸 retrofit＋gabun 裁定＋kaimyo-app 同期）

**日付**：2026-06-18／**種別**：Phase3 完走後処理（retrofit＋gabun＋sync）＝**vol7 完結／発菩提心論鈔 全巻完結**
**起点 HEAD**：vol7 Phase3 motif 完走（`7fa3ded`）／**ステータス**：完成・検証 pass・**倉庫は未 commit / kaimyo-app は別 commit**

## (1) 連動軸 retrofit（中心成句スキャン・第一〜六巻 retrofit 同型）
- **新規 sg/anchor なし＝既存アンカー軸の被覆拡張**。直接連動〔核心・術語 verbatim〕の 5 motif に限定・連動タグ +15（タグのみ変更・total 2807 不変・famous 31 不変）：
  - m2754（大乗の菩薩＝第六住心他縁大乗心・弥勒の大慈三昧・核心）→ sg17 十住心〔m599〕
  - m2770（行願三摩地を勝義の因に挙ぐ・三種の菩提心は不離）→ sg22 三種菩提心〔m506+m581〕
  - m2773（復修瑜伽＝三摩地に約して勝義・五相成身・三密・核心）→ sg22 三種菩提心〔m506+m581〕
  - m2774（従凡入仏位＝即身成仏の実義・毘盧遮那平等智身・父母所生身速証大覚位・核心）→ sg03 即身成仏〔m533〕
  - m2776（亦超十地菩薩境界・三種の菩提心は皆九種住心を超過・核心）→ **多系統** sg17 十住心〔m599〕・sg22 三種菩提心〔m506+m581〕
- 行願心 m2771（金剛薩埵・一切衆生本有薩埵が主・三種菩提心の framing 弱）／法門無辺誓願覚〔m2759〕／六度十波羅蜜の唯識論諸門〔m2762-m2766〕等はアンカー済みの中心成句に verbatim 直結しないため見送り（温存）。
- 巻き戻り assert（m506 典籍曰く／vol6 23件温存／vol7 motif text 不変）全 pass・recompute drift 0・NUL0・schema_history 218→219・補注 BBB・origin: retrofit:hotsubodaishinron-sho-vol7_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol7_retrofit.json。
- ※ retrofit 適用時、最初 verbatim チェックで「三種菩提心」literal を要求して fail したが、実表記は「三種の菩提心」（の入り）と判明。チェックを実表記に修正して再適用（連動内容は不変）。

## (2) gabun 要否裁定
- vol7 全 23 motif（m2754-m2776）の text_gendai_gabun は **意図的未設定を継続**（宥快＝非空海・経典注釈系・全件 典籍曰く＝第一〜六巻 同運用）。motifs.json は本裁定では不変。補注 CCC。
- **発菩提心論鈔 第一〜第七巻 全巻の gabun 裁定が完了（全て意図的未設定）。**

## (3) kaimyo-app への motifs.json 同期【完了】
- 倉庫 data/indices/motifs.json（total 2807・retrofit 適用版）を kaimyo-app へコピー。**SHA-256 一致・NUL0・total 2784→2807（+23）**を確認。vol7 23件・全件 典籍曰く・連動タグ反映 OK。
- 冠は解決順(3) source.著作名「発菩提心論鈔 第七巻」で正しく合成（「発菩提心論鈔 第七巻に曰く、」）＝第一〜第六巻と同じフォールバック・**コード変更不要**。
- kaimyo-app 側は `commit_motifs_sync.bat`＋`commit_message_motifs_sync.txt`（更新済み）で別途 commit。

## ★ 発菩提心論鈔 第七巻 完結／発菩提心論鈔 全巻完結
Phase1 取込（全97段 全訳＋ビルド＋登録）→ Phase2 横断索引化（23 著作目）→ Phase3 motif 抽出（23件・R1-R5）→
連動軸 retrofit（+15）→ gabun 裁定 → kaimyo-app 同期、まで全工程完了。残課題なし。
**発菩提心論鈔 第一〜第七巻（vol1 60／vol2 30／vol3 25／vol4 22／vol5 23／vol6 23／vol7 23・計 206 motif）が全巻、取込→横断索引化→motif 抽出→retrofit→gabun→kaimyo-app 同期 まで完結。**

## 次セッション
- 別著作（例：大日経疏 巻第三 等）に進むときは同じ流れ（kakikudashi-data スキル Phase1-3）。

## 注意：bash マウント stale（既知）／phantom staged deletion（既知）
bash マウント経由の grep/wc は古い版を表示することがある（virtiofs）。検証は Read/Edit と git を真値とする。package.json 等は disk 実在の既知 stale index。commit_push.bat の index リセットで自動解消。
