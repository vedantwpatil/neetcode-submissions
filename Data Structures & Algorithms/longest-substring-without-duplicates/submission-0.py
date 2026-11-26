class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0 
        seen = set()

        best = 1 

        left, right = 0, 1

        seen.add(s[left])
        while left <= right and right < len(s): 
            lValue = s[left]
            rValue = s[right]

            if rValue in seen: 
                seen.remove(lValue)
                left += 1 
                continue

            seen.add(rValue)
            diff = right - left + 1 
            best = max(best, diff)
            right+=1

        return best        