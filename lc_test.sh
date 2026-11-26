#!/usr/bin/env bash
# Offline check for lc.sh. Usage: ./lc_test.sh
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
t=$(mktemp -d)
trap 'rm -rf "$t"' EXIT

# stand-ins so the test never touches the network, clipboard or browser
mkdir "$t/bin"
cat >"$t/bin/curl" <<'EOF'
#!/bin/sh
cat >/dev/null
cat <<'JSON'
{"data":{"question":{"codeSnippets":[
  {"langSlug":"python3","code":"# def commented(\nclass Solution:\n    def containsDuplicate(self, nums):\n"},
  {"langSlug":"rust","code":"impl Solution {\n    pub fn contains_duplicate(nums: Vec<i32>) -> bool {\n"}]}}}
JSON
EOF
printf '#!/bin/sh\ncat >"%s/clip"\n' "$t" >"$t/bin/pbcopy"
printf '#!/bin/sh\necho "$1" >"%s/url"\n' "$t" >"$t/bin/open"
chmod +x "$t"/bin/*

# add <problem> <file> <source>: commit a submission the way NeetCode's sync does
add() {
  mkdir -p "$t/origin/Topic & Co/$1"
  printf '%s\n' "$3" >"$t/origin/Topic & Co/$1/$2"
  git -C "$t/origin" add -A
  git -C "$t/origin" -c user.name=t -c user.email=t@t -c commit.gpgsign=false commit -qm "$1 $2"
}
run() { PATH="$t/bin:$PATH" "$t/work/lc.sh" "$@" >/dev/null; }
check() { diff "$t/clip" - && [[ $(cat "$t/url") == "https://leetcode.com/problems/$1/" ]]; }

git init -q "$t/origin"
add two-integer-sum submission-0.py 'x'
git clone -q "$t/origin" "$t/work"
cp "$here/lc.sh" "$here/lc-aliases.txt" "$t/work/"

# committed after the clone, so lc.sh only sees it if it pulls
add duplicate-integer submission-0.py $'class Solution:\n    def hasDuplicate(self, nums):\n        return self.hasDuplicate(nums)'
run
check contains-duplicate <<'EOF'
class Solution:
    def containsDuplicate(self, nums):
        return self.containsDuplicate(nums)
EOF

add duplicate-integer submission-1.rs $'impl Solution {\n    pub fn has_duplicate(nums: Vec<i32>) -> bool {\n        Self::has_duplicate(nums)'
run
check contains-duplicate <<'EOF'
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        Self::contains_duplicate(nums)
EOF

# an old attempt synced late must not replace the highest-numbered one
add duplicate-integer submission-3.py $'class Solution:\n    def containsDuplicate(self, nums):\n        return True'
add duplicate-integer submission-2.py 'stale'
run
check contains-duplicate <<'EOF'
class Solution:
    def containsDuplicate(self, nums):
        return True
EOF

# a named problem wins over the newest one
run two-integer-sum
[[ $(cat "$t/url") == https://leetcode.com/problems/two-sum/ ]]

if run no-such-problem 2>/dev/null; then
  echo "expected failure for an unknown problem" >&2
  exit 1
fi

echo ok
