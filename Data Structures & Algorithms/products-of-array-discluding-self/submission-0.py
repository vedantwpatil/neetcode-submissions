class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum is where you build a secondary list with the previous elements summed together 
        n = len(nums)
        prefix = n * [0]
        suffix = n * [0]
        res = n * [0]

        # The first and last values of prefix and suffix need values to maintain the structure 
        prefix[0] = suffix[n-1] = 1 
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res