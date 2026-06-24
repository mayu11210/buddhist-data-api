# -*- coding: utf-8 -*-
import json,sys,shutil,os
REPO='/sessions/affectionate-sweet-keller/mnt/buddhist-data-api'
MJ=REPO+'/data/indices/motifs.json'
OUT='/sessions/affectionate-sweet-keller/mnt/outputs'
APPLY='--apply' in sys.argv
corpus=json.load(open(REPO+'/data/kukai/dainichikyo-sho-vol16.json'))
para={p['id']:p for p in corpus['paragraphs']}
plan=json.load(open('motif_plan.json'))
rnames={1:'金剛手の偈問への答〜五事〜秘密漫荼羅の法と作法 k004-k015',
2:'三部曼荼羅〔仏部・蓮華部・金剛部・不動尊・仏母〕 k016-k026',
3:'尊別印相〔仏頂・菩薩部・釈迦・五仏頂・諸天・文殊・除蓋障・地蔵・虚空蔵〕 k027-k040',
4:'入秘密漫荼羅品第十二〔阿闍梨資格・字観で業煩悩を焼く・三昧耶・末代の戒め〕 k042-k050',
5:'入秘密漫荼羅位品第十三 前半〔三種加持・毘盧遮那＝日・等至三昧・大悲胎蔵荘厳〕 k052-k061',
6:'入秘密漫荼羅位品第十三 後半〔音声偈・本不生阿字・内心漫荼羅・証入〕 k062-k071'}

def build_tags(p):
    t=['category:密教教学','出典:大日経疏 巻第十六','引用形式:典籍曰く']
    t+=['密教:'+x for x in p['密教']]
    t.append('主題:'+p['主題'])
    t+=['文体:'+x for x in p['文体']]
    t+=['典故:'+x for x in p['典故']]
    if p['core']: t.append('一句性:核心')
    return t

d=json.load(open(MJ))
ms=d['motifs']; st=d['stats']
ids={m['id'] for m in ms}
# ---- rollback canary asserts ----
m506=next(m for m in ms if m['id']=='m506')
assert '引用形式:典籍曰く' in m506['tags'], 'CANARY m506 typecast lost'
m3623=next(m for m in ms if m['id']=='m3623')
assert '連動:sg08' in m3623['tags'], 'CANARY vol15 retrofit lost (m3623 sg08)'
assert sum(1 for m in ms if m.get('source',{}).get('corpus')=='dainichikyo-sho-vol15')==78, 'vol15 count != 78'
assert st['total_motifs']==len(ms)==3709, 'total mismatch pre'
assert ms[-1]['id']=='m3678', 'last id != m3678'
print('[canary] m506 典籍曰く OK / vol15 retrofit m3623 sg08 OK / vol15=78 / total=3709 / last=m3678')

ks_all=sorted(plan, key=lambda x:int(x[1:]))
# verify plan m-ids contiguous from m3679
exp=3679
for k in ks_all:
    assert plan[k]['mid']=='m%d'%exp, ('plan mid gap',k,plan[k]['mid'])
    assert plan[k]['mid'] not in ids, ('id reuse',plan[k]['mid'])
    exp+=1
print('[plan] 66 mids m3679-m%d contiguous, none reused'%(exp-1))

