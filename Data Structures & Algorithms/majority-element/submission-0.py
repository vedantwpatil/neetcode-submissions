class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencySet = {}

        for element in nums: 
            frequencySet[element] = frequencySet.get(element, 0) + 1 
        total = 0 
        res = 0 
        for element in frequencySet: 
            if total < frequencySet[element]:
                total = frequencySet[element] 
                res = element

        return res
