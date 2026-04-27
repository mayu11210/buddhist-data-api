#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化フェーズ B v1.1 本格抽出スクリプト（梵語 IAST）

shoryoshu_miyasaka.json の全 112 篇 gendaigoyaku から
IAST 表記の梵語（Sanskrit in Latin transliteration）を網羅的に抽出し、
data/mikkyou/index_shoryoshu_sanskrit.json を生成する。

仕様：cross_index_spec.md v1.1 §9 Tier 2-4

抽出方針：
- 正規表現で IAST 候補を抽出（ASCII + ダイアクリティカル + ハイフン + ピリオド + アポストロフィ）
- 3 文字以上
- EXCLUDE_TOKENS で英単語・メタ情報語・URL 断片・ローマ字日本語を除外
- 大文字小文字を統一（小文字基準で canonical_key）
- 同 canonical_key の表記揺れを集約（aliases に出現順カウント保存）
- IAST ダイアクリティカル含有/非含有を has_diacritics に記録
- ALIAS_MAP は表記揺れの異綴り統合用（現状空。今後 vairochana → vairocana 等が必要なら追加）

extract_terms.py / extract_citations.py の構造を踏襲。
"""

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE = ROOT / 'data' / 'kukai' / 'shoryoshu_miyasaka.json'
OUTPUT = ROOT / 'data' / 'mikkyou' / 'index_shoryoshu_sanskrit.json'

# ====== 抽出パターン ======
# IAST ダイアクリティカル群
DIACRITICS = "ĀāĪīŪūṅÑñṬṭḌḍṆṇḶḷŚśṢṣṚṛḤḥṂṃ"

# 1 文字目：ASCII or IAST 文字
# 2 文字目以降：ASCII or IAST 文字 + ハイフン + ピリオド + アポストロフィ類
RE_SANSKRIT = re.compile(
    r"[A-Za-z" + DIACRITICS + r"]"
    r"[A-Za-z" + DIACRITICS + r"\-\.’ʼ']+"
)

# ====== 除外辞書（小文字基準）======
# 試行抽出（_dev_references/extract_sanskrit.py 設計時）で同定された 14 ノイズ語
EXCLUDE_TOKENS = {
    # メタ情報・自己参照
    'idx',          # 補注内「idx=12」等の自己参照
    'kindle',       # 「Kindle 本」
    'ocr',          # 「OCR 異同」
    'claude.md',    # CLAUDE.md 言及
    # URL 断片（"https://hu hu ran" 由来）
    'https',
    'ran',
    'hu',
    # 補注内の英語訳語
    'milk',         # milk gruel
    'gruel',        # milk gruel
    'brass',        # 鍮石・偽金
    'gold',         # gold elixir
    'elixir',       # gold elixir
    'clavicle',     # 鎖骨の現代医学訳
    # ローマ字日本語
    'goshin-kekkai', # 護身結界
}

# ====== 表記揺れ統合マップ（拡張余地あり・現状空）======
# canonical_key (小文字) を変換する。例：'vairochana' → 'vairocana'
# 現性霊集データには異綴り揺れがほぼないため、今後の発見次第で追加。
ALIAS_MAP = {
    # 'vairochana': 'vairocana',  # 英語綴り → IAST 綴り
}


def canonicalize(token: str) -> str:
    """大文字小文字を統一し、ALIAS_MAP の異綴り統合を適用する"""
    lower = token.lower()
    return ALIAS_MAP.get(lower, lower)


def has_diacritic(token: str) -> bool:
    """token に IAST ダイアクリティカルが含まれるか"""
    return any(c in DIACRITICS for c in token)


def extract_sanskrit():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        corpus = json.load(f)

    # canonical_key → {occurrences, forms}
    table = defaultdict(lambda: {
        'occurrences': [],
        'forms': defaultdict(int),
    })

    for idx, item in enumerate(corpus):
        篇名 = item.get('篇名', '')
        巻 = item.get('巻番号', '')
        for page_idx, page in enumerate(item.get('ページ', [])):
            text = page.get('gendaigoyaku', '')
            if not text:
                continue

            for m in RE_SANSKRIT.finditer(text):
                tok = m.group(0)
                if len(tok) < 3:
                    continue
                cl = tok.lower()
                if cl in EXCLUDE_TOKENS:
                    continue
                ck = canonicalize(tok)
                p = m.start()
                ctx_start = max(0, p - 30)
                ctx_end = min(len(text), p + len(tok) + 30)
                context = text[ctx_start:ctx_end].replace('\n', ' ')

                table[ck]['occurrences'].append({
                    'shoryoshu_idx': idx,
                    '篇名': 篇名,
                    '巻': 巻,
                    'page_idx': page_idx,
                    'context': context,
                    'context_position': p,
                    'sanskrit_form': tok,
                })
                table[ck]['forms'][tok] += 1

    # entries 整形
    entries = []
    for ck in sorted(table.keys()):
        d = table[ck]
        # forms を頻度降順にソート（最頻出を representative_form に）
        forms_sorted = sorted(d['forms'].items(), key=lambda x: (-x[1], x[0]))
        representative = forms_sorted[0][0]
        aliases = [{'form': f, 'count': c} for f, c in forms_sorted]
        篇set = sorted(set(o['shoryoshu_idx'] for o in d['occurrences']))
        entries.append({
            'canonical': ck,
            'representative_form': representative,
            'aliases': aliases,
            'alias_count': len(aliases),
            'has_diacritics': has_diacritic(ck) or any(has_diacritic(a['form']) for a in aliases),
            'occurrence_count': len(d['occurrences']),
            '篇分布': 篇set,
            'occurrences': d['occurrences'],
        })

    # 出現件数降順、同件数は canonical 昇順
    entries.sort(key=lambda e: (-e['occurrence_count'], e['canonical']))

    output = {
        'schema_version': '1.1',
        'category': '梵語 IAST 索引',
        'source_corpus': 'data/kukai/shoryoshu_miyasaka.json',
        'generated_at': str(date.today()),
        'extraction_strategy': '正規表現 IAST 抽出 + EXCLUDE_TOKENS 除外 + 小文字 canonical 集約',
        'exclude_tokens_count': len(EXCLUDE_TOKENS),
        'alias_map_size': len(ALIAS_MAP),
        'summary': {
            'unique_canonicals': len(entries),
            'total_occurrences': sum(e['occurrence_count'] for e in entries),
            'covered_shoryoshu_idx_count': len(set(
                o['shoryoshu_idx'] for e in entries for o in e['occurrences']
            )),
            'with_diacritics_count': sum(1 for e in entries if e['has_diacritics']),
            'ascii_only_count': sum(1 for e in entries if not e['has_diacritics']),
            'multi_form_canonicals': sum(1 for e in entries if e['alias_count'] > 1),
        },
        'entries': entries,
    }

    # NULL バイト混入を避けるため bytes 経由で書き込み
    payload = json.dumps(output, ensure_ascii=False, indent=2).encode('utf-8')
    # 末尾 NULL バイト除去（万一の保険）
    payload = payload.rstrip(b'\x00')
    with open(OUTPUT, 'wb') as f:
        f.write(payload)

    print(f'✓ Generated: {OUTPUT}')
    print(f'  unique_canonicals       : {output["summary"]["unique_canonicals"]}')
    print(f'  total_occurrences       : {output["summary"]["total_occurrences"]}')
    print(f'  covered_篇              : {output["summary"]["covered_shoryoshu_idx_count"]} / 112')
    print(f'  with_diacritics         : {output["summary"]["with_diacritics_count"]}')
    print(f'  ascii_only              : {output["summary"]["ascii_only_count"]}')
    print(f'  multi_form_canonicals   : {output["summary"]["multi_form_canonicals"]}')
    print(f'  exclude_tokens          : {output["exclude_tokens_count"]}')
    print(f'  alias_map_size          : {output["alias_map_size"]}')
    print(f'  file size (bytes)       : {len(payload):,}')


if __name__ == '__main__':
    extract_sanskrit()
