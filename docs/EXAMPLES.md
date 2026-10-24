# Prompt examples / 提示词示例

[English guide](../README.md) · [中文说明](../README.zh-CN.md)

## Brief template / 需求模板

Include the brand, audience, product, page language, primary message, CTA destinations, assets, and output location. Omit unknown facts rather than inventing credibility claims.

提供品牌、受众、产品、页面语言、核心信息、CTA 目标、素材及输出位置。未知事实可以留空，不能为了营销效果虚构可信度。

```text
Use $tech-brand-website.
Brand / 品牌:
Product / 产品:
Audience / 受众:
Page language / 页面语言:
Core message / 核心信息:
Primary CTA destination / 主按钮目标:
Secondary CTA destination / 次按钮目标:
Available assets and rights / 可用素材与授权:
Preferred visual balance / 视觉主次:
Output / 输出: complete index.html
```

## 1. Chinese edge AI brand / 中文边缘 AI 品牌

```text
使用 $tech-brand-website 创建「星核科技」演示官网。
受众是开发者与企业产品团队，产品是边缘 AI 计算设备。
中文页面，关键词：精密、安静、清晰。
采用暗色首屏、明亮 Bento 和暗色技术章节。
主 CTA 链接 #technology，次 CTA 链接 #contact，创建对应的有效章节。
没有实际性能数据，请明确标记演示值，不引用真实客户或奖项。
不要外部视频，使用原创 CSS/SVG 产品视觉和原生 JS。
保存完整 index.html，验证移动菜单、减少动态效果和明暗模式。
```

## 2. English research hardware / 英文科研硬件

```text
Use $tech-brand-website for “Orbit Labs”, a fictional research hardware brand.
Write all website copy in English. Target robotics engineers.
Lead with a cinematic monochrome product visual, then use a bright Bento section
and a dark technical narrative. Favor precise typography over dense decoration.
Use only labeled sample specifications. Build working #platform and #contact CTAs.
Do not require video or a paid API. Prefer vanilla JS.
Deliver the complete index.html with responsive layouts and reduced-motion support.
```

## 3. Improve an existing page / 优化已有页面

```text
使用 $tech-brand-website 优化我提供的 index.html。
保留已经确认的品牌名称、文案、真实数据、链接和功能。
统一 8px 间距、排版层级、Bento 卡片和明暗主题；
补齐键盘菜单、可见焦点与减少动态效果。
修复入场动画与 hover 倾斜争用 transform 的问题。
返回完整更新文件，并说明已验证的范围。
```

Supply the actual file with this request. The skill does not grant access to missing files or external systems.

使用此提示词时同时提供实际文件；skill 不会自动获得未提供文件或外部系统的访问权。

## 4. English output with Anime.js / 使用 Anime.js 的英文页

```text
Use $tech-brand-website to create an English technology brand presentation page.
Use Anime.js only where it materially simplifies the Hero reveal sequence.
Verify and pin one available version and use that version's official API.
Keep menu behavior and core content independent from the optional library.
Use local anchor CTAs, label all sample data, and deliver one complete index.html.
```

## Review checklist / 页面验收

| Check / 检查 | Expected result / 预期 |
| --- | --- |
| 320px / 768px / 1440px | No horizontal overflow; readable titles / 无横向溢出、标题可读 |
| Light and dark / 明暗主题 | Readable text and distinguishable cards / 文字和卡片层级清楚 |
| Keyboard / 键盘 | Menu and CTAs usable, focus visible / 菜单与按钮可用、焦点可见 |
| Escape | Menu closes and focus returns / 菜单关闭且焦点归还 |
| Reduced motion / 减少动态 | Final content and metrics immediately visible / 内容与最终数值立即显示 |
| Touch / 触屏 | No dependency on hover or tilt / 不依赖悬停和倾斜 |
| Failed CDN / CDN 失败 | Core content remains readable / 主体内容仍可读 |
| Console / 控制台 | No uncaught runtime errors / 无未捕获运行错误 |

These are acceptance criteria, not results already obtained for a generated website.

以上是验收标准，不是本仓库已经完成的网站测试结果。
