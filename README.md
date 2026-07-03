# 🎮 Game Design Blog

> 一个游戏策划的设计思考记录。
> 专注于 FPS / TPS 玩法设计、系统拆解与用户体验分析。

这是一个基于纯静态 HTML/CSS/JS 搭建的个人博客站点，无需构建工具，浏览器直接打开即可预览。使用 GitHub Pages 发布。

## ✨ 特性

- 暗色游戏主题设计，响应式布局
- 纯静态页面，无需后端或构建工具
- 完美适配 GitHub Pages 部署
- 中文阅读体验优先，FPS/TPS 游戏设计内容垂直

## 📂 目录结构

```
GameDesignBlog/
├── index.html           # 首页
├── about.html           # 关于我
├── blog.html            # 文章列表
├── posts/               # 博客文章
│   ├── hello-world.html
│   ├── fps-combat-design-thinking.html
│   └── tps-cover-system-analysis.html
├── assets/
│   ├── css/
│   │   └── style.css    # 主题样式
│   ├── js/
│   │   └── main.js      # 交互脚本
│   └── images/          # 图片资源
├── README.md
└── .gitignore
```

## 🚀 本地预览

### 方式一：直接打开（最简单）

双击 `index.html` 即可在浏览器中查看。

### 方式二：Python 服务器（推荐，能正常加载所有资源）

```bash
# 在项目目录下执行
python -m http.server 8000
```

然后访问 http://localhost:8000

## 📦 发布到 GitHub Pages

1. 在 GitHub 新建仓库，命名为 `你的用户名.github.io`
2. 将本目录所有文件推送到该仓库的 `main` 分支
3. 在仓库 Settings → Pages 中，Source 选择 `Deploy from a branch`，分支选 `main`，根目录选 `/ (root)`
4. 等待几分钟，访问 `https://你的用户名.github.io`

## ✏️ 如何添加新文章

1. 在 `posts/` 目录下创建新的 HTML 文件
2. 复制已有文章的 HTML 结构，替换标题、日期、正文内容
3. 在 `blog.html` 的文章列表中添加新文章的链接
4. 如果想在首页展示，也在 `index.html` 的"最新文章"区域添加

## 📝 写作规范

- 每篇文章包含 header 区的 meta 信息（标题、日期、分类、标签）
- 标签统一用小写英文
- 分类目前有：`设计方法论` / `游戏分析` / `数值设计` / `博客搭建`
- 图片放到 `assets/images/` 目录

## 🔗 链接

- [关于我](about.html)
- [全部文章](blog.html)

---

*用 ❤️ 和 🎮 驱动*
