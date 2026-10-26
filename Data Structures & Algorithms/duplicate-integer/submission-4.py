class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_dup = set()
        for element in nums: 
            if element not in set_dup: 
                set_dup.add(element)
            else: 
                return True
        return False
        