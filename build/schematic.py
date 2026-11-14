# -*- coding: utf-8 -*-
"""Hand-drawn offline concept / scene / explanatory SVGs. No network."""
import html as _h

def _svg(w,h,title,body,cls='scene'):
    return (f'<figure class="scene {cls}"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{_h.escape(title)}" preserveAspectRatio="xMidYMid meet">{body}</svg>'
            f'<figcaption>🎨 {_h.escape(title)}（离线示意图，不依赖网络）</figcaption></figure>')

def _defs(uid, stops=None):
    stops = stops or (('#1a2a58','#0b1a33'),)
    s=''.join(f'<stop offset="{i/(len(stops)-1 if len(stops)>1 else 1):.2f}" stop-color="{c}"/>' for i,c in enumerate(stops))
    return f'<defs><linearGradient id="{uid}-bg" x1="0" y1="0" x2="1" y2="1">{s}</linearGradient>' \
           f'</defs>'

def abraham():
    u='abrs'
    body=_defs(u,('#1d3b6e','#2a4a3a','#3a2e1a'))+f'''
<rect width="1100" height="420" rx="18" fill="url(#{u}-bg)"/>
<!-- stars of promise -->
<g fill="#f5c451" opacity=".9">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x,y,r in [(80,40,1.6),(140,28,1.2),(200,50,1.8),(260,22,1),(320,38,1.4),(900,30,1.5),(980,48,1.2),(1040,24,1.8)])}</g>
<!-- ziggurat Ur -->
<g transform="translate(40,200)">
  <path d="M10,160 L50,160 L58,120 L42,120 Z" fill="#c4a574"/><path d="M20,120 L70,120 L78,86 L32,86 Z" fill="#d4b896"/>
  <path d="M32,86 L80,86 L86,58 L40,58 Z" fill="#e2c9a8"/><rect x="52" y="36" width="16" height="22" fill="#f0dcc0"/>
  <text x="48" y="190" text-anchor="middle" fill="#f5c451" font-size="15" font-weight="700">吾珥</text>
  <text x="48" y="208" text-anchor="middle" fill="#c8d0e8" font-size="11">月神塔庙</text>
</g>
<!-- Haran crescent -->
<g transform="translate(260,150)">
  <path d="M40,20 a28,28 0 1 0 0,40 a20,20 0 1 1 0,-40" fill="#f5c451"/>
  <text x="40" y="90" text-anchor="middle" fill="#f5c451" font-size="15" font-weight="700">哈兰</text>
</g>
<!-- path -->
<path d="M130,280 C200,240 250,250 310,230 C400,200 480,260 560,230 C650,196 720,210 790,250 C860,286 920,240 1000,220" fill="none" stroke="#f5c451" stroke-width="4" stroke-dasharray="10 8" stroke-linecap="round" class="rt"/>
<!-- Canaan oaks + altar -->
<g transform="translate(520,200)">
  <ellipse cx="50" cy="90" rx="60" ry="18" fill="#1a3a28" opacity=".4"/>
  <path d="M50,90 L50,40" stroke="#6b4226" stroke-width="8"/>
  <path d="M50,48 C10,20 8,70 50,58 C90,70 92,16 50,48" fill="#3d8b5a"/>
  <path d="M20,100 h60 l-8,-18 h-44 z" fill="#8b7355"/>
  <rect x="40" y="78" width="6" height="10" fill="#f87171"/>
  <text x="50" y="132" text-anchor="middle" fill="#f5c451" font-size="15" font-weight="700">示剑 · 希伯仑</text>
  <text x="50" y="150" text-anchor="middle" fill="#c8d0e8" font-size="11">筑坛 · 应许之地</text>
</g>
<!-- Egypt pyramids -->
<g transform="translate(860,210)">
  <path d="M30,110 L70,30 L110,110 Z" fill="#e6c98a"/><path d="M70,30 L110,110 L90,110 Z" fill="#c9a86a"/>
  <path d="M90,110 L120,60 L150,110 Z" fill="#e6c98a"/><path d="M120,60 L150,110 L138,110 Z" fill="#c9a86a"/>
  <text x="90" y="132" text-anchor="middle" fill="#fb923c" font-size="15" font-weight="700">埃及</text>
  <text x="90" y="148" text-anchor="middle" fill="#c8d0e8" font-size="11">寄居又回来</text>
</g>
<text x="550" y="36" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">亚伯拉罕的旅程：应许领他走完这条路</text>
<text x="550" y="400" text-anchor="middle" fill="#c8d0e8" font-size="13">创12–25 · 吾珥 → 哈兰 → 迦南（示剑、伯特利、希伯仑）→ 埃及 → 再回迦南 · 金线为示意路线</text>
'''
    return _svg(1100,420,'亚伯拉罕旅程情景图',body)

