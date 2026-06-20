from docx import Document
import json,re
d=Document('dainichi_vol10.docx')
nonempty=[p.text for p in d.paragraphs if p.text.strip()]
def norm(t):
    t=t.replace(' ','').replace('　','')
    t=re.sub(r'[0-9０-９]+','',t)
    return t.strip()
def is_struct(t):
    n=norm(t)
    if len(n)>=32: return False
    return ('経疏巻第' in n) or ('阿闍梨記' in n) or bool(re.search(r'品第[一二三四五六七八九十]',n)) or n.startswith('已上') or ('品終' in n)
# classify
items=[]  # (kind, normed_text)  kind in struct/body
for t in nonempty:
    items.append(('struct' if is_struct(t) else 'body', norm(t)))
TARGET=480; MAXC=760; MINC=160
MARK=('経に','経いわく','経に云','経云','偈に','偈いわく','偈に云','偈云')
def starts_mark(s):
    return any(s.startswith(m) for m in MARK)
def seg_body(body):
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
    return paras,sents
# walk: accumulate body blocks between structs
final=[]   # list of dict {struct:bool, text:..}
bodybuf=''
for kind,txt in items:
    if kind=='struct':
        if bodybuf:
            for p in seg_body(bodybuf)[0]: final.append({'struct':False,'text':p})
            bodybuf=''
        final.append({'struct':True,'text':txt})
    else:
        bodybuf+=txt
if bodybuf:
    for p in seg_body(bodybuf)[0]: final.append({'struct':False,'text':p})
# assign ids
for i,f in enumerate(final): f['id']='k%03d'%(i+1)
# reconstruction check
recon=''.join(f['text'] for f in final)
orig=''.join(norm(t) for t in nonempty)
print('paras total',len(final),'struct',sum(1 for f in final if f['struct']),'body',sum(1 for f in final if not f['struct']))
print('reconstruct match',recon==orig,'len',len(recon),'orig',len(orig))
lens=[len(f['text']) for f in final if not f['struct']]
print('body len min/max/avg',min(lens),max(lens),sum(lens)//len(lens))
allk=recon
print('全角（',allk.count('（'),'半角(',allk.count('('),'全角）',allk.count('）'),'半角)',allk.count(')'))
print('--- struct paras ---')
for f in final:
    if f['struct']: print(f['id'],f['text'])
json.dump(final,open('dainichi_vol10_paras.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
