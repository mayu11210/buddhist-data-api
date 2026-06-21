from docx import Document
import json,re
d=Document('dainichi_vol11.docx')
ne=[p.text for p in d.paragraphs if p.text.strip()]
def norm(t):
    t=t.replace(' ','').replace('　','')
    t=re.sub(r'[0-9０-９]+','',t)
    return t.strip()
heads=[norm(ne[0]),norm(ne[1])]
body=''.join(norm(p) for p in ne[2:])
# extract leading 品題
PRE='悉地出現品第六'
assert body.startswith(PRE), body[:20]
body=body[len(PRE):]
TARGET=480; MAXC=760; MINC=160
MARK=('経に','経いわく','経に云','経云','偈に','偈いわく','偈に云','偈云')
def starts_mark(s): return any(s.startswith(m) for m in MARK)
sents=[]; buf=''
for ch in body:
    buf+=ch
    if ch=='。': sents.append(buf); buf=''
if buf.strip(): sents.append(buf)
paras=[]; cur=''
for s in sents:
    if cur and starts_mark(s) and len(cur)>=MINC: paras.append(cur); cur=s
    elif len(cur)+len(s)>MAXC and len(cur)>=MINC: paras.append(cur); cur=s
    elif len(cur)>=TARGET and len(cur)>=MINC: paras.append(cur); cur=s
    else: cur+=s
if cur.strip(): paras.append(cur)
final=[{'struct':True,'text':heads[0]},{'struct':True,'text':heads[1]},{'struct':True,'text':PRE}]
for p in paras: final.append({'struct':False,'text':p})
for i,f in enumerate(final): f['id']='k%03d'%(i+1)
recon=''.join(f['text'] for f in final)
orig=heads[0]+heads[1]+PRE+body
print('paras total',len(final),'struct',sum(1 for f in final if f['struct']),'body',sum(1 for f in final if not f['struct']))
print('reconstruct match',recon==orig,'len',len(recon))
lens=[len(f['text']) for f in final if not f['struct']]
print('body len min/max/avg',min(lens),max(lens),sum(lens)//len(lens))
allk=recon
print('全角（',allk.count('（'),'半角(',allk.count('('),'全角）',allk.count('）'),'半角)',allk.count(')'))
for f in final[:3]: print(f['id'],f['text'])
json.dump(final,open('dainichi_vol11_paras.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
