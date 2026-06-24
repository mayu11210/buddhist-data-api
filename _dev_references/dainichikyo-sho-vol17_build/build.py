import json,sys,re,shutil,os
sys.path.insert(0,'/sessions/great-quirky-davinci/mnt/outputs/vol17_motif')
from tags import TAGS,ROUNDS
REPO='/sessions/great-quirky-davinci/mnt/buddhist-data-api'
MJ=REPO+'/data/indices/motifs.json'
CORP=REPO+'/data/kukai/dainichikyo-sho-vol17.json'
APPLY='--apply' in sys.argv

corp=json.load(open(CORP,encoding='utf-8'))
para={p['id']:p for p in corp['paragraphs']}
order=[k for r in ROUNDS.values() for k in r]
COMMON=['category:密教教学','出典:大日経疏 巻第十七','引用形式:典籍曰く']

def build_motif(k,mid):
    p=para[k]
    # tag order: common, then 密教, 主題, 典故, 文体, 一句性
    extra=TAGS[k]
    order_pref={'密教:':0,'主題:':1,'典故:':2,'文体:':3,'一句性:':4}
    extra_sorted=sorted(extra,key=lambda t:order_pref.get(t.split(':',1)[0]+':',9))
    tags=COMMON+extra_sorted
    return {
        'id':mid,
        'source':{'corpus':'dainichikyo-sho-vol17','著作名':'大日経疏 巻第十七','著者':'善無畏口述・一行筆受','節':p['section'],'段落':k},
        'text_kakikudashi':p['kakikudashi'],
        'text_gendaigoyaku':p['gendaigoyaku'],
        'tags':tags,
    }

mids={k:f'm{3745+i}' for i,k in enumerate(order)}
newmotifs={k:build_motif(k,mids[k]) for k in order}

# ---- DRY-RUN checks ----
errs=[]
# 節==section
for k in order:
    if newmotifs[k]['source']['節']!=para[k]['section']: errs.append(f'節 mismatch {k}')
# verbatim
for k in order:
    if newmotifs[k]['text_kakikudashi']!=para[k]['kakikudashi']: errs.append(f'kk verbatim {k}')
    if newmotifs[k]['text_gendaigoyaku']!=para[k]['gendaigoyaku']: errs.append(f'gd verbatim {k}')
# half-width parens in new motifs
for k in order:
    if re.search(r'[()]',newmotifs[k]['text_kakikudashi']) or re.search(r'[()]',newmotifs[k]['text_gendaigoyaku']): errs.append(f'half-width {k}')
# id sequence
m=json.load(open(MJ,encoding='utf-8'))
existing_ids={x['id'] for x in m['motifs']}
for k in order:
    if mids[k] in existing_ids: errs.append(f'id collision {mids[k]}')
nums=[3745+i for i in range(len(order))]
if nums!=list(range(3745,3745+88)): errs.append('id not contiguous')
# all 典籍曰く, no 大師
for k in order:
    t=newmotifs[k]['tags']
    if '引用形式:典籍曰く' not in t: errs.append(f'no 典籍曰く {k}')
    if any('大師' in x for x in t): errs.append(f'大師 tag {k}')

print('DRY-RUN: 88 motifs built. errors:',len(errs))
for e in errs[:20]: print('  ',e)
core=[k for k in order if '一句性:核心' in TAGS[k]]
print('核心',len(core),' total after =',len(m['motifs'])+88,' last id m3832')
# existing stats drift check
def nonl(s): return len(s.replace('\n',''))
kk_re=sum(nonl(x['text_kakikudashi']) for x in m['motifs'])
gd_re=sum(nonl(x['text_gendaigoyaku']) for x in m['motifs'])
print('existing kk recompute',kk_re,'vs stats',m['stats']['kakikudashi_chars_total'],'drift',kk_re-m['stats']['kakikudashi_chars_total'])
print('existing gd recompute',gd_re,'vs stats',m['stats']['gendaigoyaku_chars_total'],'drift',gd_re-m['stats']['gendaigoyaku_chars_total'])
add_kk=sum(nonl(newmotifs[k]['text_kakikudashi']) for k in order)
add_gd=sum(nonl(newmotifs[k]['text_gendaigoyaku']) for k in order)
print('add kk',add_kk,'add gd',add_gd)

if not APPLY:
    print('\n(dry-run only; pass --apply to write)')
    sys.exit(0 if not errs else 1)