def joseph():
    u='joss'
    body=_defs(u,('#1a2744','#12304a','#3a2a12'))+f'''
<rect width="1100" height="400" rx="18" fill="url(#{u}-bg)"/>
<text x="550" y="36" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">约瑟：坑 → 奴 → 狱 → 宰相 → 拯救</text>
<!-- four scenes -->
<!-- pit -->
<g transform="translate(40,70)">
  <rect width="230" height="270" rx="16" fill="rgba(0,0,0,.22)"/>
  <ellipse cx="115" cy="160" rx="50" ry="22" fill="#2a1a10"/><ellipse cx="115" cy="160" rx="36" ry="14" fill="#0e0a06"/>
  <circle cx="115" cy="110" r="22" fill="#e8c39a"/><path d="M100,128 Q115,200 130,128" fill="#4b7cbf"/>
  <text x="115" y="40" text-anchor="middle" fill="#fb923c" font-size="16" font-weight="700">① 多坍的坑</text>
  <text x="115" y="250" text-anchor="middle" fill="#c8d0e8" font-size="12">被弟兄卖掉</text>
</g>
<path d="M280,200 L330,200" stroke="#f5c451" stroke-width="4" marker-end="url(#{u}-a)" class="rt"/>
<!-- caravan / egypt -->
<g transform="translate(340,70)">
  <rect width="230" height="270" rx="16" fill="rgba(0,0,0,.22)"/>
  <path d="M40,200 Q80,140 120,200" fill="none" stroke="#e6c98a" stroke-width="10"/>
  <circle cx="70" cy="150" r="16" fill="#c4a574"/><circle cx="150" cy="160" r="14" fill="#c4a574"/>
  <text x="115" y="40" text-anchor="middle" fill="#60a5fa" font-size="16" font-weight="700">② 下到埃及</text>
  <text x="115" y="250" text-anchor="middle" fill="#c8d0e8" font-size="12">波提乏家 · 监狱</text>
</g>
<path d="M580,200 L630,200" stroke="#f5c451" stroke-width="4"/>
<!-- throne -->
<g transform="translate(640,70)">
  <rect width="230" height="270" rx="16" fill="rgba(0,0,0,.22)"/>
  <path d="M70,180 L115,90 L160,180 Z" fill="#e6c98a"/>
  <rect x="95" y="150" width="40" height="40" rx="4" fill="#f5c451"/>
  <circle cx="115" cy="120" r="18" fill="#e8c39a"/><path d="M98,130 h34 v30 h-34z" fill="#7c3aed"/>
  <text x="115" y="40" text-anchor="middle" fill="#a78bfa" font-size="16" font-weight="700">③ 法老的宰相</text>
  <text x="115" y="250" text-anchor="middle" fill="#c8d0e8" font-size="12">积粮 · 金链 · 戒指</text>
</g>
<path d="M880,200 L930,200" stroke="#f5c451" stroke-width="4"/>
<!-- reunion -->
<g transform="translate(940,70)">
  <rect width="140" height="270" rx="16" fill="rgba(0,0,0,.22)"/>
  <circle cx="70" cy="130" r="16" fill="#e8c39a"/>
  <circle cx="40" cy="180" r="12" fill="#e8c39a"/><circle cx="70" cy="190" r="12" fill="#e8c39a"/><circle cx="100" cy="180" r="12" fill="#e8c39a"/>
  <text x="70" y="40" text-anchor="middle" fill="#4ade80" font-size="15" font-weight="700">④ 相认</text>
  <text x="70" y="250" text-anchor="middle" fill="#c8d0e8" font-size="11">「神的意思是好的」</text>
</g>
<defs><marker id="{u}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="#f5c451"/></marker></defs>
'''
    return _svg(1100,400,'约瑟故事情景图',body)

