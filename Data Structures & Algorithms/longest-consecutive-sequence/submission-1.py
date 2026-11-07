class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequencySet = set()

        for num in nums: 
            if num not in frequencySet: 
                frequencySet.add(num)
        res = 1 
        for i in range(len(nums)):
            diff = nums[i] -1 
            if diff in frequencySet:
                frequencySet.remove(diff)
                res+=1
        return res