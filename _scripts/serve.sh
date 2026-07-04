#!/bin/bash
# Game Design Blog — 本地预览服务器
# 用法: bash _scripts/serve.sh [端口号]

PORT=${1:-8000}
DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "🎮 Game Design Blog — 本地预览"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  地址: http://localhost:${PORT}"
echo "  目录: ${DIR}"
echo "  退出: Ctrl+C"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

cd "$DIR" && python3 -m http.server "$PORT"
