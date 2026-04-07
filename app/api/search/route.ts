import { NextRequest, NextResponse } from 'next/server';
import { searchBuddhistData, getTemplate } from '@/lib/search';

// 許可するアクセス元（戒名アプリ・法話アプリなど）
const ALLOWED_ORIGINS = [
  'http://localhost:3000',
  'http://localhost:3001',
  'https://kaimyo-app.vercel.app',
  // 将来のアプリを追加する場合はここに追記
];

function getCorsHeaders(origin: string): Record<string, string> {
  const isAllowed = ALLOWED_ORIGINS.some(o => origin.startsWith(o)) || origin === '';
  const headers: Record<string, string> = {
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };
  if (isAllowed) {
    headers['Access-Control-Allow-Origin'] = origin || '*';
  }
  return headers;
}

// キーワード検索
export async function POST(req: NextRequest) {
  const origin = req.headers.get('origin') || '';
  const corsHeaders = getCorsHeaders(origin);

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

// テンプレート取得（GET /api/search?template=hyobyaku または fusonmon）
export async function GET(req: NextRequest) {
  const origin = req.headers.get('origin') || '';
  const corsHeaders = getCorsHeaders(origin);

  const { searchParams } = new URL(req.url);
  const templateType = searchParams.get('template');

  if (templateType === 'hyobyaku' || templateType === 'fusonmon') {
    const data = getTemplate(templateType);
    if (!data) {
      return NextResponse.json(
        { error: 'テンプレートが見つかりません' },
        { status: 404, headers: corsHeaders }
      );
    }
    return NextResponse.json(data, { headers: corsHeaders });
  }

  return NextResponse.json(
    { error: 'template パラメータに hyobyaku または fusonmon を指定してください' },
    { status: 400, headers: corsHeaders }
  );
}

// プリフライトリクエスト対応
export async function OPTIONS(req: NextRequest) {
  const origin = req.headers.get('origin') || '';
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': origin || '*',
      'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  });
}