def exo_routes():
    u='exor'
    body=_defs(u,('#0c2a3a','#123050','#1a2038'))+f'''
<rect width="1100" height="460" rx="18" fill="url(#{u}-bg)"/>
<text x="550" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">出埃及路线：三种主要学说（地点均为推定，经文未给出现代坐标）</text>
<!-- shared start -->
<circle cx="180" cy="160" r="16" fill="#f87171"/><text x="180" y="130" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">兰塞 / 歌珊</text>
<!-- Mediterranean -->
<ellipse cx="400" cy="70" rx="260" ry="36" fill="#3a7ca5" opacity=".45"/><text x="400" y="76" text-anchor="middle" fill="#dbeafe" font-size="12">地中海</text>
<!-- Sinai triangle -->
<path d="M260,200 L720,200 L490,400 Z" fill="#c4a574" opacity=".25" stroke="#e6c98a" stroke-width="1.5"/>
<text x="490" y="310" text-anchor="middle" fill="#e6c98a" font-size="13">西奈半岛</text>
<!-- Gulf of Suez / Aqaba -->
<path d="M300,200 Q320,300 340,400" fill="none" stroke="#3a7ca5" stroke-width="16" opacity=".5"/>
<path d="M680,200 Q660,300 640,400" fill="none" stroke="#3a7ca5" stroke-width="14" opacity=".5"/>
<text x="250" y="360" fill="#93c5fd" font-size="11">苏伊士湾</text>
<text x="700" y="360" fill="#93c5fd" font-size="11">亚喀巴湾</text>
<!-- southern traditional -->
<path d="M180,160 C240,190 280,230 330,250 C400,280 450,330 500,370" fill="none" stroke="#4ade80" stroke-width="4" stroke-dasharray="8 6" class="rt"/>
<circle cx="500" cy="370" r="12" fill="#4ade80"/><text x="500" y="400" text-anchor="middle" fill="#4ade80" font-size="13" font-weight="700">传统南线：穆萨山</text>
<!-- northern theory -->
<path d="M180,160 C260,120 360,100 470,90 C520,110 540,140 560,150" fill="none" stroke="#fb923c" stroke-width="3.5" stroke-dasharray="7 6" class="rt"/>
<circle cx="560" cy="150" r="10" fill="#fb923c"/><text x="700" y="150" fill="#fb923c" font-size="13" font-weight="700">北线说：巴达维尔湖 / 苇海（学说）</text>
<!-- arabia theory -->
<path d="M180,160 C300,220 420,250 620,280 C700,300 760,310 820,300" fill="none" stroke="#a78bfa" stroke-width="3.5" stroke-dasharray="6 6" class="rt"/>
<circle cx="820" cy="300" r="11" fill="#a78bfa"/><text x="820" y="330" text-anchor="middle" fill="#a78bfa" font-size="13" font-weight="700">米甸/阿拉伯说：拉兹山（学说）</text>
<g font-size="13" fill="#e8ecf8">
  <rect x="40" y="410" width="1020" height="36" rx="8" fill="rgba(0,0,0,.28)"/>
  <text x="550" y="434" text-anchor="middle">绿＝传统南线（本站地图默认）· 橙＝北线说 · 紫＝过亚喀巴湾至阿拉伯说。出13:17 明记不走非利士地的路。过海地点有争议，信仰要点是「耶和华拯救」，不在坐标。</text>
</g>
'''
    return _svg(1100,460,'出埃及路线学说比较示意图',body)

