# Contributing / 贡献指南

## English

Open an issue with the actual prompt, expected behavior, observed output, relevant environment, and a minimal reproducible example. Remove secrets and private customer material before sharing.

For pull requests:

1. Keep the skill focused on technology brand showcase websites and single-file HTML delivery.
2. Change the canonical instructions in `skills/tech-brand-website/SKILL.md`; avoid adding unrelated runtime dependencies or turning the package into a mandatory framework.
3. Update English and Chinese documentation together when behavior, installation, or defaults change. Website language remains configurable; the default is Chinese.
4. Run `python scripts/validate.py`. If changing UI metadata, keep `agents/openai.yaml` aligned with the manifest name.
5. For behavioral changes, try a realistic website request and report the browser, viewports, theme, motion preference, and checks actually performed. Distinguish acceptance criteria from measured results.
6. Update `CHANGELOG.md` with the user-visible change and explain the problem and validation in the pull request.

Preserve the MIT notice. New images, fonts, videos, and copied code must have redistribution rights and appropriate attribution. Avoid reproducing reference brands' logos or claiming their endorsement.

## 中文

提交 Issue 时提供实际提示词、预期行为、观察到的结果、相关环境与最小复现示例。分享前移除密钥和客户私密内容。

提交 PR 时：

1. 保持科技品牌展示官网和单文件 HTML 的范围。
2. 修改 `skills/tech-brand-website/SKILL.md` 中的规范，不引入无关运行依赖，也不强制迁移到其他框架。
3. 行为、安装方法或默认值变化时同步更新中英文文档；默认页面语言为中文，允许用户指定其他语言。
4. 运行 `python scripts/validate.py`，修改界面元数据时保持 skill 名称一致。
5. 行为变化应使用真实场景生成页面，报告浏览器、视口、主题、动态偏好及真正执行过的检查，区分验收标准与实测结果。
6. 更新 `CHANGELOG.md`，在 PR 中说明问题、修改结果和验证范围。

保留 MIT 许可声明。新增图片、字体、视频和引用代码须具备分发授权及必要署名，避免复制参考品牌标识或宣称其背书。
