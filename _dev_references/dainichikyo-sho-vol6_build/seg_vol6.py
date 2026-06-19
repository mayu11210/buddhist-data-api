from docx import Document
import json,re
d=Document('dainichi_vol6.docx')
nonempty=[p.text for p in d.paragraphs if p.text.strip()]
def norm(t):
    t=t.replace(' ','').replace('　','')
    t=re.sub(r'[0-9０-９]+','',t)
    return t.strip()
heads=[norm(nonempty[0]),norm(nonempty[1]),norm(nonempty[2])]
bodyparts=[norm(p) for p in nonempty[3:]]
body=''.join(bodyparts)
sents=[]; buf=''
for ch in body:
    buf+=ch
    if ch=='。': sents.append(buf); buf=''
if buf.strip(): sents.append(buf)
TARGET=480; MAXC=760; MINC=160
MARK=('経に','経いわく','経に云','経云','偈に','偈いわく','偈に云','偈云')
def starts_mark(s):
    s2=s.lstrip('　 ')
    return any(s2.startswith(m) for m in MARK)
paras=[]; cur=''
for s in sents:
    if cur and starts_mark(s) and len(cur)>=MINC: paras.append(cur); cur=s
    elif len(cur)+len(s)>MAXC and len(cur)>=MINC: paras.append(cur); cur=s
    elif len(cur)>=TARGET and len(cur)>=MINC: paras.append(cur); cur=s
    else: cur+=s
if cur.strip(): paras.append(cur)
final=[heads[0],heads[1],heads[2]]+paras
recon=''.join(final); orig=''.join(heads)+body
print('sentences',len(sents),'body paragraphs',len(paras),'total',len(final))
print('reconstruct match',recon==orig,'len',len(recon))
lens=[len(p) for p in paras]
print('body para len min/max/avg',min(lens),max(lens),sum(lens)//len(lens))
out=[{'id':'k%03d'%(i+1),'kakikudashi':t} for i,t in enumerate(final)]
json.dump(out,open('dainichi_vol6_paras.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
# parens check
allk=''.join(final)
print('全角（',allk.count('（'),'半角(',allk.count('('),'全角）',allk.count('）'),'半角)',allk.count(')'))
for o in out[:6]: print(o['id'],len(o['kakikudashi']),o['kakikudashi'][:34])
