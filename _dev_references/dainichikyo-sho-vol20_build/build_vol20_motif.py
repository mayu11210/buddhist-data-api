# -*- coding: utf-8 -*-
import json, sys, re, shutil, os
REPO='/sessions/pensive-jolly-brahmagupta/mnt/buddhist-data-api'
B=REPO+'/_dev_references/dainichikyo-sho-vol20_build'
MP=REPO+'/data/indices/motifs.json'
APPLY='--apply' in sys.argv

corpus=json.load(open(REPO+'/data/kukai/dainichikyo-sho-vol20.json'))
pmap={p['id']:p for p in corpus['paragraphs']}
tab={**json.load(open(B+'/motif_table_g1.json')),**json.load(open(B+'/motif_table_g2.json'))}
mmap=json.load(open(B+'/mmap.json'))
STRUCT={'k001','k002','k003','k028','k039','k050','k067'}
order=[p['id'] for p in corpus['paragraphs'] if p['id'] not in STRUCT]
assert order==sorted(order), 'order not sorted'
assert len(order)==83

COMMON=['category:密教教学','出典:大日経疏 巻第二十','引用形式:典籍曰く']
new_motifs=[]
for pid in order:
    p=pmap[pid]; e=tab[pid]
    tags=list(COMMON)+list(e['tags'])
    if e.get('core'): tags.append('一句性:核心')
    # de-dup preserve order
    seen=set(); tg=[t for t in tags if not (t in seen or seen.add(t))]
    m={"id":mmap[pid],
       "source":{"corpus":"dainichikyo-sho-vol20","著作名":"大日経疏 巻第二十","著者":"善無畏口述・一行筆受","節":p['section'],"段落":pid},
       "text_kakikudashi":p['kakikudashi'],
       "text_gendaigoyaku":p['gendaigoyaku'],
       "tags":tg}
    new_motifs.append(m)

# ---- load main ----
d=json.load(open(MP))
ms=d['motifs']; st=d['stats']
# PRE asserts (rollback detection / consistency)
assert st['total_motifs']==len(ms)==3989, ('pre total',st['total_motifs'],len(ms))
kk0=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms)
gd0=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms)
assert kk0==st['kakikudashi_chars_total'] and gd0==st['gendaigoyaku_chars_total'], 'pre stats drift'
existing_ids={m['id'] for m in ms}
m506=next(m for m in ms if m['id']=='m506'); assert '引用形式:典籍曰く' in m506['tags'], 'm506 rollback'
m549=next(m for m in ms if m['id']=='m549'); assert '連動:sg08' in m549['tags'], 'm549 anchor rollback'
m719=next(m for m in ms if m['id']=='m719'); assert '連動:sg27' in m719['tags'], 'm719 anchor rollback'
assert st.get('from_corpus_dainichikyo-sho-vol19')==81, 'vol19 rollback'
assert st.get('from_corpus_dainichikyo-sho-vol18')==45, 'vol18 rollback'
assert 'from_corpus_dainichikyo-sho-vol20' not in st, 'vol20 already present'
# new ids unused + contiguous m3959-m4041
nids=[m['id'] for m in new_motifs]
assert all(i not in existing_ids for i in nids), 'id collision'
assert nids==['m%d'%n for n in range(3959,4042)], 'new ids not contiguous m3959-m4041'
# content checks on new motifs
for m in new_motifs:
    blob=''.join(m['tags'])
    assert '(' not in (m['text_kakikudashi']+m['text_gendaigoyaku']) and ')' not in (m['text_kakikudashi']+m['text_gendaigoyaku']), ('halfparen',m['id'])
    assert '主題:本生' not in m['tags'], ('本生',m['id'])
    assert '潅' not in blob, ('潅',m['id'])
    assert '引用形式:典籍曰く' in m['tags'] and '引用形式:大師曰く' not in m['tags'] and 'category:大師御言葉' not in m['tags'], ('attribution',m['id'])
    for f in ('id','source','text_kakikudashi','text_gendaigoyaku','tags'): assert m[f], ('field',m['id'],f)
    # verbatim: 節==corpus section, text==corpus
    assert m['source']['節']==pmap[m['source']['段落']]['section'], ('section',m['id'])
    assert m['text_kakikudashi']==pmap[m['source']['段落']]['kakikudashi'], ('kk verbatim',m['id'])
    assert m['text_gendaigoyaku']==pmap[m['source']['段落']]['gendaigoyaku'], ('gd verbatim',m['id'])

