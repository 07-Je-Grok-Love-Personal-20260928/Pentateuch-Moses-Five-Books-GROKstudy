(()=>{const d=document,b=d.body,H=d.documentElement,LS=localStorage;
const th=LS.getItem('p5-theme');if(th)H.dataset.theme=th;
const fs=LS.getItem('p5-fs');if(fs)H.style.setProperty('--fs',fs+'px');
const wide=()=>innerWidth>1024;
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(reduce)H.classList.add('rm');
if(!reduce&&matchMedia('(min-width:701px)').matches)H.classList.add('float-ok');
if(LS.getItem('p5-toc')==='off'&&wide())b.classList.add('toc-off');

const CN='一二三四五六七八九十';
const cn=n=>n<=10?CN[n-1]+'、':n+'、';
const ol=d.getElementById('tocl');
const pages=[...d.querySelectorAll('nav.pnav a')].map(a=>({href:a.getAttribute('href'),title:(a.getAttribute('title')||a.textContent||'').replace(/^[^\s]*\s/,'').trim()||a.textContent.trim(),cur:a.classList.contains('on')}));
const here=(location.pathname.split('/').pop()||'index.html');
function row(href,num,text,cls){
  const li=d.createElement('li');if(cls)li.className=cls;
  const r=d.createElement('div');r.className='row';
  const a=d.createElement('a');a.href=href;
  a.innerHTML='<span class="tx"><span class="nm"></span></span>';
  a.querySelector('.nm').textContent=num||'';
  a.querySelector('.tx').append(text);
  a.title=(num||'')+' '+text;
  r.appendChild(a);li.appendChild(r);return {li,a,r};
}
function kidsOf(li){
  let k=li.querySelector(':scope > .kids');
  if(!k){k=d.createElement('div');k.className='kids';const inn=d.createElement('ol');inn.className='in';k.appendChild(inn);li.appendChild(k)}
  return k.querySelector('.in');
}
function twisty(li,open){
  if(li.querySelector(':scope > .row > .twisty'))return;
  const t=d.createElement('button');t.className='twisty';t.type='button';t.textContent='▾';
  t.setAttribute('aria-expanded',open?'true':'false');
  t.setAttribute('aria-label',open?'折叠':'展开');
  li.querySelector('.row').insertBefore(t,li.querySelector('a'));
  li.classList.toggle('open',!!open);
  t.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();
    const on=!li.classList.contains('open');li.classList.toggle('open',on);
    t.setAttribute('aria-expanded',on?'true':'false');t.setAttribute('aria-label',on?'折叠':'展开')});
}
if(ol){
  pages.forEach((p,i)=>{
    const isCur=(p.href===here)||(p.cur);
    const {li,a}=row(p.href,cn(i+1),p.title,'l1'+(isCur?' cur':''));
    if(isCur)a.classList.add('here');
    ol.appendChild(li);
    if(!isCur)return;
    const parts=[...d.querySelectorAll('main section.part')];
    parts.forEach((part,pi)=>{
      const h2=part.querySelector(':scope > h2');if(!h2)return;
      if(!h2.id)h2.id=part.id||('p'+(pi+1));
      const pnum=(i+1)+'.'+(pi+1);
      const {li:l2,a:a2}=row('#'+h2.id,pnum,h2.dataset.t||h2.textContent.trim(),'l2');
      kidsOf(li).appendChild(l2);
      const secs=[...part.querySelectorAll(':scope > section.sec')];
      const leaves=[];
      secs.forEach((sec,si)=>{
        const h3=sec.querySelector(':scope > h3');if(!h3)return;
        if(!h3.id)h3.id=sec.id||('s'+pi+'-'+si);
        const h4s=[...sec.querySelectorAll(':scope h4[id], :scope h4[data-t]')];
        h4s.forEach((h,k)=>{if(!h.id)h.id='h4-'+pi+'-'+si+'-'+k});
        if(h4s.length){
          h4s.forEach(h=>leaves.push({el:h,t:h.dataset.t||h.textContent.trim()}));
        }else{
          leaves.push({el:h3,t:h3.dataset.t||h3.textContent.trim()});
        }
      });
      leaves.forEach((lf,k)=>{
        const num=pnum+'.'+(k+1);
        const {li:l3}=row('#'+lf.el.id,num,lf.t,'l3');
        kidsOf(l2).appendChild(l3);
      });
      if(l2.querySelector('.kids'))twisty(l2,true);
    });
    if(li.querySelector('.kids'))twisty(li,true);
  });
}
const links=ol?[...ol.querySelectorAll('a')]:[];
const q=d.getElementById('tocq');
q&&q.addEventListener('input',()=>{
  const v=q.value.trim();
  ol.querySelectorAll('li').forEach(li=>{
    const hit=!v||li.querySelector(':scope > .row a')?.textContent.includes(v)||[...li.querySelectorAll('a')].some(a=>a.textContent.includes(v));
    li.style.display=hit?'':'none';
    if(v&&hit){let n=li;while(n&&n!==ol){if(n.matches&&n.matches('li'))n.classList.add('open');n=n.parentElement}}
  });
});
links.forEach(a=>a.addEventListener('click',()=>{if(!wide())b.classList.remove('toc-open')}));
const tg=()=>{if(wide()){b.classList.toggle('toc-off');LS.setItem('p5-toc',b.classList.contains('toc-off')?'off':'on')}else b.classList.toggle('toc-open')};
d.querySelectorAll('[data-a=toc]').forEach(x=>x.addEventListener('click',tg));
d.querySelector('[data-a=toc-all]')?.addEventListener('click',()=>{
  const items=[...ol.querySelectorAll('li')].filter(li=>li.querySelector(':scope > .kids'));
  const open=items.some(li=>!li.classList.contains('open'));
  items.forEach(li=>{li.classList.toggle('open',open);const t=li.querySelector(':scope > .row > .twisty');if(t){t.setAttribute('aria-expanded',open?'true':'false')}});
});
d.querySelector('.scrim')?.addEventListener('click',()=>b.classList.remove('toc-open'));

