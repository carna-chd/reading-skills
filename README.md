# 书籍深度蒸馏与互动阅读页

将用户提供的书籍整理为有原文位置可追溯的知识数据，并生成可离线打开的互动 HTML 阅读页。

这是提供给 AI 代理使用的 skill。它包含工作方法、内容规范、网页模板和生成脚本。书籍阅读与分析由 AI 及其可用工具完成，生成脚本负责把整理好的 JSON 数据渲染成网页。

## 功能

- 阅读模式与深度探索模式。
- 导读、结构速览、逐章解读、核心概念、精选表述、批判与评价、现实问题、行动清单。
- 板块与章节折叠、全文搜索、概念关联跳转、阅读进度。
- 单文件离线网页，适配手机与电脑，支持打印。
- 区分原书观点、编辑分析和外部资料；记录完整或部分覆盖范围。

## 包内结构

```text
README.md
book-distill-web/
  SKILL.md
  agents/openai.yaml
  scripts/render_reader.py
  assets/reader-template.html
  references/content-schema.md
  references/distillation-method.md
```

必须分享整个 `book-distill-web` 文件夹，不能只上传 `SKILL.md`。它通过相对路径读取模板和参考资料。

## 运行条件

1. 能读取本地文件、分析长文并执行 Python 的 AI 代理环境。本包按 Codex skill 形式整理；其他支持 Agent Skills 的工具需要遵循各自的安装方法。
2. Python 3。网页生成脚本只使用 Python 标准库，无需额外安装 Python 包。
3. PDF、EPUB、DOCX 的提取工具由使用环境提供。扫描件还需要 OCR；本包没有内置 OCR 引擎。

生成脚本本身不调用模型、不分析书籍，也不需要 API Key。AI 工具本身的账号、用量与权限由使用者自行配置。已有 HTML 阅读页可直接在浏览器打开。

## 上传到 GitHub

以下采用仓库名 `reading-skills` 举例，可更换名称。

1. 在 GitHub 新建一个 Public 仓库 `reading-skills`。
2. 在仓库页面选择上传文件。空仓库可点击 `uploading an existing file`；已有文件时选择 `Add file → Upload files`。
3. 将本目录中的 `README.md` 和整个 `book-distill-web` 文件夹一起拖入上传区域，保留文件夹层级。
4. 点击 `Commit changes`。上传后，仓库根目录应直接包含 `README.md` 和 `book-distill-web/`。
5. 打开仓库中的 `book-distill-web` 文件夹，复制地址栏链接分享。不要只上传 ZIP，否则安装器不能按路径直接找到 skill。

此操作分享源文件，不需要开启 GitHub Pages。这个本地分享包尚未自动上传到任何仓库。

## 对方怎样安装

### 方法一：请 Codex 安装 GitHub 文件夹

上传完成后，对方可以将下面的话发给 Codex，替换成实际文件夹链接：

```text
$skill-installer 请从以下 GitHub 文件夹安装 book-distill-web：
https://github.com/你的用户名/reading-skills/tree/main/book-distill-web
```

安装后在下一轮对话调用。如果没有出现，请重启 Codex。上述 URL 是结构示例，上传后才会产生真实地址。

### 方法二：下载后手动放入本地 skill 目录

按当前官方文档，用户级目录是 `~/.agents/skills/`。将整个文件夹放进去，使路径为：

```text
~/.agents/skills/book-distill-web/SKILL.md
```

Windows 对应：

```text
C:\Users\对方用户名\.agents\skills\book-distill-web\SKILL.md
```

保留所有同级子目录。部分既有 Codex 安装器仍使用 `~/.codex/skills/`，可让当前环境的安装器处理路径；避免在多个目录重复安装同名 skill。

## 安装后怎样使用

将以下话发给 Codex，替换书籍路径和输出位置：

```text
使用 $book-distill-web，分析这本书：<本地书籍路径>。
先核对目录、总页数和可读性，再按原书顺序分析正文，记录覆盖范围。
生成 book-data.json 和可离线打开的互动 HTML 阅读页，保存到 <输出目录>。
逐章解读应讲清主线、论证与例子，概念关系应支持跳转。
缺页或无法提取的内容要明确标出，不要把节选说成全书。
```

如果已经有符合规范的 `book-data.json`，可以直接从 skill 文件夹执行：

```text
python scripts/render_reader.py --data <book-data.json路径> --output <阅读页.html路径>
```

## 分享范围

本包只含 skill 文件与说明，不含书籍 PDF、用户个人资料和已完成的书籍分析。对外分发源文件之前，可按自己的授权意愿另行添加许可证；本包没有代作者选择许可条款。

普通聊天窗口能否直接使用 ZIP，取决于它是否支持该 skill 格式以及文件读取、脚本执行；仅上传说明文字不等同于完成安装。

## 参考

- [OpenAI 官方 skills 文档](https://learn.chatgpt.com/docs/build-skills)
- [GitHub 官方上传文件说明](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

官方目前推荐通过插件进行更广泛的安装分发。本包先提供 GitHub 文件夹安装和本地使用，不代表已在插件目录发布。
