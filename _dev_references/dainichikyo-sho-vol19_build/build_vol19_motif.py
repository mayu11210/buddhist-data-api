import json,sys,shutil
APPLY='--apply' in sys.argv
MP='data/indices/motifs.json'
d=json.load(open(MP,encoding='utf-8'))
ms=d['motifs']; s=d['stats']
cor=json.load(open('data/kukai/dainichikyo-sho-vol19.json',encoding='utf-8'))
T=json.load(open('_dev_references/dainichikyo-sho-vol19_build/motif_table_refined.json',encoding='utf-8'))

# body segments in order
body=[p for p in cor['paragraphs'] if p['section_major'] not in ('首題','撰号') and not p['section_major'].startswith('品題')]
assert len(body)==81,len(body)
# pre-state captures for rollback asserts
pre_total=len(ms); pre_kk=s['kakikudashi_chars_total']; pre_gd=s['gendaigoyaku_chars_total']
pre_famous=s['famous_phrases']; pre_sg=sum(1 for m in ms if m['id'].startswith('sg'))
# rollback anchors (existing motifs must be untouched)
def findm(mid): return next(m for m in ms if m['id']==mid)
assert '引用形式:典籍曰く' in findm('m506')['tags'], "m506 typ籍曰く missing"
assert '連動:sg08' in findm('m549')['tags']
assert '連動:sg27' in findm('m719')['tags']
assert s.get('from_corpus_dainichikyo-sho-vol18')==45
assert findm('m3877')['source']['corpus']=='dainichikyo-sho-vol18'

start=3878
common3=["category:密教教学","出典:大日経疏 巻第十九","引用形式:典籍曰く"]
new=[]
add_kk=0; add_gd=0; core=0
for i,p in enumerate(body):
    mid=f"m{start+i}"
    assert not any(m['id']==mid for m in ms), "id collision "+mid
    kid=p['id']
    tags=T[kid]['tags']
    assert tags[:3]==common3, kid
    assert all('(' not in t and ')' not in t for t in tags)
    assert len(tags)==len(set(tags)), "dup tag "+kid
    kk=p['kakikudashi']; gd=p['gendaigoyaku']
    assert '(' not in kk and ')' not in kk and '(' not in gd and ')' not in gd
    m={"id":mid,"source":{"corpus":"dainichikyo-sho-vol19","著作名":"大日経疏 巻第十九",
        "著者":"善無畏口述・一行筆受","節":p['section'],"段落":kid},
        "text_kakikudashi":kk,"text_gendaigoyaku":gd,"tags":tags}
    new.append(m)
    add_kk+=len(kk.replace('\n','')); add_gd+=len(gd.replace('\n',''))
    if '一句性:核心' in tags: core+=1

print("new motifs:",len(new),"| m-id",new[0]['id'],"-",new[-1]['id'],"| 核心",core)
print("add_kk(excl nl):",add_kk,"add_gd(excl nl):",add_gd)

# verbatim assert: new kk concat per品 == corpus body concat
from itertools import groupby
sm={p['id']:p['section_major'] for p in body}
for major,grp in groupby(body,key=lambda x:x['section_major']):
    g=list(grp)
    a=''.join(x['kakikudashi'] for x in g)
    b=''.join(nm['text_kakikudashi'] for nm in new if nm['source']['段落'] in {x['id'] for x in g})
    assert a==b, "verbatim "+major
# 節==corpus section
for nm in new:
    kid=nm['source']['段落']
    csec=next(x['section'] for x in body if x['id']==kid)
    assert nm['source']['節']==csec, "節 mismatch "+kid
print("verbatim & 節==section: OK")

if APPLY:
    shutil.copy(MP,'_dev_references/dainichikyo-sho-vol19_build/motifs_backup_pre_vol19_motif.json')
    ms.extend(new)
    s['total_motifs']=len(ms)
    s['kakikudashi_chars_total']=pre_kk+add_kk
    s['gendaigoyaku_chars_total']=pre_gd+add_gd
    s['from_corpus_dainichikyo-sho-vol19']=len(new)
    s['篇別内訳']['dainichikyo-sho-vol19']={"著作名":"大日経疏 巻第十九","著者":"善無畏口述・一行筆受",
       "motif数":len(new),"id範囲":f"{new[0]['id']}-{new[-1]['id']}",
       "内訳":"本文 k004-k090 全網羅（首題k001/撰号k002/品題k003,k027,k048,k056,k065,k078,k084 は motif 化せず）・1段=1motif・束ねなし。百字位成品第二十一 k004-k026（m3878-m3900・23件）／百字成就持誦品第二十二 k028-k047（m3901-m3920・20件）／百字真言法品第二十三 k049-k055（m3921-m3927・7件）／説菩提性品第二十四 k057-k064（m3928-m3935・8件）／三三昧耶行品第二十五 k066-k077（m3936-m3947・12件）／明如来品第二十六 k079-k083（m3948-m3952・5件）／護摩法品第二十七 k085-k090（m3953-m3958・6件）。核心13件。"}
    s['motifs_without_gendai_gabun_intentional']['dainichikyo-sho-vol19_round_all']=\
       "大日経疏 巻第十九 motif（m3878-m3958・81件）gabun 意図的未設定（善無畏口述/一行筆受＝非空海・経典注釈系・全件 典籍曰く・巻第二〜十八 同運用）"
    d['schema_history'].append({"version":"0.2","date":"2026-06-25",
       "summary":"大日経疏 巻第十九 Phase3 motif 抽出（m3878-m3958・81件）：本文81段を 1段=1motif で抽出（束ねなし）。全件 引用形式:典籍曰く・大師系タグ非付与・category:密教教学／出典:大日経疏 巻第十九。7品（百字位成品第二十一 k004-k026 23件／百字成就持誦品第二十二 k028-k047 20件／百字真言法品第二十三 k049-k055 7件／説菩提性品第二十四 k057-k064 8件／三三昧耶行品第二十五 k066-k077 12件／明如来品第二十六 k079-k083 5件／護摩法品第二十七 k085-k090 6件）。核心13件。新タグ値4＝出典:大日経疏 巻第十九／主題:真言救世者／典故:月灯三昧経／典故:菩薩蔵経（いずれも既存軸内）。主題:本生 不使用（文体:譬喩で表す）・密教/主題 軸ずれ正規化・潅頂→灌頂。節は corpus.paragraphs[].section から取得し節==corpus.section 全件 assert。total 3908→3989。",
       "origin":"dainichikyo-sho-vol19_round_all"})
    with open(MP,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=1)
    print("APPLIED. total now",len(ms))
else:
    print("DRY-RUN ok (no write). total would be",pre_total+len(new))
