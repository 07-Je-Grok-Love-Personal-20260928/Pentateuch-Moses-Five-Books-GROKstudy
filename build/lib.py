# -*- coding: utf-8 -*-
import json,re,html as _h,os
from bible import verses
CCI='/workspace/cci'
_h_=json.load(open(f'{CCI}/heidelberg.json'));_b=json.load(open(f'{CCI}/belgic.json'));_d=json.load(open(f'{CCI}/dort.json'));CR=json.load(open(f'{CCI}/creeds.json'))
HCQ={q['q']:dict(q,ld=l['number'],url=l.get('url')) for l in _h_['lordsdays'] for q in l['questions']}
BCA={a['number']:a for a in _b['articles']}
DH={'1':_d['heads'][0],'2':_d['heads'][1],'3-4':_d['heads'][2],'5':_d['heads'][3]}
USED=[]  # (kind, id, url, plain text) 供在线核对
def esc(s): return _h.escape(s,quote=False)
def sup(t): return re.sub(r'\^(\d+)',r'<sup>\1</sup>',esc(t))
def plain(t): return re.sub(r'\^\d+','',t)
def V(ref,show=None):
    """和合本经文（getbible.net 'cus' 简体和合本，构建时取得）"""
    parts=[r.strip() for r in ref.split(';')]
    t=''.join(verses(p) for p in parts)
    return f'<blockquote class="vs">{esc(t)}<cite>— {esc(show or ref)}（和合本）</cite></blockquote>'
def VI(ref): return f'「{esc(verses(ref))}」<span class="cs sm">（{esc(ref)}）</span>'
def HC(n,note=''):
    q=HCQ[n];USED.append(('HC',n,q['url'],plain(q['question'])+plain(q['answer'])))
    rf='；'.join(f'{i+1}. {r}' for i,r in enumerate(q['refs']))
    return (f'<div class="cq"><div class="h"><span class="tag">海德堡要理问答</span>第 {q["ld"]} 主日 · 第 {n} 问{(" · "+note) if note else ""}</div>'
            f'<div class="q">{sup(q["question"])}</div><div class="a">{sup(q["answer"]).replace(chr(10)+chr(10),"<br>")}</div>'
            +(f'<div class="rf">经文出处：{esc(rf)}</div>' if rf else '')+f'<div class="src">原文出处：<a href="{q["url"]}" target="_blank" rel="noopener">{q["url"]}</a></div></div>')
def BC(n,note='',paras=None):
    a=BCA[n];txt=a['text'];ps=txt.split('\n\n')
    if paras: ps=[ps[i] for i in paras]
    for p in ps: USED.append(('BC',n,a['url'],plain(p)))
    rf='；'.join(f'{i+1}. {r}' for i,r in enumerate(a['refs']))
    part='' if not paras else '（节录：第 '+'、'.join(str(i+1) for i in paras)+' 段）'
    return (f'<div class="cq"><div class="h"><span class="tag">比利时信条</span>{esc(a["title"])}{part}{(" · "+note) if note else ""}</div>'
            +''.join(f'<p class="a">{sup(p)}</p>' for p in ps)+(f'<div class="rf">经文出处：{esc(rf)}</div>' if rf and not paras else '')
            +f'<div class="src">原文出处：<a href="{a["url"]}" target="_blank" rel="noopener">{a["url"]}</a></div></div>')
def DT(h,n,note=''):
    hd=DH[h];a=[x for x in hd['articles'] if x['number']==int(n)][0]
    body=[l for l in a['text'].split('\n') if l.strip() and not l.startswith('- ')]
    for p in body: USED.append(('DT',f'{h}/{n}',a['url'],plain(p)))
    rf='；'.join(f'{i+1}. {r}' for i,r in enumerate(a['refs']))
    return (f'<div class="cq"><div class="h"><span class="tag">多特信经</span>{esc(hd["title"])} · {esc(a["title"])}{(" · "+note) if note else ""}</div>'
            +''.join(f'<p class="a">{sup(p)}</p>' for p in body)+(f'<div class="rf">经文出处：{esc(rf)}</div>' if rf else '')
            +f'<div class="src">原文出处：<a href="{a["url"]}" target="_blank" rel="noopener">{a["url"]}</a></div></div>')
def CQ(tag,title,text,url):
    """其他 ccifellowship.org 逐字摘引（如仪文）"""
    USED.append(('CCI',title,url,text))
    return f'<div class="cq"><div class="h"><span class="tag">{esc(tag)}</span>{esc(title)}</div><p class="a">{esc(text)}</p><div class="src">原文出处：<a href="{url}" target="_blank" rel="noopener">{url}</a></div></div>'
# ---------- 组件 ----------
def sec(id,icon,title,body,c1='#7c3aed',c2='#0ea5e9',no=''):
    return f'<section class="sec" id="{id}"><h2 data-t="{esc(title)}"><span class="ic" style="--c1:{c1};--c2:{c2}">{icon}</span><span>{title}</span>{f"<span class=no>{no}</span>" if no else ""}</h2>{body}</section>'
def h3(id,t): return f'<h3 id="{id}">{t}</h3>'
KIND={'key':('⭐','重点'),'hard':('🧩','难点'),'christ':('✝️','指向基督'),'cov':('🤝','圣约神学'),'app':('🌱','应用'),'bg':('🏺','真实背景'),'ane':('🌍','古代近东文化'),'mem':('🧠','记忆'),'conf':('📜','信条')}
def card(kind,title,body):
    ic,lab=KIND[kind]
    return f'<div class="card {kind}"><div class="ct0"><i>{ic}</i>{lab} · {title}</div>{body}</div>'
