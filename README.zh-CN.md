# Tech Brand Website Skill · 科技品牌官网

[English](README.md) · **简体中文**

一个可重复调用的 Codex skill，用于生成具有电影叙事、Bento 网格和精致交互的科技品牌展示官网，交付完整、响应式的单文件 `index.html`。

技术栈为 **Tailwind CSS v3 + 原生 JavaScript + 可选 Anime.js**。设计融合 Apple 的留白、Google 的模块化、Microsoft 的深色科技质感与影视飓风的影像叙事。品牌名称仅用于说明设计参考；本项目与这些品牌没有隶属或背书关系，也不表示获得 Awwwards 奖项。

## 项目提供什么

- 可安装的 `SKILL.md`，包含完整设计要求、实施约束和交付检查。
- 导航、Hero、Bento 亮点、交替图文叙事、技术数据、四列页脚六段默认架构。
- 集中的 CSS 主题变量、明暗自动切换、移动优先布局和键盘操作要求。
- 滚动揭示、追光、倾斜、粒子、数字递增等动效的实施与降级规则。
- 中英文说明、可复制的调用示例、发布指南和无第三方依赖的项目校验脚本。

这是提供给 AI 编程助手的工作指令项目，不是 npm 动画库，也不是已经完成的网站。本版本没有网站 Demo 或预览截图；生成页面的视觉质量、性能和无障碍结果仍需实际验证。

## 安装

下载或克隆仓库后，将 **`skills/tech-brand-website/` 文件夹本身**放进当前 Codex 客户端识别的 skills 目录，不要将整个仓库作为一个 skill 复制进去。

