# KennyLia Game Design Blog

> 建筑学背景 × 游戏关卡策划 | FPS/TPS 设计笔记

一个游戏策划的个人博客，专注射击游戏的**关卡设计、玩法设计、系统拆解与游玩体验分析**。

基于纯静态 HTML/CSS/JS 搭建，GitHub Pages 自动部署。

---

## 🚀 快速发布流程

```
┌─ 写文章 ──────────────────────────┐
│  你：丢 Word/MD 到 _inbox/        │
│  或：python _scripts/new-post.py   │  ← 自动化创建
└──────────┬────────────────────────┘
           ▼
┌─ 编辑内容 ────────────────────────┐
│  编辑 posts/xxx.html              │
│  配图 → 放到 assets/images/       │
└──────────┬────────────────────────┘
           ▼
┌─ 生成列表 ────────────────────────┐
│  python _scripts/build.py          │  ← 自动更新 blog.html / index.html
└──────────┬────────────────────────┘
           ▼
┌─ 本地预览 ────────────────────────┐
│  bash _scripts/serve.sh           │  ← http://localhost:8000
│  或：python -m http.server 8000   │
└──────────┬────────────────────────┘
           ▼
┌─ git push ────────────────────────┐
│  GitHub Pages 自动部署上线         │
└──────────────────────────────────┘
```

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

| 目录 | 谁管 | 说明 |
|------|------|------|
| `_inbox/` | **你放我取** | Word/MD 草稿、截图、参考图 — 丢进去告诉我就行 |
| `_scripts/` | **自动/你** | 维护脚本：`build.py`（更新文章列表）、`new-post.py`（新建文章） |
| `posts/` | AI 维护 | 已发布的 HTML 文章，有我创建 |
| `assets/images/` | AI 维护 | 按文章分类存放配图，路径已优化适配 GitHub Pages |
| `_templates/` | AI 维护 | 文章模板，保证每篇风格统一 |

---

## 🖼️ 图片管理规则

需要配图时，直接跟我说清楚就行：

> "帮我找一张 FPS 后坐力模式的示意图，放到 fps-combat 那篇文章里"

我会：
1. 搜索合适的图片
2. 放到 `assets/images/<分类>/` 目录下
3. 在文章中引用正确的相对路径

**图片引用路径示例：**
```html
<img src="../assets/images/fps-combat/recoil-pattern.png" alt="弹道后坐力模式示意图">
```

---

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
| [关于我](about.html) | 简历、游戏经历（6839H）、设计方向 |
| [文章](blog.html) | FPS/TPS 深度分析文章 |

### 文章列表

- [FPS 战斗设计思考：从射击手感说起](posts/fps-combat-design-thinking.html)
- [TPS 掩体系统拆解：从 Gears of War 到 The Division](posts/tps-cover-system-analysis.html)
- [Hello World — 这个博客是关于什么的](posts/hello-world.html)

---

## 🎨 设计参考

- Marathon（数字艺术感文字）
- Arc Raiders（深蓝 + 米白色调）
- Massive / Battlefield 6（卡片网格 + 固定导航）
- Gears of War / The Division（布局结构）

---

## 👤 关于作者

**KennyLia** — 哈工大深圳建筑学硕士在读 · 广美建筑学学士 · 期望关卡策划岗位（FPS/TPS）。
Steam 总时长 6839H，深度 FPS/TPS 玩家，写过代码、画过图纸、打过几千小时射击游戏。

---

*从建筑空间到关卡空间 · 设计让人沉浸的体验*
