class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for elem in nums:
            if elem in s:
                return true
            else:
                s.add(elem)
        return false  