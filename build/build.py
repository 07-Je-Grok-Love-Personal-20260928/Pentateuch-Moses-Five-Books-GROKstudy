# -*- coding: utf-8 -*-
import os,re,json,importlib,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import lib,tpl
from bible import verses
OUT='../site'
MODS={'index.html':'p_index','genesis.html':'p_genesis','exodus.html':'p_exodus','leviticus.html':'p_leviticus','numbers.html':'p_numbers','deuteronomy.html':'p_deuteronomy','covenant.html':'p_covenant','atlas.html':'p_atlas','creeds.html':'p_creeds','confessions.html':'p_confessions','memory.html':'p_memory','sources.html':'p_sources'}
warn=[]
def norm(s): return re.sub(r'[\s，。；：、！？「」『』“”‘’―…—,.;:!?()（）《》·]','',s)
DEF={'genesis.html':'创','exodus.html':'出','leviticus.html':'利','numbers.html':'民','deuteronomy.html':'申'}
BK='(?:创|出|利|民|申|书|士|王上|王下|诗|赛|耶|何|太|可|路|约壹|约|徒|罗|林前|林后|加|弗|西|来|彼前|彼后|启|雅)'
def lint(fn,html):
    txt=re.sub(r'<[^>]+>','',html)
    for m in re.finditer(r'「([^「」]{4,160})」[^「」（]{0,3}（('+BK+r'?)(\d+:\d+(?:[-–]\d+)?)[^）]*）',txt):
        bk=m[2] or DEF.get(fn)
        if not bk: continue
        q,ref=m[1],bk+m[3].replace('–','-')
        try: v=verses(ref)
        except Exception as e: warn.append((fn,ref,q,'ERR '+str(e)));continue
        vv=norm(re.sub(r'（[^）]*）','',v)); parts=[norm(p) for p in re.split(r'……|…',q) if norm(p)]
        pos=0;ok=True
        for p in parts:
            i=vv.find(p,pos)
            if i<0: ok=False;break
            pos=i+len(p)
        if not ok: warn.append((fn,ref,q,v[:90]))
for fn,mod in MODS.items():
    m=importlib.import_module(mod)
    body=m.build_body() if hasattr(m,'build_body') else m.BODY
    h=tpl.page(fn,m.TITLE,m.DESC,m.HERO,body)
    lint(fn,h)
    open(f'{OUT}/{fn}','w',encoding='utf-8').write(h)
    print(fn,len(h))
json.dump(lib.USED,open('used.json','w'),ensure_ascii=False,indent=0)
print('USED',len(lib.USED)); print('LINT',len(warn))
for w in warn: print(' ',w)
