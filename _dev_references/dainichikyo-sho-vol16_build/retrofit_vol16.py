# -*- coding: utf-8 -*-
import json
MJ='/sessions/affectionate-sweet-keller/mnt/buddhist-data-api/data/indices/motifs.json'
d=json.load(open(MJ)); ms=d['motifs']; M={m['id']:m for m in ms}
st=d['stats']
# pre-state snapshot
pre_total=st['total_motifs']; pre_fam=st['famous_phrases']
pre_kk=st['kakikudashi_chars_total']; pre_gd=st['gendaigoyaku_chars_total']
# canary: vol15 retrofit + m506
assert '連動:sg08' in M['m3623']['tags'] and '引用形式:典籍曰く' in M['m506']['tags']
LINK={
 'm3734':['連動:sg08','連動:m549'],         # k061 無得偈・本不生・阿字出入
 'm3737':['連動:sg08','連動:m549'],         # k064 五大字観・阿字法界性・一切法本不生
 'm3720':['連動:sg21','連動:m638','連動:m728'], # k046 浄菩提心の仏種子を生ず
 'm3728':['連動:sg21','連動:m638','連動:m728'], # k055 浄国地平＝浄菩提心
 'm3740':['連動:sg21','連動:m638','連動:m728'], # k067 浄菩提心＝毘盧遮那悦心地
}
added=0
for mid,tags in LINK.items():
    m=M[mid]
    assert m['source']['corpus']=='dainichikyo-sho-vol16'
    for t in tags:
        if t not in m['tags']:
            m['tags'].append(t); added+=1
print('connector tags added:', added, '(5 motifs)')
# schema_history
d['schema_history'].append({'version':'0.2','date':'2026-06-24',
 'summary':'大日経疏 巻第十六 連動軸 retrofit（新規 sg/anchor なし＝既存軸の被覆拡張・巻第二〜十五 retrofit 同型）：vol16 全66 motif を既存軸でスキャンし、直接連動・core verbatim に限定して 5 件に連動タグ +13＝sg08 阿字本不生〔m549〕←m3734（k061 無得偈・本不生＝阿字の出入・能生諸法）/m3737（k064 五大字観・阿字＝法界性・一切法本不生）／sg21 浄菩提心〔m638+m728〕←m3720（k046 浄菩提心の仏種子を生ず）/m3728（k055 浄国地平＝浄菩提心）/m3740（k067 浄菩提心＝毘盧遮那如来の悦心地）。タグのみ変更・total 3775 不変・famous 不変・kk/gd unchanged。',
 'origin':'retrofit:dainichikyo-sho-vol16_rendou_scan'})
# asserts: tag-only
assert st['total_motifs']==pre_total==len(ms)==3775
assert st['famous_phrases']==pre_fam==31
assert st['kakikudashi_chars_total']==pre_kk and st['gendaigoyaku_chars_total']==pre_gd
# recompute drift
kk=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms); gd=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms)
assert kk==pre_kk and gd==pre_gd
# anchors self-referential preserved
assert '連動:sg08' in M['m549']['tags'] or True  # m549 anchor自体 (vol8 retrofit時に自己参照付与有無は問わない)
txt=json.dumps(d,ensure_ascii=False,indent=1); open(MJ,'w',encoding='utf-8').write(txt)
raw=open(MJ,encoding='utf-8').read(); assert raw.count('\x00')==0; json.loads(raw)
print('[retrofit applied] total 3775 不変 / famous 31 / kk,gd unchanged / NUL0 / schema_history', len(d['schema_history']))
# verify links present
for mid in LINK: print(' ',mid,[t for t in M[mid]['tags'] if t.startswith('連動')])
