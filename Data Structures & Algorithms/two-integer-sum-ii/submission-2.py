class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 

        while left < right and right < len(numbers):
            lValue = numbers[left]
            rValue = numbers[right]

            diff = target - rValue
            if diff == lValue: 
                return [left + 1, right + 1]
            if diff > lValue: 
                left+=1
            elif diff < lValue: 
                right-=1

        return [-1,-1]