assert not errs, errs
# ---- APPLY: per-round backup + append + schema_history ----
import datetime
DATE='2026-06-24'
round_meta={
 'R1 秘密八印品第十四':('round1','秘密八印品第十四（八印の印相・漫荼羅・真言、八印を八仏菩薩に配当、阿闍梨授法の誡め・六月三月）','m3745-m3754',10,1),
 'R2 持明禁戒品第十五':('round2','持明禁戒品第十五（戒の二種・五頌の問・大日の讃・偈の答〔三平等・戒=如来無師の慧〕・落叉=見・六月持誦法・功徳）','m3755-m3775',21,5),
 'R3 阿闍梨真実智品第十六 前半':('round3','阿闍梨真実智品第十六 前半（一切真言の心=阿字・本不生・種子・布字・根本字と増加字の不一不異）','m3776-m3788',13,3),
 'R4 阿闍梨真実智品第十六 後半':('round4','阿闍梨真実智品第十六 後半（阿字八葉観・阿闍梨即如来・諸天尊号はみな我=遍一切処・一百八号皆阿字・五大字布字・常住即仏）','m3789-m3801',13,5),
 'R5 布字品第十七＋受方便学処品第十八 前半':('round5','布字品第十七（身体への梵字配当・仏即一切智）＋受方便学処品第十八 前半（菩薩戒=自性本源の戒・十善戒・授戒次第・仏制戒方便・真四重禁=捨佛断命・十重禁戒）','m3802-m3817',16,4),
 'R6 受方便学処品第十八 後半':('round6','受方便学処品第十八 後半（修学句同事・声聞外道との差別=一道法門〔阿字門〕・大乗十善=一切法平等・不殺/不与取戒の方便〔毒蟒・五百商人・師子の譬〕）','m3818-m3832',15,4),
}
bkdir='/sessions/great-quirky-davinci/mnt/outputs/vol17_motif'
ridx=0
for rname,ks in ROUNDS.items():
    ridx+=1
    shutil.copy(MJ, f'{bkdir}/motifs_backup_pre_vol17_r{ridx}.json')
    m=json.load(open(MJ,encoding='utf-8'))
    for k in ks: m['motifs'].append(newmotifs[k])
    key,summ_topic,idr,cnt,corecnt=round_meta[rname]
    m['schema_history'].append({'version':'0.2','date':DATE,
        'summary':f'大日経疏 巻第十七 Phase3 motif 抽出 {rname.split()[0]}（{idr}・{cnt}件）：{summ_topic}。引用形式:典籍曰く 全件・大師系タグ非付与・1段=1motif・gabun 意図的未設定・核心{corecnt}件。',
        'origin':f'dainichikyo-sho-vol17_{key}'})
    json.dump(m, open(MJ,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'applied {rname}: +{cnt} -> total {len(m["motifs"])}')

# ---- final stats update ----
m=json.load(open(MJ,encoding='utf-8'))
st=m['stats']
st['total_motifs']=len(m['motifs'])
st['kakikudashi_chars_total']=sum(nonl(x['text_kakikudashi']) for x in m['motifs'])
st['gendaigoyaku_chars_total']=sum(nonl(x['text_gendaigoyaku']) for x in m['motifs'])
st['from_corpus_dainichikyo-sho-vol17']=88
st['篇別内訳']['dainichikyo-sho-vol17']={'著作名':'大日経疏 巻第十七','著者':'善無畏口述・一行筆受','motif数':88,'id範囲':'m3745-m3832',
  '内訳':'本文 k004-k095 全網羅（首題k001/撰号k002/品題k003,k014,k036,k063,k065 は motif 化せず）・1段=1motif・束ねなし。R1 秘密八印品第十四 k004-k013／R2 持明禁戒品第十五 k015-k035／R3 阿闍梨真実智品第十六 前半 k037-k049／R4 同 後半 k050-k062／R5 布字品第十七 k064＋受方便学処品第十八 前半 k066-k080／R6 同 後半 k081-k095。核心20件。'}
for rname,(key,summ_topic,idr,cnt,corecnt) in round_meta.items():
    rks=ROUNDS[rname]
    st['motifs_without_gendai_gabun_intentional'][f'dainichikyo-sho-vol17_{key}']=f'大日経疏 巻第十七 {key} motif（{idr}）gabun 意図的未設定（善無畏口述/一行筆受＝非空海・経典注釈系・全件 典籍曰く・巻第二〜十六 同運用）'
json.dump(m, open(MJ,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('final stats: total',st['total_motifs'],'kk',st['kakikudashi_chars_total'],'gd',st['gendaigoyaku_chars_total'],'from_vol17',st['from_corpus_dainichikyo-sho-vol17'])