added_total=0
for r in range(1,7):
    rks=[k for k in ks_all if plan[k]['round']==r]
    # backup pre-round
    if APPLY:
        shutil.copy(MJ, OUT+'/motifs_backup_pre_vol16_r%d.json'%r)
    newms=[]
    for k in rks:
        p=plan[k]; cp=para[k]
        kk=cp['kakikudashi']; gd=cp['gendaigoyaku']
        # checks: half-width parens
        assert '(' not in kk and ')' not in kk, ('half-paren kk',k)
        assert '(' not in gd and ')' not in gd, ('half-paren gd',k)
        m={'id':p['mid'],
           'source':{'corpus':'dainichikyo-sho-vol16','著作名':'大日経疏 巻第十六','著者':'善無畏口述・一行筆受','節':p['sec'],'段落':k},
           'text_kakikudashi':kk,'text_gendaigoyaku':gd,'tags':build_tags(p)}
        newms.append(m)
    ms.extend(newms)
    added_total+=len(newms)
    # stats update
    st['total_motifs']=len(ms)
    st['kakikudashi_chars_total']+=sum(len(m['text_kakikudashi']) for m in newms)
    st['gendaigoyaku_chars_total']+=sum(len(m['text_gendaigoyaku']) for m in newms)
    st['from_corpus_dainichikyo-sho-vol16']=st.get('from_corpus_dainichikyo-sho-vol16',0)+len(newms)
    st['motifs_without_gendai_gabun_intentional']['dainichikyo-sho-vol16_round%d'%r]=(
        '大日経疏 巻第十六 R%d motif（%s-%s）gabun 意図的未設定（善無畏口述/一行筆受＝非空海・経典注釈系・全件 典籍曰く・巻第二〜十五 同運用）'%(r,newms[0]['id'],newms[-1]['id']))
    # 篇別内訳 (cumulative)
    st['篇別内訳']['dainichikyo-sho-vol16']={'著作名':'大日経疏 巻第十六','著者':'善無畏口述・一行筆受',
        'motif数':st['from_corpus_dainichikyo-sho-vol16'],'id範囲':'m3679-%s'%newms[-1]['id'],
        '内訳':'本文66段（k004-k040／k042-k050／k052-k071）・構造段 k001/k002/k003/k041/k051 除く・1段=1motif・束ねなし。3品（秘密漫荼羅品第十一之余／入秘密漫荼羅品第十二／入秘密漫荼羅位品第十三）。核心15件。'}
    # schema_history per round
    d['schema_history'].append({'version':'0.2','date':'2026-06-24',
        'summary':'大日経疏 巻第十六 Phase3 motif 抽出 第%dラウンド（%s・%d件 %s-%s）。引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・1段=1motif・束ねなし。'%(r,rnames[r],len(newms),newms[0]['id'],newms[-1]['id']),
        'origin':'dainichikyo-sho-vol16_round%d'%r})
    print('[R%d] +%d motif %s-%s (total now %d)'%(r,len(newms),newms[0]['id'],newms[-1]['id'],len(ms)))

# ---- final verification ----
assert added_total==66
assert st['total_motifs']==len(ms)==3709+66==3775
mids=[m['id'] for m in ms if m['id'].startswith('m')]
nums=sorted(int(x[1:]) for x in mids)
assert nums==list(range(1,3745)), ('m-id not contiguous 1-3744', nums[0], nums[-1], len(nums))
assert len(set(mids))==len(mids), 'dup m-id'
assert sum(1 for m in ms if m['id'].startswith('sg'))==31, 'sg count changed'
# required fields + verbatim
for m in ms[-66:]:
    for f in ['id','source','text_kakikudashi','text_gendaigoyaku','tags']:
        assert f in m and m[f]!=''
    assert m['source']['段落'] in para
    assert m['text_kakikudashi']==para[m['source']['段落']]['kakikudashi']
    assert m['text_gendaigoyaku']==para[m['source']['段落']]['gendaigoyaku']
    assert '(' not in m['text_kakikudashi'] and ')' not in m['text_kakikudashi']
    assert '(' not in m['text_gendaigoyaku'] and ')' not in m['text_gendaigoyaku']
# stats recompute drift zero
kk=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms)
gd=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms)
assert kk==st['kakikudashi_chars_total'], ('kk drift',kk,st['kakikudashi_chars_total'])
assert gd==st['gendaigoyaku_chars_total'], ('gd drift',gd,st['gendaigoyaku_chars_total'])
assert st['from_corpus_dainichikyo-sho-vol16']==66
assert st['famous_phrases']==31
print('[final] total=3775 / m1-m3775 contiguous / sg=31 / kk,gd drift 0 / from_corpus_vol16=66 / verbatim OK / half-paren 0')
print('[final] schema_history len:', len(d['schema_history']))

if APPLY:
    txt=json.dumps(d, ensure_ascii=False, indent=1)
    open(MJ,'w',encoding='utf-8').write(txt)
    # NUL + reparse
    raw=open(MJ,encoding='utf-8').read()
    assert raw.count('\x00')==0
    json.loads(raw)
    print('[APPLY] written. NUL0, reparse OK, bytes', len(raw.encode('utf-8')))
else:
    print('[DRYRUN] no write')
