# -*- coding: utf-8 -*-
import html as _h
VERSION='v1.0.0'; DATE='2026-10-23'; TAG='v1.0.0-20261023'
SLUG='pentateuch-20261023-v1-grokstudy'
PAGES=[('index.html','🏠','总览'),('genesis.html','🌅','创世记'),('exodus.html','🔥','出埃及记'),('leviticus.html','🐑','利未记'),('numbers.html','🏕️','民数记'),('deuteronomy.html','📜','申命记'),
('covenant.html','🤝','圣约神学'),('atlas.html','🗺️','地图·时间线'),('creeds.html','✝️','三大信经'),('confessions.html','📚','信条与五经'),('memory.html','🧠','记忆中心'),('sources.html','🔗','来源')]
def page(fn,title,desc,hero,body):
    nav=''.join(f'<a href="{f}"{" class=on" if f==fn else ""}>{i} {t}</a>' for f,i,t in PAGES)
    pl=''.join(f'<a href="{f}"{" class=on" if f==fn else ""}><span>{i}</span>{t}</a>' for f,i,t in PAGES)
    idx=[p[0] for p in PAGES].index(fn)
    prv=PAGES[idx-1] if idx>0 else None; nxt=PAGES[idx+1] if idx<len(PAGES)-1 else None
    pager='<nav class="pager">'+(f'<a href="{prv[0]}"><small>← 上一页</small>{prv[1]} {prv[2]}</a>' if prv else '<span></span>')+(f'<a class="nx" href="{nxt[0]}"><small>下一页 →</small>{nxt[1]} {nxt[2]}</a>' if nxt else '')+'</nav>'
    return f'''<!doctype html><html lang="zh-CN" data-theme="dark"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{_h.escape(title)} · 摩西五经 GROKstudy</title><meta name="description" content="{_h.escape(desc)}">
<meta name="theme-color" content="#0d1430"><link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
<link rel="stylesheet" href="assets/site.css?v={VERSION}"><script>try{{var t=localStorage.getItem('p5-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script></head>
<body><header class="top"><button class="tb" data-a="toc" aria-label="显示/隐藏目录" title="目录（快捷键 T）">☰</button>
<a class="brand" href="index.html"><b>摩西五经</b><small>GROKstudy · 欧陆改革宗</small></a><nav class="pnav" aria-label="页面">{nav}</nav>
<button class="tb" data-a="focus" title="只看重点/难点/基督卡片" aria-label="只看重点">🎯</button><button class="tb" data-a="fs" data-v="-1" aria-label="缩小字号">A-</button><button class="tb" data-a="fs" data-v="1" aria-label="放大字号">A+</button><button class="tb" data-a="theme" aria-label="切换明暗主题">🌓</button></header>
<div class="prog"></div><aside class="toc" aria-label="目录"><h4><span>📑 本页目录</span><button class="tb" data-a="toc" style="width:30px;height:30px;font-size:14px" aria-label="收起目录">⟨</button></h4>
<input id="tocq" type="search" placeholder="🔍 筛选目录…" aria-label="筛选目录"><ol id="tocl"></ol><div class="pages"><h4>🧭 全站页面</h4>{pl}</div></aside><div class="scrim"></div>
<main id="main"><div class="hero">{hero}</div>{body}{pager}
<footer>📜 摩西五经 · 欧陆改革宗深度解读 · <span class="ver">{SLUG}</span> · {VERSION}（{DATE}，台北时间）<br>
信经与三项联合信条原文逐字取自 <a href="https://ccifellowship.org" target="_blank" rel="noopener">ccifellowship.org</a>（基督教华人网络团契《敬拜手册》）；经文为和合本。本站为学习用途的个人整理，解读文字为本站概括。<br>
<a href="sources.html">🔗 来源与核对报告</a> · 快捷键：T 目录 · 🎯 只看重点</footer></main>
<button class="totop" aria-label="回到顶部">↑</button><script src="assets/site.js?v={VERSION}" defer></script></body></html>'''
