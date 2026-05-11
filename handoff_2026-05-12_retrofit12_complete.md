# 引き継ぎメモ：retrofit 12 完走〔法華経 如来寿量品 良医病子連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 12（retrofit 11 完走に続く第九の retrofit セッション）
**対象**：法華経 如来寿量品 良医病子連動軸の新設。新規 sg-id `sg11`「良医病子」を追加し、書き下し anchor として **二重体制を継承**：既存 `m44`（性霊集 第二巻 恵果和尚の碑・弔辞・追悼 碑文系 anchor）と既存 `m70`（性霊集 第十巻 故僧正勤操影讃・弔辞・追悼 讃系 anchor）の二つを並立 anchor として指定。連動軸が六系統 → 七系統並立に到達。法華経内部で「諸法実相（抽象的核心）」+「火宅三車（具体的譬喩 三乗教判）」+「良医病子（具体的譬喩 方便涅槃）」の三段構成に到達。二重 anchor 体制の第二例（retrofit 11 sg10 に続く・補注 K 案 A 運用ルール継承）。
**ステータス**：完走〔Phase A 軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 L 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 13 候補〔法華経譬喩別軸（化城喩品 化城／見宝塔品 多宝塔）／華厳経 一即一切／弁顕密二教論 顕密判 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸七系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_12:doctrine〕
- [x] motifs_index_design.md に補注 L 追加済〔A-L 全 12 件 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 12 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-12_retrofit12_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 半角括弧バランス確認〔追加部分 open=close〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

retrofit 11 完走〔法華経 譬喩品 火宅三車連動・新規 sg10 + 既存 m209/m636 を書き下し anchor 二重体制で採用・commit `fc285e6`〕に続く第九の retrofit セッション。

