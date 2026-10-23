# 摩西五经 Pentateuch-20261023-v1.0.0-GROKstudy

**欧陆改革宗正统视角的摩西五经（创世记 · 出埃及记 · 利未记 · 民数记 · 申命记）研读网站**：全本圣经视野 → 逐卷深读；时间线、故事线、地理地图、真实历史背景、古代近东文化、圣经神学与圣约神学；三项联合信条（海德堡要理问答、比利时信条、多特信经）与三大公教会信经原文逐字引自 [ccifellowship.org](https://ccifellowship.org)。

## 🌐 在线访问

| 平台 | 链接 |
|---|---|
| GitHub Pages | https://07-je-grok-love-personal-20260928.github.io/Pentateuch-Moses-Five-Books-GROKstudy/ |
| Surge | https://pentateuch-20261023-v1-grokstudy.surge.sh |
| Netlify | https://pentateuch-20261023-v1-grokstudy.netlify.app |

- 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/Pentateuch-Moses-Five-Books-GROKstudy
- 发布：https://github.com/07-Je-Grok-Love-Personal-20260928/Pentateuch-Moses-Five-Books-GROKstudy/releases/tag/v1.0.0-20261023

## 📚 页面（12 页）

| 页面 | 内容 |
|---|---|
| index.html 总览 | 五经在整本圣经中的位置、五卷一览表、故事流程、总时间线、思维导图、作者问题（摩西作者与 JEDP 批判） |
| genesis.html 创世记 | 十个「后代/记载」(toledot) 大纲、故事线、先祖年代、古代近东地图与迦南地图、ANE 文化对照、工作之约/恩典之约 |
| exodus.html 出埃及记 | 出埃及路线图、十灾、逾越节、西奈之约、十诫与律法三重用途、会幕 |
| leviticus.html 利未记 | 五祭、洁净条例、赎罪日、圣洁法典、节期，指向基督 |
| numbers.html 民数记 | 两次数点、旷野路线图、悖逆与审判、铜蛇、巴兰 |
| deuteronomy.html 申命记 | 宗主条约结构、示玛、摩押平原地图、祝福与咒诅、心里受割礼 |
| covenant.html 圣约神学 | 救赎之约、工作之约、恩典之约各施行阶段、再版论讨论 |
| creeds.html 三大信经 | 使徒信经、尼西亚信经、亚他那修信经纯净背诵版（遮盖/首字提示/朗读/复制）+ 深度比较与异端对照 |
| confessions.html 信条对照 | 13 个主题的 HC/BC/DT 原文、西敏斯特标准参考（要旨） |
| atlas.html 地图·时间线 | 5 幅 SVG 地图（Natural Earth 底图）、地区表、总时间线 |
| memory.html 记忆 | 五指记忆法、数字表、26 张翻转卡、20 题测验 |
| sources.html 来源与核对 | CCI 原文链接、实时逐字核对报告、参考网站、版本记录 |

## ✅ 引文核对

- 信条/信经引文共 165 处（HC 53、DT 35、BC 30、行内片段 40、其他 CCI 4、三大信经全文 3），2026-10-23 23:51（台北时间）对 ccifellowship.org（及 reformedbeginner.net 一处）实时页面逐字核对：**165/165 通过**。
- 经文采用和合本（CUV），构建时以脚本比对引号内经文。
- 西敏斯特标准仅以「要旨」形式概述，不作逐字引用。

## 🛠 构建

```bash
cd build && python3 build.py   # 生成 site/
python3 verify.py              # 实时核对引文 → verify.json，再次 build 写入 sources.html
```

## 📝 更新说明 / 版本记录

| 版本 | 日期 | 说明 |
|---|---|---|
| v1.0.0 (v1.0.0-20261023) | 2026-10-23 | 首次发布：12 页、5 幅地图、三大信经背诵版与比较、HC/BC/DT 165 处逐字引文实时核对、闪卡与测验、响应式毛玻璃设计、可隐藏目录、深浅主题 |