/* 目录横向拖宽 */
const MINW=200,MAXW=()=>Math.min(Math.floor(innerWidth*.8),640);
const setTocW=n=>{n=Math.round(Math.min(MAXW(),Math.max(MINW,n)));H.style.setProperty('--toc',n+'px');try{LS.setItem('p5-tocw',n)}catch(e){}return n};
const rz=d.querySelector('.toc-resizer');
if(rz){
  let startX=0,startW=0,pid=null;
  const widthNow=()=>parseFloat(getComputedStyle(H).getPropertyValue('--toc'))||300;
  const down=e=>{
    if(e.pointerType==='mouse'&&e.button!==0)return;
    e.preventDefault();
    startX=e.clientX;startW=widthNow();pid=e.pointerId;
    try{rz.setPointerCapture(pid)}catch(err){}
    b.classList.add('toc-drag');
  };
  const move=e=>{if(!b.classList.contains('toc-drag'))return;if(pid!==null&&e.pointerId!==pid)return;setTocW(startW+(e.clientX-startX))};
  const up=e=>{if(pid!==null&&e.pointerId!==pid)return;b.classList.remove('toc-drag');pid=null};
  rz.addEventListener('pointerdown',down);
  rz.addEventListener('pointermove',move);
  rz.addEventListener('pointerup',up);
  rz.addEventListener('pointercancel',up);
  rz.addEventListener('keydown',e=>{
    if(e.key==='ArrowLeft'){e.preventDefault();setTocW(widthNow()-16)}
    if(e.key==='ArrowRight'){e.preventDefault();setTocW(widthNow()+16)}
    if(e.key==='Home'){e.preventDefault();setTocW(MINW)}
    if(e.key==='End'){e.preventDefault();setTocW(MAXW())}
  });
}

d.querySelector('[data-a=theme]')?.addEventListener('click',()=>{const n=H.dataset.theme==='light'?'dark':'light';H.dataset.theme=n;LS.setItem('p5-theme',n)});
d.querySelectorAll('[data-a=fs]').forEach(x=>x.addEventListener('click',()=>{let c=parseFloat(getComputedStyle(H).getPropertyValue('--fs'))||17;c=Math.min(22,Math.max(14,c+(+x.dataset.v)));H.style.setProperty('--fs',c+'px');LS.setItem('p5-fs',c)}));

