from docx import Document
import json,re
d=Document('dainichi_vol5.docx')
nonempty=[p.text for p in d.paragraphs if p.text.strip()]
# normalize: strip half-width spaces, remove stray digit artifacts (none expected)
def norm(t):
    t=t.replace(' ','')  # half-width space
    t=t.replace('　','')  # full-width (none)
    t=re.sub(r'[0-9０-９]+','',t)
    return t.strip()
heads=[norm(nonempty[0]),norm(nonempty[1]),norm(nonempty[2])]
print('heads:',heads)
bodyparts=[norm(p) for p in nonempty[3:]]
body=''.join(bodyparts)
print('body chars',len(body))
# sentence split on 。 keeping 。; also handle 」。 etc -> split after 。
sents=[]
buf=''
for ch in body:
    buf+=ch
    if ch=='。':
        sents.append(buf); buf=''
if buf.strip(): sents.append(buf)
print('sentences',len(sents))
# group into paragraphs ~480, force-cut before 経/偈 markers
TARGET=480; MAXC=760; MINC=160
MARK=('経に','経いわく','経に云','偈に','偈いわく','偈に云','経云','偈云')
paras=[]; cur=''
def starts_mark(s):
    s2=s.lstrip('　 ')
    return any(s2.startswith(m) for m in MARK)
for s in sents:
    if cur and starts_mark(s) and len(cur)>=MINC:
        paras.append(cur); cur=s
    elif len(cur)+len(s)>MAXC and len(cur)>=MINC:
        paras.append(cur); cur=s
    elif len(cur)>=TARGET and len(cur)>=MINC:
        paras.append(cur); cur=s
    else:
        cur+=s
if cur.strip(): paras.append(cur)
print('body paragraphs',len(paras))
# assemble final with headers
final=[heads[0],heads[1],heads[2]]+paras
# verify reconstruction == normalized original (heads+body)
recon=''.join(final)
orig=''.join(heads)+body
print('reconstruct match', recon==orig, 'recon len',len(recon),'orig len',len(orig))
lens=[len(p) for p in paras]
print('body para len min/max/avg',min(lens),max(lens),sum(lens)//len(lens))
# save paras.json
out=[]
for i,t in enumerate(final):
    out.append({'id':'k%03d'%(i+1),'kakikudashi':t})
json.dump(out,open('dainichi_vol5_paras.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('total paragraphs',len(out))
# show head of each for outline planning
for o in out[:6]:
    print(o['id'],len(o['kakikudashi']),o['kakikudashi'][:40])
