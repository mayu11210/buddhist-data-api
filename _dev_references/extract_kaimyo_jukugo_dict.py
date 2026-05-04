#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2-C（dict 型著作向け・戒名向け熟語抽出）

dict 型コーパス（弁顕密二教論・吽字義 等）の **トップレベル `gendaigoyaku`**
から、kaimyo-app の戒名選定用辞書として価値の高い 2 字漢語熟語を抽出し、
`data/mikkyou/index_<corpus>_kaimyo.json` を生成する。

`_tmp_extract_kaimyo_jukugo.py`（性霊集・list 型 112 篇向け）の dict 型版。
KAIMYO_ICHIJI / SANSKRIT_TO_KAIMYO_JUKUGO / DOCTRINAL_2CHAR_WHITELIST /
KAIMYO_NOISE はそのまま継承（性霊集版と完全互換）。

仕様：cross_index_spec.md v1.7 §16 G2-C / 旧 §10 Tier 2-3 dict 拡張

抽出方針（性霊集版と同一・3 起点合成）：
  起点 1：密教教学用語の戒名適合 11 語（index_<corpus>_terms.json kaimyo_suitable=true）
  起点 2：梵語の漢訳対応（index_<corpus>_sanskrit.json + 手書きマッピング）
  起点 3：補注内 2 字漢語熟語の機械抽出 → DOCTRINAL_2CHAR_WHITELIST で絞込

スコアリング（0〜75 点）：
  freq_score      : log10(count+1) * 12（上限 25）
  doctrinal_score : seed_terms=30 / seed_sanskrit=20 / paren_doctrinal=10
  ichiji_score    : KAIMYO_ICHIJI 含字数 × 8（上限 16）
  aesthetic_score : 字形・響きヒューリスティック（上限 4）

使い方：
    python3 _dev_references/extract_kaimyo_jukugo_dict.py --corpus nikyo-ron.json
    python3 _dev_references/extract_kaimyo_jukugo_dict.py --corpus all
