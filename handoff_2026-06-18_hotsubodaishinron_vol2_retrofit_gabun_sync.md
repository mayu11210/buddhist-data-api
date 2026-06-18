# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第二巻 完走後処理（連動軸 retrofit＋gabun 裁定＋kaimyo-app 同期）

**日付**：2026-06-18／**種別**：Phase3 完走後処理（retrofit＋gabun＋sync）＝**vol2 完結／発菩提心論鈔 全巻完結**
**起点 HEAD**：vol2 Phase3 motif 完走（`42f7d4b`）／**ステータス**：完成・検証 pass・**倉庫は未 commit / kaimyo-app は別 commit**

## (1) 連動軸 retrofit（中心成句スキャン・第一/三/四巻 retrofit 同型）
- **新規 sg/anchor なし＝既存アンカー軸の被覆拡張**。直接連動〔核心・術語 verbatim〕の 5 motif に限定・連動タグ +12（タグのみ変更・total 2738 不変・famous 31 不変）：
  - m2685（外道二乗の所簡・九種住心皆所簡・核心）→ sg17 十住心〔m599〕
  - m2687（宜修仏乗＝真言秘密仏乗・顕密対弁・核心）→ sg18 顕密二教〔m571〕
  - m2689（我今志求不求余果・心王心数・阿耨菩提＝三種菩提心〔勝義捨劣得勝〕・核心）→ sg22 三種菩提心〔m506+m581〕
  - m2697（常在人天受勝快楽の八義・惟真言法中即身成仏・核心）→ sg03 即身成仏〔m533〕
  - m2704（三種の譬の配釈の五義・名官＝勝義/財宝＝行願/善悪＝三摩地・核心）→ sg22 三種菩提心〔m506+m581〕
- 諸尊皆同大日〔m2702〕・十方諸仏証知〔m2696〕・人法不二〔m2699/m2700〕等はアンカー済みの中心成句に verbatim 直結しないため見送り（温存）。
- 巻き戻り assert（m506 典籍曰く／vol4 22件温存／vol2 motif text 不変）全 pass・recompute drift 0・NUL0・schema_history 200→201・補注 VV・origin: retrofit:hotsubodaishinron-sho-vol2_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol2_retrofit.json。

## (2) gabun 要否裁定
- vol2 全 30 motif（m2678-m2707）の text_gendai_gabun は **意図的未設定を継続**（宥快＝非空海・経典注釈系・全件 典籍曰く＝第一/三/四巻 同運用）。motifs.json は本裁定では不変。補注 WW。
- **発菩提心論鈔 第一〜第四巻 全巻の gabun 裁定が完了（全て意図的未設定）。**

## (3) kaimyo-app への motifs.json 同期【完了】
- 倉庫 data/indices/motifs.json（total 2738・retrofit 適用版）を kaimyo-app/data/indices/motifs.json へコピー。**SHA-256 一致・NUL0・total 2708→2738（+30）**を確認。vol2 30件・全件 典籍曰く・連動タグ反映 OK。
- CORPUS_DISPLAY_NAME に hotsubodaishinron 系は未登録だが、冠は解決順(3) source.著作名「発菩提心論鈔 第二巻」で正しく合成（「発菩提心論鈔 第二巻に曰く、」）＝第一/三/四巻と同じフォールバック・**コード変更不要**。
- kaimyo-app 側は `commit_motifs_sync.bat`＋`commit_message_motifs_sync.txt`（更新済み）で別途 commit。

## ★ 発菩提心論鈔 第二巻 完結／発菩提心論鈔 全巻完結
Phase1 取込（全111段 全訳＋ビルド＋登録）→ Phase2 横断索引化（20 著作目）→ Phase3 motif 抽出（30件・R1-R6）→
連動軸 retrofit（+12）→ gabun 裁定 → kaimyo-app 同期、まで全工程完了。残課題なし。
**発菩提心論鈔 第一〜第四巻が全巻、倉庫入り＋横断索引化＋motif 抽出＋retrofit＋gabun＋kaimyo-app 同期 まで完結。**

## 次セッション
- 別著作（例：大日経疏 巻第三 等）に進むときは同じ流れ（kakikudashi-data スキル Phase1-3）。

## 注意：phantom staged deletion（既知）
package.json 等は disk 実在の既知 stale index。commit_push.bat の index リセットで自動解消。
