class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        left, right = 0,1 

        while right < len(prices): 
            profit = prices[right]- prices[left] 
            best = max(best, profit)
            if prices[left] > prices[right]: 
                left = right 
            right += 1 

        return best 