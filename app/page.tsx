export default function Home() {
  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>仏教データ保管庫 API</h1>
      <p>信頼できる仏教辞典データの検索APIです。</p>
      <h2>使い方</h2>
      <pre style={{ background: '#f5f5f5', padding: '1rem', borderRadius: '4px' }}>
{`POST /api/search
Content-Type: application/json

{
  "keywords": ["阿字", "大日"],
  "maxChars": 2000
}`}
      </pre>
      <h2>収録データ</h2>
      <ul>
        <li>密教大辞典（全巻）</li>
      </ul>
    </main>
  );
}