retrofit 11 完走 handoff §(c) 選択肢 A〔retrofit 12 候補：法華経譬喩別軸〕に着手。2026-05-12 にケンシン裁定で「寿量品 良医病子軸」を選定し、判断 1-5 を 1 セッション内で連続裁定〔(1) 中心成句 = 良医病子、(2) 二重 anchor m44+m70、(3) 規模 4 件、(4) 強連動 m455+m494、(5) 二重 anchor タグ運用 案 A 継承〕。Phase A〜D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg11`「良医病子」を追加〔出典:法華経 如来寿量品「諸子幼稚、無有知者、雖見其父、不識薬色、飲服不肯」〕
- 書き下し anchor の **二重体制を継承**：m44（弔辞・追悼 碑文系 anchor）+ m70（弔辞・追悼 讃系 anchor）
- 強連動 4 motif に「連動:sg11」「連動:m44」「連動:m70」を付与（+12 タグ・案 A 採用＝全 motif に二重 anchor 明示）
- 法華経内部で抽象的核心（sg09 諸法実相）と具体的譬喩二段（sg10 火宅三車 三乗教判・sg11 良医病子 方便涅槃）の三段構成に到達
- 連動軸七系統並立に到達
- **弔辞・追悼系 motif の anchor 化の初例**：retrofit 11 までの anchor は性霊集 願文系・秘蔵宝鑰 教学系・性霊集 詩系が中心で、弔辞・追悼系（カテゴリ:悲嘆・故人タグ保持）が anchor 化されるのは本 retrofit が初

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg11 = 「良医病子」（簡潔な 4 字成句・retrofit 8 sg08「阿字本不生」・retrofit 10 sg09「諸法実相」・retrofit 11 sg10「火宅三車」と同型）
- **判断 2**：書き下し anchor = m44（弔辞・追悼 碑文系）+ m70（弔辞・追悼 讃系）の二重体制
- **判断 3**：規模 = 強連動 4 件（retrofit 11 同規模）
- **判断 4**：強連動 2 件の選定 = m455（性霊集 第八巻 idx=83 表白・願文表白系）+ m494（般若心経秘鍵 第二節・教学般若系）
- **判断 5**：二重 anchor タグ運用 = 案 A〔retrofit 11 補注 K 採用ルール継承・全 motif に二重 anchor 明示〕

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

**判定対象 motif 候補**：

法華経 良医病子関連 motif の分布把握：
- 典故:法華経 タグ保有 26 件
- 寿量品系タグ保有 motif: 2 件（m455, m70）
- primary keyword「良医/病子/狂子/狂児」直接含有 motif: 4 件（m44, m70, m331, m391）
- secondary keyword「医王」直接含有 motif: 9 件（m44, m70, m494, m502, m513, m569, m611, m619, m676）
- tangential keyword「解毒/毒気/好色/失心」直接含有 motif: 3 件（m474, m495, m728）

候補 motif の整理：
- m44：性霊集 第二巻 恵果和尚の碑・「医王迹を匿す。狂児誰に憑りてか毒を解かん」直接含有・既存タグ「典故:法華経:良医病子」保持・弔辞・追悼 碑文系 anchor 候補
- m70：性霊集 第十巻 勤操影讃・「医王・狂子・酔児」直接含有・既存タグ「典故:法華経:如来寿量品」「典故:法華経:五百弟子授記品」保持・弔辞・追悼 讃系 anchor 候補
- m455：性霊集 第八巻 idx=83 表白・「吾が子、多病にして医薬遑あらず」・既存タグ「典故:法華経:良医薬子」保持・願文表白系
- m494：般若心経秘鍵 第二節・「医王の薬」直接含有・教学般若系
- m495：般若心経秘鍵 第三節・「解毒・慈父導子の方」直接含有・教学般若系第二段
- m569：弁顕密二教論 巻上 第一章・「化城+楊葉+医王」化城+良医複合譬
- m611：秘蔵宝鑰 巻の上 第三章 嬰童無畏心・「狂毒自から解けず、医王能く治す」
- m619：秘蔵宝鑰 巻の中 第四章 唯蘊無我心 十四問答・「仏は医王の如く」
- m502/m513/m676/m331：周辺候補

本セッション開始時の判断（AskUserQuestion でケンシン確定）：

- 強連動 2 件 = m455 + m494（案 X 推奨採用・願文表白 + 教学般若の二系統カバー）
- 二重 anchor タグ運用 = 案 A（全 motif に「連動:sg11」「連動:m44」「連動:m70」3 タグ全付与・retrofit 11 補注 K 採用ルール継承）

### Phase B：4 motif の判定表

| m-id | 出典 | 既存連動タグ | 既存関連タグ（主要） | kakikudashi 良医病子 keyword 直接含有 | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m44 | 性霊集 第二巻 恵果和尚の碑 | なし | category:悲嘆・故人:師・故人:大徳・典故:法華経:良医病子 | 「医王迹を匿す。狂児誰に憑りてか毒を解かん」（医王・狂児・解毒 3 keyword 直接含有） | 弔辞・追悼系（碑文） | **anchor（碑文系）** | **採用** |
| m70 | 性霊集 第十巻 勤操影讃 | なし | category:悲嘆・故人:僧侶・主題:無常・典故:法華経:如来寿量品・典故:法華経:五百弟子授記品 | 「如知の医王は、狂子に因りて而も影を滅し、大士の弘誓は、酔児に逐て以て迹を顕わす」（医王・狂子・酔児 3 keyword 直接含有） | 弔辞・追悼系（讃） | **anchor（讃系）** | **採用** |
| m455 | 性霊集 第八巻 idx=83 表白 | なし | 主題:慈愛・主題:衆生救済・主題:無常・典故:法華経:如来寿量品・典故:法華経:良医薬子 | 「吾が子、多病にして医薬遑あらず」（多病・医薬 直接含有・良医薬子既タグ） | 願文系（表白） | 強連動 | **採用** |
| m494 | 般若心経秘鍵 第二節 | なし | 主題:無明・主題:衆生迷情 | 「曾つて医王の薬を訪らわずんば、何れの時にか大日の光を見ん」（医王・薬・狂酔の人 直接含有） | 教学系（般若心経秘鍵 第二段） | 強連動 | **採用** |
| m495 | 般若心経秘鍵 第三節 | なし | — | 解毒・慈父導子の方（直接含有） | 教学系第三段 | 温存 | スコープ外 |
| m569 | 弁顕密二教論 巻上 第一章 | なし | — | 化城+楊葉+医王（複合譬・化城軸候補） | 教学系（弁顕密） | 温存（化城軸候補） | スコープ外 |
| m611 | 秘蔵宝鑰 第三住心 嬰童無畏心 | なし | — | 狂毒・医王（直接含有） | 教学第三住心 | 温存 | スコープ外 |
| m619 | 秘蔵宝鑰 第四住心 十四問答 | なし | — | 仏は医王の如く・教えは方経の如く | 教学第四住心 | 温存 | スコープ外 |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 754 | 755 | +1（sg11 新規追加） |
| ファイルサイズ | 2,600,303 bytes | 2,604,832 bytes | +4,529 |
| 連動タグを持つ motif | 37 | 41 | +4（m44/m70/m455/m494 新規連動） |
| famous_phrases | 10 | 11 | +1（sg11 追加で recompute） |
| schema_history 件数 | 69 | 70 | +1 |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 755 vs 755 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔m44/m70/m455/m494 + 各 3 タグ〕 | missing=[] ✓ |
| 7 | sg11 配列追加〔sg10 直後〕 | ✓ |

### Phase D：補注 L 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 L〔法華経 如来寿量品 良医病子連動の運用〕新規追加〔74,761→86,062 bytes・+11,301 bytes〕。anchor 構成表（二重 anchor 体制継続）・追加連動タグ値表・二重 anchor タグ運用ルール（案 A 継承・補注 K 参照）・retrofit 12 実施結果・設計上の論点 7 項目〔(i) 二重 anchor 体制の第二例／(ii) 連動軸七系統並立に到達／(iii) 法華経内部の三段構成／(iv) 弔辞・追悼系 motif の anchor 化の初例／(v) kakikudashi 直接含有を客観基準とする継続／(vi) 譬喩別軸の今後の展開／(vii) schema_history origin タグの定着〕を明文化。補注 A-L 全 12 件 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 12 完走エントリを追加〔235,797→240,881 bytes・+5,084 bytes〕。retrofit 4-12 全エントリ intact 確認済。半角括弧バランス維持。NUL バイト 0 件確認。全角括弧 〔=〕=590 完全バランス到達。
- `commit_message.txt` を retrofit 12 用に完全書き換え〔8,963 bytes・NUL 0・冒頭行整合確認済〕。冒頭行を「retrofit 12 完走：法華経 如来寿量品 良医病子連動 retrofit〔新規 sg11「良医病子」+ 既存 m44/m70 を書き下し anchor 二重体制で採用・連動軸七系統並立に到達〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成。

### 設計上の新規ポイント

#### (i) 二重 anchor 体制の第二例

retrofit 11 sg10/m209+m636 が初例で、本 retrofit が第二例。retrofit 11 は「願文系（性霊集 法事願文）+ 教学系（秘蔵宝鑰 教判論）」の系統対比型二重化だったのに対し、本 retrofit は「碑文系（恵果和尚の碑）+ 讃系（勤操影讃）」の文体対比型二重化。良医病子譬の典籍系統は両者ともに性霊集 弔辞・追悼系（カテゴリ:悲嘆）に属しながら、文体（碑文 vs 讃）と位置づけが分化しているため、いずれか一方では包摂できない判断から二重化を採用。

**案 A 継承ルール**：すべての強連動 motif に「連動:sg11」「連動:m44」「連動:m70」の 3 タグ全てを付与。kaimyo-app 検索で「連動:m44」「連動:m70」のいずれの anchor 検索でも 4 件全件取得可能。検索ロジック単純化が利点。補注 K §「二重 anchor タグ運用ルール（案 A 採用）」末尾の「将来の譬喩別軸でも踏襲」明文化を本 retrofit で実証。

#### (ii) 連動軸七系統並立に到達

本 retrofit で連動軸は以下の七系統が並立：

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5 |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8 |
| 諸法実相 | sg09 | m637 | 連動:sg09・連動:m637 | retrofit 10 |
| 火宅三車 | sg10 | m209 + m636（二重・系統対比型） | 連動:sg10・連動:m209・連動:m636 | retrofit 11 |
| **良医病子** | **sg11** | **m44 + m70（二重・文体対比型）** | **連動:sg11・連動:m44・連動:m70** | **retrofit 12（本 retrofit）** |

kaimyo-app は「即身成仏」「菩薩道の三句」「般若空観」「密教空観」「法華空観（諸法実相）」「法華譬喩（火宅三車・三乗教判）」「法華譬喩（良医病子・方便涅槃）」の七つの教学テーマで素材プールを切替可能。

#### (iii) 法華経内部の三段構成

retrofit 10 sg09「諸法実相」（抽象的核心）・retrofit 11 sg10「火宅三車」（具体的譬喩 三乗教判）・retrofit 12 sg11「良医病子」（具体的譬喩 方便涅槃）の三段構成に到達。法華経の最も抽象的・中心的な空観と二大具体的譬喩（火宅三車・良医病子）が、別個の連動軸として明示的に弁別可能となる。今後の譬喩別軸展開（化城喩・多宝塔等）への基盤がさらに整備。

#### (iv) 弔辞・追悼系 motif の anchor 化の初例

retrofit 11 までの anchor は性霊集 願文系（m209）・秘蔵宝鑰 教学系（m636）・性霊集 願文系（m533）・性霊集 詩系（m637）・秘蔵宝鑰 教学系（m549）等が中心で、弔辞・追悼系（カテゴリ:悲嘆・故人タグ保持）が anchor 化されるのは本 retrofit が初。これは良医病子譬が法華経の譬喩素材中で最も弔辞・追悼系に親和的な譬であることに起因する。kaimyo-app の追善文脈（戒名・諷誦文・引導文）への直結が最も強い譬として、本軸は kaimyo-app 側の素材検索の中核となる見通し。今後 kaimyo-app 側で「連動:sg11」「連動:m44」「連動:m70」を持つ 4 motif を諷誦文・引導文生成の最有力候補プールとして活用可能。

#### (v) 4 系統カバー設計

4 motif の選定は以下の 4 系統を一括包摂する設計：

- 弔辞・追悼 碑文系：m44（性霊集 第二巻 恵果和尚の碑・anchor）
- 弔辞・追悼 讃系：m70（性霊集 第十巻 勤操影讃・anchor）
- 願文表白系：m455（性霊集 第八巻 idx=83 表白）
- 教学般若系：m494（般若心経秘鍵 第二節）

kaimyo-app の素材検索で、戒名・諷誦文・引導文・法話のジャンル別に対応可能な多様性を確保。retrofit 11 と異なり、本 retrofit は弔辞・追悼系が anchor の主体となるため、kaimyo-app 追善文脈との親和性が極めて高い。

#### (vi) kakikudashi 直接含有を客観基準とする継続

本 retrofit でも強連動の客観基準として「kakikudashi 本文に良医病子関連 keyword 直接含有」を採用：

- m44：医王・狂児・解毒（3 keyword 直接含有）+ 既存「典故:法華経:良医病子」タグ
- m70：医王・狂子・酔児（3 keyword 直接含有）+ 既存「典故:法華経:如来寿量品」「典故:法華経:五百弟子授記品」タグ
- m455：多病・医薬（直接含有）+ 既存「典故:法華経:良医薬子」タグ
- m494：医王の薬・狂酔の人（直接含有）

retrofit 10 補注 J §「kakikudashi 直接含有を客観基準とする選定」・retrofit 11 補注 K §「kakikudashi 直接含有を客観基準とする継続」の方針を継続適用。

#### (vii) 譬喩別軸の今後の展開

法華経の譬喩素材は他に「化城喩品 化城（m227/m486/m489 と m569 の弁顕密化城+良医複合譬）」「見宝塔品 多宝塔（m222/m262/m424）」等が存在。本 retrofit 12 で sg11「良医病子」を譬喩別軸の第二例として確立し、retrofit 11 sg10「火宅三車」と並ぶ二例目の譬喩別軸として位置づく。retrofit 13 以降で順次これらの譬喩別軸を追加可能。特に m569（弁顕密二教論 巻上 第一章「化城に息むの賓、楊葉を愛するの児、医王手を拱き」）は化城+良医の複合譬を保持するため、将来の化城喩軸 retrofit で本 retrofit との接続点として活用可能。

#### (viii) Phase D 必須チェックリストの完全運用化（retrofit 12 で 4 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10 が 2 回目、retrofit 11 が 3 回目、本 retrofit 12 で 4 回目の完全準拠 retrofit として位置づく。Phase D 必須チェックリストが定着した運用基盤として機能。特に commit_message.txt の冒頭行整合確認〔「retrofit 12 完走：法華経 如来寿量品 良医病子連動 retrofit〔新規 sg11「良医病子」+ 既存 m44/m70 を書き下し anchor 二重体制で採用・連動軸七系統並立に到達〕」〕が、retrofit 7 §(d-9) の不整合（commit message が retrofit 6 のまま push された問題）を再発させない運用基盤として継続機能。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 13〔法華経譬喩別軸〕

連動軸の譬喩別細分化（本 retrofit の延長）：

- 化城喩品 化城（m227/m486/m489）を anchor 候補・m569 弁顕密二教論との複合譬接続点も活用可能
- 見宝塔品 多宝塔（m222/m262/m424）を anchor 候補・idx=78 先師勤操 m424 多宝塔探索とも連携可能
- 規模 4-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 13 候補〔華厳経 一即一切連動／弁顕密二教論 顕密判 等〕

- 華厳経 一即一切：「一即一切、一切即一」を anchor に、空海著作中の華厳経関連 motif を紐づけ
- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸七系統 anchor 完全整合済〕

本 retrofit で連動軸七系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg11」を持つ 4 motif → 良医病子連動素材プール（法華譬喩・方便涅槃）
- 「連動:m44」「連動:m70」のいずれでも 4 motif 取得可能（案 A 二重 anchor 設計）
- 二重 anchor 体制と既存単一 anchor 体制の同型運用（kaimyo-app 検索ロジックは単一 anchor と同等）
- 法華経内部の三段構成検索：「諸法実相（抽象的）」 vs 「火宅三車（三乗教判）」 vs 「良医病子（方便涅槃）」の弁別
- 譬喩別軸の追加準備〔retrofit 13 以降の化城喩・多宝塔等への拡張〕
- **特に良医病子軸は弔辞・追悼系 anchor を初導入したため、kaimyo-app の追善文脈（戒名・諷誦文・引導文）への直結が最も強い**

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 二重 anchor 体制の第二例の確立

retrofit 11 sg10/m209+m636 が初例で、本 retrofit sg11/m44+m70 が第二例。retrofit 11 は「願文系（性霊集）+ 教学系（秘蔵宝鑰）」の **系統対比型** 二重化だったのに対し、本 retrofit は「碑文系（性霊集 第二巻 碑文）+ 讃系（性霊集 第十巻 讃）」の **文体対比型** 二重化。両者ともに性霊集 弔辞・追悼系（カテゴリ:悲嘆）に属しながら、文体と位置づけが分化しているため二重化が必要。今後の譬喩別軸展開で「弔辞 vs 教学」「願文 vs 詩」等の多様な二重化パターンが運用基盤として確立される見通し。

### (d-2) 弔辞・追悼系 anchor 化の初例

retrofit 11 までの anchor は性霊集 願文系・秘蔵宝鑰 教学系・性霊集 詩系が中心で、弔辞・追悼系（カテゴリ:悲嘆・故人タグ保持）が anchor 化されるのは本 retrofit が初。これは良医病子譬が法華経の譬喩素材中で最も弔辞・追悼系に親和的な譬であることに起因する。kaimyo-app の追善文脈への直結が極めて強く、今後の素材検索の中核となる見通し。

### (d-3) Write tool truncate 事象の予防対策（本 retrofit で 0 件発生）

本 retrofit では Python script を bash heredoc + write_bytes 方式で直接書き込みする運用を全面採用したため、Write tool truncate 事象は発生せず。retrofit 9-11 で複数回再発生した事象を完全に予防。今後も Python script 作成時は Write tool ではなく bash heredoc + Python write_bytes 方式を優先することが推奨される。

### (d-4) CLAUDE.md 全角括弧バランス完全到達

CLAUDE.md は本 retrofit 前は 〔/〕 各 571 件で完全バランスだったが、本 retrofit の初期 FINAL_R12 で 1 件の不整合〔末尾「完全準拠する第四の retrofit」の closing 括弧が余分〕を発生させた。即座に検出し、「引き継ぎメモ：handoff_2026-05-12_retrofit12_complete.md〔ASCII 名〕」パターンへの差し替えで修復。結果として 〔=〕=590 の完全バランス到達。半角括弧バランスも追加部分 open=close で確認済。

### (d-5) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9-11 で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を採用。最終検証で NUL 0 件確認。

### (d-6) retrofit 12 後の motifs.json サイズ

retrofit 12 で +4,529 bytes〔2,600,303 → 2,604,832 bytes〕。retrofit 11〔+3,314〕・retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 9 連続で +1,000〜4,600 bytes 規模の retrofit。新規 sg11 motif の description が長め（良医病子譬の完全な譬喩内容と空海著作中の運用を網羅）かつ強連動 4 motif への +12 タグの累積で過去最大値を更新。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-7) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg11 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg11 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg10 と同方針）。gendai_gabun_chars_total も 154,931 維持。

### (d-8) git 状態の異常（retrofit 9-11 §(d-1) 同型・継続中の可能性）

セッション開始時に `git status --short` で大量の untracked outputs/ 配下ファイルが表示されたが、誤ステージ済の削除や異常 rename は本 retrofit セッション開始時には検出されず。retrofit 11 完走後の git 状態が比較的クリーンに保たれている。ただし commit_push.bat 実行時に bash mount 側と Windows 側の乖離が再発する可能性があるため、ケンシン実行時に確認推奨。

### (d-9) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 1 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-10) Phase D 必須チェックリストの retrofit 12 で完全運用化（4 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10 で 2 回目、retrofit 11 で 3 回目、本 retrofit 12 で 4 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 12 完走：法華経 如来寿量品 良医病子連動 retrofit〔新規 sg11「良医病子」+ 既存 m44/m70 を書き下し anchor 二重体制で採用・連動軸七系統並立に到達〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔755 件・m1-m744 + sg01-sg11・2,604,832 bytes〕
- 本 retrofit build script：`outputs/retrofit12_ryoi_byoshi.py`〔dry-run + 本番適用の二段運用〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit12.json`〔retrofit 前 motifs.json・2,600,303 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit12.md`〔retrofit 前 motifs_index_design.md・74,761 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit12.md`〔retrofit 前 CLAUDE.md・235,797 bytes〕
- 前 retrofit handoff：`handoff_2026-05-12_retrofit11_complete.md`〔法華経 譬喩品 火宅三車連動〕
- 補注 L 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 12 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11 完走〔法華経 譬喩品 火宅三車連動・新規 sg10 + 既存 m209/m636 を書き下し anchor 二重体制で採用・連動軸六系統並立に到達〕→ 同日 retrofit 12 完走〔法華経 如来寿量品 良医病子連動・新規 sg11 + 既存 m44/m70 を書き下し anchor 二重体制で採用・連動軸七系統並立に到達〕。本体 motifs.json は 755 件・2,604,832 bytes・schema_history 70 件。motifs_index_design.md §2 に補注 L 追加〔補注 A-L 全 12 件 intact・86,062 bytes〕。CLAUDE.md は 240,881 bytes〔retrofit 4-12 全エントリ intact〕。連動軸七系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の三段構成〔諸法実相（抽象的核心）+ 火宅三車（具体的譬喩 三乗教判）+ 良医病子（具体的譬喩 方便涅槃）〕も成立。二重 anchor 体制の第二例（碑文系+讃系・文体対比型）。弔辞・追悼系 motif の anchor 化の初例。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit12_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit11_complete.md`〔retrofit 11 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F/G/H/I/J/K/L 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・755 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 12 commit です。

【本セッションの選択肢】
(A) retrofit 13 候補〔法華経譬喩別軸：化城喩品 化城／見宝塔品 多宝塔〕
(B) retrofit 13 候補〔華厳経 一即一切／弁顕密二教論 顕密判 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸七系統 anchor 完全整合済の素材プール活用〔特に sg11 良医病子は弔辞・追悼系 anchor で kaimyo-app 追善文脈に最適〕
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 二重 anchor 体制の運用ルール（案 A）は将来の譬喩別軸でも踏襲（補注 K・補注 L 参照）
- 本体 motifs.json は 2,604,832 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 12 完走・法華経 如来寿量品 良医病子連動 retrofit。新規 sg-id sg11「良医病子」を追加〔出典:法華経 如来寿量品「諸子幼稚、無有知者、雖見其父、不識薬色、飲服不肯」〕、書き下し anchor として **二重体制を継承**：m44（性霊集 第二巻 恵果和尚の碑・弔辞・追悼 碑文系 anchor）+ m70（性霊集 第十巻 勤操影讃・弔辞・追悼 讃系 anchor）。強連動 4 motif〔m44(anchor 碑文系)/m70(anchor 讃系)/m455(性霊集 第八巻 表白 願文系)/m494(般若心経秘鍵 第二節 教学般若系)〕に `連動:sg11`・`連動:m44`・`連動:m70` を付与（+12 タグ・案 A 採用＝全 motif に二重 anchor 明示）。total_motifs 754→755（+1 新規 sg11）・famous_phrases 10→11。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,604,832 bytes〔+4,529〕・schema_history 70 件〔+1・origin: retrofit_12:doctrine〕・補注 L 追加〔motifs_index_design.md §2・74,761→86,062 bytes・+11,301〕・CLAUDE.md 更新完了〔235,797→240,881 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸七系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70〕に到達——法華経内部で諸法実相（抽象的核心）+ 火宅三車（具体的譬喩 三乗教判）+ 良医病子（具体的譬喩 方便涅槃）の三段構成に到達。二重 anchor 体制の第二例（碑文系+讃系・文体対比型）として将来の譬喩別軸展開（化城喩・多宝塔等）への運用基盤をさらに整備。弔辞・追悼系 motif の anchor 化は本 retrofit が初例〔kaimyo-app 追善文脈との親和性が極めて高い〕。Phase D 必須チェックリストに完全準拠する第四の retrofit〕
