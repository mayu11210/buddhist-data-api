# -*- coding: utf-8 -*-
import json
paras=json.load(open('dainichi_vol10_paras.json',encoding='utf-8'))
T={}
for n in range(1,8):
    T.update(json.load(open(f'dv10_trans_{n}.json',encoding='utf-8')))
STRUCT={
 'k001':'首題','k002':'撰号',
 'k003':'品題（息障品 第三之余）',
 'k008':'品題（普通真言蔵品 第四）',
 'k064':'品題（世間成就品 第五）',
 'k079':'尾題',
}
STRUCT_TRANS={
 'k001':'大毘盧遮那成仏神変加持経疏 巻第十',
 'k002':'沙門一行阿闍梨〔善無畏三蔵の口述を一行が筆受した〕の記である。',
 'k003':'息障品 第三之余',
 'k008':'普通真言蔵品 第四',
 'k064':'世間成就品 第五',
 'k079':'以上で、成就世間品〔世間成就品〕を終わる。',
}
GROUPS=[
 ('k004','k007','彩色と漫荼羅・劣慧不信の障り〔本尊の色形・信のみ深境に入る・疑網〕','彩色と劣慧不信の障り'),
 ('k009','k010','諸菩薩の請願と不空の法門〔法界清浄門・無尽法爾の加持〕','諸菩薩の請願と不空の法門'),
 ('k011','k015','普賢・弥勒・虚空蔵・除蓋障の真言〔無礙力/大慈生/本性清浄/悲力〕','四菩薩の真言'),
 ('k016','k021','観自在部の諸尊の真言〔観音/得大勢/多羅/毘倶胝/白住処/馬頭/地蔵〕','観自在部の諸尊の真言'),
 ('k022','k028','文殊と金剛部の諸尊の真言〔文殊/金剛手/忙莽計/金剛鎖/月壓/金剛針/持金剛/奉教者〕','文殊と金剛部の諸尊の真言'),
 ('k028','k032','釈迦宝処と毫相・仏頂・無能勝の真言','釈迦と仏頂の真言'),
 ('k032','k039','諸天・諸尊の真言〔地神/毘紐/嚕捺羅/風神/美音/羅刹/焔魔/黒夜/七母/帝釈/龍王/梵天/日天/月天/諸龍/二龍王〕','諸天・諸尊の真言'),
 ('k039','k042','虚空眼の明妃と不動主の真言〔教迹不定悉地・火生名三昧・内外二障〕','虚空眼の明妃と不動主'),
 ('k042','k046','降三世・声聞・縁覚・諸仏菩薩心の真言','降三世と三乗の真言'),
 ('k046','k051','普世天・一切諸仏・守護者・結大界の真言','守護と結界の真言'),
 ('k051','k063','一百字輪の種子と諸尊の種子・毘盧遮那真言の心〔阿字＝一切真言の生処〕','一百字輪と毘盧遮那真言の心'),
 ('k065','k068','字句声の三観と世間成就〔一洛叉=一見・字/声/句義の三観〕','字句声の三観と世間成就'),
 ('k069','k074','月輪観と本尊観・持誦の果・出入の息〔円明月輪・字輪・六根清浄〕','月輪観と持誦の果'),
 ('k075','k078','一花供養と両月・山牛欄四道・成相の上中下〔息災増益降伏・三乗の果〕','一花供養と成就の相'),
]
def num(i):return int(i[1:])
def grp(idx):
    n=num(idx)
    for s,e,maj,sec in GROUPS:
        if num(s)<=n<=num(e): return maj,sec
    return None
out=[]
for f in paras:
    i=f['id']
    if i in STRUCT:
        maj=sec=STRUCT[i]; gd=STRUCT_TRANS[i]
    else:
        maj,sec=grp(i); gd=T[i]
    out.append({'id':i,'section_major':maj,'section':sec,'kakikudashi':f['text'],'gendaigoyaku':gd})
# outline in document order: build by iterating ids and grouping consecutive same section_major
outline=[]
cur=None
for p in out:
    key=(p['section_major'],p['section'])
    if cur and cur['key']==key and num(p['id'])==cur['last']+1:
        cur['last']=num(p['id'])
    else:
        if cur: outline.append(cur)
        cur={'key':key,'first':num(p['id']),'last':num(p['id'])}
if cur: outline.append(cur)
ol=[]
for c in outline:
    a=c["first"]; b=c["last"]
    ol.append({"section_major":c["key"][0],"section":c["key"][1],"id_range":"k%03d-k%03d"%(a,b),"para_range":[a,b]})
kk=''.join(p['kakikudashi'] for p in out); gd=''.join(p['gendaigoyaku'] for p in out)
corpus={
 'section':'大毘盧遮那成仏神変加持経疏 巻第十',
 'source':'沙門一行阿闍梨記（善無畏口述・一行筆受）',
 'base_text':'大毘盧遮那成佛神変加持経（大日経）息障品第三之余・普通真言蔵品第四・世間成就品第五',
 'genten':'',
 'genten_source':'漢文原典は後送（T1796 vol.39 巻第十・CBETA 線上閱讀 T1796_010）',
 'text':'',
 'format_note':'paragraphs に段落単位 section_major／section／kakikudashi／gendaigoyaku。outline は科段。元 doc が巨大ブロック（11段・最大20,943字）であったため科文・話題境界で 79 段に段落化（巻第三〜九 同型・ケンシン裁定 2026-06-20）。品題（息障品之余/普通真言蔵品/世間成就品）と尾題は文書中の構造段落として保持。割注の全角括弧は kakikudashi に温存。',
 'outline':ol,
 'translation_status':{'total_paragraphs':len(out),'translated':sum(1 for p in out if p['gendaigoyaku']),'remaining':sum(1 for p in out if not p['gendaigoyaku'])},
 'kakikudashi':kk,'gendaigoyaku':gd,'paragraphs':out,
}
p='/sessions/zen-practical-davinci/mnt/buddhist-data-api/data/kukai/dainichikyo-sho-vol10.json'
json.dump(corpus,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
raw=open(p,'rb').read()
print('paras',len(out),'kk',len(kk),'gd',len(gd),'outline',len(ol))
print('translated',corpus['translation_status'])
print('nulls',len(raw)-len(raw.rstrip(b'\x00')),'kk半角(',kk.count('('),'gd半角(',gd.count('('),gd.count(')'))
