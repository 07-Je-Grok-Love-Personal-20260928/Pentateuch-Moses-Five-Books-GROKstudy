(()=>{const d=document,b=d.body,H=d.documentElement,LS=localStorage;
const th=LS.getItem('p5-theme');if(th)H.dataset.theme=th;
const fs=LS.getItem('p5-fs');if(fs)H.style.setProperty('--fs',fs+'px');
const wide=()=>innerWidth>1024;
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(LS.getItem('p5-toc')==='off'&&wide())b.classList.add('toc-off');
/* 目录 */
const ol=d.getElementById('tocl'),hs=[...d.querySelectorAll('main section.sec>h2, main section.sec h3[id]')];
hs.forEach((h,i)=>{if(!h.id)h.id='s'+i;const li=d.createElement('li');li.className=h.tagName==='H2'?'l2':'l3';const a=d.createElement('a');a.href='#'+h.id;a.textContent=h.dataset.t||h.textContent.replace(/^\S+\s/,m=>/[\u{1F300}-\u{1FAFF}\u2600-\u27BF]/u.test(m)?'':m).replace(/\s*\d+\s*\/\s*\d+\s*$/,'').trim();li.appendChild(a);ol&&ol.appendChild(li)});
const links=ol?[...ol.querySelectorAll('a')]:[];
const q=d.getElementById('tocq');q&&q.addEventListener('input',()=>{const v=q.value.trim();links.forEach(a=>a.parentNode.style.display=!v||a.textContent.includes(v)?'':'none')});
links.forEach(a=>a.addEventListener('click',()=>{if(!wide())b.classList.remove('toc-open')}));
const tg=()=>{if(wide()){b.classList.toggle('toc-off');LS.setItem('p5-toc',b.classList.contains('toc-off')?'off':'on')}else b.classList.toggle('toc-open')};
d.querySelectorAll('[data-a=toc]').forEach(x=>x.addEventListener('click',tg));
d.querySelector('.scrim')?.addEventListener('click',()=>b.classList.remove('toc-open'));
d.querySelector('[data-a=theme]')?.addEventListener('click',()=>{const n=H.dataset.theme==='light'?'dark':'light';H.dataset.theme=n;LS.setItem('p5-theme',n)});
d.querySelectorAll('[data-a=fs]').forEach(x=>x.addEventListener('click',()=>{let c=parseFloat(getComputedStyle(H).getPropertyValue('--fs'))||17;c=Math.min(22,Math.max(14,c+(+x.dataset.v)));H.style.setProperty('--fs',c+'px');LS.setItem('p5-fs',c)}));
/* 滚动：进度 / 回顶 / 高亮 —— rAF + passive */
const pr=d.querySelector('.prog'),tt=d.querySelector('.totop');let tick=0;
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){const id=e.target.id;links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+id));const on=ol&&ol.querySelector('a.on');if(on&&!b.classList.contains('toc-open')&&wide()){const r=on.getBoundingClientRect(),t=ol.closest('.toc').getBoundingClientRect();if(r.top<t.top+60||r.bottom>t.bottom-20)on.scrollIntoView({block:'nearest'})}}})},{rootMargin:'-15% 0px -75% 0px'});
hs.forEach(h=>io.observe(h));
addEventListener('scroll',()=>{if(tick)return;tick=requestAnimationFrame(()=>{tick=0;const m=H.scrollHeight-innerHeight;pr&&(pr.style.width=(m>0?scrollY/m*100:0)+'%');tt&&tt.classList.toggle('on',scrollY>600)})},{passive:true});
tt&&tt.addEventListener('click',()=>scrollTo({top:0,behavior:reduce?'auto':'smooth'}));
/* 出现动画（尊重减少动态；只使用 transform/opacity） */
if(reduce){d.querySelectorAll('.rv').forEach(x=>x.classList.add('in'))}
else{
  const rv=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');rv.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
  d.querySelectorAll('.card,.tl .it,.flow .st,.mind .br>div,.big5 a,.cq,.vs,.call,.mapblock,.scene').forEach(x=>{x.classList.add('rv');rv.observe(x)});
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