以下命令采用制作本项目时本地 skill-installer 支持的 `$CODEX_HOME/skills` 约定；未设置时回退到 `~/.codex/skills`。其他客户端发行版本的发现路径可能不同，请以客户端配置为准。参考[官方 skill 编写文档](https://learn.chatgpt.com/docs/build-skills)。

### Windows PowerShell

在下载后的仓库根目录运行：

```powershell
$skillBase = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
$skillTarget = Join-Path $skillBase 'tech-brand-website'
if (Test-Path -LiteralPath $skillTarget) { throw 'Skill 已存在，请先备份再更新。' }
New-Item -ItemType Directory -Path $skillBase -Force | Out-Null
Copy-Item -LiteralPath './skills/tech-brand-website' -Destination $skillTarget -Recurse
```

### macOS / Linux

在下载后的仓库根目录运行：

```bash
skill_base="${CODEX_HOME:-$HOME/.codex}/skills"
skill_target="$skill_base/tech-brand-website"
if [ -e "$skill_target" ]; then
  echo 'Skill already exists. Back it up before updating.' >&2
else
  mkdir -p "$skill_base" && cp -R ./skills/tech-brand-website "$skill_target"
fi
```

### 发布后从 GitHub 安装

仓库上传 GitHub 后，可向带有 skill-installer 的 Codex 发送：

```text
使用 $skill-installer，从
https://github.com/YOUR_USERNAME/YOUR_REPOSITORY
安装 skills/tech-brand-website。
```

请替换用户名和仓库名占位符。此方式需要联网并提供 skill-installer；当前交付包还没有远端仓库地址。

安装后在下一轮消息中调用。若尚未刷新发现结果，打开新聊天或重新加载客户端。

## 使用示例

```text
使用 $tech-brand-website 为「星核科技」创建中文官网。
产品是面向开发者的边缘 AI 计算设备，风格克制、精密、具有未来感。
采用深色电影感 Hero、明亮 Bento 亮点和深色技术章节。
主 CTA 跳转 #technology，次 CTA 跳转 #contact。
使用明确标识的演示数据，不引用未经证实的真实客户或性能指标。
采用原生 JS，不使用外部视频。
保存完整可运行的 index.html。
```

skill 正文为中文，默认生成中文页面；需要英文网站时请在提示词中指定。更多中英文场景见 [docs/EXAMPLES.md](docs/EXAMPLES.md)。

## 设计与技术规范

| 维度 | 默认要求 |
| --- | --- |
| 空间系统 | 8px 间距节奏，桌面 12 栏 Bento，支持 7:5 / 6:6 组合 |
| 首屏 | 视口高度 Hero、双 CTA、约 64px 桌面标题 / 48px 移动标题 |
| 排版 | Inter 或系统无衬线字体，主要字重 300–600 |
| 色彩 | 黑白中性色主导，克制蓝色点缀，蓝紫青技术光源 |
| 动效 | 400–600ms，24px 滚动揭示，同组 150ms 错峰 |
| 交互 | 精细指针设备启用追踪、倾斜与追光；按钮有 hover 和按压反馈 |
| 响应式 | 移动优先，640 / 768 / 1024px 调整，并检查 320px 窄屏 |
| 无障碍 | 可见焦点、键盘菜单、Escape 关闭、正文对比度目标至少 4.5:1 |
| 减少动态 | 关闭装饰性运动，立即显示完整内容、最终数字和进度 |
| 交付 | 语义 HTML、内联 CSS/JS、Tailwind v3 CDN、可选 Anime.js |

原生 JS 优先；使用 Anime.js 时需要核对版本与 API，不依赖 GSAP。资源通过 CDN 加载需要联网，不能将单文件等同于完全离线。Tailwind 浏览器 CDN 适合本需求的快速交付形式；正式上线前应评估资源部署、授权、CSP 和性能，必要时另行要求编译并内联 CSS。

## 推荐操作流程

1. 提供品牌定位、目标受众、内容语言、产品优势、可用素材与有效 CTA 地址。
2. 调用 skill 生成完整 `index.html`，在联网浏览器中打开。
3. 检查手机与桌面、明暗模式、减少动态效果、键盘、资源加载异常和控制台错误。
4. 将明确标记的演示内容替换为核实过的实际数据和已获授权的素材。
5. 审阅后再部署到明确授权的目标。生成 HTML 不会自动发布网站。

## 目录结构

```text
.
├── README.md                   # English guide
├── README.zh-CN.md             # 中文说明
├── LICENSE                    # MIT
├── CONTRIBUTING.md            # 中英文贡献指南
├── CHANGELOG.md               # 中英文版本记录
├── docs/
│   ├── EXAMPLES.md             # 中英文提示词示例
│   └── PUBLISHING.md           # 中英文 GitHub 发布步骤
├── scripts/
│   └── validate.py             # 项目结构与链接检查
└── skills/tech-brand-website/
    ├── SKILL.md                # 实际安装入口
    └── agents/openai.yaml      # Codex 展示信息
```

## 校验与维护

在仓库根目录运行以下命令，需 Python 3.10+；仅安装和读取 skill 不需要 Python 或 npm。

```bash
python scripts/validate.py
```

校验覆盖结构、入口元数据、必要文档、UTF-8 可读性及 Markdown 本地链接目标。它不执行生成网站，不代表浏览器行为或设计质量验证通过。

- **未识别：** 检查实际 skills 路径、嵌套层级和 `SKILL.md` 是否存在，刷新客户端并显式输入 `$tech-brand-website`。
- **目标已存在：** 先备份再替换，安装命令不会自动覆盖。卸载时移除已安装的该 skill 文件夹；已生成的网站文件另行保留。
- **语言不对：** 提示词明确指定英文或中文。
- **CDN 不可用：** 使用可用资源，或改为打包/编译资源版本；主体内容不能依赖动效初始化才能显示。
- **动效没有运行：** 先检查系统减少动态效果偏好、触屏条件和移动端降级规则。

## 贡献与许可

贡献流程见 [CONTRIBUTING.md](CONTRIBUTING.md)，版本记录见 [CHANGELOG.md](CHANGELOG.md)。项目以 [MIT License](LICENSE) 发布。第三方库、字体、图片和视频仍适用各自许可，本仓库不分发这些外部资源。
