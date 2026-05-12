# 引き継ぎメモ：retrofit 13 完走〔法華経 化城喩品 化城宝処連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 13（retrofit 12 完走に続く第十の retrofit セッション）
**対象**：法華経 化城喩品 化城宝処連動軸の新設。新規 sg-id `sg12`「化城宝処」を追加し、書き下し anchor として **二重体制を継承**：既存 `m227`（性霊集 第六巻 idx=45 願文・願文系 anchor）と既存 `m569`（弁顕密二教論 巻上 第一章 序説・顕密判教学系 anchor）の二つを並立 anchor として指定。連動軸が七系統 → 八系統並立に到達。法華経内部で「諸法実相（抽象的核心）」+「火宅三車（具体的譬喩 三乗教判）」+「良医病子（具体的譬喩 方便涅槃）」+「化城宝処（具体的譬喩 方便引導／顕密二教判）」の四段構成に到達。二重 anchor 体制の第三例（系統対比型の第二例：願文系 + 顕密判教学系・retrofit 11 sg10 と同パターン）。**顕密二教判の譬喩別軸として位置づく初例**（空海の顕密判教学の核心譬を初めて連動軸化）。**空間軸＋時間軸の同時カバー初例**（化城→宝処の空間軸 + 塵点劫・芥石劫・九年劫の時間軸を同時包摂）。
**ステータス**：完走〔Phase A 軸設計合意・Phase B 6 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 M 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 14 候補〔法華経譬喩別軸（見宝塔品 多宝塔 m222/m262/m424・idx=78 先師勤操 m424 多宝塔探索連携／信解品 長者窮子／五百弟子授記品 衣裏珠／薬草喩品 三草二木）／弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸八系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_13:doctrine〕
- [x] motifs_index_design.md に補注 M 追加済〔A-M 全 13 件 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 13 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-12_retrofit13_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 半角・全角括弧バランス確認〔追加部分 open=close・全角 611/611〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

retrofit 12 完走〔法華経 如来寿量品 良医病子連動・新規 sg11 + 既存 m44/m70 を書き下し anchor 二重体制で採用・commit `f65ceef`〕に続く第十の retrofit セッション。

