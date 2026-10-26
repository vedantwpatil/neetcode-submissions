class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = set()

        for num in nums:
            if not num in frequency:
                frequency.add(num)
            else: 
                return True 
            
        return False


