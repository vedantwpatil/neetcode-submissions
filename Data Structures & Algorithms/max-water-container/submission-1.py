class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0
        while left < right: 
            h = min(heights[left], heights[right])
            length = right - left
            area = length * h
            best = max(area, best)

            if heights[left] < heights[right]:
                left += 1 
            else: 
                right-= 1

        return best  