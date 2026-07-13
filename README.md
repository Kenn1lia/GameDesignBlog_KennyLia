# KennyLia Game Design Blog

> FPS/TPS 游戏设计笔记 — 关卡设计、玩法机制、系统拆解

一个游戏策划的个人博客，专注射击游戏的**关卡设计、玩法设计、系统拆解与游玩体验分析**。

基于纯静态 HTML/CSS/JS 搭建，GitHub Pages 自动部署。

---

## 🚀 发布流程

**你只需要做两步：**

```
① 把 .md/.docx 草稿丢到 _inbox/
② 在 Claude 里跟我说"帮我发新文章"
```

**剩下的事我来干：**
- 读取草稿 → 转成 HTML
- 处理配图 → 放到 `assets/images/`
- 更新文章列表 → `blog.html` + `index.html`
- 清理已发布的草稿
- `git add + commit + push`

---

## 📁 项目架构

```
├── index.html                  # 首页
├── about.html                  # 关于我（简历 + 游戏数据）
├── blog.html                   # 文章列表页
│
├── _inbox/                     # 🚚  中转区 — 你丢文件给我处理的地方
│   └── README.md               #     使用说明
│
├── _scripts/                   # ⚙️  自动化维护脚本
│   ├── build.py                #     文章列表自动生成
│   ├── new-post.py             #     新文章创建向导
│   ├── serve.sh                #     本地预览服务器
│   └── README.md               #     使用说明
│
├── posts/                      # 📄 已发布文章
│   ├── hello-world.html
│   ├── fps-combat-design-thinking.html
│   └── tps-cover-system-analysis.html
│
├── assets/
│   ├── css/style.css           # 主题样式（深蓝 + 米白）
│   ├── js/main.js              # 交互脚本
│   └── images/                 # 🖼️ 网站用图，按文章分类
│       ├── _reference/         #    参考图/设计灵感（不提交）
│       ├── fps-combat/         #    FPS战斗设计相关配图
│       └── tps-cover/          #    TPS掩体系统相关配图
│
├── _templates/                 # 📋 文章模板
│   └── post-template.html      #     新建文章时复制此模板
│
├── CLAUDE.md                   # 🤖 Claude Code 项目指南
├── README.md                   # 项目说明（就是这个文件）
└── .gitignore                  # Git 忽略规则
```

### 各目录职责

| 目录 | 说明 |
|------|------|
| `_inbox/` | 🚚 **你放我取** — 丢草稿/配图进来，告诉我就行 |
| `posts/` | 📄 已发布的 HTML 文章 |
| `assets/images/` | 🖼️ 按文章分类存放的配图 |
| `_templates/` | 📋 文章模板 |
| `_scripts/` | ⚙️ 后台脚本（你不用管）|

---

## 🖼️ 配图

需要配图直接跟我说就行，比如：

> "帮我找一张 FPS 后坐力示意图放到文章里"

## 🌐 本地预览

```bash
python -m http.server 8000
```

浏览器打开 **http://localhost:8000**

---

## 📝 站点内容

| 页面 | 说明 |
|------|------|
| [首页](index.html) | 个人设计理念 + 最新文章 |
| [关于我](about.html) | 简历、游戏经历、设计方向 |
| [文章](blog.html) | FPS/TPS 深度分析文章 |

---

## 🎨 设计参考

- Marathon（数字艺术感文字）
- Arc Raiders（深蓝 + 米白色调）
- Massive / Battlefield 6（卡片网格 + 固定导航）
- Gears of War / The Division（布局结构）

---

## 👤 关于作者

**KennyLia** — 深度 FPS/TPS 玩家，Steam 总时长 6839H，专注射击游戏设计分析。

---

*从建筑空间到关卡空间 · 设计让人沉浸的体验*
