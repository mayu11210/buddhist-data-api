import re
raw = open('raw_body.txt', encoding='utf-8').read()
# 1. remove校勘 anchors
body = re.sub(r'\[(\d+|[A-Z]+\d*|＊)\]', '', raw)
# 2. 夾註 half-width parens -> 〔〕
body = body.replace('(', '〔').replace(')', '〕')
# 3. normalize lines
body = '\n'.join(s.strip() for s in body.split('\n') if s.strip())
# 4. header
HEADER = '大毘盧遮那成佛經疏卷第二　原典（大正蔵 No.1796, vol.39・CBETA 線上閱讀 T1796_002）'
genten = HEADER + '\n' + body
open('genten.txt','w',encoding='utf-8').write(genten)

P = 2305843009213693951
def poly(s, base):
    acc = 0
    for c in s:
        acc = (acc*base + ord(c)) % P
    return acc
def sumcp(s):
    return sum(ord(c) for c in s)

print('len', len(genten))
print('sum', sumcp(genten))
print('h131', poly(genten,131))
print('h1000003', poly(genten,1000003))
print('residualBrackets', len(re.findall(r'[\[\]]', genten)))
print('halfParens', len(re.findall(r'[()]', genten)))
print('fullBrackets', len(re.findall(r'[〔〕]', genten)))
print('lines', len(genten.split(chr(10))))
print('--- region h131 / sum ---')
for i in range(0, len(genten), 2000):
    sl = genten[i:i+2000]
    print(i, len(sl), poly(sl,131), sumcp(sl))
