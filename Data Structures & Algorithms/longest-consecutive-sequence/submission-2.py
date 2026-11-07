class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequencySet = set(nums)
        res = 0 
        for num in frequencySet:
            if num - 1 not in frequencySet:
                length = 1
                while num + length in frequencySet:
                    length += 1
                res = max(res, length)
        return res