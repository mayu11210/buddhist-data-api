# -*- coding: utf-8 -*-
import json
paras=json.load(open('dainichi_vol9_paras.json',encoding='utf-8'))
T={}
for n in range(1,7):
    T.update(json.load(open(f'dv9_trans_{n}.json',encoding='utf-8')))
# struct labels
STRUCT={
 'k001':('首題','首題'),
 'k002':('撰号','撰号'),
 'k003':('品題（入漫荼羅具縁真言品 第二之余）','品題（入漫荼羅具縁真言品 第二之余）'),
 'k053':('品題（息障品 第三）','品題（息障品 第三）'),
}
STRUCT_TRANS={
 'k001':'大毘盧遮那成仏神変加持経疏 巻第九',
 'k002':'沙門一行阿闍梨〔善無畏三蔵の口述を一行が筆受した〕の記である。',
 'k003':'入漫荼羅具縁真言品 第二之余',
 'k053':'息障品 第三',
}
# section groupings for body: (id_start,id_end, section_major, section)
GROUPS=[
 ('k004','k007','慶賀偈の結びと十一偈〔八相の慶び・初法明道への往詣〕','慶賀偈の結び'),
 ('k008','k012','金籌偈・明鏡偈・法輪法螺偈・三昧耶偈〔四偈の梵本と字義〕','四偈の梵本と字義'),
 ('k013','k016','四波羅夷戒〔三世無障礙智戒の戒相・正法/菩提心/慳法/不饒益〕','四波羅夷戒'),
 ('k017','k022','無作の功徳と福徳聚〔善性戒者・福徳は如来と等し・瞿醯の灌頂作法〕','無作の功徳と福徳聚'),
 ('k023','k032','大力大護の明妃〔広長語輪・清浄法幢高峰観・訶佉二字門〕','大力大護の明妃'),
 ('k033','k042','法界加持と三三昧耶〔入仏三昧耶・法界生・金剛薩埵・金剛鎧〕','法界加持と三三昧耶'),
 ('k043','k052','如来眼・塗香等六種真言・如来頂相等の四真言','供養と荘厳の真言'),
 ('k054','k055','障は自心より生ず〔慳貪が因・菩提心の対治・不動明王〕','障は自心より生ず'),
 ('k056','k057','風水の障りを止める作法〔阿字訶字囉字・金剛橛〕','風水の障りを止める作法'),
 ('k058','k061','不動明王の漫荼羅と摩醯首羅の降伏〔三角壇・大自在天の成仏〕','不動明王と摩醯首羅降伏'),
 ('k062','k063','教令使と金剛の家法〔尊主の現威・如来種家の家法〕','教令使と金剛の家法'),
]
def num(i):return int(i[1:])
def grp(idx):
    n=num(idx)
    for s,e,maj,sec in GROUPS:
        if num(s)<=n<=num(e): return maj,sec
    return None
out_paras=[]
for f in paras:
    i=f['id']
    if i in STRUCT:
        maj,sec=STRUCT[i]; gd=STRUCT_TRANS[i]
    else:
        maj,sec=grp(i); gd=T[i]
    out_paras.append({'id':i,'section_major':maj,'section':sec,'kakikudashi':f['text'],'gendaigoyaku':gd})
# outline
outline=[]
# struct singletons + groups in order
def add(maj,sec,a,b):
    outline.append({'section_major':maj,'section':sec,'id_range':f'{a}-{b}','para_range':[num(a),num(b)]})
add('首題','首題','k001','k001')
add('撰号','撰号','k002','k002')
add(STRUCT['k003'][0],STRUCT['k003'][1],'k003','k003')
for s,e,maj,sec in GROUPS[:7]:
    add(maj,sec,s,e)
add(STRUCT['k053'][0],STRUCT['k053'][1],'k053','k053')
for s,e,maj,sec in GROUPS[7:]:
    add(maj,sec,s,e)
kk=''.join(p['kakikudashi'] for p in out_paras)
gd=''.join(p['gendaigoyaku'] for p in out_paras)
corpus={
 'section':'大毘盧遮那成仏神変加持経疏 巻第九',
 'source':'沙門一行阿闍梨記（善無畏口述・一行筆受）',
 'base_text':'大毘盧遮那成佛神変加持経（大日経）入漫荼羅具縁真言品第二之余・息障品第三',
 'genten':'',
 'genten_source':'漢文原典は後送（T1796 vol.39 巻第九・CBETA 線上閱讀 T1796_009）',
 'text':'',
 'format_note':'paragraphs に段落単位 section_major／section／kakikudashi／gendaigoyaku。outline は科段。元 doc が巨大ブロック（12段・最大7,691字）であったため科文・話題境界で 63 段に段落化（巻第三〜八 同型・ケンシン裁定 2026-06-20）。品題（息障品第三）は文書途中の構造段落として保持。割注の全角括弧は kakikudashi に温存。',
 'outline':outline,
 'translation_status':{'total_paragraphs':len(out_paras),'translated':sum(1 for p in out_paras if p['gendaigoyaku']),'remaining':sum(1 for p in out_paras if not p['gendaigoyaku'])},
 'kakikudashi':kk,
 'gendaigoyaku':gd,
 'paragraphs':out_paras,
}
p='/sessions/zen-practical-davinci/mnt/buddhist-data-api/data/kukai/dainichikyo-sho-vol9.json'
json.dump(corpus,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
raw=open(p,'rb').read()
print('paras',len(out_paras),'kk',len(kk),'gd',len(gd))
print('translated',corpus['translation_status'])
print('nulls',len(raw)-len(raw.rstrip(b'\x00')))
print('kk半角(',kk.count('('),'gd半角(',gd.count('('),'gd半角)',gd.count(')'))
# reconstruction check vs normalized doc
import re
print('outline entries',len(outline))