def camp():
    u='camp'
    # classic Israel camp around tabernacle
    tribes={
        'E':('犹大营（东，领头）',['犹大','以萨迦','西布伦'],'#f5c451'),
        'S':('流便营（南）',['流便','西缅','迦得'],'#fb923c'),
        'W':('以法莲营（西）',['以法莲','玛拿西','便雅悯'],'#60a5fa'),
        'N':('但营（北）',['但','亚设','拿弗他利'],'#2dd4bf'),
    }
    levs=[('东 摩西·亚伦',550,250,'#f5c451'),('南 哥辖',430,310,'#a78bfa'),('西 革顺',310,250,'#60a5fa'),('北 米拉利',430,190,'#fb923c')]
    body=_defs(u,('#1a1630','#12243a'))+f'''
<rect width="900" height="620" rx="18" fill="url(#{u}-bg)"/>
<text x="450" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">会幕与安营：圣所在正中，十二支派四面环绕（民2；3）</text>
<!-- outer camps -->
<g>
  <rect x="300" y="50" width="300" height="80" rx="12" fill="rgba(45,212,191,.18)" stroke="#2dd4bf"/>
  <text x="450" y="78" text-anchor="middle" fill="#2dd4bf" font-size="14" font-weight="700">但营（北）</text>
  <text x="450" y="100" text-anchor="middle" fill="#c8d0e8" font-size="12">但 · 亚设 · 拿弗他利</text>
  <rect x="300" y="500" width="300" height="80" rx="12" fill="rgba(251,146,60,.18)" stroke="#fb923c"/>
  <text x="450" y="528" text-anchor="middle" fill="#fb923c" font-size="14" font-weight="700">流便营（南）</text>
  <text x="450" y="550" text-anchor="middle" fill="#c8d0e8" font-size="12">流便 · 西缅 · 迦得</text>
  <rect x="40" y="200" width="130" height="230" rx="12" fill="rgba(96,165,250,.18)" stroke="#60a5fa"/>
  <text x="105" y="250" text-anchor="middle" fill="#60a5fa" font-size="14" font-weight="700">以法莲营</text>
  <text x="105" y="272" text-anchor="middle" fill="#60a5fa" font-size="13">（西）</text>
  <text x="105" y="310" text-anchor="middle" fill="#c8d0e8" font-size="12">以法莲</text>
  <text x="105" y="330" text-anchor="middle" fill="#c8d0e8" font-size="12">玛拿西</text>
  <text x="105" y="350" text-anchor="middle" fill="#c8d0e8" font-size="12">便雅悯</text>
  <rect x="730" y="200" width="130" height="230" rx="12" fill="rgba(245,196,81,.18)" stroke="#f5c451"/>
  <text x="795" y="250" text-anchor="middle" fill="#f5c451" font-size="14" font-weight="700">犹大营</text>
  <text x="795" y="272" text-anchor="middle" fill="#f5c451" font-size="13">（东，领头）</text>
  <text x="795" y="310" text-anchor="middle" fill="#c8d0e8" font-size="12">犹大</text>
  <text x="795" y="330" text-anchor="middle" fill="#c8d0e8" font-size="12">以萨迦</text>
  <text x="795" y="350" text-anchor="middle" fill="#c8d0e8" font-size="12">西布伦</text>
</g>
<!-- levites ring -->
<rect x="260" y="160" width="380" height="290" rx="14" fill="rgba(167,139,250,.08)" stroke="#a78bfa" stroke-dasharray="6 4"/>
<text x="450" y="184" text-anchor="middle" fill="#c4b5fd" font-size="12">利未人护卫一圈</text>
<text x="450" y="226" text-anchor="middle" fill="#fb923c" font-size="11">北 · 米拉利（板与柱）</text>
<text x="450" y="424" text-anchor="middle" fill="#a78bfa" font-size="11">南 · 哥辖（圣物）</text>
<text x="290" y="310" fill="#60a5fa" font-size="11">西 · 革顺</text>
<text x="560" y="310" fill="#f5c451" font-size="11">东 · 摩西·亚伦（门口）</text>
<!-- tabernacle -->
<g transform="translate(370,250)">
  <rect width="160" height="90" rx="6" fill="#8b5a2b" stroke="#f5c451" stroke-width="2"/>
  <rect x="100" y="10" width="50" height="70" fill="#f5c451" opacity=".35"/>
  <rect x="10" y="18" width="28" height="54" fill="#e8ecf8" opacity=".25" stroke="#f5c451"/>
  <text x="80" y="44" text-anchor="middle" fill="#fff" font-size="13" font-weight="800">会 幕</text>
  <text x="80" y="62" text-anchor="middle" fill="#fde68a" font-size="10">入口向东</text>
</g>
<text x="450" y="600" text-anchor="middle" fill="#c8d0e8" font-size="13">云柱停，就安营；云柱收上去，就起行（民9:15–23）。神住在民中，这是整卷利未记的前提。</text>
'''
    return _svg(900,620,'会幕与十二支派安营示意图',body,'scene tall')

