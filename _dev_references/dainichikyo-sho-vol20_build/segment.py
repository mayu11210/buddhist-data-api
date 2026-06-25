# -*- coding: utf-8 -*-
import json, re

blocks = json.load(open('blocks_full.json'))  # keys p27yo,p28,p29,p30,p31,p31b

# structural segments (verbatim from doc)
STRUCT = [
    ("首題","首題","大毘盧遮那成仏神変加持経疏巻第二十"),
    ("撰号","撰号","沙門一行阿闍梨記"),
]
# 品題 verbatim text from doc (the short title blocks)
PIN = {
 'p27yo':  ("世出世護摩法品第二十七之余","世出世護摩法品第二十七之余"),
 'p28':    ("本尊三昧品第二十八","次本尊三昧品第二十八"),
 'p29':    ("無相三昧品第二十九","次無相三昧品第二十九"),
 'p30':    ("世出世持誦品第三十","次世出世持誦品第三十"),
 'p31':    ("囑累品第三十一","次囑累品第三十一"),
}
ORDER = ['p27yo','p28','p29','p30','p31','p31b']  # p31b continues 囑累品 (after image)

def normalize(t):
    # strip leading/trailing whitespace (half-width spaces, full, newlines), keep internal
    return t.strip(' 　\n\t\r')

def sentences(t):
    """Split into sentences keeping trailing '。 ' (or '。' at end). Do not split inside （）."""
    out=[]; buf=[]; depth=0
    i=0; n=len(t)
    while i<n:
        c=t[i]; buf.append(c)
        if c in '（(': depth+=1
        elif c in '）)': depth=max(0,depth-1)
        if c=='。' and depth==0:
            # include following spaces
            j=i+1
            sp=''
            while j<n and t[j] in ' 　':
                sp+=t[j]; j+=1
            buf.append(sp)
            out.append(''.join(buf)); buf=[]
            i=j; continue
        i+=1
    if buf:
        out.append(''.join(buf))
    return [s for s in out if s]

# 科文 markers that prefer a fresh segment start
HEADMARK = ('経に','経いわく','経云','復た次に','復次に','次に','又','問うて','問う','答えて','謂わく','所謂','いわく')
TARGET=430; HARD=720

def group(sents):
    segs=[]; cur=[]; curlen=0
    for s in sents:
        slen=len(s)
        # decide break BEFORE adding s
        if cur and curlen>=TARGET:
            head_here = any(s.lstrip(' 　').startswith(m) for m in HEADMARK)
            if head_here or curlen>=HARD:
                segs.append(''.join(cur)); cur=[]; curlen=0
        cur.append(s); curlen+=slen
    if cur: segs.append(''.join(cur))
    return segs

paras=[]  # (block_label, section_major, kakikudashi)
# structural
for sm,_sec,txt in STRUCT:
    paras.append((sm, sm, txt))

for lab in ORDER:
    if lab in PIN:
        pin_sm, pin_txt = PIN[lab]
        paras.append(("品題（%s）"%pin_sm, "品題（%s）"%pin_sm, pin_txt))
        sm = pin_sm
    else:
        # p31b continues 囑累品 -> section_major 囑累品第三十一, no new 品題
        sm = "囑累品第三十一"
    body = normalize(blocks[lab])
    sents = sentences(body)
    segs = group(sents)
    # verify reconstruction of this block
    assert ''.join(segs)==body, "RECON FAIL "+lab
    for s in segs:
        paras.append((sm, None, s))

# assign ids
sk=[]
for i,(sm,sec,kk) in enumerate(paras):
    sk.append({"seq":i+1,"section_major":sm,"section":sec,"kakikudashi":kk})

json.dump(sk, open('paras_skeleton.json','w'), ensure_ascii=False, indent=1)

# report
print("total segments:", len(sk))
from collections import Counter
print("per section_major:")
c=Counter(x['section_major'] for x in sk)
for k,v in c.items(): print(f"  {v:3d}  {k}")
# size distribution of body segments
bodylen=[len(x['kakikudashi']) for x in sk if x['section'] is None]
print("body seg count:", len(bodylen), "min",min(bodylen),"max",max(bodylen),"avg",sum(bodylen)//len(bodylen))
# paren balance check
bad=[x['seq'] for x in sk if x['kakikudashi'].count('（')!=x['kakikudashi'].count('）') or x['kakikudashi'].count('(')!=x['kakikudashi'].count(')')]
print("paren-imbalanced segs:", bad)
# half-width ( ) anywhere?
half=[x['seq'] for x in sk if '(' in x['kakikudashi'] or ')' in x['kakikudashi']]
print("segs with half-width parens:", half[:10], "count", len(half))
