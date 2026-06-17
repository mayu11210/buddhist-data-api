# 引き継ぎメモ 2026-06-17 発菩提心論鈔 第三巻 完走後処理（連動軸 retrofit＋gabun 裁定＋kaimyo-app 同期）

**日付**：2026-06-17／**種別**：Phase3 完走後処理（retrofit＋gabun＋sync）＝**vol3 完結**
**起点 HEAD**：vol3 Phase3 motif 完走（`bd1534d`）／**ステータス**：完成・検証 pass・**倉庫は未 commit / kaimyo-app は別 commit**

## (1) 連動軸 retrofit（中心成句スキャン・第一巻 retrofit 36 同型）
- **新規 sg-id なし＝既存軸被覆拡張**。vol3 は『菩提心論』の注釈ゆえ既存中心成句軸と親子連動。**直接連動〔核心・術語 verbatim〕の 7 motif に限定**・連動タグ +21（タグのみ変更・total 2686 不変・famous 31 不変）：
  - m2632（四種の心・万行の根源・核心）→ sg22 三種菩提心〔m506+m581〕
  - m2639（勝義行願三摩地為戒・父母所生身速証無上覚）→ sg22／sg03 即身成仏〔m533〕
  - m2644（三門の名字・大定智悲・核心）→ sg22
  - m2641（即身成仏は真言法のみ・顕密分斉・父母所生・核心）→ **多系統** sg18 顕密二教〔m571〕／sg03
  - m2642（於諸教中＝顕教・他受用）→ sg18
  - m2647（三句配釈：菩提心因・大悲根・方便究竟）→ sg07 三句法門〔m713〕
  - m2640（乃至成仏無時暫忘・三句配釈・方便究竟）→ sg07
- 巻き戻り assert（m506 典籍曰く／対象 7 motif の元タグ温存／vol3 25件温存）全 pass・recompute drift 0・NUL0・schema_history 188→189・補注 RR・origin: retrofit:hotsubodaishinron-sho-vol3_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol3_rendou_retrofit.json。script：outputs/retrofit_vol3_rendou.py。

## (2) gabun 要否裁定
- vol3 全 25 motif（m2631-m2655）の text_gendai_gabun は **意図的未設定を継続**（宥快＝非空海・経典注釈系・全件 典籍曰く＝第一巻/hizoki/理趣釈/大日経疏 巻第二と同運用）。motifs.json は本裁定では不変。補注 SS。

## (3) kaimyo-app への motifs.json 同期【完了】
- 倉庫 data/indices/motifs.json（total 2686・retrofit 適用版）を kaimyo-app/data/indices/motifs.json へコピー。**SHA-256 一致・NUL0・total 2661→2686（+25）**を確認。vol3 25件・全件 典籍曰く・連動タグ反映 OK。
- CORPUS_DISPLAY_NAME に hotsubodaishinron 系は未登録だが、冠は解決順(3) source.著作名「発菩提心論鈔 第三巻」で正しく合成（「発菩提心論鈔 第三巻に曰く、」）＝第一巻と同じフォールバック・**コード変更不要**。
- kaimyo-app 側は `commit_motifs_sync.bat`（motifs.json のみ stage）＋`commit_message_motifs_sync.txt`（更新済み）で別途 commit。

## ★ 発菩提心論鈔 第三巻 完結
Phase1 取込（全70段 全訳＋ビルド＋登録）→ Phase2 横断索引化（18 著作目）→ Phase3 motif 抽出（25件・R1-R4）→
連動軸 retrofit（+21）→ gabun 裁定 → kaimyo-app 同期、まで全工程完了。残課題なし。

## 次セッション
- 別著作（例：発菩提心論鈔 第二巻 等）に進むときは同じ流れ（kakikudashi-data スキル Phase1-3）。

## 注意：phantom staged deletion（既知）
package.json 等は disk 実在の既知 stale index。commit_push.bat の index リセットで自動解消。
