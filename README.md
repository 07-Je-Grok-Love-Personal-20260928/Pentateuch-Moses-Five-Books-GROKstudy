# 摩西五经 Pentateuch-20261114-v2.0.0-GROKstudy

**欧陆改革宗正统视角的摩西五经（创世记 · 出埃及记 · 利未记 · 民数记 · 申命记）研读网站**：全本圣经视野 → 逐卷深读；时间线、故事线、地理地图、真实历史背景、古代近东文化、圣经神学与圣约神学；三项联合信条（海德堡要理问答、比利时信条、多特信经）与三大公教会信经原文逐字引自 [ccifellowship.org](https://ccifellowship.org)。

当前版本：**v2.0.0**（2026-11-14，台北时间）。

## 🌐 在线访问（v2.0.0）

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/Pentateuch-Moses-Five-Books-GROKstudy/ |
| Surge | https://pentateuch-20261114-v2-grokstudy.surge.sh |
| Netlify | https://pentateuch-20261114-v2-grokstudy.netlify.app |

- 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/Pentateuch-Moses-Five-Books-GROKstudy
- 本版发布：https://github.com/07-Je-Grok-Love-Personal-20260928/Pentateuch-Moses-Five-Books-GROKstudy/releases/tag/v2.0.0-20261114

## 📚 页面（12 页）

| 页面 | 内容 |
|---|---|
| index.html 总览 | 核心主线、五卷一览、故事与时间线、思维导图、作者问题、圣经工程普通话概述（点击播放） |
| genesis.html 创世记 | 核心一把抓、toledot 大纲、近东 / 亚伯拉罕 / 约瑟地图（示意图+离线底图+实时底图）、创15立约图、信条原文 |
| exodus.html 出埃及记 | 路线诸说对照、会幕安营示意图、十灾与西奈之约、实时可换底图 |
| leviticus.html 利未记 | 五祭示意图、会幕空间神学、赎罪日与圣洁 |
| numbers.html 民数记 | 加低斯与漂流、外约旦征服、安营图、巴兰背景 |
| deuteronomy.html 申命记 | 毗斯迦眺望、支派地业预览、示玛与圣约更新 |
| covenant.html 圣约神学 | 救赎之约 / 工作之约 / 恩典之约，创15情景图 |
| creeds.html 三大信经 | 纯净背诵版 + 深度比较与异端对照 |
| confessions.html 信条对照 | 13 个主题的 HC/BC/DT 原文（西敏斯特仅作要旨） |
| atlas.html 地图·时间线 | 11 组地图（情景图 + 概念图 + Natural Earth 底图 + 9 源实时地图），历史与文化栏，总时间线 |
| memory.html 记忆 | 标记图例、五指法、26 张翻转卡、20 题测验 |
| sources.html 来源与核对 | CCI 原文链接、实时逐字核对报告、参考网站、版本记录 |

## 🗺️ 地图说明（v2）

每一组地图都包含：

1. **情景示意图（离线）**：手绘讲解图，完全不依赖网络。
2. **概念方位图 + 真实地理底图（离线）**：按经纬度投影；地理底图使用 Natural Earth（公有领域）海岸线，SVG 自托管。
3. **实时地图（可换底图）**：自托管 Leaflet（无 CDN）。可在 OpenStreetMap、Humanitarian OSM、CARTO Voyager / 浅色 / 深色、Esri 卫星影像 / 地形 / 街道、OpenTopoMap 共 9 种无需密钥的全球底图之间切换；某一源瓦片连续失败会自动改用下一源。

地图主题包括：古代近东、亚伯拉罕旅程、族长迦南、约瑟与埃及、出埃及主路线、路线诸说（南线 / 北线 / 阿拉伯说）、会幕安营、旷野与加低斯、外约旦与摩押平原、毗斯迦眺望、支派地业预览。古代地点多为通行推定。

## ✅ 引文核对

- 信条/信经引文共 165 处（HC 53、DT 35、BC 30、行内片段 40、其他 CCI 4、三大信经全文 3），2026-11-14 10:18（台北时间）对 ccifellowship.org（及 reformedbeginner.net 一处）实时页面逐字核对：**165/165 通过**。
- 经文采用和合本（CUV）。西敏斯特标准仅以「要旨」形式概述，不作逐字引用。

## 🛠 构建

```bash
cd build && python3 build.py   # 生成 site/（同时复制自托管 Leaflet 与样式）
python3 verify.py              # 实时核对引文 → verify.json，再次 build 写入 sources.html
```

请勿把 `site/CNAME` 提交进仓库，以免 GitHub Pages 被重定向到 Surge 域名。部署 Surge 时请从单独的副本目录发布。

## 📝 更新说明 / 版本记录

| 版本 | 日期（台北时间） | 说明 | 部署 |
|---|---|---|---|
| v2.0.0（v2.0.0-20261114） | 2026-11-14 | 新增多幅地图与离线情景示意图；实时地图可切换 9 种全球底图并自动换源（自托管 Leaflet）；笔记标记系统与图例；圣经工程普通话概述（点击后加载）；滚动与动画性能优化（去掉大面积毛玻璃模糊）；更鲜明的配色与可视化。 | [Pages](https://07-je-grok-love-personal-20260928.github.io/Pentateuch-Moses-Five-Books-GROKstudy/) · [Surge](https://pentateuch-20261114-v2-grokstudy.surge.sh) · [Netlify](https://pentateuch-20261114-v2-grokstudy.netlify.app) |
| v1.0.0（v1.0.0-20261023） | 2026-10-23 | 首次发布：12 页、5 幅地图、三大信经背诵版与比较、HC/BC/DT 165 处逐字引文实时核对、闪卡与测验。 | [Surge v1](https://pentateuch-20261023-v1-grokstudy.surge.sh) · [Netlify v1](https://pentateuch-20261023-v1-grokstudy.netlify.app) · [Release](https://github.com/07-Je-Grok-Love-Personal-20260928/Pentateuch-Moses-Five-Books-GROKstudy/releases/tag/v1.0.0-20261023) |
