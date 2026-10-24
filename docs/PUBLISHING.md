# Publish to GitHub / 发布到 GitHub

[English guide](../README.md) · [中文说明](../README.zh-CN.md)

## English

This package is ready for a source repository. No GitHub account, remote repository, tag, or release has been created by packaging it.

1. Extract the ZIP and open the `tech-brand-website-github` folder. Upload the **contents of that folder**, so `README.md` is at the GitHub repository root.
2. Review the MIT license. Keep it if you intend to distribute under MIT; choose your licensing terms before publishing. The neutral contributor attribution avoids guessing your identity.
3. Run `python scripts/validate.py`. Review the canonical skill and both READMEs. Confirm there are no private files, personal absolute paths, credentials, or unsupported claims.
4. Create an empty GitHub repository, for example `tech-brand-website-skill`. Use the web upload flow or the Git commands below. With the command flow, do not initialize the remote with a separate README or license.
5. Replace `YOUR_USERNAME/YOUR_REPOSITORY` in both README installation examples with the actual repository coordinates. Leave the `skills/tech-brand-website` path unchanged.
6. Push, then verify both language links and the skill path on GitHub. Test installation in a separate skills directory or client before replacing an existing installation.
7. Optionally create a `v1.0.0` tag and GitHub Release after review. Use the changelog as release notes. Tag creation and release publication are separate actions from preparing this package.

Run these commands **inside the extracted project folder**, after replacing the remote URL:

```bash
git init -b main
git add .
git commit -m "Initial release: bilingual tech brand website skill"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Optional release tag, after checking the pushed content:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Suggested repository description:

> A Codex skill for cinematic technology brand websites with Bento layouts, Tailwind CSS, and accessible motion. 中英文说明。

Suggested topics: `codex`, `agent-skills`, `frontend`, `tailwindcss`, `animejs`, `landing-page`, `web-design`.

GitHub Pages is unnecessary for distributing the skill. It would serve website files, not install this skill into a user's agent. Add a separately tested demo later if desired; this package has no demo to deploy.

## 中文

本项目已具备源代码仓库的结构。整理和打包不代表已经创建 GitHub 仓库、标签或 Release。

1. 解压 ZIP，打开 `tech-brand-website-github` 文件夹。上传该文件夹内的内容，使 `README.md` 位于 GitHub 仓库根目录。
2. 审阅 MIT 许可；只有你打算采用 MIT 开源时才保留。贡献者署名采用中性写法，没有擅自填入个人姓名。
3. 运行 `python scripts/validate.py`，检查 skill 正文及两份 README。确认没有私有文件、个人绝对路径、凭据或未经证实的声明。
4. 在 GitHub 创建空仓库，建议命名 `tech-brand-website-skill`。可通过网页上传，也可使用上面的 Git 命令；命令方式要求远端没有预先创建独立的 README 或 LICENSE。
5. 将两份 README 中的 `YOUR_USERNAME/YOUR_REPOSITORY` 替换为实际用户名和仓库名。保留 `skills/tech-brand-website` 安装路径。
6. 推送后检查中英文链接与 skill 路径，在独立的 skills 目录或客户端中试装，避免覆盖已有安装。
7. 审阅后可创建 `v1.0.0` 标签和 GitHub Release，并使用 CHANGELOG 内容作为说明。准备发布包本身不会执行这些外部操作。

建议仓库描述：

> 用于生成电影感科技品牌官网的 Codex skill，支持 Bento 布局、Tailwind CSS、精致动效及无障碍降级，含中英文文档。

分发 skill 不需要启用 GitHub Pages。Pages 用于托管网站文件，不会把 skill 安装进用户的 AI 助手；当前版本没有可部署 Demo，可后续另行添加并验证。
