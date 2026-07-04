#!/usr/bin/env python3
"""
Game Design Blog — 新文章创建器
================================
从 _templates/post-template.html 复制模板，
自动填入标题、日期、分类、标签。
"""

import os
import re
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_FILE = PROJECT_ROOT / "_templates" / "post-template.html"
POSTS_DIR = PROJECT_ROOT / "posts"


def slugify(text: str) -> str:
    """将中文标题转为拼音式 slug（保留字母数字和连字符）。"""
    # 只保留字母数字和中文，空格转连字符
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"\s+", "-", slug.strip())
    # 如果是纯中文，直接用英文关键词或简短拼音替代
    if not slug:
        slug = "new-post"
    return slug


def create_post():
    print("📝 Game Design Blog — 创建新文章\n")

    # --- 收集信息 ---
    title = input("文章标题: ").strip()
    if not title:
        print("❌ 标题不能为空")
        sys.exit(1)

    category = input("分类 (如: 设计方法论/游戏分析/关卡设计): ").strip()
    if not category:
        category = "未分类"

    tags_input = input("标签 (用逗号分隔, 如: FPS,战斗设计): ").strip()
    tags = [t.strip() for t in tags_input.split(",") if t.strip()]

    today_str = date.today().strftime("%Y.%m.%d")
    date_input = input(f"日期 (默认 {today_str}): ").strip()
    if not date_input:
        date_input = today_str

    excerpt = input("文章摘要 (60-80字): ").strip()
    if not excerpt:
        excerpt = title

    # --- 文件名 ---
    slug = slugify(title)
    filename = f"{slug}.html"
    filepath = POSTS_DIR / filename

    if filepath.exists():
        overwrite = input(f"⚠️  {filename} 已存在，覆盖? (y/N): ").strip().lower()
        if overwrite != "y":
            print("❌ 已取消")
            sys.exit(1)

    # --- 读取模板 ---
    if not TEMPLATE_FILE.exists():
        print(f"❌ 找不到模板文件: {TEMPLATE_FILE}")
        sys.exit(1)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # --- 替换占位符 ---
    html = html.replace("<!-- DESC: 文章摘要，60-80字 -->", excerpt)
    html = html.replace("<!-- TITLE: 文章标题 -->", title)
    html = html.replace("<!-- DATE: YYYY.MM.DD -->", date_input)
    html = html.replace("<!-- CATEGORY: 分类标签 -->", category)

    # 替换标签
    if tags:
        # 找标签占位区域并替换
        tags_html = "\n        ".join(f'<span>{t}</span>' for t in tags)
        # 替换第一个标签占位
        html = re.sub(r"<span><!-- TAG\d --></span>", "", html)
        # 在注释标签的地方插入新标签
        first_tag_comment = "<!-- 更多标签... -->"
        if first_tag_comment in html:
            html = html.replace(first_tag_comment, tags_html)
        else:
            # 如果找不到注释，就替换 .post-tags div 的内容
            html = re.sub(
                r'(<div class="post-tags">)\s*(.*?)\s*(</div>)',
                f'\\1\n        {tags_html}\n      \\3',
                html,
                flags=re.DOTALL,
            )

    # 移除空的标签占位行
    html = re.sub(r"<span></span>\s*", "", html)

    # --- 写入文件 ---
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✅ 文章已创建: {filepath}")
    print(f"   标题: {title}")
    print(f"   日期: {date_input}")
    print(f"   分类: {category}")
    print(f"   标签: {', '.join(tags)}")
    print()
    print("👉 接下来:")
    print("   1. 编辑文章内容: 打开 posts/ 下的 HTML 文件")
    print("   2. 更新页面: python _scripts/build.py")
    print("   3. 本地预览: python -m http.server 8000")


if __name__ == "__main__":
    create_post()
