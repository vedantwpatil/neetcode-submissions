class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1 

        while left < right: 
            runningSum = numbers[left] + numbers[right] 
            if runningSum < target:
                left += 1
            elif runningSum > target:
                right -= 1 

            elif runningSum == target:
                return [left+1,right+1] 
        return [-1,-1]
        