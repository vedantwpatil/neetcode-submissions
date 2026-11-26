#!/usr/bin/env bash
# Copy your latest NeetCode solve and open the matching LeetCode problem to paste it into.
# Usage: ./lc.sh [neetcode-problem-folder]
set -euo pipefail

cd "$(dirname "$0")"

git pull --ff-only --quiet

# git picks the problem (latest to gain a submission); a bulk sync that added several takes the last
latest=$(git -c core.quotePath=false log -1 --diff-filter=A --name-only --format= \
  -- ":(glob)*/${1:-*}/submission-*" | tail -n 1)
# the highest number picks the attempt: bulk syncs commit old attempts late
file=''
[[ -z $latest ]] || file=$(ls "${latest%/*}"/submission-* | sort -V | tail -n 1)
[[ -f $file ]] || {
  echo "no submission found${1:+ for $1}" >&2
  exit 1
}

slug=$(basename "$(dirname "$file")")
lc=$(awk -v s="$slug" '$1 == s { print $2 }' lc-aliases.txt)
lc=${lc:-$slug}

case $file in
  *.py) lang=python3 def='^[[:space:]]*def ' ;;
  *.rs) lang=rust def='^[[:space:]]*pub fn ' ;;
  *) lang=${file##*.} def='' ;;
esac

res=$(jq -n --arg s "$lc" \
  '{query: "query($s: String!) { question(titleSlug: $s) { codeSnippets { langSlug code } } }", variables: {s: $s}}' |
  curl -fsS --max-time 20 https://leetcode.com/graphql -H 'Content-Type: application/json' -d @-)
jq -e '.data.question' >/dev/null <<<"$res" || {
  echo "no LeetCode problem '$lc': add '$slug <leetcode-slug>' to lc-aliases.txt" >&2
  exit 1
}

code=$(cat "$file")

# method names defined in the source on stdin (commented-out lines don't match)
names() { sed -nE "s/$def([A-Za-z0-9_]+).*/\1/p"; }

want=''
[[ -z $def ]] || want=$(jq -r --arg l "$lang" '.data.question.codeSnippets[]? | select(.langSlug == $l) | .code' <<<"$res" | names)

if [[ -z $want ]]; then
  echo "warning: method name not checked (Premium problem or unsupported language)"
else
  have=$(names <<<"$code")
  missing=$(comm -23 <(sort -u <<<"$want") <(sort -u <<<"$have"))
  old=$(sed -n 1p <<<"$have")
  if [[ -n $missing ]]; then
    # only a single-method problem is safe to rename; design problems are left alone
    if [[ -n $old && $want != *$'\n'* ]]; then
      code=$(sed -E "s/(def |fn |self\.|Self::|Solution::)$old\(/\1$want(/g" <<<"$code")
      echo "renamed $old -> $want (check that was your main method)"
    else
      echo "warning: LeetCode also expects: $(tr '\n' ' ' <<<"$missing")"
    fi
  fi
fi

url="https://leetcode.com/problems/$lc/"
printf '%s\n' "$code" | pbcopy
echo "copied $file"
echo "set the editor to $lang, select all, paste, Submit: $url"
open "$url"
