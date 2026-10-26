class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for elem in nums:
            if elem in s:
                return True
            else:
                s.add(elem)
        return False  