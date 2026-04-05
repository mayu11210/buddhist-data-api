import { NextRequest, NextResponse } from 'next/server';
import { searchBuddhistData } from '@/lib/search';

// 許可するアクセス元（戒名アプリ・法話アプリなど）
const ALLOWED_ORIGINS = [
  'http://localhost:3000',
  'http://localhost:3001',
  'https://kaimyo-app.vercel.app',
  // 将来のアプリを追加する場合はここに追記
];

export async function POST(req: NextRequest) {
  // CORS設定
  const origin = req.headers.get('origin') || '';
  const isAllowed = ALLOWED_ORIGINS.some(o => origin.startsWith(o)) || origin === '';

  const corsHeaders: Record<string, string> = {
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };

  if (isAllowed) {
    corsHeaders['Access-Control-Allow-Origin'] = origin || '*';
  }

  try {
    const body = await req.json();
    const keywords: string[] = body.keywords ?? [];
    const maxChars: number = body.maxChars ?? 2000;

    if (!Array.isArray(keywords) || keywords.length === 0) {
      return NextResponse.json(
        { error: 'keywords は配列で指定してください' },
        { status: 400, headers: corsHeaders }
      );
    }

    const results = searchBuddhistData(keywords, maxChars);

    return NextResponse.json(
      {
        results,
        found: results.length > 0,
        keywords,
        source: '密教大辞典（信頼できる仏教辞典データ）',
      },
      { headers: corsHeaders }
    );
  } catch {
    return NextResponse.json(
      { error: 'リクエスト処理中にエラーが発生しました' },
      { status: 500, headers: corsHeaders }
    );
  }
}

// プリフライトリクエスト対応
export async function OPTIONS(req: NextRequest) {
  const origin = req.headers.get('origin') || '';
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': origin || '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  });
}
