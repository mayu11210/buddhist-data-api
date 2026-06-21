# -*- coding: utf-8 -*-
import json
paras=json.load(open('dainichi_vol11_paras.json',encoding='utf-8'))
T={}
for n in range(1,8): T.update(json.load(open(f'dv11_trans_{n}.json',encoding='utf-8')))
STRUCT={'k001':'首題','k002':'撰号','k003':'品題（悉地出現品 第六）'}
STRUCT_TRANS={
 'k001':'大毘盧遮那成仏神変加持経疏 巻第十一',
 'k002':'沙門一行阿闍梨〔善無畏三蔵の口述を一行が筆受した〕の記である。',
 'k003':'悉地出現品 第六',
}
GROUPS=[
 ('k004','k008','三世無量門決定智円満の法句〔虚空無自性が巧智を授く・甚深縁起・極清浄修行の法〕','三世無量門決定智の法句'),
 ('k009','k012','諸菩薩の請願と羞恥の二法〔法主の前の謙退・作すべからざるを作さず衆に称讃せらる・尸羅と人天の生〕','諸菩薩の請願と羞恥の二法'),
 ('k013','k018','真言成就流出相応の句と行者の徳〔曼荼羅を見・印可・菩提心/深信/調伏/十喩観/持明具戒/巧方便〕','真言成就流出相応の句と行者の徳'),
 ('k019','k023','真言成就の相と威力の譬喩〔自在悦満意明・摩醯首羅勝意生明・甚深縁起・真言道を断ぜず〕','真言成就の相と威力の譬喩'),
 ('k024','k028','荘厳清浄蔵三昧の四処流出〔阿字より四字・四徳四色四与願・互出声・広大智句〕','荘厳清浄蔵三昧の四処流出'),
 ('k029','k033','正等覚の心の出世成就〔処の選択・菩提心観・本尊観と心鏡・影像成就〕','正等覚の心の出世成就'),
 ('k034','k039','摂意の念誦と一洛叉・三月の行〔一見一境・第二月の供養・第三月の悲願・三種加持句〕','摂意の念誦と三月の行'),
 ('k040','k046','虚空蔵転明妃と曼荼羅造立・成就の薬物〔三力回向・金剛界の壇・上中下の成相・有分別成就〕','虚空蔵転明妃と曼荼羅造立'),
 ('k047','k052','方便波羅蜜と無為に有為を表す〔三世仏の通達・長寿五欲娯楽・一生成就・計都剣傘蓋等の薬物〕','方便波羅蜜と無為に有為を表す'),
 ('k053','k057','因果の破斥と真言は法界〔因も果も本不生・因業を離る・無相三摩地・悉地は心より生ず〕','因果の破斥と真言は法界'),
 ('k058','k062','法界の不可分析と成就〔不思議界は金剛性・見法成就・五根清浄と従生〕','法界の不可分析と成就'),
 ('k063','k068','阿字門の成就法と如幻三昧〔出入の息・摂毒・愛敬・業戯の行舞・如来の如幻三昧〕','阿字門の成就法と如幻三昧'),
 ('k069','k072','降伏四魔金剛戯の五字〔阿味囉訶佉/吽欠・四魔を降し六趣を解脱・財富＝法宝〕','降伏四魔金剛戯の五字'),
 ('k073','k077','阿字布字観と金剛座の法〔住心一境・金剛地際の加持・阿/長阿/暗字・大因陀羅観〕','阿字布字観と金剛座の法'),
]
def num(i):return int(i[1:])
def grp(idx):
    n=num(idx)
    for s,e,maj,sec in GROUPS:
        if num(s)<=n<=num(e): return maj,sec
out=[]
for f in paras:
    i=f['id']
    if i in STRUCT: maj=sec=STRUCT[i]; gd=STRUCT_TRANS[i]
    else: maj,sec=grp(i); gd=T[i]
    out.append({'id':i,'section_major':maj,'section':sec,'kakikudashi':f['text'],'gendaigoyaku':gd})
outline=[];cur=None
for p in out:
    key=(p['section_major'],p['section'])
    if cur and cur['key']==key and num(p['id'])==cur['last']+1: cur['last']=num(p['id'])
    else:
        if cur: outline.append(cur)
        cur={'key':key,'first':num(p['id']),'last':num(p['id'])}
if cur: outline.append(cur)
ol=[]
for c in outline:
    a=c['first'];b=c['last']
    ol.append({'section_major':c['key'][0],'section':c['key'][1],'id_range':'k%03d-k%03d'%(a,b),'para_range':[a,b]})
kk=''.join(p['kakikudashi'] for p in out); gd=''.join(p['gendaigoyaku'] for p in out)
corpus={
 'section':'大毘盧遮那成仏神変加持経疏 巻第十一','source':'沙門一行阿闍梨記（善無畏口述・一行筆受）',
 'base_text':'大毘盧遮那成佛神変加持経（大日経）悉地出現品第六',
 'genten':'','genten_source':'漢文原典は後送（T1796 vol.39 巻第十一・CBETA 線上閱讀 T1796_011）','text':'',
 'format_note':'paragraphs に段落単位 section_major／section／kakikudashi／gendaigoyaku。outline は科段。元 doc が巨大ブロック（5段・最大12,671字）であったため科文・話題境界で 77 段に段落化（巻第三〜十 同型・ケンシン裁定 2026-06-20）。品題（悉地出現品第六）は本文ブロック先頭にインライン埋込であったため構造段落として切り出し保持。割注の全角括弧は kakikudashi に温存。尾題なし（巻第十二へ続く）。',
 'outline':ol,
 'translation_status':{'total_paragraphs':len(out),'translated':sum(1 for p in out if p['gendaigoyaku']),'remaining':sum(1 for p in out if not p['gendaigoyaku'])},
 'kakikudashi':kk,'gendaigoyaku':gd,'paragraphs':out,
}
p='/sessions/zen-practical-davinci/mnt/buddhist-data-api/data/kukai/dainichikyo-sho-vol11.json'
json.dump(corpus,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
raw=open(p,'rb').read()
print('paras',len(out),'kk',len(kk),'gd',len(gd),'outline',len(ol))
print('translated',corpus['translation_status'])
print('nulls',len(raw)-len(raw.rstrip(b'\x00')),'kk半角(',kk.count('('),'gd半角(',gd.count('('),gd.count(')'))
