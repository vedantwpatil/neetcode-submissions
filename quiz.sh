#!/usr/bin/env bash
# Pick 3-6 random solved problems to redo on neetcode.io (These serve as additional practice and would be solved in rust to give additional familiarity with the problem).
# Usage: ./quiz.sh [count]   (count must be 3-6; default random)
set -euo pipefail

cd "$(dirname "$0")"

n=${1:-$((RANDOM % 4 + 3))}
[[ $n =~ ^[3-6]$ ]] || {
  echo "count must be 3-6" >&2
  exit 1
}

# topic/problem-id dirs; skip .git
picked=$(find . -mindepth 2 -maxdepth 2 -type d -not -path './.git*' | sort -R | head -n "$n")
[[ -n $picked ]] || {
  echo "no solved problems found" >&2
  exit 1
}

i=1
while IFS= read -r dir; do
  slug=$(basename "$dir")
  topic=$(basename "$(dirname "$dir")")
  printf '%d. %s  [%s]\n   https://neetcode.io/problems/%s/question\n' "$i" "$slug" "$topic" "$slug"
  i=$((i + 1))
done <<<"$picked"