retrofit 12 完走 handoff §(c) 選択肢 A〔retrofit 13 候補：法華経譬喩別軸〕に着手。2026-05-12 にケンシン裁定で「化城喩品 化城宝処軸」を選定し、判断 1-5 を 1 セッション内で連続裁定〔(1) 中心成句 = 化城宝処、(2) 二重 anchor m227+m569、(3) 規模 強連動 4 + anchor 2 = 6 motif、(4) 強連動 m486+m460+m688+m623、(5) 二重 anchor タグ運用 案 A 継承〕。Phase A〜D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg12`「化城宝処」を追加〔出典:法華経 化城喩品「仏曾以方便力 於険道中 過三百由旬 化作一城」「汝等才来、去宝処不遠」〕
- 書き下し anchor の **二重体制を継承**：m227（願文系 anchor）+ m569（顕密判教学系 anchor）
- 強連動 6 motif（anchor 2 + 強連動 4）に「連動:sg12」「連動:m227」「連動:m569」を付与（+18 タグ・案 A 採用＝全 motif に二重 anchor 明示）
- 法華経内部で抽象的核心（sg09 諸法実相）と具体的譬喩三段（sg10 火宅三車 三乗教判・sg11 良医病子 方便涅槃・sg12 化城宝処 方便引導／顕密二教判）の四段構成に到達
- 連動軸八系統並立に到達
- **顕密二教判の譬喩別軸として位置づく初例**：retrofit 1-12 までの連動軸は法華経内部の譬喩・経典内部の教学を中心としていたが、本 retrofit で空海の顕密判教学（顕教は化城、密教は宝処）の核心譬を初めて連動軸化
- **空間軸＋時間軸の同時カバー初例**：化城→宝処の空間軸 + 塵点劫・芥石劫・九年劫の時間軸を同時包摂

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg12 = 「化城宝処」（4字成句・retrofit 8 sg08「阿字本不生」・retrofit 10 sg09「諸法実相」・retrofit 11 sg10「火宅三車」・retrofit 12 sg11「良医病子」と同型）
- **判断 2**：書き下し anchor = m227（願文系）+ m569（顕密判教学系）の二重体制
- **判断 3**：規模 = 強連動 4 件 + anchor 2 件 = 6 motif（retrofit 11/12 より 2 件大）
- **判断 4**：強連動 4 件 = m486（性霊集 第八巻 idx=67 願文・塵点劫）+ m460（性霊集 第八巻 idx=83 表白・長劫）+ m688（大日経疏 §18-19 摩訶菩提薩埵釈・「化城」原語）+ m623（秘蔵宝鑰 巻の中 第五章 抜業因種心 第二節・菩提心論引用・「化城」原語）
- **判断 5**：二重 anchor タグ運用 = 案 A〔retrofit 11/12 補注 K/L 採用ルール継承・全 motif に二重 anchor 明示〕

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

**判定対象 motif 候補**：

法華経 化城関連 motif の分布把握：
- 「化城」原語 直接含有 motif: 5 件（m227, m569, m623, m688, m733・m733 は「化作浄戒」で別文脈）
- 「典故:法華経化城喩品」系タグ保持 motif: 3 件（m227, m460, m486）
- 「楊葉/嬰児/幼児/宝所/歇息」含有 motif: 4 件（m334, m569, m599, m717）

候補 motif の整理：
- m227：性霊集 第六巻 idx=45 願文・「化城に脂して而も烏兎喘ぐ」直接含有・既存タグ「典故:法華経化城喩品」「主題:化城脂烏兎喘」「場面:化城脂烏兎喘」三重保持・**最有力 anchor 候補（願文系）**
- m569：弁顕密二教論 巻上 第一章 序説・「化城に息むの賓、楊葉を愛するの児…医王手を拱き」化城+楊葉+医王の三譬複合・retrofit 12 で「将来の化城喩軸 retrofit との接続点として位置づけ」と温存指定・**最有力 anchor 候補（顕密判教学系）**
- m486：性霊集 第八巻 idx=67 願文・「塵墨憑仰・沙点津梁」・既存タグ「典故:法華経化城喩品塵点劫」保持・願文塵点劫系
- m460：性霊集 第八巻 idx=83 表白・「洪祚永永・芥石」・既存タグ「典故:法華経化城喩品」「典故:大智度論芥石劫」保持・表白長劫系
- m688：大日経疏 §18-19 摩訶菩提薩埵釈・「化城」原語含有・大日経疏教学系
- m623：秘蔵宝鑰 巻の中 第五章 抜業因種心 第二節・菩提心論引用文中「化城」原語含有・秘蔵宝鑰教学系
- m717：大日経疏 §58 自心実知・「功徳宝所」（宝所概念の核心）・将来の宝所軸 retrofit 候補・温存
- m334：性霊集 第十巻 詩・「乾闥婆城」・将来の乾闥婆城軸 retrofit 候補・温存
- m733：大日経疏 別文脈・「化作浄戒」・別文脈につき不採用

### Phase B：6 motif の判定表

| m-id | 出典 | kakikudashi 化城関連 keyword 直接含有 | 既存連動タグ | 既存関連タグ（主要） | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m227 | 性霊集 第六巻 idx=45 願文 | 「化城に脂して而も烏兎喘ぐ」（化城 1 直接含有） | なし | 典故:法華経化城喩品・主題:化城脂烏兎喘・場面:化城脂烏兎喘 | 願文系 | **anchor（願文系）** | **採用** |
| m569 | 弁顕密二教論 巻上 第一章 序説 | 「化城に息むの賓、楊葉を愛するの児…医王手を拱き」（化城/楊葉/医王 3 直接含有） | なし | 典故:法華経・典故:涅槃経・主題:顕密二教 | 教学系（顕密判） | **anchor（顕密判教学系）** | **採用** |
| m486 | 性霊集 第八巻 idx=67 願文 | （化城原語なし・「塵墨憑仰・沙点津梁」塵点劫概念） | なし | 典故:法華経化城喩品塵点劫 | 願文塵点劫系 | 強連動 | **採用** |
| m460 | 性霊集 第八巻 idx=83 表白 | （化城原語なし・「洪祚永永・芥石」長劫概念） | なし | 典故:法華経化城喩品・典故:大智度論芥石劫・典故:書経禹貢九年 | 表白長劫系 | 強連動 | **採用** |
| m688 | 大日経疏 §18-19 摩訶菩提薩埵釈 | 「化城」原語含有 | なし | 典故:大智度論・主題:菩提心・主題:十住心 | 教学系（大日経疏） | 強連動 | **採用** |
| m623 | 秘蔵宝鑰 巻の中 第五章 抜業因種心 第二節 | 「化城」原語含有（菩提心論引用文中） | なし | 典故:菩提心論・主題:住心・主題:声聞乗 | 教学系（秘蔵宝鑰） | 強連動 | **採用** |
| m717 | 大日経疏 §58 自心実知 | 「功徳宝所」（宝所概念） | なし | 典故:法華経・典故:大日経 | 宝所概念系 | 温存 | スコープ外 |
| m334 | 性霊集 第十巻 詩 乾闥婆城 | （化城原語なし・「乾闥婆城」類似譬） | なし | 典故:大品般若経・主題:虚実 | 詩系 | 温存 | スコープ外 |
| m733 | 大日経疏 別文脈 | 「化作浄戒」（化作） | — | — | 別文脈 | スコープ外 | 不採用 |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 755 | 756 | +1（sg12 新規追加） |
| ファイルサイズ | 2,604,832 bytes | 2,610,239 bytes | +5,407 |
| 連動タグを持つ motif | 41 | 47 | +6（m227/m569/m486/m460/m688/m623 新規連動） |
| famous_phrases | 11 | 12 | +1（sg12 追加で recompute） |
| schema_history 件数 | 70 | 71 | +1 |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 756 vs 756 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[], count=744 ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔6 motif + 各 3 タグ〕 | missing=[] ✓ |
| 7 | sg12 配列追加〔末尾 pos=755〕 | ✓ |

### Phase D：補注 M 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 M〔法華経 化城喩品 化城宝処連動の運用〕新規追加〔86,062→100,507 bytes・+14,445 bytes〕。anchor 構成表（二重 anchor 体制継続）・追加連動タグ値表・二重 anchor タグ運用ルール（案 A 継承・補注 K/L 参照）・retrofit 13 実施結果・設計上の論点 8 項目〔(i) 二重 anchor 体制の第三例（系統対比型の第二例）／(ii) 連動軸八系統並立に到達／(iii) 法華経内部の四段構成／(iv) 顕密二教判の譬喩別軸として位置づく初例／(v) kakikudashi 直接含有を客観基準とする継続＋タグ保持補助基準の例外運用／(vi) 空間軸＋時間軸の同時カバー／(vii) 譬喩別軸の今後の展開／(viii) schema_history origin タグの定着〕を明文化。補注 A-M 全 13 件 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 13 完走エントリを追加〔240,881→247,340 bytes・+6,459 bytes〕。retrofit 4-13 全エントリ intact 確認済。半角・全角括弧バランス維持〔〔=611, 〕=611〕。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 13 用に完全書き換え〔11,723 bytes・NUL 0・冒頭行整合確認済・全角括弧 26/26〕。冒頭行を「retrofit 13 完走：法華経 化城喩品 化城宝処連動 retrofit〔新規 sg12「化城宝処」+ 既存 m227/m569 を書き下し anchor 二重体制で採用・連動軸八系統並立に到達〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成。

### 設計上の新規ポイント

#### (i) 二重 anchor 体制の第三例（系統対比型の第二例）

retrofit 11 sg10/m209+m636 が初例（系統対比型：願文系 + 教学系）、retrofit 12 sg11/m44+m70 が第二例（文体対比型：碑文系 + 讃系）、本 retrofit 13 sg12/m227+m569 が第三例（系統対比型の第二例：願文系 + 顕密判教学系）。系統対比型と文体対比型の二パターンが運用基盤として確立。

**案 A 継承ルール**：すべての強連動 motif（anchor を含む 6 motif）に「連動:sg12」「連動:m227」「連動:m569」の 3 タグ全てを付与。kaimyo-app 検索で「連動:m227」「連動:m569」のいずれの anchor 検索でも 6 件全件取得可能。検索ロジック単純化が利点。補注 L §「二重 anchor タグ運用ルール（案 A 継承・補注 K 参照）」末尾の「将来の譬喩別軸でも踏襲」明文化を本 retrofit で実証。これにより二重 anchor 体制（案 A）は譬喩別軸の標準運用基盤として確立。

#### (ii) 連動軸八系統並立に到達

本 retrofit で連動軸は以下の八系統が並立：

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5 |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8 |
| 諸法実相 | sg09 | m637 | 連動:sg09・連動:m637 | retrofit 10 |
| 火宅三車 | sg10 | m209 + m636（二重・系統対比型） | 連動:sg10・連動:m209・連動:m636 | retrofit 11 |
| 良医病子 | sg11 | m44 + m70（二重・文体対比型） | 連動:sg11・連動:m44・連動:m70 | retrofit 12 |
| **化城宝処** | **sg12** | **m227 + m569（二重・系統対比型）** | **連動:sg12・連動:m227・連動:m569** | **retrofit 13（本 retrofit）** |

kaimyo-app は「即身成仏」「菩薩道の三句」「般若空観」「密教空観」「法華空観（諸法実相）」「法華譬喩（火宅三車・三乗教判）」「法華譬喩（良医病子・方便涅槃）」「法華譬喩（化城宝処・方便引導／顕密二教判）」の八つの教学テーマで素材プールを切替可能。

#### (iii) 法華経内部の四段構成

retrofit 10 sg09「諸法実相」（抽象的核心）・retrofit 11 sg10「火宅三車」（具体的譬喩 三乗教判）・retrofit 12 sg11「良医病子」（具体的譬喩 方便涅槃）・retrofit 13 sg12「化城宝処」（具体的譬喩 方便引導／顕密二教判）の四段構成に到達。法華経の最も抽象的・中心的な空観（諸法実相）と三大具体的譬喩（火宅三車・良医病子・化城宝処）が、別個の連動軸として明示的に弁別可能となる。今後の譬喩別軸展開（見宝塔品 多宝塔・五百弟子授記品 衣裏珠・信解品 長者窮子・薬草喩品 三草二木 等）への基盤がさらに整備。

#### (iv) 顕密二教判の譬喩別軸として位置づく初例

本 sg12「化城宝処」は anchor m569（弁顕密二教論 巻上 第一章 序説）を通じて、空海の顕密判教学（顕教は化城、密教は宝処）の核心譬を初めて連動軸化する。retrofit 1-12 までの連動軸は法華経内部の譬喩・経典内部の教学を中心としていたが、本 retrofit で空海の顕密二教判という独自の教判構造そのものを譬喩別軸として明示化。今後の弁顕密二教論軸・秘蔵宝鑰十住心軸の retrofit への基盤となる見通し。kaimyo-app は「顕教化城／密教宝処」という空海独自の教判構造を素材検索の基盤として活用可能。

#### (v) 5 系統カバー設計

6 motif の選定は以下の 5 系統を一括包摂する設計：

- 願文系：m227（性霊集 第六巻 idx=45 願文・anchor）
- 顕密判教学系：m569（弁顕密二教論 巻上 第一章 序説・anchor）
- 願文塵点劫系：m486（性霊集 第八巻 idx=67 願文）
- 表白長劫系：m460（性霊集 第八巻 idx=83 表白）
- 教学系（大日経疏 + 秘蔵宝鑰）：m688/m623

kaimyo-app の素材検索で、戒名・諷誦文・引導文・法話のジャンル別に対応可能な多様性を確保。retrofit 11/12 と異なり、本 retrofit は願文系と教学系の対称的二重化を維持しつつ、塵点劫概念（時間軸）と長劫概念（永世軸）を本格導入し、化城宝処譬の **空間軸（化城→宝処）+ 時間軸（塵点劫・長劫）** を同時にカバーする初の retrofit。

#### (vi) kakikudashi 直接含有を客観基準とする継続＋タグ保持補助基準の例外運用確立

本 retrofit でも強連動の客観基準として「kakikudashi 本文に化城関連 keyword（化城・化作・宝処・宝所・楊葉 等）直接含有」を採用：

- m227：化城（1 直接含有）+ 既存「典故:法華経化城喩品」「主題:化城脂烏兎喘」「場面:化城脂烏兎喘」三重タグ
- m569：化城/楊葉/医王（3 直接含有）+ 既存「典故:法華経」「主題:顕密二教」タグ
- m688：化城（1 直接含有）
- m623：化城（1 直接含有・菩提心論引用文中）

m486/m460 は化城原語なしだが既存「典故:法華経化城喩品（塵点劫）」タグ保持で化城喩品に直結する補助基準を採用。retrofit 10 補注 J §「kakikudashi 直接含有を客観基準とする選定」・retrofit 11 補注 K §「kakikudashi 直接含有を客観基準とする継続」・retrofit 12 補注 L §「kakikudashi 直接含有を客観基準とする継続」の方針を継続適用しつつ、タグ保持補助基準の例外運用を本 retrofit で確立。

#### (vii) 空間軸＋時間軸の同時カバー初例

本 retrofit は強連動 motif の選定で、空間軸（化城→宝処の方便引導）と時間軸（塵点劫・芥石劫・九年の長劫概念）を同時にカバーする初の retrofit。m486（塵点劫）と m460（芥石劫・九年劫）は化城喩品本体の「過三百由旬」「三千塵点劫」概念に対応する時間軸 motif として組み入れ。これにより化城宝処軸は単なる譬喩素材プールに留まらず、法華経 化城喩品全体の時空構造を明示化する軸として機能。

#### (viii) Phase D 必須チェックリストの完全運用化（retrofit 13 で 5 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10 が 2 回目、retrofit 11 が 3 回目、retrofit 12 が 4 回目、本 retrofit 13 で 5 回目の完全準拠 retrofit として位置づく。Phase D 必須チェックリストが定着した運用基盤として機能。特に commit_message.txt の冒頭行整合確認〔「retrofit 13 完走：法華経 化城喩品 化城宝処連動 retrofit〔新規 sg12「化城宝処」+ 既存 m227/m569 を書き下し anchor 二重体制で採用・連動軸八系統並立に到達〕」〕が、retrofit 7 §(d-9) の不整合（commit message が retrofit 6 のまま push された問題）を再発させない運用基盤として継続機能。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 14〔法華経譬喩別軸〕

連動軸の譬喩別細分化（本 retrofit の延長）：

- 見宝塔品 多宝塔（m222/m262/m424）を anchor 候補・idx=78 先師勤操 m424 多宝塔探索とも連携可能
- 信解品 長者窮子（m717 大日経疏 §58「人の宝蔵を開いて」自心実知）を anchor 候補・本 retrofit で温存
- 五百弟子授記品 衣裏珠（要候補調査）
- 薬草喩品 三草二木（要候補調査）
- 規模 4-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 14 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕

- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。本 retrofit で sg12 が顕密判の譬喩別軸として位置づいたため、本軸はその抽象的・体系的版に当たる
- 秘蔵宝鑰 十住心：「十住心」を anchor に、住心論系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸八系統 anchor 完全整合済〕

本 retrofit で連動軸八系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg12」を持つ 6 motif → 化城宝処連動素材プール（法華譬喩・方便引導／顕密二教判）
- 「連動:m227」「連動:m569」のいずれでも 6 motif 取得可能（案 A 二重 anchor 設計）
- 二重 anchor 体制と既存単一 anchor 体制の同型運用（kaimyo-app 検索ロジックは単一 anchor と同等）
- 法華経内部の四段構成検索：「諸法実相（抽象的）」 vs 「火宅三車（三乗教判）」 vs 「良医病子（方便涅槃）」 vs 「化城宝処（方便引導／顕密二教判）」の弁別
- 譬喩別軸の追加準備〔retrofit 14 以降の見宝塔品 多宝塔・長者窮子等への拡張〕
- **特に化城宝処軸は顕密二教判の譬喩別軸を初導入したため、kaimyo-app の密教教学解説（顕教は化城、密教は宝処）への直結が極めて強い**

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 二重 anchor 体制の第三例の確立（系統対比型の第二例）

retrofit 11 sg10/m209+m636 が初例（系統対比型：願文系 + 教学系）、retrofit 12 sg11/m44+m70 が第二例（文体対比型：碑文系 + 讃系）、本 retrofit sg12/m227+m569 が第三例（系統対比型の第二例：願文系 + 顕密判教学系）。系統対比型と文体対比型の二パターンが運用基盤として確立。今後の譬喩別軸展開で「弔辞 vs 教学」「願文 vs 詩」「碑 vs 讃」等の多様な二重化パターンが順次追加される見通し。

### (d-2) 顕密二教判の譬喩別軸として位置づく初例

retrofit 1-12 までの連動軸は法華経内部の譬喩・経典内部の教学を中心としていたが、本 retrofit で空海の顕密二教判という独自の教判構造そのものを譬喩別軸として明示化。今後の弁顕密二教論軸・秘蔵宝鑰十住心軸の retrofit への基盤となる見通し。

### (d-3) 空間軸＋時間軸の同時カバー初例

m486（塵点劫）と m460（芥石劫・九年劫）の時間軸 motif を含め、化城宝処軸は法華経 化城喩品全体の時空構造（空間軸：化城→宝処 + 時間軸：塵点劫・長劫）を明示化する軸として機能。

### (d-4) Write tool truncate 事象の予防対策（本 retrofit で 0 件発生）

本 retrofit では Python script を bash heredoc + write_bytes 方式で直接書き込みする運用を全面採用したため、Write tool truncate 事象は発生せず。retrofit 9-12 で複数回再発生した事象を継続予防。今後も Python script 作成時は Write tool ではなく bash heredoc + Python write_bytes 方式を優先することが推奨される。

### (d-5) CLAUDE.md 全角括弧バランス維持

CLAUDE.md は本 retrofit 前は 〔/〕 各 590 件で完全バランス、本 retrofit 後は 〔/〕 各 611 件で完全バランスに到達。半角括弧バランスも追加部分 open=close で確認済（TITLE_INSERT 6/6・FOOTER_INSERT 6/6）。

### (d-6) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9-12 で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を継続採用。最終検証で NUL 0 件確認。

### (d-7) retrofit 13 後の motifs.json サイズ

retrofit 13 で +5,407 bytes〔2,604,832 → 2,610,239 bytes〕。retrofit 12〔+4,529〕・retrofit 11〔+3,314〕・retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 10 連続で +1,000〜5,500 bytes 規模の retrofit。新規 sg12 motif の description が長め（化城宝処譬の完全な譬喩内容と空海著作中の運用を網羅・text_gendaigoyaku 675 字）かつ強連動 6 motif への +18 タグの累積で過去最大値を更新（retrofit 12 +12 タグ → retrofit 13 +18 タグ）。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-8) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg12 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg12 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg11 と同方針）。gendai_gabun_chars_total も 154,931 維持。kakikudashi_chars_total は +4 字（「化城宝処」4 字）、gendaigoyaku_chars_total は +675 字（sg12 description）増加。

### (d-9) git 状態の異常（retrofit 9-12 §(d-1) 同型・継続中の可能性）

セッション開始時に `git status --short` は確認していないが、retrofit 12 完走後の git 状態は比較的クリーンに保たれている見込み。commit_push.bat 実行時に bash mount 側と Windows 側の乖離が再発する可能性があるため、ケンシン実行時に確認推奨。

### (d-10) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 4 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-11) Phase D 必須チェックリストの retrofit 13 で完全運用化（5 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10 で 2 回目、retrofit 11 で 3 回目、retrofit 12 で 4 回目、本 retrofit 13 で 5 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 13 完走：法華経 化城喩品 化城宝処連動 retrofit〔新規 sg12「化城宝処」+ 既存 m227/m569 を書き下し anchor 二重体制で採用・連動軸八系統並立に到達〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔756 件・m1-m744 + sg01-sg12・2,610,239 bytes〕
- 本 retrofit build script：`outputs/retrofit13_kejo_hosho.py`〔dry-run + 本番適用の二段運用〕
- 補注 M 追加 script：`outputs/update_motifs_index_design_r13.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_r13.py`
- commit_message.txt 書き換え script：`outputs/write_commit_message_r13.py`
- 本 handoff 作成 script：`outputs/write_handoff_r13.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit13.json`〔retrofit 前 motifs.json・2,604,832 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit13.md`〔retrofit 前 motifs_index_design.md・86,062 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit13.md`〔retrofit 前 CLAUDE.md・240,881 bytes〕
- 前 retrofit handoff：`handoff_2026-05-12_retrofit12_complete.md`〔法華経 如来寿量品 良医病子連動〕
- 補注 M 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 13 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11/12/13 完走に到達。retrofit 13 完走〔法華経 化城喩品 化城宝処連動・新規 sg12 + 既存 m227/m569 を書き下し anchor 二重体制で採用・連動軸八系統並立に到達〕。本体 motifs.json は 756 件・2,610,239 bytes・schema_history 71 件。motifs_index_design.md §2 に補注 M 追加〔補注 A-M 全 13 件 intact・100,507 bytes〕。CLAUDE.md は 247,340 bytes〔retrofit 4-13 全エントリ intact〕。連動軸八系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の四段構成〔諸法実相（抽象的核心）+ 火宅三車（三乗教判）+ 良医病子（方便涅槃）+ 化城宝処（方便引導／顕密二教判）〕も成立。二重 anchor 体制の第三例（系統対比型の第二例：願文系 + 顕密判教学系）。顕密二教判の譬喩別軸として位置づく初例。空間軸＋時間軸の同時カバー初例。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit13_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit12_complete.md`〔retrofit 12 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-M 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・756 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 13 commit です。

