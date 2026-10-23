# -*- coding: utf-8 -*-
from lib import *
import json,os
HERO=hero('🔗 来源 · 核对报告 · 版本','来源与核对','本站的信条引文全部来自 ccifellowship.org，并在发布前逐条在线核对；其他改革宗网站作为参考与背景资料。',('🔗','✅','📑'),'')
def build_body():
    S=[]
    vf='verify.json'; v=json.load(open(vf)) if os.path.exists(vf) else None
    if v:
        rows=[[esc(r['kind']),esc(str(r['id'])),f'<a href="{r["url"]}" target="_blank" rel="noopener">{esc(r["url"].replace("https://",""))}</a>','✅ 逐字相符' if r['ok'] else '⚠️ 未通过'] for r in v['items']]
        S.append(sec('verify','✅','逐字核对报告',P(f'核对时间：<b>{v["time"]}</b>（台北时间，UTC+8）。方法：构建时记录每一处引文 → 在线抓取对应 CCI 原页 → 去除 HTML 标签与空白、脚注标记后，检查引文是否完整包含在原页文字中。')
          +kv([('引文段落数',str(v['n'])),('逐字相符',str(v['ok'])),('未通过',str(v['n']-v['ok'])),('核对的原页数',str(v['pages']))])
          +fold('📋 展开完整核对清单',table(['类型','编号','原页','结果'],rows)),'#22c55e','#0ea5e9','01'))
    S.append(sec('cci','📜','主要来源：ccifellowship.org（逐字引用）',table(['内容','网址'],[
     ['使徒信经','<a href="https://ccifellowship.org/books/book-of-praise/creeds/apostles-creed">ccifellowship.org/…/creeds/apostles-creed</a>'],['尼西亚信经','<a href="https://ccifellowship.org/books/book-of-praise/creeds/nicene-creed">ccifellowship.org/…/creeds/nicene-creed</a>'],['亚他那修信经','<a href="https://ccifellowship.org/books/book-of-praise/creeds/athanasian-creed">ccifellowship.org/…/creeds/athanasian-creed</a>'],['海德堡要理问答','<a href="https://ccifellowship.org/books/book-of-praise/confessions/heidelberg-catechism">ccifellowship.org/…/heidelberg-catechism</a>'],['比利时信条','<a href="https://ccifellowship.org/books/book-of-praise/confessions/the-belgic-confession">ccifellowship.org/…/the-belgic-confession</a>'],['多特信经','<a href="https://ccifellowship.org/books/book-of-praise/confessions/canons-of-dort">ccifellowship.org/…/canons-of-dort</a>'],['洗礼仪文','<a href="https://ccifellowship.org/books/book-of-praise/liturgical-forms/2">ccifellowship.org/…/liturgical-forms/2</a>'],['圣经故事（创世记—申命记）','<a href="https://ccifellowship.org/books/bible-story/1/1">ccifellowship.org/books/bible-story/1/1</a> 起']])
     +card('hard','说明','站内「本站概括」「要旨」字样的内容是本站的总结，不是信条原文；凡加「CCI 原文」框或链接的才是逐字引用。CCI《圣经故事》第一册第23–30章在网站上不存在（返回404），本站未引用。'),'#a16207','#7c2d12','02'))
    S.append(sec('refs','📚','参考网站（背景与教义立场）',UL(*[f'<a href="{u}" target="_blank" rel="noopener">{esc(t)}</a>' for t,u in [
     ('ccreformed.org（基督教华人改革宗教会）三项联合信条','https://www.ccreformed.org/threeforms/'),('reformedbeginner.net 为什么再版论如此有争议？','https://www.reformedbeginner.net/why-is-republication-so-controversial/'),('reformedbeginner.net 加尔文论新旧约的连续性','https://www.reformedbeginner.net/sacramental-scaffolding-calvin-on-the-continuity-of-the-old-and-new-covenants/'),('reformedbeginner.net 大公信经','https://www.reformedbeginner.net/ecumenical-creeds/'),('reformedbeginner.net 关于异端','https://www.reformedbeginner.net/all-about-heresy/'),('canrc.org 加拿大改革宗教会 · 合一','https://canrc.org/unity'),('urcna.org 联合改革宗教会 · 三项联合信条','https://www.urcna.org/threeforms'),('heritagereformed.com 传承改革宗教会 · 教义重点','https://heritagereformed.com/about-the-hrc/doctrinal-emphasis-major-teachings/'),('prca.org 新教改革宗教会 · 多特信经','https://www.prca.org/about/official-standards/creeds/three-forms-of-unity/canons-of-dordrecht'),('opc.org 正统长老会 · 信条','https://www.opc.org/confessions.html'),('canadianreformedseminary.ca 加拿大改革宗神学院','https://canadianreformedseminary.ca/about/who-we-are/'),('wts.edu 威斯敏斯特神学院 · 历史','https://www.wts.edu/about/history'),('crts.edu','https://crts.edu/en/intro/')]]),'#0ea5e9','#6366f1','03'))
    S.append(sec('data','🧰','数据与技术',UL('经文：和合本（简体），构建时由 getbible.net API（cus 译本）取得。','地图：Natural Earth（公有领域）1:10m / 1:50m 海岸线、河流、湖泊数据，Python + Shapely 本地投影绘制为 SVG。','纯静态 HTML/CSS/JS，无追踪、无外部字体与脚本。','参考书目（背景）：O. T. Allis《The Five Books of Moses》(1943)；M. G. Kline《Treaty of the Great King》(1963)；G. Vos《Biblical Theology》(1948)；O. P. Robertson《The Christ of the Covenants》(1980)；加尔文《基督教要义》。'),'#64748b','#0ea5e9','04'))
    S.append(sec('ver','🏷️','版本历史',table(['版本','日期（台北时间）','说明'],[['v1.0.0','2026-10-23','首次发布：总览、五卷书、圣约神学、地图·时间线、三大信经、信条与五经、记忆中心、来源与核对报告。']]),'#7c3aed','#ec4899','05'))
    return ''.join(S)
TITLE='来源'; DESC='来源、逐字核对报告与版本历史。'