"""

import argparse
import json
import math
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE_DIR = ROOT / 'data' / 'kukai'
OUTPUT_DIR = ROOT / 'data' / 'mikkyou'

# ====== dict 型 primary_corpus 著作 ======
DICT_CORPUS_LIST = [
    'nikyo-ron.json',
    'ujiji.json',
    'shoji-jisso.json',
    'sokushin-jobutsu.json',
    'hannya-hiken.json',
    'hizo-houyaku.json',
    'dainichikyo-sho-vol1.json',
    'sankyo-shiki.json',
    'bodaishinron.json',  # 2026-05-04 追加（候補 D・9 著作目）
]

# ====== 戒名適合一字辞書（性霊集版と完全同期）======
KAIMYO_ICHIJI = {
    '智', '慧', '明', '覚', '悟', '聡', '叡', '哲', '玄',
    '慈', '悲', '仁', '優', '善', '愛',
    '浄', '信', '清', '澄', '純', '潔',
    '寂', '静', '安', '穏', '和', '雅',
    '真', '常', '実', '直', '正',
    '法', '道', '理', '心', '性', '体',
    '空', '無', '元', '本',
    '妙', '宝', '貴', '尊', '神',
    '大', '広', '恵', '徳', '栄',
    '光', '明', '照', '輝',
    '月', '華', '蓮', '雲', '霞',
    '山', '海', '泉', '水', '河',
    '永', '長', '久',
    '密', '真', '言', '阿', '吽', '金', '剛',
    '仏', '如', '尊', '聖', '師',
    '経', '律', '論',
    '志', '誓', '願', '念',
}

# ====== 起点 2：梵語の漢訳対応辞書 ======
SANSKRIT_TO_KAIMYO_JUKUGO = {
    'prajñā':       ['般若', '智慧'],
    'karuṇā':       ['大悲', '慈悲'],
    'mahā-karuṇā':  ['大悲'],
    'bodhi':        ['菩提'],
    'bodhicitta':   ['菩提'],
    'bodhisattva':  ['菩薩'],
    'śūnya':        ['空観'],
    'śūnyatā':      ['空観'],
    'samādhi':      ['三昧'],
    'dhyāna':       ['禅定'],
    'dharma':       ['法身', '正法'],
    'dharmakāya':   ['法身'],
    'dharma-dhātu': ['法界'],
    'mantra':       ['真言'],
    'vajra':        ['金剛'],
    'mahāvairocana':['大日', '遮那'],
    'vairocana':    ['遮那'],
    'tathāgata':    ['如来'],
    'amitābha':     ['弥陀'],
    'avalokiteśvara':['観音'],
    'mañjuśrī':     ['文殊'],
    'samantabhadra':['普賢'],
    'mahāyāna':     ['大乗'],
    'ekayāna':      ['一乗'],
    'nirvāṇa':      ['涅槃'],
    'śīla':         ['持戒'],
    'kṣānti':       ['忍辱'],
    'vīrya':        ['精進'],
    'satya':        ['真実'],
    'maitrī':       ['慈悲'],
    'ratna':        ['宝珠'],
    'cintāmaṇi':    ['宝珠'],
    'hṛdaya':       ['心要'],
    'ācārya':       ['阿闍梨'],
    'guru':         ['上師'],
    'puṇya':        ['福徳'],
    'siddhi':       ['成就'],
    'mokṣa':        ['解脱'],
    'tathatā':      ['真如'],
    'sattva':       ['薩埵'],
    'buddha':       ['仏陀'],
    'saṃgha':       ['僧伽'],
    'gāthā':        ['偈頌'],
    'sumeru':       ['須弥'],
    'pāramitā':     ['波羅蜜'],
    'upāya':        ['方便'],
    'śraddhā':      ['浄信'],
    'kṣetra':       ['仏土'],
    'lokadhātu':    ['世界'],
    'praṇidhāna':   ['誓願'],
    'mahāmudrā':    ['大印'],
}

# ====== 起点 3：補注内 2 字熟語のホワイトリスト ======
DOCTRINAL_2CHAR_WHITELIST = {
    '智慧', '般若', '菩提', '菩薩', '法身', '法界', '法性',
    '真言', '真如', '真実', '真理', '真常', '真性',
    '大悲', '慈悲', '大慈', '大徳', '大智', '大悟', '大覚', '大空', '大円',
    '即身', '即心', '本性', '本覚', '本来', '本有',
    '一乗', '一心', '一念', '一実',
    '三密', '三昧', '三摩', '三宝',
    '阿字', '阿閦', '蓮華', '金剛', '宝珠', '宝蓋',
    '禅定', '禅那', '解脱', '涅槃', '寂滅', '寂静',
    '玄機', '玄妙', '玄理', '玄旨', '玄門',
    '智剣', '智明', '智海', '智円',
    '光明', '光寿', '光徳', '光円',
    '浄信', '浄土', '浄心', '浄智', '浄行', '浄業',
    '聖徳', '聖智', '聖恩', '聖王',
    '妙法', '妙智', '妙覚', '妙音', '妙荘', '妙慧', '妙理',
    '慧明', '慧智', '慧覚',
    '念仏', '念定',
    '常住', '常寂', '常楽',
    '正法', '正覚', '正念', '正定', '正智',
    '功徳', '徳用', '徳行', '徳本',
    '六度', '六波', '四摂',
    '密厳', '密宗', '密門',
    '理趣', '理事', '理智',
    '心王', '心地', '心源', '心要',
    '清浄', '純真', '純信',
    '修行', '修禅', '修学',
    '蓮台', '蓮花', '蓮宇', '蓮社',
    '浄域', '浄場',
    '教王', '教主', '教法',
    '譲徳', '功用',
    '如来', '如実', '如法',
    '仏法', '仏徳', '仏智', '仏果', '仏因', '仏陀', '仏国',
    '法子', '法孫', '法縁', '法器', '法門', '法乳', '法雨',
    '甘露', '甘雨',
    '慈雲', '慈光', '慈船', '慈徳',
    '霊妙', '霊光', '霊根',
}

# ====== 戒名向けに不適なノイズ熟語 ======
KAIMYO_NOISE = {
    '八一', '八二', '八三', '八四', '七一', '七二', '六一', '九一',
    '一二', '二三', '三四', '十二', '二十', '九〇',
    '嵯峨', '弘仁', '天長', '大同', '延暦', '宝亀', '淳和', '仁明', '貞観',
    '空海', '恵果', '不空', '善無', '龍樹', '最澄', '真済', '吉備',
    '徳一', '泰範', '智泉', '杲隣', '智周', '安然',
    '老子', '荘子', '孔子', '釈尊', '釈迦', '黄帝', '葉公', '許由', '伯夷',
    '青龍', '長安', '高野', '天竺', '五台', '東大', '神泉', '比叡',
    '大和', '山城', '河内', '摂津', '播磨',
    '譬喩', '故事', '象徴', '音写', '時代', '文献', '内容', '意味', '解釈',
    '一般', '比喩', '対比', '構造', '原典', '底本', '異同', '本文', '詳細',
    '概要', '記述', '背景', '出典', '出処', '引用', '言及', '言葉',
    '可能', '不能', '無理', '必須', '必要',
    '日本', '中国', '世界', '人間', '人類',
    '出家', '在俗', '俗世', '世俗', '帝室',
    '天皇', '皇帝', '天子', '国王', '太上', '王位',
    '父母', '兄弟', '夫婦', '子孫', '祖先',
    '麒麟', '鳳凰', '麒鱗', '蛟龍',
    '荘子', '詩経', '書経', '論語', '礼記', '法華', '涅槃',
    '大智', '瑜伽', '華厳', '理趣', '小雅', '春秋', '淮南',
    '左氏', '漢書', '史記', '三礼', '尚書', '毛詩', '楚辞',
    '一切', '一個', '一面',
    '対句', '並列',
}

# ====== 抽出パターン ======
RE_PAREN = re.compile(r'(([^()]{1,80}))')  # placeholder; overwritten below
RE_PAREN = re.compile(r'（([^（）]{1,80})）')  # 全角丸括弧
RE_2KAN = re.compile(r'[一-龥々]{2}')


def freq_score(count: int) -> float:
    if count <= 0:
        return 0.0
    return min(25.0, round(math.log10(count + 1) * 12, 2))


def doctrinal_score(source_tag: str) -> float:
    return {'seed_terms': 30.0, 'seed_sanskrit': 20.0, 'paren_doctrinal': 10.0}.get(source_tag, 0.0)


def ichiji_score(jukugo: str) -> float:
    s = sum(8.0 for c in jukugo if c in KAIMYO_ICHIJI)
    return min(16.0, s)


def aesthetic_score(jukugo: str) -> float:
    s = 0.0
    if len(set(jukugo)) < len(jukugo):
        return 0.0
    if all(c in KAIMYO_ICHIJI for c in jukugo):
        s += 2.0
    GOOD_PAIRS = {('光', '明'), ('浄', '信'), ('智', '慧'), ('慈', '悲'),
                  ('真', '常'), ('妙', '法'), ('清', '浄'), ('正', '覚'),
                  ('大', '悲'), ('法', '身'), ('菩', '提')}
    if len(jukugo) == 2 and (jukugo[0], jukugo[1]) in GOOD_PAIRS:
        s += 2.0
    return min(4.0, s)


def calc_kaimyo_score(jukugo: str, count: int, source_tag: str) -> dict:
    fs = freq_score(count)
    ds = doctrinal_score(source_tag)
    iss = ichiji_score(jukugo)
    aes = aesthetic_score(jukugo)
    return {
        'kaimyo_score': round(fs + ds + iss + aes, 2),
        'freq_score': fs,
        'doctrinal_score': ds,
        'ichiji_score': iss,
        'aesthetic_score': aes,
    }


def needs_review(scores: dict, source_tag: str) -> bool:
    if source_tag in ('seed_terms', 'seed_sanskrit'):
        return False
    return scores['kaimyo_score'] < 35


def corpus_id_of(filename: str) -> str:
    return Path(filename).stem


def extract_one_corpus(corpus_filename: str):
    cid = corpus_id_of(corpus_filename)
    src_path = SOURCE_DIR / corpus_filename
    terms_path = OUTPUT_DIR / f'index_{cid}_terms.json'
    sanskrit_path = OUTPUT_DIR / f'index_{cid}_sanskrit.json'

    if not src_path.exists():
        raise FileNotFoundError(f'{src_path} not found')
    if not terms_path.exists():
        raise FileNotFoundError(f'{terms_path} not found (run extract_terms_dict.py first)')
    if not sanskrit_path.exists():
        raise FileNotFoundError(f'{sanskrit_path} not found (run extract_sanskrit_dict.py first)')

    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f'{corpus_filename}: 想定 dict だが {type(data).__name__}')

    text = data.get('gendaigoyaku', '') or ''
    if not text:
        return None

    with open(terms_path, 'r', encoding='utf-8') as f:
        terms_idx = json.load(f)
    with open(sanskrit_path, 'r', encoding='utf-8') as f:
        sanskrit_idx = json.load(f)

    # === 起点 1: terms から kaimyo_suitable=true の語をシード ===
    seed_terms_set = set()
    seeds_from_terms = {}
    for e in terms_idx['entries']:
        if e.get('kaimyo_suitable'):
            t = e['term']
            seed_terms_set.add(t)
            seeds_from_terms[t] = {
                'sanskrit': e.get('sanskrit', ''),
                'definition': e.get('definition', ''),
                'kaimyo_chars': e.get('kaimyo_chars', []),
            }

    # === 起点 2: 梵語の漢訳対応 ===
    sanskrit_canonicals = {e['canonical'] for e in sanskrit_idx['entries']}
    seeds_from_sanskrit = defaultdict(list)
    for canon, jukugo_list in SANSKRIT_TO_KAIMYO_JUKUGO.items():
        if canon in sanskrit_canonicals:
            for j in jukugo_list:
                if j not in seed_terms_set:
                    seeds_from_sanskrit[j].append(canon)

    # === 起点 3 + occurrence 走査 ===
    paren_table = defaultdict(lambda: {'occurrences': []})

    # 1) 全文走査（シード語の出現箇所を捕捉）
    for jukugo in (seed_terms_set | set(seeds_from_sanskrit.keys())):
        start = 0
        while True:
            p = text.find(jukugo, start)
            if p < 0:
                break
            ctx_s = max(0, p - 30)
            ctx_e = min(len(text), p + len(jukugo) + 30)
            ctx = text[ctx_s:ctx_e].replace('\n', ' ')
            paren_table[jukugo]['occurrences'].append({
                'corpus_id': cid,
                'context': ctx,
                'context_position': p,
                'matched_in': 'corpus_full',
            })
            start = p + len(jukugo)

    # 2) 括弧書き内の 2 字漢語熟語（起点 3）
    for m in RE_PAREN.finditer(text):
        content = m.group(1)
        seen_in_paren = set()
        for k in RE_2KAN.findall(content):
            if k in KAIMYO_NOISE:
                continue
            if k in seed_terms_set or k in seeds_from_sanskrit:
                continue
            if k not in DOCTRINAL_2CHAR_WHITELIST:
                continue
            if k in seen_in_paren:
                continue
            seen_in_paren.add(k)
            ctx_s = max(0, m.start() - 20)
            ctx_e = min(len(text), m.end() + 20)
            ctx = text[ctx_s:ctx_e].replace('\n', ' ')
            paren_table[k]['occurrences'].append({
                'corpus_id': cid,
                'context': ctx,
                'context_position': m.start(),
                'matched_in': 'paren_doctrinal',
            })

    return {
        'corpus_id': cid,
        'corpus_filename': corpus_filename,
        'gendaigoyaku_length': len(text),
        'paren_table': paren_table,
        'seed_terms_set': seed_terms_set,
        'seeds_from_terms': seeds_from_terms,
        'seeds_from_sanskrit': seeds_from_sanskrit,
    }


def build_doc(corpus_filename: str, gendaigoyaku_length: int, ext: dict) -> dict:
    paren_table = ext['paren_table']
    seed_terms_set = ext['seed_terms_set']
    seeds_from_terms = ext['seeds_from_terms']
    seeds_from_sanskrit = ext['seeds_from_sanskrit']

    all_jukugo = set(paren_table.keys()) | seed_terms_set | set(seeds_from_sanskrit.keys())
    entries = []
    for j in sorted(all_jukugo):
        occs = paren_table.get(j, {}).get('occurrences', [])
        if j in seed_terms_set:
            source_tag = 'seed_terms'
        elif j in seeds_from_sanskrit:
            source_tag = 'seed_sanskrit'
        else:
            source_tag = 'paren_doctrinal'
        scores = calc_kaimyo_score(j, len(occs), source_tag)
        review = needs_review(scores, source_tag)
        seed_meta = seeds_from_terms.get(j, {})
        sanskrit_origins = seeds_from_sanskrit.get(j, [])
        entries.append({
            'jukugo': j,
            'source_tag': source_tag,
            'sanskrit_origins': sanskrit_origins,
            'seed_definition': seed_meta.get('definition', ''),
            'seed_sanskrit': seed_meta.get('sanskrit', ''),
            'kaimyo_chars': [c for c in j if c in KAIMYO_ICHIJI],
            **scores,
            'needs_human_review': review,
            'occurrence_count': len(occs),
            'occurrences': occs,
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], -e['kaimyo_score'], e['jukugo']))

    return {
        'schema_version': '1.2',
        'category': '戒名向け熟語索引',
        'source_corpus': corpus_filename,
        'corpus_type': 'dict',
        'extraction_field': 'gendaigoyaku',
        'generated_at': str(date.today()),
        'extraction_strategy': '起点 1（密教教学用語の戒名適合 11 語）+ 起点 2（梵語の漢訳対応）+ 起点 3（補注内 2 字漢語熟語のホワイトリスト抽出）',
        'scoring_rule': 'kaimyo_score = freq(log10×12, 上限25) + doctrinal(seed_terms=30 / seed_sanskrit=20 / paren_doctrinal=10) + ichiji(KAIMYO_ICHIJI 含字数 × 8, 上限16) + aesthetic(美字構成・最大4)',
        'review_policy': 'needs_human_review=true の語は kaimyo-app 連携前に専門家校閲を要する',
        'dictionary_sizes': {
            'kaimyo_ichiji': len(KAIMYO_ICHIJI),
            'sanskrit_to_kaimyo_jukugo': len(SANSKRIT_TO_KAIMYO_JUKUGO),
            'doctrinal_2char_whitelist': len(DOCTRINAL_2CHAR_WHITELIST),
            'kaimyo_noise': len(KAIMYO_NOISE),
        },
        'gendaigoyaku_length': gendaigoyaku_length,
        'summary': {
            'unique_terms': len(entries),
            'unique_jukugo': len(entries),
            'total_occurrences': sum(e['occurrence_count'] for e in entries),
            'seed_terms_count': sum(1 for e in entries if e['source_tag'] == 'seed_terms'),
            'seed_sanskrit_count': sum(1 for e in entries if e['source_tag'] == 'seed_sanskrit'),
            'paren_doctrinal_count': sum(1 for e in entries if e['source_tag'] == 'paren_doctrinal'),
            'needs_review_count': sum(1 for e in entries if e['needs_human_review']),
            'matched_jukugo_count': sum(1 for e in entries if e['occurrence_count'] > 0),
        },
        'entries': entries,
    }


def write_doc(doc: dict, corpus_filename: str) -> Path:
    cid = corpus_id_of(corpus_filename)
    out_path = OUTPUT_DIR / f'index_{cid}_kaimyo.json'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(doc, ensure_ascii=False, indent=2).encode('utf-8')
    payload = payload.rstrip(b'\x00')
    with open(out_path, 'wb') as f:
        f.write(payload)
    raw = out_path.read_bytes()
    nul = b'\x00'
    nulls = len(raw) - len(raw.rstrip(nul))
    if nulls != 0:
        raise AssertionError(f'NULL byte tail detected in {out_path}: {nulls}')
    return out_path


def process(corpus_filename: str, *, verbose=True):
    res = extract_one_corpus(corpus_filename)
    if res is None:
        if verbose:
            print(f'[SKIP] {corpus_filename}: gendaigoyaku が空')
        return None
    doc = build_doc(corpus_filename, res['gendaigoyaku_length'], res)
    out_path = write_doc(doc, corpus_filename)
    if verbose:
        s = doc['summary']
        print(f"[OK] {corpus_filename:<28s} -> {out_path.name}")
        print(f"     gendaigoyaku={doc['gendaigoyaku_length']:,} 字"
              f" / unique={s['unique_jukugo']}"
              f" / matched={s['matched_jukugo_count']}"
              f" / occ={s['total_occurrences']}"
              f" (seed_terms={s['seed_terms_count']} / seed_sanskrit={s['seed_sanskrit_count']} / paren={s['paren_doctrinal_count']})"
              f" / review={s['needs_review_count']}")
        top = [e for e in doc['entries'] if e['occurrence_count'] > 0][:5]
        if top:
            top_str = ', '.join(f"{e['jukugo']}={e['occurrence_count']}({e['kaimyo_score']:.0f})" for e in top)
            print(f"     top: {top_str}")
    return doc


def main():
    ap = argparse.ArgumentParser(description='dict 型著作向け 戒名向け熟語索引生成')
    ap.add_argument('--corpus', required=True,
                    help="対象著作 (例: nikyo-ron.json) または 'all'")
    args = ap.parse_args()
    targets = DICT_CORPUS_LIST if args.corpus == 'all' else [args.corpus]
    print('=' * 70)
    print(f'extract_kaimyo_jukugo_dict.py — 対象 {len(targets)} 著作')
    print('=' * 70)
    for fn in targets:
        try:
            process(fn)
        except Exception as e:
            print(f'[ERR] {fn}: {e}', file=sys.stderr)
            raise
    print('\n完了。')


if __name__ == '__main__':
    main()
