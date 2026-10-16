class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l , r = 0, len(heights)-1
        max_Area = 0 

        while l <= r:

            h = min (heights[l] , heights[r])
            w = r-l
            max_Area = max(max_Area , h*w)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        
        return max_Area