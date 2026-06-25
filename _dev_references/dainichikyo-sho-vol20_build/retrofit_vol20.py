# -*- coding: utf-8 -*-
import json,sys,shutil,re
REPO='/sessions/pensive-jolly-brahmagupta/mnt/buddhist-data-api'
B=REPO+'/_dev_references/dainichikyo-sho-vol20_build'
MP=REPO+'/data/indices/motifs.json'
APPLY='--apply' in sys.argv
RETRO={
 'm4016':['連動:sg07','連動:m713'],
 'm4024':['連動:sg07','連動:m713'],
 'm4002':['連動:sg08','連動:m549'],
 'm4009':['連動:sg08','連動:m549'],
 'm3994':['連動:sg21','連動:m638','連動:m728'],
 'm4033':['連動:sg21','連動:m638','連動:m728'],
}
d=json.load(open(MP)); ms=d['motifs']; st=d['stats']
mp={m['id']:m for m in ms}
# PRE rollback asserts
assert st['total_motifs']==len(ms)==4072
assert '引用形式:典籍曰く' in mp['m506']['tags']
assert '連動:sg08' in mp['m549']['tags'] and '連動:sg27' in mp['m719']['tags']
assert st['from_corpus_dainichikyo-sho-vol20']==83 and st['from_corpus_dainichikyo-sho-vol19']==81
kk0=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms)
gd0=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms)
# verify targets exist + are vol20 + verbatim signature present
sig={'m4016':'三句の義','m4024':'三句を問う','m4002':'阿字門','m4009':'本来不生','m3994':'浄菩提心の初法明門','m4033':'浄菩提心'}
added=0
for mid,tags in RETRO.items():
    m=mp[mid]; assert m['source']['corpus']=='dainichikyo-sho-vol20', mid
    assert sig[mid] in m['text_kakikudashi'], ('sig',mid)
    for t in tags:
        if t not in m['tags']:
            m['tags'].append(t); added+=1
st['total_motifs']=len(ms)  # unchanged
# schema_history
d['schema_history'].append({"version":"0.2","date":"2026-06-25","summary":"大日経疏 巻第二十 連動軸 retrofit（新規 sg/anchor なし＝既存軸の被覆拡張・巻第二〜十九 retrofit 同型・ケンシン裁定 新設なし）：core verbatim に限定し 6 件に +%d 連動タグ＝sg07 三句法門〔m713〕←m4016（k064 菩提心種子＝因・大悲為根・方便為究竟＝大日経 住心品 三句 verbatim・強連動）/m4024（k073 三句を問う＝菩提心種子・大悲根・方便後）／sg08 阿字本不生〔m549〕←m4002（k049 三事縁生＝不生不滅＝阿字門・法界性）/m4009（k057 当に本来不生に住すべし＝心これなり）／sg21 浄菩提心〔m638+m728〕←m3994（k041 浄菩提心の初法明門に入る・強連動）/m4033（k082 此の地は即ち是れ浄菩提心）。sg27 自心本性清浄 は core verbatim 直結なく見送り。タグのみ変更・total 4072 不変。"%added,"origin":"retrofit:dainichikyo-sho-vol20_rendou_scan"})
out=json.dumps(d,ensure_ascii=False,indent=1)
# POST asserts
assert out.count('\x00')==0
d2=json.loads(out); ms2=d2['motifs']; mp2={m['id']:m for m in ms2}
assert d2['stats']['total_motifs']==len(ms2)==4072
nums=sorted(int(m['id'][1:]) for m in ms2 if re.fullmatch(r'm\d+',m['id']))
assert nums==list(range(1,4042))
assert len([m for m in ms2 if m['id'].startswith('sg')])==31
kk2=sum(len(m['text_kakikudashi'].replace('\n','')) for m in ms2)
gd2=sum(len(m['text_gendaigoyaku'].replace('\n','')) for m in ms2)
assert kk2==kk0==d2['stats']['kakikudashi_chars_total'] and gd2==gd0==d2['stats']['gendaigoyaku_chars_total'], 'char drift (tags-only must be 0)'
for mid,tags in RETRO.items():
    for t in tags: assert t in mp2[mid]['tags'], ('missing',mid,t)
# rollback温存
assert '連動:sg08' in mp2['m549']['tags'] and '連動:sg27' in mp2['m719']['tags']
assert '引用形式:典籍曰く' in mp2['m506']['tags']
assert d2['stats']['from_corpus_dainichikyo-sho-vol20']==83
assert d2['schema_version']=='0.2' and len(d2['schema_history'])==295
print('=== %s: ASSERTS PASS ==='%('APPLY' if APPLY else 'DRY-RUN'))
print('connecting tags added:',added,' (total unchanged 4072)')
print('schema_history:',len(d2['schema_history']))
if APPLY:
    shutil.copy(MP,B+'/motifs_backup_pre_vol20_retrofit.json')
    open(MP,'w',encoding='utf-8').write(out)
    print('WROTE',MP)
else:
    print('(dry-run)')
