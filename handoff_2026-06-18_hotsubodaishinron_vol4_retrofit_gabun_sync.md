# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第四巻 完走後処理（連動軸 retrofit＋gabun 裁定＋kaimyo-app 同期）

**日付**：2026-06-18／**種別**：Phase3 完走後処理（retrofit＋gabun＋sync）＝**vol4 完結**
**起点 HEAD**：vol4 Phase3 motif 完走（`7cf9b59`）／**ステータス**：完成・検証 pass・**倉庫は未 commit / kaimyo-app は別 commit**

## (1) 連動軸 retrofit（中心成句スキャン・第一巻/第三巻 retrofit 同型）
- **新規 sg/anchor なし＝既存アンカー軸の被覆拡張**。直接連動〔核心・術語 verbatim〕の 5 motif に限定・連動タグ +16（タグのみ変更・total 2708 不変・famous 31 不変）：
  - m2660（不応作・勝義の菩提心捨劣得勝・九種住心皆所遣・核心）→ sg22 三種菩提心〔m506+m581〕・sg17 十住心〔m599〕
  - m2662（如来蔵・六大四曼三密本有の三大を如来蔵性・核心）→ sg20 六大無礙〔m534〕
  - m2671（三智＝一切智/無師智/無碍智・両部不二配・核心）→ sg26 一切智智〔m698〕
  - m2676（能施の心の広大・即身成仏・五相三密の上に速疾兼行・核心）→ sg03 即身成仏〔m533〕
  - m2677（機根契当の十住心・勝義の菩提心の釈に依る・核心）→ **多系統** sg17 十住心〔m599〕・sg22 三種菩提心〔m506+m581〕
- **一切衆生悉有仏性〔sg04〕は見送り**：sg04 はアンカー未確立（連動:sg04 使用 0 件・sg 単独連動の前例なし）ゆえ「新規 sg/anchor なし」規律の範囲外。m2661（一切衆生悉有仏性の核心）・m2662 の如来蔵次元は将来 sg04 アンカー確立時に再検討（温存）。
- 巻き戻り assert（m506 典籍曰く／vol3 25件温存／vol4 motif text 不変）全 pass・recompute drift 0・NUL0・schema_history 193→194・補注 TT・origin: retrofit:hotsubodaishinron-sho-vol4_rendou_scan。
- バックアップ：outputs/motifs_backup_pre_vol4_retrofit.json。

## (2) gabun 要否裁定
- vol4 全 22 motif（m2656-m2677）の text_gendai_gabun は **意図的未設定を継続**（宥快＝非空海・経典注釈系・全件 典籍曰く＝第一巻/第三巻/hizoki/理趣釈/大日経疏 巻第二と同運用）。motifs.json は本裁定では不変。補注 UU。

## (3) kaimyo-app への motifs.json 同期【完了】
- 倉庫 data/indices/motifs.json（total 2708・retrofit 適用版）を kaimyo-app/data/indices/motifs.json へコピー。**SHA-256 一致・NUL0・total 2686→2708（+22）**を確認。vol4 22件・全件 典籍曰く・連動タグ反映 OK。
- CORPUS_DISPLAY_NAME に hotsubodaishinron 系は未登録だが、冠は解決順(3) source.著作名「発菩提心論鈔 第四巻」で正しく合成（「発菩提心論鈔 第四巻に曰く、」）＝第一巻/第三巻と同じフォールバック・**コード変更不要**。
- kaimyo-app 側は `commit_motifs_sync.bat`（motifs.json のみ stage）＋`commit_message_motifs_sync.txt`（更新済み）で別途 commit。

## ★ 発菩提心論鈔 第四巻 完結
Phase1 取込（全79段 全訳＋ビルド＋登録）→ Phase2 横断索引化（19 著作目）→ Phase3 motif 抽出（22件・R1-R4）→
連動軸 retrofit（+16）→ gabun 裁定 → kaimyo-app 同期、まで全工程完了。残課題なし。

## 次セッション
- 別著作（例：発菩提心論鈔 第二巻・第五巻 等／大日経疏 巻第三 等）に進むときは同じ流れ（kakikudashi-data スキル Phase1-3）。

## 注意：phantom staged deletion（既知）
package.json 等は disk 実在の既知 stale index。commit_push.bat の index リセットで自動解消。
