class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqSet = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in freqSet: 
                indx = freqSet[diff]     
                return [indx, index]
            freqSet[num] = index 
        return []