def grid(*cs,cls=''): return f'<div class="grid {cls}">{"".join(cs)}</div>'
def table(head,rows,stack=True):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td data-l="{esc(re.sub("<[^>]+>","",head[i]))}">{c}</td>' for i,c in enumerate(r))+'</tr>' for r in rows)
    return f'<div class="tw"><table class="{"st" if stack else ""}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
def tl(items,two=True):
    o=[]
    for it in items:
        y,t,desc,ref,c=(list(it)+[None]*5)[:5]
        o.append(f'<div class="it" style="--c:{c or "var(--gold)"}"><div class="yr">{y}</div><div class="tt">{t}</div><div>{desc}</div>{f"<div class=ref>📖 {ref}</div>" if ref else ""}</div>')
    return f'<div class="tl{" two" if two else ""}">{"".join(o)}</div>'
COL=['#f5c451','#fb923c','#ff6b8b','#a78bfa','#60a5fa','#2dd4bf','#4ade80','#f472b6']
def flow(steps):
    o=[]
    for i,s in enumerate(steps):
        t,desc,ref=(list(s)+[None]*3)[:3]
        o.append(f'<div class="st" style="--c:{COL[i%len(COL)]}"><b>{t}</b><span>{desc}</span>{f"<em>{ref}</em>" if ref else ""}</div>')
    return f'<div class="flow">{"".join(o)}</div>'
def mind(core,branches):
    o=[]
    for i,(t,leaves) in enumerate(branches):
        o.append(f'<div style="--c:{COL[i%len(COL)]}"><h5>{t}</h5><div class="lf">{"".join(f"<span>{l}</span>" for l in leaves)}</div></div>')
    return f'<div class="mind"><div class="core">{core}</div><div class="br">{"".join(o)}</div></div>'
def flash(cards):
    return '<div class="flash">'+''.join(f'<div class="fc" role="button" aria-label="记忆卡：{esc(re.sub("<[^>]+>","",a))}"><div class="in"><div class="fa">{a}<small>点按翻面</small></div><div class="fb">{b}</div></div></div>' for a,b in cards)+'</div>'
def quiz(items):
    o=['<div class="quiz"><div class="score"></div>']
    for q,ops,ans,ex in items:
        bt=''.join(f'<button type="button" data-k="{1 if i==ans else 0}">{"ABCD"[i]}. {op}</button>' for i,op in enumerate(ops))
        o.append(f'<div class="qz"><p>❓ {q}</p><div class="op">{bt}</div><div class="ex">💡 {ex}</div></div>')
    o.append('<button type="button" class="btn" data-a="reset">🔄 重新作答</button></div>')
    return ''.join(o)
def mn(t,s=''): return f'<div class="mn">{t}{f"<small>{s}</small>" if s else ""}</div>'
def fold(t,body,open_=False): return f'<details class="fold"{" open" if open_ else ""}><summary>{t}</summary><div>{body}</div></details>'
def chips(*cs): return '<div class="legend">'+''.join(f'<span class="chip {c}">{t}</span>' for t,c in cs)+'</div>'
LEGEND=chips(('⭐ 重点','g'),('🧩 难点','r'),('✝️ 指向基督','v'),('🤝 圣约','t'),('🏺 真实背景','s'),('🌍 近东文化','o'),('🌱 应用','n'),('📜 信条原文（CCI 逐字）',''))
def hero(kick,title,lead,fl=('📜','🔥','🐑'),extra=''):
    return f'<div class="kick">{kick}</div><h1>{title}</h1><p class="lead">{lead}</p>{extra}<div class="floaters">{"".join(f"<span>{x}</span>" for x in fl)}</div>'
def kv(pairs): return '<dl class="kv">'+''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in pairs)+'</dl>'
BKC=[('#b45309','#7c2d12'),('#be123c','#7f1d1d'),('#0f766e','#134e4a'),('#4338ca','#1e1b4b'),('#7e22ce','#3b0764'),('#0369a1','#0c4a6e'),('#a16207','#713f12')]
def big5(items): return '<div class="big5">'+''.join(f'<a href="{h}" style="--c1:{BKC[i%7][0]};--c2:{BKC[i%7][1]}"><span class="e">{e}</span><span class="t">{t}</span><span class="s">{s}</span></a>' for i,(h,e,t,s) in enumerate(items))+'</div>'
def P(*ps): return ''.join(f'<p>{p}</p>' for p in ps)
def UL(*xs): return '<ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
def hl(t,c='g'): return f'<mark class="{c}">{t}</mark>'
import glob as _g
_ALL=None
def _alltext():
    global _ALL
    if _ALL is None:
        _ALL=re.sub(r'\^\d+','',''.join(open(f,encoding='utf-8').read() for f in [f'{CCI}/heidelberg.json',f'{CCI}/belgic.json',f'{CCI}/dort.json',f'{CCI}/creeds.json']))
    return _ALL
def QI(text,url,label=''):
    """正文中内嵌的信条短语（逐字，纳入在线核对）"""
    if 'ccifellowship' in url: assert text in _alltext(), ('QI not found',text)
    USED.append(('INL',label or text[:12],url,text))
    return f'「<a class="qi" href="{url}" target="_blank" rel="noopener" title="CCI 原文">{esc(text)}</a>」'
def HCu(n): return HCQ[n]['url']
def BCu(n): return BCA[n]['url']
def DTu(h,n): return [x for x in DH[h]['articles'] if x['number']==int(n)][0]['url']
