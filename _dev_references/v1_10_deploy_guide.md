# v1.10 Render デプロイ手順書（ケンシン用）

最終更新：2026-04-28

---

## 全体像

```
[GitHub mayu11210/buddhist-data-api]
        ↓ 連携
[Render：Blueprint 読み込み]
        ↓ 自動ビルド・自動デプロイ
[https://buddhist-data-api-xxxx.onrender.com]
        ↓ X-API-Key 認証
[戒名アプリ・法話アプリ]
```

---

## Step 1：Render アカウント作成（初回のみ・5 分）

1. https://render.com にアクセス
2. 「Get Started」→ GitHub アカウントでサインアップ
3. メール確認

---

## Step 2：GitHub リポジトリと連携（初回のみ・3 分）

1. Render Dashboard 右上の「New +」→ **「Blueprint」** を選択
2. 「Connect a repository」→ `mayu11210/buddhist-data-api` を選ぶ
3. Branch は `main` を選択
4. Render が自動的に `render.yaml` を検出して読み込む
5. 「Apply」をクリック

これで Web Service が作成されるが、まだ環境変数が空なので動かない。次のステップへ。

---

## Step 3：環境変数を設定する（重要・5 分）

1. 作成された `buddhist-data-api` サービスを開く
2. 左メニューの **「Environment」** をクリック
3. 「Add Environment Variable」で以下 2 つを追加：

### `BUDDHIST_API_KEY`（必須）

値はこのセッションで生成済（別チャットで通知）。**Cowork に「APIキーを表示して」と頼めば再表示できる**。
コピーしてそのまま貼り付け。

### `BUDDHIST_API_ALLOWED_ORIGINS`（任意・推奨）

現状の戒名アプリだけ許可するなら：
```
https://kaimyo-app.vercel.app
```

将来 法話アプリも追加するなら CSV で：
```
https://kaimyo-app.vercel.app,https://houwa-app.vercel.app
```

未設定でも main.py のデフォルト（kaimyo-app + localhost）が使われるが、**明示推奨**。

4. 「Save Changes」→ 自動再デプロイが走る（5〜10 分）

---

## Step 4：デプロイ完了確認（3 分）

1. サービスのトップ画面で「Live」状態になるまで待つ
2. URL（例：`https://buddhist-data-api-xxxx.onrender.com`）をメモ
3. **動作確認 3 連発**：

### 4-A：認証スキップ系（ブラウザでアクセス可能）

ブラウザで以下を開く：
```
https://buddhist-data-api-xxxx.onrender.com/health
```
→ `{"status":"ok"}` が返れば OK

```
https://buddhist-data-api-xxxx.onrender.com/robots.txt
```
→ `User-agent: *\nDisallow: /` が返れば OK（検索エンジン除け有効）

### 4-B：認証必須系（ブラウザでは弾かれるはず）

ブラウザで以下を開く：
```
https://buddhist-data-api-xxxx.onrender.com/api/篇/0
```
→ `{"error":"UNAUTHORIZED",...}` が 401 で返れば OK（認証が効いている）

### 4-C：APIキー付きアクセス（curl でテスト）

PowerShell で：
```powershell
curl -H "X-API-Key: 【ここにAPIキーを貼る】" `
  https://buddhist-data-api-xxxx.onrender.com/api/篇/0
```
→ 篇カルテの JSON が返れば OK（v1.10 完全動作）

---

## Step 5：戒名アプリ側を改修する（別作業）

戒名アプリのコードに以下の変更を入れる必要がある：

```javascript
// 旧（API ① の呼び出し例）
const res = await fetch('https://buddhist-data-api.vercel.app/api/search', {
  method: 'POST',
  body: JSON.stringify({ keywords: [...] }),
});

// 新（API ② の呼び出し例）
const res = await fetch(
  'https://buddhist-data-api-xxxx.onrender.com/api/kaimyo/candidates?'
  + 'characteristics=' + encodeURIComponent('学問熱心,温和')
  + '&limit=20',
  {
    headers: {
      'X-API-Key': process.env.BUDDHIST_API_KEY, // .env で管理
    },
  }
);
```

**戒名アプリ側のリポジトリは別なので、そちらの作業は別セッションで実施。**
詳細は `_dev_references/v1_10_kaimyo_app_migration.md` 参照。

---

## トラブルシューティング

| 症状 | 原因と対策 |
|---|---|
| デプロイがビルド失敗 | Build Logs を見る。`pip install` 系なら requirements.txt の問題 |
| `/health` も 401 | middleware が AUTH_EXEMPT_PATHS を見ていない可能性。最新 main.py か確認 |
| `/api/篇/0` が 200 で返る（認証効かない） | BUDDHIST_API_KEY が未設定。Render の Environment を確認 |
| 戒名アプリから CORS エラー | BUDDHIST_API_ALLOWED_ORIGINS に正しい URL が入っているか確認 |
| 503 Service Unavailable | Free プランはアイドル時にスリープ。最初の 1 リクエストで起動するため 30 秒程度待つ |

---

## 撤回手順（万一公開やめたい場合）

1. Render Dashboard で `buddhist-data-api` サービスを開く
2. 「Settings」→ 一番下の「Delete Service」
3. これで URL は失効・データは Render から完全削除（GitHub には残る）

---

## 運用上の注意

- **APIキーは一度漏洩したら必ず再生成**。再生成手順：
  ```bash
  python3 -c "import secrets; print(secrets.token_urlsafe(48))"
  ```
  → Render の Environment と戒名アプリの両方を新しい値で更新

- **Free プランの制約**：月 750 時間（≒ 24h × 31 日 = 744h）まで無料。
  ただし 15 分アイドルで自動スリープ → 次のリクエストで 30 秒程度の起動遅延。
  本番運用で遅延が気になるなら Starter プラン（$7/月）に切替。

- **検索エンジン除けは三重の防御**：
  1. `/robots.txt` の Disallow（行儀の良いクローラー除け）
  2. `X-Robots-Tag: noindex, nofollow` ヘッダー（行儀問わず除け）
  3. APIキー認証（そもそも中身を見せない）