def wander():
    u='wan'
    body=_defs(u,('#1a2030','#2a2418'))+f'''
<rect width="1000" height="430" rx="18" fill="url(#{u}-bg)"/>
<text x="500" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">旷野漂流：加低斯的不信，把十一年的路走成四十年</text>
<!-- Kadesh hub -->
<circle cx="280" cy="220" r="54" fill="none" stroke="#a78bfa" stroke-width="3" stroke-dasharray="6 5" class="rt"/>
<circle cx="280" cy="220" r="16" fill="#a78bfa"/>
<text x="280" y="180" text-anchor="middle" fill="#c4b5fd" font-size="14" font-weight="700">加低斯巴尼亚</text>
<text x="280" y="290" text-anchor="middle" fill="#c8d0e8" font-size="12">探子回报 · 哀哭 · 倒毙（民13–14；20）</text>
<!-- spiral of years -->
<path d="M280,220 C300,160 360,150 390,200 C410,250 340,300 280,290 C210,278 190,210 250,170 C330,120 450,160 460,240" fill="none" stroke="#fb923c" stroke-width="3" stroke-dasharray="5 6" class="rt"/>
<text x="430" y="140" fill="#fb923c" font-size="13">约三十八年绕行</text>
<!-- Edom block -->
<rect x="520" y="160" width="90" height="80" rx="10" fill="rgba(248,113,113,.2)" stroke="#f87171"/>
<text x="565" y="205" text-anchor="middle" fill="#f87171" font-size="13" font-weight="700">以东</text>
<text x="565" y="222" text-anchor="middle" fill="#c8d0e8" font-size="11">不许路过</text>
<!-- around to transjordan -->
<path d="M460,240 C500,300 560,330 640,300 C720,270 760,200 800,170" fill="none" stroke="#2dd4bf" stroke-width="4" class="rt"/>
<circle cx="800" cy="170" r="14" fill="#2dd4bf"/>
<text x="800" y="140" text-anchor="middle" fill="#2dd4bf" font-size="14" font-weight="700">摩押平原</text>
<text x="800" y="210" text-anchor="middle" fill="#c8d0e8" font-size="12">绕行红海路 · 击败西宏与噩</text>
<text x="500" y="400" text-anchor="middle" fill="#c8d0e8" font-size="13">橙线＝悖逆的循环（加低斯为圆心）· 青线＝新一代绕过以东、转向得胜。铜蛇事件发生在绕行路上（民21）。</text>
'''
    return _svg(1000,430,'旷野漂流与加低斯示意图',body)

def transjordan():
    u='trj'
    body=_defs(u,('#102030','#1a2a28'))+f'''
<rect width="1000" height="420" rx="18" fill="url(#{u}-bg)"/>
<text x="500" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">外约旦得胜：亚嫩河 → 希实本（西宏）→ 以得来（噩）→ 摩押平原</text>
<!-- Jordan / Dead Sea -->
<path d="M280,60 C300,140 290,200 300,250 C270,300 290,350 280,400" fill="none" stroke="#3a7ca5" stroke-width="18" opacity=".5"/>
<ellipse cx="300" cy="340" rx="40" ry="60" fill="#3a7ca5" opacity=".45"/>
<text x="230" y="200" fill="#93c5fd" font-size="12">约旦河</text>
<text x="300" y="348" text-anchor="middle" fill="#dbeafe" font-size="11">盐海</text>
<!-- arrows of conquest -->
<g>
  <circle cx="420" cy="300" r="12" fill="#60a5fa"/><text x="460" y="304" fill="#60a5fa" font-size="13" font-weight="700">亚嫩河（界河）</text>
  <path d="M430,280 L500,220" stroke="#2dd4bf" stroke-width="4"/>
  <circle cx="520" cy="210" r="14" fill="#2dd4bf"/><text x="548" y="214" fill="#2dd4bf" font-size="14" font-weight="700">希实本 · 西宏</text>
  <path d="M530,190 L600,110" stroke="#a78bfa" stroke-width="4"/>
  <circle cx="620" cy="100" r="14" fill="#a78bfa"/><text x="648" y="104" fill="#a78bfa" font-size="14" font-weight="700">以得来 · 巴珊王噩</text>
  <path d="M510,230 L620,300" stroke="#f472b6" stroke-width="4"/>
  <circle cx="640" cy="310" r="14" fill="#f472b6"/><text x="668" y="314" fill="#f472b6" font-size="14" font-weight="700">摩押平原 / 什亭</text>
  <circle cx="700" cy="250" r="10" fill="#fb923c"/><text x="720" y="254" fill="#fb923c" font-size="13">巴兰四次祝福</text>
  <circle cx="580" cy="360" r="10" fill="#f5c451"/><text x="600" y="364" fill="#f5c451" font-size="13">尼波山：摩西观望</text>
</g>
<text x="500" y="400" text-anchor="middle" fill="#c8d0e8" font-size="13">民21–36；申2–3。河东之地先作「首付」，却也成为两支派半「先安顿、后争战」的试验（民32）。</text>
'''
    return _svg(1000,420,'外约旦征服示意图',body)

