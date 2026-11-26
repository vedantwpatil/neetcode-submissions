class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        seen_letters = defaultdict(int)
        best = 0

        while right < len(s):
            r_letter = s[right]
            seen_letters[r_letter] += 1

            while (right - left + 1) - max(seen_letters.values()) > k:
                l_letter = s[left]
                seen_letters[l_letter] -= 1
                left += 1

            diff = right - left + 1
            best = max(best, diff)
            right += 1
        return best 