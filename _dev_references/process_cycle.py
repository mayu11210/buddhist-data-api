#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""process_cycle.py — 注 raw 取込 1 サイクルの完全自動化パイプライン

paste.txt を入力して以下を一気通貫で実行：
1. 篇分割（【篇名】区切り）
2. 各篇を JSON の篇名で idx 解決
3. 各項目を書き下しと突合し、自動判定で漢字置換 or raw 維持
4. raw 末尾に追記（書込済み・bash 経由相当）
5. commit_message.txt 更新
6. 結果サマリを標準出力

Usage:
    python3 _dev_references/process_cycle.py --paste /tmp/paste.txt

判定ロジック（シンプル）：
  完全一致／語幹一致 → raw のまま
  VARIANTS 異体字 → 書き下し字に置換
  1 字違い近接（漢字→漢字）→ 書き下し字に置換
  1 字違い近接（漢字→ひら/カナ/句読点/数字）→ raw のまま（活用語尾棄却）
  一致なし → raw のまま
"""
import argparse
import json
import re
import sys
from pathlib import Path

VARIANTS = {
    '灌':'潅','燈':'灯','毗':'毘','廈':'厦','島':'嶋','藪':'薮','辯':'弁',
    '鳧':'鳬','聰':'聡','飧':'飡','舶':'舳','瀆':'涜','羲':'曦','秉':'乗',
    '落':'洛','葱':'䓗','雞':'鷄','烏':'鳥','鉄':'䥫','澮':'浍','嬀':'媯',
    '舞':'儛','囗':'口',
}
# 双方向化
VARIANTS_BI = dict(VARIANTS)
VARIANTS_BI.update({v:k for k,v in VARIANTS.items()})

NUM_RE = re.compile(r'^([一二三四五六七八九〇十百]+)([\s\u3000]+)(\S+?)([\s\u3000]+)(.*)$')
HEAD_RE = re.compile(r'^(【[^】]+】)$', re.MULTILINE)

def is_kanji(ch):
    return '\u3400' <= ch <= '\u9fff' or '\uf900' <= ch <= '\ufaff'

def strip_ruby(s):
    s = re.sub(r'（[ぁ-んァ-ン・ー\s\u3000]+）', '', s)
    s = re.sub(r'《[^》]+》', '', s)
    return s.strip()

def auto_decide(headword, kakikudashi):
    """戻り値: ('keep', None) or ('replace', new_headword, raw_ch, kak_ch)"""
    hw = strip_ruby(headword)
    if hw in kakikudashi:
        return ('keep', None, None, None)
    # 語幹一致
    m = re.match(r'^(.*?[^\u3040-\u309f\u30a0-\u30ff])([\u3040-\u309f]+)$', hw)
    if m and len(m.group(1)) >= 2 and m.group(1) in kakikudashi:
        return ('keep', None, None, None)
    # VARIANTS
    for raw_ch, kak_ch in VARIANTS_BI.items():
        if raw_ch in hw:
            v = hw.replace(raw_ch, kak_ch)
            if v in kakikudashi:
                return ('replace', v, raw_ch, kak_ch)
    # 1 字違い近接
    if len(hw) >= 2:
        for i in range(len(hw)):
            before, after = hw[:i], hw[i+1:]
            if after:
                pat = re.compile(re.escape(before) + r'([^\s\u3000\n])' + re.escape(after))
            else:
                if not before: continue
                pat = re.compile(re.escape(before) + r'([^\s\u3000\n])')
            mm = pat.search(kakikudashi)
            if mm:
                kak_ch = mm.group(1)
                raw_ch = hw[i]
                if kak_ch == raw_ch:
                    continue
                # 漢字→漢字なら置換、それ以外は raw 維持（活用語尾・句読点棄却）
                if is_kanji(kak_ch) and is_kanji(raw_ch):
                    return ('replace', before + kak_ch + after, raw_ch, kak_ch)
                return ('keep', None, None, None)
    return ('keep', None, None, None)

_DRY = False

def process(paste_path, raw_path, json_path, cmsg_path, repo_root):
    text = Path(paste_path).read_text(encoding='utf-8')
    parts = HEAD_RE.split(text)
    sections = []
    if parts[0].strip():
        sections.append(('（無題）', parts[0]))
    for i in range(1, len(parts), 2):
        h = parts[i]
        b = parts[i+1] if i+1 < len(parts) else ''
        sections.append((h, b))

    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
    title_to_idx = {}
    for i, e in enumerate(data):
        title_to_idx[e['篇名']] = i

    def normalize_title(s):
        """ひらがな・カタカナ・空白・記号を除いて漢字のみにし、VARIANTS で正規化"""
        out = ''.join(c for c in s if is_kanji(c))
        for raw, kak in VARIANTS_BI.items():
            out = out.replace(raw, kak)
        return out

    norm_to_idx = {normalize_title(t): i for t, i in title_to_idx.items()}

    def find_idx(header):
        # 【〔注〕 X】や【X（続き）】 → X を抽出
        h = header.strip('【】')
        h = re.sub(r'^〔注〕\s*', '', h)
        h = re.sub(r'（[^）]+）$', '', h).strip()
        nh = normalize_title(h)
        if not nh:
            return None
        # 完全一致優先
        if nh in norm_to_idx:
            return norm_to_idx[nh]
        # 双方向部分一致（最長を採用）
        cands = []
        for nt, i in norm_to_idx.items():
            if nh in nt or nt in nh:
                cands.append((min(len(nh), len(nt)), i))
        if cands:
            cands.sort(reverse=True)
            return cands[0][1]
        return None

    cycle_summary = []
    raw_append_blocks = []

    for header, body in sections:
        if not body.strip():
            continue
        idx = find_idx(header)
        if idx is None:
            cycle_summary.append(f'WARN: 篇名「{header}」未解決・スキップ')
            continue
        entry = data[idx]
        kak = '\n'.join(p.get('kakikudashi','') for p in entry.get('ページ',[]))

        replace_count = 0
        keep_count = 0
        replacements = []
        new_lines = []
        for line in body.split('\n'):
            line = line.rstrip()
            if not line:
                new_lines.append('')
                continue
            m = NUM_RE.match(line)
            if not m:
                # 続き行・パース不可：そのまま
                new_lines.append(line)
                continue
            num, sp1, hw, sp2, rest = m.groups()
            decision, new_hw, raw_ch, kak_ch = auto_decide(hw, kak)
            if decision == 'replace' and new_hw != hw:
                new_lines.append(f'{num}{sp1}{new_hw}{sp2}{rest}')
                replace_count += 1
                replacements.append(f'注{num} {hw}→{new_hw} ({raw_ch}↔{kak_ch})')
            else:
                new_lines.append(line)
                keep_count += 1
        # 末尾改行
        while new_lines and new_lines[-1] == '':
            new_lines.pop()
        block_body = '\n'.join(new_lines) + '\n'
        meta = f'\n【{entry["篇名"]}】\n（idx={idx}・訂正 {replace_count} 件）\n\n'
        raw_append_blocks.append(meta + block_body)
        cycle_summary.append(f'idx={idx} {entry["篇名"]}: 訂正 {replace_count} / そのまま {keep_count}')
        for r in replacements:
            cycle_summary.append(f'  ・{r}')

    # raw 末尾追記
    raw_data = Path(raw_path).read_bytes()
    append_text = ''.join(raw_append_blocks)
    new_raw = raw_data + append_text.encode('utf-8')
    if not _DRY:
        Path(raw_path).write_bytes(new_raw)
        verify = Path(raw_path).read_bytes()
        nulls = len(verify) - len(verify.rstrip(b'\x00'))
    else:
        verify = new_raw
        nulls = 0
        print('===== DRY RUN: raw 追記内容（実書込なし）=====')
        print(append_text)
        print('===== DRY RUN: 追記内容ここまで =====\n')

    # commit_message 自動生成
    total_replace = sum(int(s.split('訂正 ')[1].split(' /')[0]) for s in cycle_summary if '訂正 ' in s and ' / ' in s)
    idx_list = [s.split(' ',1)[0] for s in cycle_summary if s.startswith('idx=')]  # idx=N のみ
    cmsg_lines = [
        f'性霊集 注 raw 追記：{", ".join(idx_list)}（訂正 {total_replace} 件）',
        '',
    ]
    cmsg_lines.extend(cycle_summary)
    if not _DRY:
        Path(cmsg_path).write_text('\n'.join(cmsg_lines) + '\n', encoding='utf-8')
    else:
        print('===== DRY RUN: commit_message 内容 =====')
        print('\n'.join(cmsg_lines))
        print('===== DRY RUN: commit_message ここまで =====\n')

    print('=' * 60)
    print('処理完了')
    print('=' * 60)
    for s in cycle_summary:
        print(s)
    print('-' * 60)
    print(f'raw 増分: {len(verify) - len(raw_data)} bytes / NULL バイト: {nulls}')
    print(f'合計訂正: {total_replace} 件')
    print(f'commit_message.txt 行数: {len(cmsg_lines) + 1}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--paste', required=True)
    ap.add_argument('--raw', default='_dev_references/shoryoshu_gendaigoyaku_raw.txt')
    ap.add_argument('--json', default='data/kukai/shoryoshu_miyasaka.json')
    ap.add_argument('--cmsg', default='commit_message.txt')
    ap.add_argument('--dry', action='store_true', help='書込なし・追記内容を標準出力のみ')
    args = ap.parse_args()
    global _DRY
    _DRY = args.dry
    process(args.paste, args.raw, args.json, args.cmsg, '.')

if __name__ == '__main__':
    main()