# ---- apply ----
ms2=ms+new_motifs
addkk=sum(len(m['text_kakikudashi'].replace('\n','')) for m in new_motifs)
addgd=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in new_motifs)
core=sum(1 for m in new_motifs if '一句性:核心' in m['tags'])
st['total_motifs']=len(ms2)
st['kakikudashi_chars_total']=kk0+addkk
st['gendaigoyaku_chars_total']=gd0+addgd
st['from_corpus_dainichikyo-sho-vol20']=83
st['篇別内訳']['dainichikyo-sho-vol20']={
  "著作名":"大日経疏 巻第二十","著者":"善無畏口述・一行筆受","motif数":83,"id範囲":"m3959-m4041",
  "内訳":"本文 k004-k090（首題k001/撰号k002/品題k003,k028,k039,k050,k067 は motif 化せず・囑累品の種子字段 k080＝doc 埋込画像 image1.png 本文転記 を motif 化）・1段=1motif・束ねなし。世出世護摩法品第二十七之余 k004-k027（m3959-m3982・24件）／本尊三昧品第二十八 k029-k038（m3983-m3992・10件）／無相三昧品第二十九 k040-k049（m3993-m4002・10件）／世出世持誦品第三十 k051-k066（m4003-m4018・16件）／囑累品第三十一 k068-k090〔k080 種子字含む〕（m4019-m4041・23件）。核心%d件。新タグ値4＝主題:不放逸/主題:付属/主題:邪正/典故:普賢観経（既存軸内）。**T1796 全20巻 最終巻 motif 抽出完了**。"%core}
st['motifs_without_gendai_gabun_intentional']['dainichikyo-sho-vol20_round_all']="大日経疏 巻第二十 motif（m3959-m4041・83件）gabun 意図的未設定（善無畏口述/一行筆受＝非空海・経典注釈系・全件 典籍曰く・巻第二〜十九 同運用）"
d['schema_history'].append({"version":"0.2","date":"2026-06-25","summary":"大日経疏 巻第二十（dainichikyo-sho-vol20・善無畏口述/一行筆受＝非空海・T1796 全20巻の最終巻）Phase3 motif 抽出 round_all：本文82段＋囑累品の種子字段 k080（doc 埋込画像 image1.png 本文転記・vol18 precedent）を m3959-m4041 の83件に抽出。全件 引用形式:典籍曰く・大師系非付与・source に著者保持・1段=1motif（束ねなし）・gabun 意図的未設定・節は corpus paragraphs[].section から直接取得し節==corpus.section を全83件 assert。共通タグ category:密教教学/出典:大日経疏 巻第二十/引用形式:典籍曰く。新タグ値4（既存軸内）＝主題:不放逸/主題:付属/主題:邪正/典故:普賢観経。一句性:核心 %d件。連動軸 retrofit は完走後。total 3989→%d。"%(core,len(ms2)),"origin":"dainichikyo-sho-vol20_round_all"})
d['motifs']=ms2
d['stats']=st

# ---- POST asserts ----
out=json.dumps(d,ensure_ascii=False,indent=1)
assert out.count('\x00')==0
d2=json.loads(out)  # reparse
ms3=d2['motifs']
assert d2['stats']['total_motifs']==len(ms3)==4072, ('post total',len(ms3))
# m-id contiguity m1..m4041 + sg
nums=sorted(int(m['id'][1:]) for m in ms3 if re.fullmatch(r'm\d+',m['id']))
assert nums==list(range(1,4042)), 'm-id gap/dup'
assert len(nums)==len(set(nums))
sgc=[m for m in ms3 if m['id'].startswith('sg')]
assert len(sgc)==31, ('sg',len(sgc))
# recompute drift
kk2=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms3)
gd2=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms3)
assert kk2==d2['stats']['kakikudashi_chars_total'] and gd2==d2['stats']['gendaigoyaku_chars_total'], 'post drift'
assert d2['stats']['from_corpus_dainichikyo-sho-vol20']==83
assert d2['stats']['from_corpus_dainichikyo-sho-vol19']==81  # rollback guard
assert d2['schema_version']=='0.2'
assert len(d2['schema_history'])==294, ('schema_history',len(d2['schema_history']))
# all vol20 motifs 典籍曰く / no 大師系 / half-paren 0
v20=[m for m in ms3 if m['source'].get('corpus')=='dainichikyo-sho-vol20']
assert len(v20)==83
for m in v20:
    assert '引用形式:典籍曰く' in m['tags'] and 'category:大師御言葉' not in m['tags']
print('=== DRY-RUN ALL ASSERTS PASS ===' if not APPLY else '=== APPLY: ALL ASSERTS PASS ===')
print('new motifs:',len(new_motifs),'core:',core,'addkk:',addkk,'addgd:',addgd)
print('total 3989 ->',len(ms2),'kk',kk0,'->',st['kakikudashi_chars_total'],'gd',gd0,'->',st['gendaigoyaku_chars_total'])
print('new tag values:', sorted({t for m in new_motifs for t in m['tags'] if t.split(':')[0] in('主題','典故')} - {'主題:菩提','主題:菩提心'}))
if APPLY:
    shutil.copy(MP, B+'/motifs_backup_pre_vol20_motif.json')
    open(MP,'w',encoding='utf-8').write(out)
    print('WROTE', MP, 'backup at motifs_backup_pre_vol20_motif.json')
else:
    print('(dry-run; no write)')
