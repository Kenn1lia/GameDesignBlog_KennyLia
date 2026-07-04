#!/usr/bin/env python3
"""
Game Design Blog — 自动文章列表生成器
=======================================
从 posts/ 目录扫描 HTML 文章，提取元数据，
自动更新 blog.html（文章列表）和 index.html（最新文章）。
"""

import re
import os
import sys
from datetime import datetime
from pathlib import Path

# ---------- 路径配置 ----------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = PROJECT_ROOT / "posts"
OUTPUT_BLOG = PROJECT_ROOT / "blog.html"
OUTPUT_INDEX = PROJECT_ROOT / "index.html"


def parse_post(filepath: Path) -> dict | None:
    """从 HTML 文章中提取元数据。"""
    if filepath.name.startswith("_") or filepath.name.startswith("."):
        return None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception:
        return None

    # --- 提取 title ---
    title_match = re.search(r"<h1>(.*?)</h1>", html)
    title = title_match.group(1).strip() if title_match else filepath.stem

    # --- 提取 description / excerpt ---
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html)
    excerpt = desc_match.group(1).strip() if desc_match else ""

    # --- 提取 date ---
    date_match = re.search(r"<span>(\d{4}\.\d{2}\.\d{2})</span>", html)
    if not date_match:
        date_match = re.search(r"(\d{4})[年.-](\d{1,2})[月.-](\d{1,2})", html)
    date = date_match.group(1) if date_match else "2099.12.31"
    # Normalize date format
    date = date.replace("年", ".").replace("月", ".").replace("日", "")
    if date_match and date_match.lastindex == 3:
        date = f"{int(date_match.group(1)):04d}.{int(date_match.group(2)):02d}.{int(date_match.group(3)):02d}"

    # --- 提取 category ---
    cat_match = re.search(r"<span>([^<>\d.]+?)</span>\s*</div>\s*<h1>", html)
    if not cat_match:
        cat_match = re.search(r"class=\"post-meta\".*?<span>([^<>\n]+?)</span>", html, re.DOTALL)
    category = cat_match.group(1).strip() if cat_match else "未分类"

    # --- 提取 tags ---
    tags_section = re.search(
        r'<div\s+class="post-tags">(.*?)</div>\s*</header>', html, re.DOTALL
    )
    tags = []
    if tags_section:
        tags = re.findall(r"<span>(.*?)</span>", tags_section.group(1))
    tags = tags[:6]  # 最多 6 个标签

    return {
        "filename": filepath.name,
        "title": title,
        "date": date,
        "category": category,
        "tags": tags,
        "excerpt": excerpt,
    }


def collect_posts() -> list[dict]:
    """收集所有文章并按日期降序排列。"""
    posts = []
    for f in sorted(POSTS_DIR.glob("*.html")):
        parsed = parse_post(f)
        if parsed:
            posts.append(parsed)

    # 按日期降序（最新的在前面）
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def generate_blog_list(posts: list[dict]) -> str:
    """生成文章列表的 HTML 片段。"""
    cards = []
    for i, p in enumerate(posts):
        featured_class = " featured" if i == 0 else ""
        tags_html = "".join(f'<span>{t}</span>' for t in p["tags"])

        card = f"""      <article class="post-card{featured_class}">
        <span class="post-category">{p['category']}</span>
        <span class="post-date">{p['date']}</span>
        <h2><a href="posts/{p['filename']}">{p['title']}</a></h2>
        <p class="post-excerpt">
          {p['excerpt']}
        </p>
        <div class="post-tags">
          {tags_html}
        </div>
      </article>"""
        cards.append(card)

    return "\n".join(cards)


def generate_featured_posts(posts: list[dict], count: int = 3) -> str:
    """生成首页最新文章的 HTML 片段。"""
    return generate_blog_list(posts[:count])


def update_blog_html(posts: list[dict]) -> bool:
    """更新 blog.html 中的文章列表。"""
    if not OUTPUT_BLOG.exists():
        print(f"❌ 找不到 {OUTPUT_BLOG}")
        return False

    with open(OUTPUT_BLOG, "r", encoding="utf-8") as f:
        content = f.read()

    # 替换文章列表（在 blog-grid 中）
    list_html = generate_blog_list(posts)
    updated = re.sub(
        r'(<div class="blog-grid">).*?(</div>\s*</div>\s*<footer)',
        rf'\1\n{list_html}\n\n    \2',
        content,
        flags=re.DOTALL,
    )

    # 更新文章计数
    updated = re.sub(
        r"共 \d+ 篇文章",
        f"共 {len(posts)} 篇文章",
        updated,
    )

    if updated == content:
        print("⚠️  blog.html 无变化")
        return False

    with open(OUTPUT_BLOG, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"✅ blog.html 已更新 — 共 {len(posts)} 篇文章")
    return True


def update_index_html(posts: list[dict]) -> bool:
    """更新 index.html 中的最新文章列表。"""
    if not OUTPUT_INDEX.exists():
        print(f"❌ 找不到 {OUTPUT_INDEX}")
        return False

    with open(OUTPUT_INDEX, "r", encoding="utf-8") as f:
        content = f.read()

    # 替换首页最新文章列表
    featured_html = generate_featured_posts(posts)
    marker_pattern = r'(<div class="blog-grid" style="margin-bottom:32px;">).*?(</div>\s*</div>\s*<div style="text-align)'
    updated = re.sub(
        marker_pattern,
        rf'\1\n{featured_html}\n\n      \2',
        content,
        flags=re.DOTALL,
    )

    if updated == content:
        print("⚠️  index.html 无变化")
        return False

    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"✅ index.html 已更新")
    return True


def main():
    print(f"🔍 扫描目录: {POSTS_DIR}")
    posts = collect_posts()

    if not posts:
        print("❌ 没有找到文章")
        sys.exit(1)

    print(f"📄 找到 {len(posts)} 篇文章:")
    for p in posts:
        print(f"   [{p['date']}] {p['title']}")

    print("\n🔄 更新 blog.html...")
    update_blog_html(posts)

    print("🔄 更新 index.html...")
    update_index_html(posts)

    print("\n✨ 完成！运行 python -m http.server 8000 本地预览")


if __name__ == "__main__":
    main()
