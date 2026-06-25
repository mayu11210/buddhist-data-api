# -*- coding: utf-8 -*-
# Assembles data/kukai/dainichikyo-sho-vol20.json from skeleton + translations + (optional) image segment.
import json, sys, glob

REPO='/sessions/pensive-jolly-brahmagupta/mnt/buddhist-data-api'
B=REPO+'/_dev_references/dainichikyo-sho-vol20_build'

sk=json.load(open(B+'/paras_skeleton.json'))
trans={}
for f in ['out_struct.json','out_A_homa.json','out_B_honzon_musou.json','out_C_jiju.json','out_D_zokurui.json']:
    for k,v in json.load(open(B+'/'+f)).items():
        trans[int(k)]=v

# optional image segment: out_image.json = {"after_seq":79,"section_major":"囑累品第三十一","section":"...","kakikudashi":"...","gendaigoyaku":"..."}
img=None
import os
if os.path.exists(B+'/out_image.json'):
    img=json.load(open(B+'/out_image.json'))

# build ordered paragraph list (seq order), inserting image after its after_seq
rows=[]
for x in sorted(sk,key=lambda r:r['seq']):
    seq=x['seq']
    t=trans[seq]
    rows.append({"section_major":x['section_major'],"section":t['section'],
                 "kakikudashi":x['kakikudashi'],"gendaigoyaku":t['gendaigoyaku']})
    if img and seq==img['after_seq']:
        rows.append({"section_major":img['section_major'],"section":img['section'],
                     "kakikudashi":img['kakikudashi'],"gendaigoyaku":img['gendaigoyaku']})

# assign k-ids
for i,r in enumerate(rows):
    r2={"id":"k%03d"%(i+1),"section_major":r['section_major'],"section":r['section'],
        "kakikudashi":r['kakikudashi'],"gendaigoyaku":r['gendaigoyaku']}
    rows[i]=r2

# outline: one entry per paragraph (vol19 style: 1段=1科段)
outline=[]
for r in rows:
    n=int(r['id'][1:])
    outline.append({"section_major":r['section_major'],"section":r['section'],
                    "id_range":"%s-%s"%(r['id'],r['id']),"para_range":[n,n]})

kk_all='\n'.join(r['kakikudashi'] for r in rows)
gd_all='\n'.join(r['gendaigoyaku'] for r in rows)

# genten: filled separately (placeholder empty until CBETA extraction)
genten=''
gtsrc='大正新脩大藏經 No.1796『大毘盧遮那成佛神變加持經疏』卷第二十（善無畏口述・一行筆受）／CBETA 線上閱讀 T1796_020'
gpath=B+'/genten_T1796_020_clean.txt'
if os.path.exists(gpath):
    genten=open(gpath,encoding='utf-8').read()

corpus={
 "section":"大毘盧遮那成仏神変加持経疏 巻第二十",
 "source":"沙門一行阿闍梨記（善無畏口述・一行筆受）",
 "base_text":"大毘盧遮那成佛神変加持経（大日経）世出世護摩法品第二十七之余／本尊三昧品第二十八／無相三昧品第二十九／世出世持誦品第三十／囑累品第三十一",
 "genten":genten,
 "genten_source":gtsrc,
 "text":"",
 "format_note":"paragraphs に段落単位 section_major／section／kakikudashi／gendaigoyaku。outline は科段（本巻は1段=1科段で対応）。囑累品の種子字段（k0XX）は doc 埋込画像 image1.png の本文転記＝種字は割注化・読みは CBETA 音写（ケンシン裁定）。",
 "outline":outline,
 "translation_status":{"total_paragraphs":len(rows),"translated":len(rows),"remaining":0},
 "kakikudashi":kk_all,
 "gendaigoyaku":gd_all,
 "paragraphs":rows,
}
out=REPO+'/data/kukai/dainichikyo-sho-vol20.json'
with open(out,'w',encoding='utf-8') as f:
    json.dump(corpus,f,ensure_ascii=False,indent=1)
print('wrote',out)
print('paragraphs:',len(rows),'(image segment:',bool(img),')')
print('kk chars (no nl):',len(kk_all.replace('\n','')),'gd chars (no nl):',len(gd_all.replace('\n','')))
# checks
nul=open(out,'rb').read().count(b'\x00'); print('NUL:',nul)
half=sum(1 for r in rows if '(' in r['kakikudashi']+r['gendaigoyaku'] or ')' in r['kakikudashi']+r['gendaigoyaku'])
print('paras with half-width parens:',half)
