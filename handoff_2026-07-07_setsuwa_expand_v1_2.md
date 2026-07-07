# handoff: 説話ライブラリ v1.2（忍耐・慈悲系4話 拡充）

**日付**：2026-07-07（v1.1＝1cf0956 の後続）
**着手時 HEAD**：倉庫 1cf0956／kaimyo-app aee5a0c（いずれも push 済確認済）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-07）＝残タスク (c') 忍耐・慈悲系の穏やかな異伝（非大智度論）を厳選追加

## 経緯

handoff_2026-07-05 残タスク (c') 「忍耐・慈悲系の穏やかな異伝（非大智度論）の拡充」。
既存 忍耐(A08)＝s011 忍辱仙人（受難型）・s029 長寿王（和解型）／慈悲(A07)＝s009/s017/s021/s030
と重複せず、葬送法話の穏やかなトーンに適う4話を、いずれも既存99タグ内で厳選追加した
（凄惨な描写のものは不採用＝v1.1 の毒龍・薩陀波崙 見送りと同基準）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 41→45（schema 1.1 のまま）
  - s042 富楼那（プンナ）の覚悟（雑阿含経／パーリ 富楼那教誡経・early）
    tags=忍耐／不動心／寛容／志（A08+A04）。罵倒・危害にも感謝で応じる能動的忍耐
  - s043 慈経の因縁（スッタニパータ 慈経＋パーリ註釈・early）
    tags=慈悲／寛容／和解／思いやり（A07+A08）。恐れ・敵意を慈しみで包み和解へ
  - s044 睒子（サーマ）本生の孝養（六度集経／菩薩睒子経・tale）
    tags=親の恩／親子の絆／慈悲／看病・介護（A02+A09+A07）。盲目の両親への孝養と真実の力
  - s045 大海を泳ぐ王子（マハージャナカ本生・ジャータカ539・tale）
    tags=不退転／あきらめない／精進／信念（A04+A11）。岸が見えずとも七日七夜泳ぎ切る忍耐・精進
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - description（41話→45話）更新
- **_dev_references/setsuwa_tag_axes_v1.md**：§9「忍耐・慈悲系の拡充（v1.1 続）」追加・対象を45話へ
  （§2 の20軸・§4 割当は不変＝仕様は v1 のまま）
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 41→45 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_2.md**（本ファイル）

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.2 から同期（45話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）

## 検証（ホスト権威）

⚠️ setsuwa.json は sandbox mount が stale/truncate 表示（46966→編集後も 49280 で char23372 parse 失敗）
のため、**bash パースは非採用**。整合は Read ツール（ホスト権威）＋自己完結ハーネスで実施：

- 新4レコード fragment を単体 JSON 検証：synopsis 215/201/221/219字（全て150-250内）・
  半角括弧0・全タグ既存99内・新タグ0・NUL0
- Edit 後 Read 再確認：count 45・s041 は `},` で閉じ s042-045 挿入・レコード間カンマ適正・
  配列 `]`＋オブジェクト `}` 健全
- picker 回帰（41話 vs 45話・タグ埋め込み自己完結ハーネス・lib/setsuwa-picker.ts 忠実移植）：
  - **文書化5テーマの top1 完全不変**＝誠実 s001・感謝と自立 s006・信念 s008・看取り s021・無常 s028
    （信念の #2 が s001→s045、看取りの #2 が s035→s044 に改善したが、織り込み対象=#1 は保存）
  - 新4話は 忍耐→s011継続(s042 #2)・慈悲和解→s043・親孝行→s044・諦めない→s045 で正しく上位化
- kaimyo-app tsc：コード不変。v1.1 の warehouse.ts 型追加を含む HEAD aee5a0c で TSC_EXIT=0 を
  本セッションで確認済（git archive HEAD を /tmp 展開＋node_modules symlink で mount truncate 回避）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.2＋spec §9＋push4（count45）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count45）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
   （commit_message_setsuwa_sync.txt 更新済＝データのみ・warehouse/picker は no-op ステージ）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit（push4 前に kaimyo commit
   すると取りこぼす。v1.1 で一度発生→再コミットで是正した経緯あり）

## 落とし穴メモ

- sandbox mount は setsuwa.json/picker.ts/warehouse.ts/多数の .bat を truncate/stale 表示する
  既知 phantom。git status の M・git diff の deletions も同 phantom＝committed 内容に変更なし。
  Windows 側 git は真の host ファイルをコミットするため pipeline は安全。整合は Read＋git show HEAD
  ＋SHA-256（ホスト権威）で行う。source.doc 2件（vol19/vol20_build）M 表示も既知。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash での read-modify-write は truncate
  由来のファイル破壊リスクがあるため禁止。
- 新4話は corpus_refs なし（非大智度論）。将来これら原典（六度集経・雑阿含経・スッタニパータ・
  ジャータカ）を倉庫 corpus に取り込んだ際に §8 と同形式で相互参照を検討。
- picker prompt 文字列 `出典検証済みの40話から選定`（lib/setsuwa-picker.ts formatSetsuwaForPrompt）
  は v1 以来「40話」のまま（現在45話）＝軽微な表示ずれ。コード変更＝要ホスト tsc のため本 v1.2
  では触らず（データのみ同期の原則保持）。修正するなら「40」→「45」の1語＋ホスト tsc 確認。

## 次にやること

- (c') さらなる拡充の余地：忍耐・慈悲系のほか、和合・謙虚系や自然・世界への眼差し系の穏やかな
  異伝。新タグは20軸へ割当し被覆100%維持、収まらぬ新テーマのみ軸追加で仕様書 v2 に更新。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。
- 任意：picker prompt の「40話→45話」表示ずれ修正（要ホスト tsc）。