def tribes():
    u='trib'
    # stylized allotment preview
    boxes=[
        (520,40,200,70,'但 / 拿弗他利 / 亚设','#2dd4bf'),
        (430,120,160,70,'西布伦 / 以萨迦','#60a5fa'),
        (360,200,140,90,'玛拿西（西半）','#818cf8'),
        (520,200,140,80,'以法莲','#a78bfa'),
        (400,300,120,70,'便雅悯','#f472b6'),
        (300,360,220,90,'犹 大','#f5c451'),
        (300,460,120,60,'西缅','#fb923c'),
        (200,360,90,160,'但（沿海迁徙前）','#94a3b8'),
        (700,80,140,100,'玛拿西东半 / 巴珊','#34d399'),
        (700,200,140,90,'迦 得 / 基列','#4ade80'),
        (700,310,140,80,'流 便','#86efac'),
    ]
    rec=''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}" fill-opacity=".28" stroke="{c}"/><text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">{t}</text>' for x,y,w,h,t,c in boxes)
    body=_defs(u,('#152238','#1a2a28'))+f'''
<rect width="980" height="560" rx="18" fill="url(#{u}-bg)"/>
<text x="490" y="28" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">支派地业预览（民32；34；申3 · 示意分区，精确边界见约书亚记）</text>
<!-- sea + jordan -->
<ellipse cx="160" cy="300" rx="36" ry="200" fill="#3a7ca5" opacity=".4"/>
<text x="160" y="300" text-anchor="middle" fill="#dbeafe" font-size="11">西海</text>
<path d="M660,50 C680,180 650,300 670,500" fill="none" stroke="#3a7ca5" stroke-width="10" opacity=".45"/>
<ellipse cx="640" cy="400" rx="28" ry="70" fill="#3a7ca5" opacity=".4"/>
<text x="640" y="404" text-anchor="middle" fill="#dbeafe" font-size="10">盐海</text>
{rec}
<text x="490" y="540" text-anchor="middle" fill="#c8d0e8" font-size="13">绿色在河东（先得之地）；金色犹大在南；约瑟家（以法莲、玛拿西）在中央山地。利未无连片地业，在各支派中得城（民35）。</text>
'''
    return _svg(980,560,'十二支派地业预览示意图',body,'scene tall')

def ane_world():
    u='anew'
    body=_defs(u,('#1a2748','#2a2018'))+f'''
<rect width="1100" height="420" rx="18" fill="url(#{u}-bg)"/>
<text x="550" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">创世记的世界舞台：两河 · 迦南 · 尼罗</text>
<!-- regions as lively blobs -->
<ellipse cx="820" cy="200" rx="200" ry="110" fill="#fb923c" fill-opacity=".22" stroke="#fb923c"/>
<text x="820" y="180" text-anchor="middle" fill="#fb923c" font-size="18" font-weight="800">美索不达米亚</text>
<text x="820" y="204" text-anchor="middle" fill="#e8ecf8" font-size="13">吾珥 · 巴比伦（示拿）· 哈兰</text>
<text x="820" y="224" text-anchor="middle" fill="#e8ecf8" font-size="12">塔庙 · 楔形文字 · 汉谟拉比</text>
<ellipse cx="470" cy="230" rx="130" ry="90" fill="#f5c451" fill-opacity=".22" stroke="#f5c451"/>
<text x="470" y="220" text-anchor="middle" fill="#f5c451" font-size="18" font-weight="800">迦 南</text>
<text x="470" y="244" text-anchor="middle" fill="#e8ecf8" font-size="13">应许之地 · 城邦 · 巴力</text>
<ellipse cx="200" cy="260" rx="140" ry="100" fill="#f87171" fill-opacity=".2" stroke="#f87171"/>
<text x="200" y="250" text-anchor="middle" fill="#f87171" font-size="18" font-weight="800">埃 及</text>
<text x="200" y="274" text-anchor="middle" fill="#e8ecf8" font-size="13">尼罗河 · 法老 · 约瑟</text>
<path d="M700,200 C620,160 560,180 500,210" fill="none" stroke="#f5c451" stroke-width="3" stroke-dasharray="8 6" class="rt"/>
<path d="M400,250 C320,280 280,280 230,270" fill="none" stroke="#f87171" stroke-width="3" stroke-dasharray="8 6" class="rt"/>
<text x="550" y="390" text-anchor="middle" fill="#c8d0e8" font-size="13">一条家族的路，把三个文明连成一条救赎故事线。金线＝蒙召西迁；红线＝下埃及。</text>
'''
    return _svg(1100,420,'古代近东世界情景图',body)