【本セッションの選択肢】
(A) retrofit 14 候補〔法華経譬喩別軸：見宝塔品 多宝塔／信解品 長者窮子／五百弟子授記品 衣裏珠／薬草喩品 三草二木〕
(B) retrofit 14 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸八系統 anchor 完全整合済の素材プール活用〔特に sg12 化城宝処は顕密二教判の譬喩別軸として kaimyo-app の密教教学解説に最適〕
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 二重 anchor 体制の運用ルール（案 A）は将来の譬喩別軸でも踏襲（補注 K・L・M 参照）
- 本体 motifs.json は 2,610,239 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 13 完走・法華経 化城喩品 化城宝処連動 retrofit。新規 sg-id sg12「化城宝処」を追加〔出典:法華経 化城喩品「仏曾以方便力 於険道中 過三百由旬 化作一城」「汝等才来、去宝処不遠」〕、書き下し anchor として **二重体制を継承**：m227（性霊集 第六巻 idx=45 願文・「化城に脂して而も烏兎喘ぐ」・「化城」原語直接含有・願文系 anchor）+ m569（弁顕密二教論 巻上 第一章 序説・「化城に息むの賓、楊葉を愛するの児…医王手を拱き」・「化城」原語直接含有・化城+楊葉+医王の三譬複合・顕密判教学系 anchor）。強連動 6 motif〔m227(anchor 願文系)/m569(anchor 顕密判教学系)/m486(性霊集 第八巻 idx=67 願文 塵点劫)/m460(性霊集 第八巻 idx=83 表白 長劫)/m688(大日経疏 §18-19 摩訶菩提薩埵釈・「化城」原語)/m623(秘蔵宝鑰 巻の中 第五章 抜業因種心 第二節・菩提心論引用「化城」原語)〕に `連動:sg12`・`連動:m227`・`連動:m569` を付与（+18 タグ・案 A 採用＝全 motif に二重 anchor 明示）。total_motifs 755→756（+1 新規 sg12）・famous_phrases 11→12。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,610,239 bytes〔+5,407〕・schema_history 71 件〔+1・origin: retrofit_13:doctrine〕・補注 M 追加〔motifs_index_design.md §2・86,062→100,507 bytes・+14,445〕・CLAUDE.md 更新完了〔240,881→247,340 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸八系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569〕に到達——法華経内部で諸法実相（抽象的核心）+ 火宅三車（具体的譬喩 三乗教判）+ 良医病子（具体的譬喩 方便涅槃）+ 化城宝処（具体的譬喩 方便引導／顕密二教判）の四段構成に到達。二重 anchor 体制の第三例（系統対比型の第二例：願文系 + 顕密判教学系）として将来の譬喩別軸展開（見宝塔品 多宝塔等）への運用基盤をさらに整備。**顕密二教判の譬喩別軸として位置づく初例**〔m569 anchor を通じて空海の顕密判教学の核心譬を初めて連動軸化〕・**空間軸＋時間軸の同時カバー初例**〔化城→宝処の空間軸 + 塵点劫・芥石劫・九年劫の時間軸〕。Phase D 必須チェックリストに完全準拠する第五の retrofit〕
