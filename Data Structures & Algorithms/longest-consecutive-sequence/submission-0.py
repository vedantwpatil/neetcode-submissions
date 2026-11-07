class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequencySet = set()

        for num in nums: 
            if num not in frequencySet: 
                frequencySet.add(num)
        res = 0 
        for i in range(len(nums)):
            diff = nums[i] -1 
            if diff in frequencySet:
                res+=1 
        return res