/* 滚动：进度 / 回顶 / 高亮 —— rAF + passive */
const pr=d.querySelector('.prog'),tt=d.querySelector('.totop');let tick=0;
const heads=[...d.querySelectorAll('main section.part>h2, main section.sec>h3, main h4[id]')];
const expandBranch=a=>{
  let n=a.closest('li');
  while(n&&n!==ol){if(n.matches&&n.matches('li')){n.classList.add('open');const t=n.querySelector(':scope > .row > .twisty');if(t)t.setAttribute('aria-expanded','true')}n=n.parentElement}
};
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){
  const id=e.target.id;links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+id));
  const on=ol&&ol.querySelector('a.on');
  if(on){expandBranch(on);const nav=ol.closest('.tocnav')||ol;const r=on.getBoundingClientRect(),t=nav.getBoundingClientRect();if(r.top<t.top+8||r.bottom>t.bottom-8)on.scrollIntoView({block:'nearest'})}
}})},{rootMargin:'-15% 0px -75% 0px'});
heads.forEach(h=>io.observe(h));
addEventListener('scroll',()=>{if(tick)return;tick=requestAnimationFrame(()=>{tick=0;const m=H.scrollHeight-innerHeight;pr&&(pr.style.width=(m>0?scrollY/m*100:0)+'%');tt&&tt.classList.toggle('on',scrollY>600)})},{passive:true});
tt&&tt.addEventListener('click',()=>scrollTo({top:0,behavior:reduce?'auto':'smooth'}));

/* 出现动画：更少观察目标 */
if(reduce){d.querySelectorAll('.rv').forEach(x=>x.classList.add('in'))}
else{
  const rv=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');rv.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
  d.querySelectorAll('.card,.tl .it,.scene,.mapblock,.flow').forEach(x=>{x.classList.add('rv');rv.observe(x)});
  setTimeout(()=>d.querySelectorAll('.rv:not(.in)').forEach(x=>{const r=x.getBoundingClientRect();if(r.top<innerHeight)x.classList.add('in')}),60);
}

/* 翻转卡 */
d.querySelectorAll('.fc').forEach(c=>{c.tabIndex=0;const f=()=>c.classList.toggle('flip');c.addEventListener('click',f);c.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();f()}})});
d.querySelectorAll('[data-a=flipall]').forEach(x=>x.addEventListener('click',()=>{const cs=x.closest('section').querySelectorAll('.fc');const any=[...cs].some(c=>!c.classList.contains('flip'));cs.forEach(c=>c.classList.toggle('flip',any))}));
/* 测验 */
d.querySelectorAll('.quiz').forEach(Z=>{const sc=Z.querySelector('.score');let ok=0,n=0;const up=()=>sc&&(sc.innerHTML='✅ 答对 '+ok+' / 已答 '+n+' / 共 '+Z.querySelectorAll('.qz').length);up();
Z.querySelectorAll('.qz').forEach(Q=>Q.querySelectorAll('.op button').forEach(B=>B.addEventListener('click',()=>{if(Q.classList.contains('done'))return;Q.classList.add('done');n++;if(B.dataset.k==='1'){B.classList.add('ok');ok++}else{B.classList.add('no');Q.querySelector('[data-k="1"]').classList.add('ok')}up()})));
Z.querySelector('[data-a=reset]')?.addEventListener('click',()=>{ok=n=0;Z.querySelectorAll('.qz').forEach(Q=>{Q.classList.remove('done');Q.querySelectorAll('button').forEach(B=>B.classList.remove('ok','no'))});up()})});
/* 信经背诵 */
d.querySelectorAll('.creedbox').forEach(X=>{const C=X.querySelector('.creed');
X.querySelectorAll('[data-m]').forEach(B=>B.addEventListener('click',()=>{const m=B.dataset.m;
if(m==='mask'||m==='first'){const on=!C.classList.contains(m);C.classList.remove('mask','first');X.querySelectorAll('[data-m=mask],[data-m=first]').forEach(y=>y.classList.remove('on'));if(on){C.classList.add(m);B.classList.add('on')}C.querySelectorAll('.cl.show').forEach(l=>l.classList.remove('show'))}
if(m==='big'||m==='small'){let v=parseFloat(getComputedStyle(C).getPropertyValue('--cfs'))||20;v=Math.min(30,Math.max(15,v+(m==='big'?2:-2)));C.style.setProperty('--cfs',v+'px')}
if(m==='speak'){if(!('speechSynthesis' in window)){alert('此浏览器不支持朗读');return}if(speechSynthesis.speaking){speechSynthesis.cancel();B.classList.remove('on');return}
const u=new SpeechSynthesisUtterance([...C.querySelectorAll('.cl')].map(l=>l.textContent).join('。'));u.lang='zh-CN';u.rate=.9;u.onend=()=>B.classList.remove('on');B.classList.add('on');speechSynthesis.speak(u)}
if(m==='copy'){navigator.clipboard?.writeText([...C.querySelectorAll('.cl')].map(l=>l.textContent).join('\n')).then(()=>{B.textContent='✅ 已复制';setTimeout(()=>B.textContent='📋 复制全文',1500)})}}));
C.addEventListener('click',e=>{const l=e.target.closest('.cl');if(l&&C.classList.contains('mask'))l.classList.toggle('show')})});
d.querySelectorAll('[data-a=say]').forEach(B=>B.addEventListener('click',()=>{if(!('speechSynthesis' in window))return;if(speechSynthesis.speaking){speechSynthesis.cancel();return}const t=d.querySelector(B.dataset.t);if(!t)return;const u=new SpeechSynthesisUtterance(t.innerText);u.lang='zh-CN';u.rate=.95;speechSynthesis.speak(u)}));
d.querySelector('[data-a=focus]')?.addEventListener('click',e=>{b.classList.toggle('focus');e.currentTarget.classList.toggle('on')});
addEventListener('keydown',e=>{if(e.target.matches('input,textarea,select'))return;if(e.key==='t'||e.key==='T')tg();if(e.key==='Escape')b.classList.remove('toc-open')});

