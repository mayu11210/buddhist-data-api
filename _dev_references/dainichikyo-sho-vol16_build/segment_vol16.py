# -*- coding: utf-8 -*-
import json, re
d=json.load(open('vol16_sents.json'))
S=d['sentences']; B=d['block_of']
# rebuild block text exactly (sentences were stripped; original blocks had leading space + joined)
raw=open('vol16.txt',encoding='utf-8').read()
blocks=[b for b in raw.split('\n') if b.strip()]
blocks=[b.lstrip('﻿') for b in blocks]
# structural blocks: 0,1,2,7,10
# text paragraph break-start sentence indices per block (topical / 科文 boundaries)
breaks = {
 3:[3,13,35,48,58,65,67,85,93,106,121,139],
 4:[158,173],
 5:[181,200,221,231,259,270,290,306,315],
 6:[329,340,353,372,388,404,417,439,469,501,536,568,596,618],
 8:[627],
 9:[633,653,669,694,711,727,749,771],
 11:[802,807,821,843,866,898,933,962,981,1001,1024,1048,1070,1093,1108,1121,1148,1170,1188,1211],
}
# block end sentence index (inclusive)
bend={3:157,4:180,5:328,6:625,8:632,9:800,11:1215}

# section_major labels
P11='秘密漫荼羅品第十一之余'
P12='入秘密漫荼羅品第十二'
P13='入秘密漫荼羅位品第十三'

def seg_block(bi):
    st=breaks[bi]; en=bend[bi]
    out=[]
    for i,s in enumerate(st):
        e=(st[i+1]-1) if i+1<len(st) else en
        text=''.join(S[s:e+1])  # sentences already include trailing 。; join w/o space
        out.append((s,e,text))
    return out

paras=[]
def add(pid, smaj, sec, text):
    paras.append({'id':pid,'section_major':smaj,'section':sec,'kakikudashi':text})

# structural
add('k001','首題','首題', blocks[0])
add('k002','撰号','撰号', blocks[1])
add('k003','品題','品題', blocks[2])

# block3 sections
b3secs=['果数寿量劫量への答','三昧の答（離想有相清浄）','業従果得・悉地成就・業生解脱','心の無自性回向（質多因果）','断滅見の否定・法性生・功徳無辺','略説偈の結び','長行・五事（印色尊位住三昧）','五趣・法界虚空行・諦受','金剛手応答・秘密漫荼羅の法','作法（四方漫荼羅・十字金剛印・九点・十二字真言王）','蓮子・本尊像・四菩薩配置','最初悲生壇・流出・四種造の秘法']
b4secs=['仏部漫荼羅（円壇白蓮三角仏像）','真言主・遍身光流出']
b5secs=['蓮華部漫荼羅（方壇商佉観音）','明妃資財主・得自在・蓮華部壇中胎','馬頭漫荼羅（三角日暉）','金剛部第二漫荼羅（四方金剛瓶風火）','汝の漫荼羅・諸明王坐類形色','金剛執自在者・諸金剛名の列挙','金剛刹塵・所持印（三古一古五股鬘）','不動尊漫荼羅（風火）','仏母漫荼羅（金色四方蓮華仏頂）']
b6secs=['仏頂印・火災中種子布','菩薩部漫荼羅（十字台真陀末尼如意珠）','釈迦漫荼羅（金剛方壇鉢袈裟錫杖）','五仏頂の列挙・印漫荼羅','仏眼・無能勝明妃王・釈迦中胎','浄居天の印（思惟善笑花虚空掌）','地神火天請召・諸大仙・火院','閻魔王・諸天母印・七母眷属','七母眷属鳥・泥哩底等諸天の印・釈迦部終','文殊曼荼羅（青蓮印・使者童女）','除蓋障菩薩と眷属','地蔵菩薩（大因陀羅輪宝幢）','虚空蔵菩薩（円壇刀）','四菩薩主中壇・第二院八部']
b8secs=['入秘密漫荼羅品の序（執金剛秘密）']
b9secs=['唯仏与仏・金剛頂経分別積品・持金剛智印','秘密漫荼羅遍学・阿闍梨の資格','弟子の罪を焼く・業煩悩薪と方便智火（字焼字）','阿字の弟子身・嚩字生浄菩提心','火風空五字・十二字真言王の身布','十二字を身に配す・三等布字・三昧耶成就','三昧耶＝我等仏仏等我・遍入諸壇自在','要用の法・末代学人への戒め・明師を求む']
b11secs=['住秘密漫荼羅品の序・三種加持','毘盧遮那＝日・遍照円明常住','三昧入・無相に有相を現ず・等至三昧の義','浄国地平・浄菩提心・五宝五行（戒信進定慧）','大宝蓋・門幖（四念住四梵住）・雑色幡','摩尼幢・八功徳水池・瓔珞楽器・意生座三重','法界幖・法界体性蓮華王・無礙力の身','無礙力の出生・十力六度十度・諸世界大会の妙音','音声偈・無蔵性の中に慧を含蔵す','無得偈・空義・本不生阿字の出入','彼仏＝毘盧遮那・内心漫荼羅秘密蔵','外漫荼羅の治地に准ず・瑜伽座阿字金剛地','水火風の字観（嚩囉訶）・五大法界清浄性','業金剛の加護・満奴末那仙の外道見を除く','四角四門・八大宝柱・大蓮華王八葉','身語意を超越す・毘盧遮那無師智・悦意の果','八葉の諸仏配置・仏母波羅蜜・執金剛の茎・大海','灯花偈・意生花・囉字浄除・師瑜伽座','肉身八葉囉字目・暗字潅頂・花投・八葉の位','前品大秘密・今は証入・室宅に入る喩']

def run(bi, secs, smaj):
    for (s,e,text),sec in zip(seg_block(bi), secs):
        pid='k%03d'%(len(paras)+1)
        add(pid, smaj, sec, text)

run(3,b3secs,P11); run(4,b4secs,P11); run(5,b5secs,P11); run(6,b6secs,P11)
add('k%03d'%(len(paras)+1),'品題','品題', blocks[7])  # 入秘密漫荼羅品第十二
run(8,b8secs,P12); run(9,b9secs,P12)
add('k%03d'%(len(paras)+1),'品題','品題', blocks[10]) # 入秘密漫荼羅位品第十三
run(11,b11secs,P13)

json.dump(paras, open('paras.json','w'), ensure_ascii=False, indent=1)
print('total paragraphs:', len(paras))
print('ids:', paras[0]['id'], '..', paras[-1]['id'])
# reproduction assert: concat of all kakikudashi == concat of blocks (structural+joined sentences)
# Build expected from blocks: structural blocks as-is; text blocks = concat of their sentences (==block stripped of internal? sentences were split by 。 keep)
# Verify: total chars of paras vs sum of sentences + structural
allcat=''.join(p['kakikudashi'] for p in paras)
# expected = block0+block1+block2 + sents(3..157) + sents(158..180)+...+block7+sents+block10+sents
exp=blocks[0]+blocks[1]+blocks[2]
exp+=''.join(S[3:158])+''.join(S[158:181])+''.join(S[181:329])+''.join(S[329:626])
exp+=blocks[7]+''.join(S[627:633])+''.join(S[633:801])
exp+=blocks[10]+''.join(S[802:1216])
print('ASSERT concat match:', allcat==exp, '| len paras', len(allcat),'exp', len(exp))
# structural count
struct=[p['id'] for p in paras if p['section_major'] in ('首題','撰号','品題')]
print('structural (non-motif) ids:', struct, 'count', len(struct))
print('text paragraph count:', len(paras)-len(struct))
