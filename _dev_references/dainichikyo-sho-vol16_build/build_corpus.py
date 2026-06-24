# -*- coding: utf-8 -*-
import json
paras=json.load(open('paras.json'))
T=json.load(open('trans_all.json'))
for p in paras:
    p['gendaigoyaku']=T[p['id']]

# outline: one entry per paragraph (each paragraph = one 科段/topical unit)
outline=[]
for i,p in enumerate(paras,1):
    sm=p['section_major']; sec=p['section']
    if p['id'] in ('k003','k041','k051'):
        # 品題: enrich label with the chapter title from kakikudashi
        title=p['kakikudashi'].strip()
        sm='品題（%s）'%title; sec=sm
    outline.append({'section_major':sm,'section':sec,'id_range':'%s-%s'%(p['id'],p['id']),'para_range':[i,i]})

corpus={
 'section':'大毘盧遮那成仏神変加持経疏 巻第十六',
 'source':'沙門一行阿闍梨記（善無畏口述・一行筆受）',
 'base_text':'大毘盧遮那成佛神変加持経（大日経）秘密漫荼羅品第十一之余／入秘密漫荼羅品第十二／入秘密漫荼羅位品第十三',
 'genten':'',
 'genten_source':'大正新脩大藏經 No.1796『大毘盧遮那成佛神變加持經疏』卷第十六（善無畏口述・一行筆受）／CBETA 線上閱讀 T1796_016',
 'genten_unavailable_reason':'Phase1 時点では未取得。CBETA 線上閱讀 T1796_016 を Chrome 経由で後送取得し、Downloads でのバイト一致照合の上で投入予定（巻第十五と同手順）。',
 'text':'',
 'format_note':'paragraphs に段落単位 section_major／section／kakikudashi／gendaigoyaku。outline は科段（本巻は1段=1科段で対応）。元 doc が巨大ブロック（本文ブロック最大10,404字・3品にわたる）であったため、科文・話題境界で本文を66段に段落化し、首題・撰号・品題（3品ぶん）の構造5段を加えて全71段（k001-k071）。重複ブロックの有無を確認し、巻第十五のような重複は無し（全文連結が段落化前の科文連結と完全一致 assert pass）。割注の全角括弧は kakikudashi に温存。本巻は「秘密漫荼羅品第十一之余」「入秘密漫荼羅品第十二」「入秘密漫荼羅位品第十三」の3品を収める。genten は CBETA 線上閱讀 T1796_016 を後送取得予定（Phase genten）。',
 'outline':outline,
 'translation_status':{'total_paragraphs':len(paras),'translated':len(paras),'remaining':0},
 'kakikudashi':'\n'.join(p['kakikudashi'] for p in paras),
 'gendaigoyaku':'\n'.join(p['gendaigoyaku'] for p in paras),
 'paragraphs':[{'id':p['id'],'section_major':p['section_major'],'section':p['section'],'kakikudashi':p['kakikudashi'],'gendaigoyaku':p['gendaigoyaku']} for p in paras],
}
out='/sessions/affectionate-sweet-keller/mnt/buddhist-data-api/data/kukai/dainichikyo-sho-vol16.json'
with open(out,'w',encoding='utf-8') as f:
    json.dump(corpus,f,ensure_ascii=False,indent=1)
# verify
raw=open(out,encoding='utf-8').read()
re=json.loads(raw)
print('written:', out)
print('keys:', list(re.keys()))
print('paragraphs:', len(re['paragraphs']), 'outline:', len(re['outline']))
print('kakikudashi chars:', len(re['kakikudashi']), 'gendaigoyaku chars:', len(re['gendaigoyaku']))
print('NUL bytes:', raw.count('\x00'))
# half-width paren check in gendaigoyaku fields
bad=[p['id'] for p in re['paragraphs'] if '(' in p['gendaigoyaku'] or ')' in p['gendaigoyaku']]
print('half-width paren in gendai:', bad)
allt=all(len(p['gendaigoyaku'])>0 for p in re['paragraphs'])
print('all translated:', allt)
