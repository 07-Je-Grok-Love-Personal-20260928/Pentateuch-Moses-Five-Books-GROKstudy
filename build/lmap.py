# -*- coding: utf-8 -*-
"""Live Leaflet maps (lazy, multi-source, auto fallback) + tabbed map block."""
import json,html as _h
import maps, schematic, rmap

TILES=[
    dict(id='carto-v',name='CARTO Voyager',url='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',sub='abcd',attr='© OpenStreetMap © CARTO'),
    dict(id='osm',name='OpenStreetMap',url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',sub='abc',attr='© OpenStreetMap contributors'),
    dict(id='hot',name='Humanitarian OSM',url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',sub='abc',attr='© OpenStreetMap, Humanitarian OSM Team'),
    dict(id='carto-l',name='CARTO 浅色',url='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',sub='abcd',attr='© OpenStreetMap © CARTO'),
    dict(id='carto-d',name='CARTO 深色',url='https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',sub='abcd',attr='© OpenStreetMap © CARTO'),
    dict(id='esri-img',name='Esri 卫星影像',url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',sub='',attr='Tiles © Esri'),
    dict(id='esri-topo',name='Esri 地形图',url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',sub='',attr='Tiles © Esri'),
    dict(id='esri-street',name='Esri 街道图',url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',sub='',attr='Tiles © Esri'),
    dict(id='otm',name='OpenTopoMap',url='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',sub='abc',attr='© OpenStreetMap, SRTM, OpenTopoMap (CC-BY-SA)'),
]

def _bbox_center(bbox):
    w,e,s,n=bbox
    return ((s+n)/2,(w+e)/2)

def live_from_spec(spec, zoom=7, extra_routes=None, extra_markers=None):
    """Build live-map payload from a maps.py spec."""
    c=_bbox_center(spec['bbox'])
    mk=[]
    for m in spec['markers']:
        lon,lat=m['ll']
        mk.append(dict(n=m['n'],en=m.get('en',''),lat=lat,lon=lon,c=m.get('c','blue'),y=m.get('y',''),t=m.get('t',''),hl=bool(m.get('hl'))))
    if extra_markers:
        mk.extend(extra_markers)
    routes=[]
    pos={m['k']:m['ll'] for m in spec['markers']}
    for r in spec.get('routes') or []:
        a,b,col,*_=r
        if a in pos and b in pos:
            routes.append(dict(c=col,pts=[[pos[a][1],pos[a][0]],[pos[b][1],pos[b][0]]]))
    for lab,pts,col in spec.get('lines') or []:
        routes.append(dict(c=col,dash=True,pts=[[p[1],p[0]] for p in pts],lab=lab))
    if extra_routes:
        routes.extend(extra_routes)
    w,e,s,n=spec['bbox']
    return dict(id=spec['id'],title=spec['title'],center=[c[0],c[1]],zoom=zoom,bounds=[[s,w],[n,e]],markers=mk,routes=routes)

def live_html(data):
    opts=''.join(f'<option value="{t["id"]}">{_h.escape(t["name"])}</option>' for t in TILES)
    payload=_h.escape(json.dumps(data,ensure_ascii=False,separators=(',',':')),quote=True)
    tiles=_h.escape(json.dumps(TILES,ensure_ascii=False,separators=(',',':')),quote=True)
    return (f'<figure class="livebox" data-live="{payload}" data-tiles="{tiles}">'
            f'<div class="livebar"><label>底图来源</label><select class="tilesel" aria-label="选择地图底图">{opts}</select>'
            f'<span class="livestat">进入视野并打开此页后再加载 · 失败将自动切换下一源</span></div>'
            f'<div class="livepane" role="application" aria-label="{_h.escape(data.get("title","实时地图"))}"></div>'
            f'<figcaption>🌐 实时地图：{ _h.escape(data.get("title",""))} · 可切换 9 种无需密钥的全球底图（OSM / CARTO / Esri / OpenTopoMap 等）。瓦片需网络；若当前源失败会自动换源。离线请看「情景示意图」与「真实地理底图」。</figcaption></figure>')

def block(title, scene_key=None, spec=None, live=None, zoom=7, history='', culture='', note=''):
    """Tabbed: scene (offline) / geo SVG (offline) / live (network). Plus history/culture panels."""
    tabs=[]; panes=[]
    if scene_key:
        tabs.append(('scene','🎨 情景示意图（离线）'))
        panes.append(('scene', schematic.scene(scene_key)))
    if spec is not None:
        tabs.append(('idea','🧭 概念方位图（离线）'))
        panes.append(('idea', rmap.new_concept(spec)))
        tabs.append(('geo','🗺️ 真实地理底图（离线）'))
        panes.append(('geo', maps.render(spec)))
    if live is None and spec is not None:
        live=live_from_spec(spec, zoom=zoom)
    if live:
        tabs.append(('live','🌐 实时地图（可换底图）'))
        panes.append(('live', live_html(live)))
    bar=''.join(f'<button type="button" class="{"on" if i==0 else ""}" data-tab="{k}">{lab}</button>' for i,(k,lab) in enumerate(tabs))
    body=''.join(f'<div class="tabp{" on" if i==0 else ""}" data-tab="{k}">{html}</div>' for i,(k,html) in enumerate(panes))
    side=''
    if history or culture:
        from lib import card,grid
        cs=[]
        if history: cs.append(card('bg','历史背景',history))
        if culture: cs.append(card('ane','文化特征',culture))
        side=grid(*cs,cls='g2')
    n=f'<p class="note">{note}</p>' if note else ''
    return (f'<div class="mapblock"><h3 class="mh">{_h.escape(title)}</h3>'
            f'<div class="maptabs"><div class="tabbar" role="tablist">{bar}</div>{body}</div>{n}{side}</div>')