/* 悬停预取 */
const prefetched=new Set();
const prefetch=href=>{if(!href||prefetched.has(href)||!href.endsWith('.html'))return;prefetched.add(href);const l=d.createElement('link');l.rel='prefetch';l.href=href;d.head.appendChild(l)};
d.querySelectorAll('a[href$=".html"]').forEach(a=>{
  const go=()=>prefetch(a.getAttribute('href'));
  a.addEventListener('pointerenter',go,{passive:true});
  a.addEventListener('focus',go);
});

/* ===== 地图页卡 ===== */
d.querySelectorAll('.maptabs').forEach(box=>{
  const btns=[...box.querySelectorAll('.tabbar button')];
  const panes=[...box.querySelectorAll('.tabp')];
  btns.forEach(btn=>btn.addEventListener('click',()=>{
    btns.forEach(b=>b.classList.toggle('on',b===btn));
    panes.forEach(p=>p.classList.toggle('on',p.dataset.tab===btn.dataset.tab));
    if(btn.dataset.tab==='live'){const lb=box.querySelector('.livebox');if(lb)initLive(lb)}
  }));
});

/* ===== 点击播放视频 ===== */
d.querySelectorAll('.yt').forEach(fig=>{
  const btn=fig.querySelector('.ytbtn');if(!btn)return;
  btn.addEventListener('click',()=>{
    const id=fig.dataset.yt;if(!id)return;
    const f=d.createElement('iframe');
    f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';
    f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.allowFullscreen=true;f.title=btn.getAttribute('aria-label')||'视频';
    btn.replaceWith(f);
  });
});

