import json,re,html,subprocess,datetime,collections
U=json.load(open('used.json'))
by=collections.defaultdict(list)
for k,i,u,t in U: by[u].append((k,i,t))
def fetch(u):
    r=subprocess.run(['curl','-sL','--max-time','40','-A','Mozilla/5.0 (GROKstudy verify)','-w','\n%{http_code}',u],capture_output=True,text=True)
    body,code=r.stdout.rsplit('\n',1); return int(code),body
def clean(h):
    h=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>','',h)
    h=re.sub(r'(?is)<sup[^>]*>.*?</sup>','',h)
    h=html.unescape(re.sub(r'<[^>]+>','',h))
    return re.sub(r'\s+','',h)
def ns(t): return re.sub(r'\s+','',re.sub(r'\^\d+','',t))
items=[];pages=0;bad=[]
for u,lst in by.items():
    code,b=fetch(u); pages+=1; c=clean(b) if code==200 else ''
    for k,i,t in lst:
        ok = code==200 and ns(t) in c
        if not ok and code==200 and k=='CREED':
            ok=all(ns(p) in c for p in re.split(r'\n\n',t) if p.strip())
        items.append(dict(kind=k,id=i,url=u,ok=ok,code=code))
        if not ok: bad.append((k,i,u,code,t[:60]))
now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
json.dump(dict(time=now,n=len(items),ok=sum(x['ok'] for x in items),pages=pages,items=items),open('verify.json','w'),ensure_ascii=False,indent=1)
print('pages',pages,'items',len(items),'ok',sum(x['ok'] for x in items))
for x in bad: print('BAD',x)
