# ⚙️ _scripts / 自动化维护工具

## 快速使用

```bash
# 1. 创建新文章（交互式）
python _scripts/new-post.py

# 2. 写完后更新文章列表（blog.html + index.html）
python _scripts/build.py

# 3. 本地预览
bash _scripts/serve.sh        # 默认 8000 端口
bash _scripts/serve.sh 3000   # 自定义端口
```

## 脚本说明

| 脚本 | 功能 | 什么时候用 |
|------|------|-----------|
| `new-post.py` | 从模板创建新文章，自动填入标题/日期/分类/标签 | 写新文章时 |
| `build.py` | 扫描 `posts/` 目录，自动更新 `blog.html` 和 `index.html` 的文章列表 | 文章增删改后 |
| `serve.sh` | 启动本地 HTTP 服务器预览 | 想看看效果时 |

## 工作流

```
  python _scripts/new-post.py       创建新文章
         │
         ▼
  编辑 posts/xxx.html                写内容
         │
         ▼
  python _scripts/build.py          更新页面列表
         │
         ▼
  bash _scripts/serve.sh            本地预览
         │
         ▼
  git add + git push                发布上线
```

## 依赖

- Python 3.7+
- 无需额外安装任何第三方库（只用标准库）
