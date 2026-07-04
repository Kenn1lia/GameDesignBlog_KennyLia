# Game Design Blog — Claude Code 项目指南

## 项目概述
KennyLia 的个人游戏设计博客，纯静态 HTML/CSS/JS，托管在 GitHub Pages。
专注 FPS/TPS 品类的关卡设计、玩法机制、系统拆解与分析。

## 目录结构

```
├── index.html              # 首页（设计信条 + 最新文章）
├── about.html              # 关于我（简历 + 游戏经历）
├── blog.html               # 文章列表页
│
├── _inbox/                 # 🚚 中转区 — 用户丢草稿/素材给我
├── posts/                  # 📄 已发布文章（HTML）
├── _templates/             # 📋 文章模板
│
├── assets/
│   ├── css/style.css       # 主题样式
│   ├── js/main.js          # 交互脚本
│   └── images/             # 🖼️ 配图（按文章分类存放）
│       ├── fps-combat/
│       ├── tps-cover/
│       └── _reference/     # 参考素材（不提交）
│
├── _scripts/               # ⚙️ 自动化工具
│   ├── build.py            #   文章列表自动生成
│   ├── new-post.py         #   新文章创建向导
│   ├── serve.sh            #   本地预览服务器
│   └── README.md           #   使用说明
│
├── CLAUDE.md               # 项目指南（这个文件）
└── README.md               # 项目说明
```

## 维护规范

### 写新文章
1. 从 `_templates/post-template.html` 复制
2. 命名：`posts/英文短描述.html`（如 `level-design-principles.html`）
3. 头部 meta：description 写 60-80 字摘要
4. 日期格式：`YYYY.MM.DD`
5. 分类可选：设计方法论 / 游戏分析 / 关卡设计 / 博客搭建
6. 标签 2-6 个，大写英文优先

### 更新文章列表
每次增删文章后，运行 `python _scripts/build.py` 自动更新：
- `blog.html` — 文章列表页
- `index.html` — 首页最新文章区

### 配图管理
- 文章配图放 `assets/images/<分类>/`
- 参考素材/草稿图放 `assets/images/_reference/`（不提交）
- 引用路径示例：`../assets/images/fps-combat/recoil-pattern.png`

### 发布
```bash
python _scripts/build.py     # 更新文章列表
python -m http.server 8000   # 本地预览
git add .
git commit -m "feat: 新文章 xxx"
git push                     # GitHub Pages 自动部署
```

### 样式主题
- 主色：深蓝基底（`--navy-900`）+ 米白段落（`--cream-50`）
- 强调色：FPS 橙色（`--orange-500`）/ TPS 蓝色（`--blue-400`）
- 字体：Space Grotesk（标题）+ JetBrains Mono（代码）
- 设计参考：Marathon / Arc Raiders / Battlefield 6
