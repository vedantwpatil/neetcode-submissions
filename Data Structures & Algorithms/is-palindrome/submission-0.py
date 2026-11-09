class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s_filtered = ''.join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(s_filtered) - 1 
        while left < right:
            if s_filtered[left] != s_filtered[right]:
                return False
            left += 1
            right -= 1
        return True