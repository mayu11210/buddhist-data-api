# 戒名アプリ・法話アプリ移行ガイド（v1.10 → API ② への切替）

最終更新：2026-04-28

---

## このドキュメントの目的

戒名アプリ・法話アプリを、現在の **API ①（Next.js / Vercel）** から、
新しい **API ②（FastAPI / Render）** に乗り換えるための具体的な手順書。

**この作業は kaimyo-app 側のリポジトリで実施するため、buddhist-data-api 側の
作業ではない。** 別セッションで kaimyo-app をマウントして実施すること。

---

## 移行戦略（推奨：段階的）

いきなり API ① を捨てるのではなく、**両方を併用**しながら段階移行する：

### フェーズ A：API ② を「素材取得」用途で使い始める（リスク最小）

戒名生成のロジックは今のまま AI に任せる。ただし AI に渡す素材を、
API ① の生のキーワード検索から、API ② の構造化レスポンスに置き換える。

```
旧：API ① で「学問熱心」を検索 → 関連辞書文を AI に渡す → AI が戒名を考える
新：API ② で「学問熱心」を検索 → 戒名候補20個 + 根拠 を AI に渡す → AI が選ぶ
```

### フェーズ B：API ② の戒名候補をそのまま採用（AI 介在を減らす）

戒名候補のスコア順で十分な品質が出ると確認できたら、AI 微調整なしで
そのまま採用する選択肢を増やす。

### フェーズ C：API ① の依存を切る

完全移行できたら API ① の Vercel デプロイを止める（または素材検索専用に残す）。

---

## API ② エンドポイント早見表

| 用途 | エンドポイント | 主要パラメータ |
|---|---|---|
| 戒名候補生成 | `GET /api/kaimyo/candidates` | `characteristics`（必須・CSV） |
| 法話典故検索 | `GET /api/houwa/citations` | `theme`（必須） |
| 篇カルテ参照 | `GET /api/篇/{idx}` | `idx`（0..111） |
| 用語の関連参照 | `GET /api/term/{key}` | 例：三密・即身成仏 |
| 人物参照 | `GET /api/person/{key}` | alias 解決対応（弘法大師→空海） |
| 地名参照 | `GET /api/place/{key}` | 例：高野山 |
| 典故書名参照 | `GET /api/citation/{key}` | 例：荘子・書経 |
| 梵語参照 | `GET /api/sanskrit/{key}` | IAST 形式（例：prajñā） |
| 空海著作参照 | `GET /api/kukai-work/{key}` | 例：性霊集 |
| マッピング表 | `GET /api/mappings` | 故人特性 / テーマ語 一覧 |

すべて **`X-API-Key` ヘッダーが必要**（GET / と /health のみ例外）。

---

## 戒名アプリ側のコード例（Next.js / TypeScript）

### 環境変数の追加（kaimyo-app の `.env.local`）

```
NEXT_PUBLIC_BUDDHIST_API_BASE=https://buddhist-data-api.onrender.com
BUDDHIST_API_KEY=【Render と同じキー】
```

注：**APIキーはサーバーサイドのみ**（`NEXT_PUBLIC_` を付けない）にすること。
ブラウザに漏れると認証の意味がない。

### サーバーサイドのプロキシ関数（推奨パターン）

```typescript
// kaimyo-app/lib/buddhist-api.ts
const BASE = process.env.NEXT_PUBLIC_BUDDHIST_API_BASE!;
const KEY = process.env.BUDDHIST_API_KEY!; // server-only

export async function fetchKaimyoCandidates(
  characteristics: string[],
  options: {
    preferPersons?: string[];
    preferPlaces?: string[];
    length?: 2 | 4;
    limit?: number;
  } = {}
) {
  const url = new URL(`${BASE}/api/kaimyo/candidates`);
  url.searchParams.set("characteristics", characteristics.join(","));
  if (options.preferPersons?.length)
    url.searchParams.set("prefer_persons", options.preferPersons.join(","));
  if (options.preferPlaces?.length)
    url.searchParams.set("prefer_places", options.preferPlaces.join(","));
  if (options.length) url.searchParams.set("length", String(options.length));
  if (options.limit) url.searchParams.set("limit", String(options.limit));

  const res = await fetch(url, {
    headers: { "X-API-Key": KEY },
    cache: "no-store",
  });
  if (!res.ok) throw new Error(`API ② error ${res.status}`);
  return res.json();
}

export async function fetchHouwaCitations(
  theme: string,
  options: {
    expand?: boolean;
    limit?: number;
    excerptRadius?: number;
  } = {}
) {
  const url = new URL(`${BASE}/api/houwa/citations`);
  url.searchParams.set("theme", theme);
  if (options.expand !== undefined)
    url.searchParams.set("expand", String(options.expand));
  if (options.limit) url.searchParams.set("limit", String(options.limit));
  if (options.excerptRadius)
    url.searchParams.set("excerpt_radius", String(options.excerptRadius));

  const res = await fetch(url, {
    headers: { "X-API-Key": KEY },
    cache: "no-store",
  });
  if (!res.ok) throw new Error(`API ② error ${res.status}`);
  return res.json();
}
```

### Next.js API Route（クライアントから呼ばれる側）

```typescript
// kaimyo-app/app/api/generate-kaimyo/route.ts
import { fetchKaimyoCandidates } from "@/lib/buddhist-api";

export async function POST(req: Request) {
  const { characteristics, length } = await req.json();
  const data = await fetchKaimyoCandidates(characteristics, { length, limit: 20 });

  // ここで AI（OpenAI / Claude 等）に渡して最終戒名を組み立てる
  // const finalKaimyo = await llm.completion({ candidates: data.results, ... });

  return Response.json(data);
}
```

クライアント（戒名アプリの画面側）は今までと同じく自分の API Route を叩くだけ。
**APIキーがブラウザに出ない設計**になる。

---

## 法話アプリの場合も同じパターン

```typescript
// houwa-app の場合
import { fetchHouwaCitations } from "@/lib/buddhist-api";

const data = await fetchHouwaCitations("無常", {
  expand: true,
  limit: 5,
  excerptRadius: 200,
});
// data.citations に「無常」関連の性霊集 5 篇が抜粋付きで返る
```

---

## トラブルシューティング

| 症状 | 原因と対策 |
|---|---|
| 401 UNAUTHORIZED | `X-API-Key` ヘッダーが未送信 / 値ミスマッチ |
| CORS エラー | Render の `BUDDHIST_API_ALLOWED_ORIGINS` に kaimyo-app の URL を追加 |
| 504 Gateway Timeout | Render Free のスリープ起動。初回 30 秒待つ or Starter プランに切替 |
| データが古い | API ② はメモリ常駐索引のため、データ更新後はサービス再起動が必要 |

---

## 切替後の確認チェックリスト

- [ ] `.env.local` に新しい URL とキーが入っている
- [ ] サーバーサイドのみで APIキーを参照している（ブラウザに漏れていない）
- [ ] CORS が通っている（kaimyo-app から API ② へリクエストが届く）
- [ ] 戒名候補のレスポンス構造が想定通り（`results[].jukugo` など）
- [ ] AI への素材渡しが新形式に対応している
- [ ] 旧 API ① の呼び出しコードが削除済（または併用なら残す方針が明文化）