def covenant_pieces():
    u='c15'
    body=_defs(u,('#1a1428','#2a1a10'))+f'''
<rect width="900" height="320" rx="18" fill="url(#{u}-bg)"/>
<text x="450" y="32" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">创15：只有神从肉块中经过——恩典之约由神单方面担保</text>
<!-- split pieces -->
<g transform="translate(150,90)">
  <rect x="0" y="40" width="70" height="90" rx="8" fill="#8b3a3a"/>
  <rect x="110" y="40" width="70" height="90" rx="8" fill="#8b3a3a"/>
  <rect x="220" y="50" width="55" height="70" rx="8" fill="#7a3333"/>
  <rect x="310" y="50" width="55" height="70" rx="8" fill="#7a3333"/>
  <rect x="420" y="60" width="40" height="50" rx="6" fill="#6b2d2d"/>
  <rect x="490" y="60" width="40" height="50" rx="6" fill="#6b2d2d"/>
  <path d="M40,180 L560,180" stroke="#f5c451" stroke-width="3" stroke-dasharray="6 6" class="rt"/>
  <!-- furnace -->
  <g transform="translate(280,100)">
    <ellipse cx="0" cy="0" rx="22" ry="14" fill="#fb923c" opacity=".8"/>
    <path d="M-10,-20 Q0,-50 10,-20" fill="#f87171"/>
    <text x="0" y="-58" text-anchor="middle" fill="#f5c451" font-size="13" font-weight="700">冒烟的炉 · 烧着的火把</text>
  </g>
</g>
<text x="450" y="290" text-anchor="middle" fill="#c8d0e8" font-size="14">近东立约：双方走过肉块，违约者当如此被劈。此约唯独神走过——预表祂自己担当咒诅。</text>
'''
    return _svg(900,320,'创15立约情景图',body)

def sacrifices():
    u='sac'
    items=[('燔祭','全然焚烧','完全献给神','#fb923c'),('素祭','面与油','感恩的生活','#f5c451'),('平安祭','共享筵席','与神相交','#4ade80'),('赎罪祭','血涂坛角','挽回罪污','#f87171'),('赎愆祭','赔偿加五分一','修复亏负','#a78bfa')]
    cards=''.join(f'<g transform="translate({70+i*160},80)"><rect width="140" height="170" rx="16" fill="{c}" fill-opacity=".2" stroke="{c}"/><text x="70" y="40" text-anchor="middle" fill="{c}" font-size="18" font-weight="800">{n}</text><text x="70" y="80" text-anchor="middle" fill="#e8ecf8" font-size="13">{a}</text><text x="70" y="130" text-anchor="middle" fill="#c8d0e8" font-size="13">{b}</text></g>' for i,(n,a,b,c) in enumerate(items))
    body=_defs(u,('#1a1830','#2a1a18'))+f'''
<rect width="940" height="320" rx="18" fill="url(#{u}-bg)"/>
<text x="470" y="36" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">五祭一览：路，开向圣洁之神（利1–7）</text>
{cards}
<text x="470" y="290" text-anchor="middle" fill="#c8d0e8" font-size="14">核心：不是人买通神，乃是神赐下亲近祂的路。全部指向「一次永远的献上」（来10）。</text>
'''
    return _svg(940,320,'利未记五祭示意图',body)

SCENES={
    'ane':ane_world,'abraham':abraham,'joseph':joseph,'exo_routes':exo_routes,
    'camp':camp,'wander':wander,'transjordan':transjordan,'tribes':tribes,
    'covenant':covenant_pieces,'sacrifices':sacrifices,
}
def scene(key):
    return SCENES[key]()
