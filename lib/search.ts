import fs from 'fs';
import path from 'path';

interface MikkyouEntry {
  section: string;
  pages: string;
  source: string;
  text: string;
}

/**
 * 信頼できる仏教辞典データから関連テキストを検索する
 * ハルシネーション防止のため、このデータに存在する用語のみ参照する
 */
export function searchBuddhistData(keywords: string[], maxChars = 2000): string {
  const dataDir = path.join(process.cwd(), 'data', 'mikkyou');

  if (!fs.existsSync(dataDir)) return '';

  const files = fs.readdirSync(dataDir).filter(f => f.endsWith('.json'));
  const results: string[] = [];

  for (const file of files) {
    try {
      const raw = fs.readFileSync(path.join(dataDir, file), 'utf-8');
      const entry: MikkyouEntry = JSON.parse(raw);
      const text = entry.text;

      for (const keyword of keywords) {
        if (!keyword || keyword.length < 2) continue;

        let idx = 0;
        let found = 0;
        while (found < 2) {
          const pos = text.indexOf(keyword, idx);
          if (pos === -1) break;

          const start = Math.max(0, pos - 100);
          const end = Math.min(text.length, pos + 300);
          const snippet = text.slice(start, end).replace(/\n+/g, ' ').trim();

          if (snippet.length > 50) {
            results.push(`【${keyword}／${entry.source}】...${snippet}...`);
          }
          idx = pos + keyword.length;
          found++;
        }
      }
    } catch {
      // ファイル読み込みエラーは無視
    }
  }

  if (results.length === 0) return '';

  const unique = [...new Set(results)];
  let combined = unique.join('\n');
  if (combined.length > maxChars) {
    combined = combined.slice(0, maxChars) + '...';
  }

  return combined;
}