/* ===== Leaflet 懒加载 + 多源底图 + 自动换源 ===== */
let leafletP=null;
function loadLeaflet(){
  if(window.L)return Promise.resolve();
  if(leafletP)return leafletP;
  leafletP=new Promise((res,rej)=>{
    const css=d.createElement('link');css.rel='stylesheet';css.href='assets/vendor/leaflet/leaflet.css';
    const js=d.createElement('script');js.src='assets/vendor/leaflet/leaflet.js';js.onload=()=>res();js.onerror=rej;
    d.head.append(css);d.body.append(js);
  });
  return leafletP;
}
const COL={gold:'#f5c451',rose:'#ff6b8b',vio:'#a78bfa',teal:'#2dd4bf',green:'#4ade80',blue:'#60a5fa',amb:'#fbbf24',orange:'#fb923c',pink:'#f472b6',red:'#f87171',purple:'#a78bfa',gray:'#94a3b8'};
function initLive(box){
  if(box.dataset.ready==='1'||box.dataset.busy==='1'){
    if(box._map)setTimeout(()=>box._map.invalidateSize(),80);
    return;
  }
  box.dataset.busy='1';
  const stat=box.querySelector('.livestat');
  const pane=box.querySelector('.livepane');
  const sel=box.querySelector('.tilesel');
  let data={}, tiles=[];
  try{data=JSON.parse(box.dataset.live||'{}');tiles=JSON.parse(box.dataset.tiles||'[]')}catch(e){stat&&(stat.textContent='地图数据无法解析');return}
  const pick=id=>tiles.find(t=>t.id===id)||tiles[0];
  loadLeaflet().then(()=>{
    const L=window.L;
    L.Icon.Default.imagePath='assets/vendor/leaflet/images/';
    const map=L.map(pane,{scrollWheelZoom:false,attributionControl:true});
    box._map=map;
    if(data.bounds) map.fitBounds(data.bounds,{padding:[16,16],maxZoom:data.zoom||8});
    else map.setView(data.center||[31.5,35.2],data.zoom||7);
    let layer=null, srcIdx=tiles.findIndex(t=>t.id===sel.value); if(srcIdx<0)srcIdx=0;
    let fail=0, switching=false;
    const setSrc=(i,reason)=>{
      if(!tiles.length)return;
      i=((i%tiles.length)+tiles.length)%tiles.length;
      srcIdx=i; const t=tiles[i];
      if(sel&&sel.value!==t.id)sel.value=t.id;
      if(layer) map.removeLayer(layer);
      const opts={attribution:t.attr||'',maxZoom:19};
      if(t.sub)opts.subdomains=t.sub;
      layer=L.tileLayer(t.url,opts);
      fail=0; switching=false;
      layer.on('tileerror',()=>{
        fail++;
        if(!switching&&fail>=4){switching=true;const n=(srcIdx+1)%tiles.length;
          stat&&(stat.textContent='「'+(tiles[srcIdx].name)+'」加载失败，正在切换「'+tiles[n].name+'」…');
          setSrc(n,'fallback')}
      });
      layer.on('load',()=>{stat&&(stat.textContent='当前底图：'+t.name+(reason==='fallback'?'（已自动换源）':'')+' · 可在菜单中切换')});
      layer.addTo(map);
    };
    setSrc(srcIdx);
    sel&&sel.addEventListener('change',()=>setSrc(tiles.findIndex(t=>t.id===sel.value)));
    (data.routes||[]).forEach(r=>{
      const c=COL[r.c]||r.c||'#f5c451';
      L.polyline(r.pts,{color:c,weight:r.dash?2.5:3.5,dashArray:r.dash?'7 6':'',opacity:.9}).addTo(map);
    });
    (data.markers||[]).forEach(m=>{
      const c=COL[m.c]||'#60a5fa';
      const icon=L.divIcon({className:'',html:`<div style="width:${m.hl?16:12}px;height:${m.hl?16:12}px;border-radius:50%;background:${c};border:2px solid #fff;box-shadow:0 0 0 2px ${c}"></div>`,iconSize:[16,16],iconAnchor:[8,8]});
      const html=`<b>${m.n}</b> ${m.en?('<i>'+m.en+'</i>'):''}<br>${m.y||''}<br>${m.t||''}`;
      L.marker([m.lat,m.lon],{icon}).addTo(map).bindPopup(html);
    });
    box.dataset.ready='1';box.dataset.busy='0';
    setTimeout(()=>map.invalidateSize(),120);
  }).catch(()=>{box.dataset.busy='0';stat&&(stat.textContent='实时地图库未能加载。请改看离线示意图或地理底图。')});
}
const liveIO=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){const tab=e.target.closest('.tabp');if(!tab||tab.classList.contains('on')) initLive(e.target);liveIO.unobserve(e.target)}})},{rootMargin:'80px'});
d.querySelectorAll('.livebox').forEach(x=>liveIO.observe(x));
})();
