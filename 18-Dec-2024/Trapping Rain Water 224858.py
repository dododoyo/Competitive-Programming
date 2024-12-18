# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        # for each day if we register what is maximum 
        # before us and what is maximum after us
        # we can solve this by taking minimum of the two maxes

        # to do this we can use 
        # array => O(n) or heap => O(n*logn)

        # get max before
        max_before = [heights[0]]
        for i in range(1,n):
            max_before.append(max(max_before[-1],heights[i]))
        
        max_after = [heights[-1]]
        for i in range(n-2,-1,-1):
            max_after.append(max(max_after[-1],heights[i]))

        rain = 0
        max_after = max_after[::-1]

        for i in range(1,n-1):
            rain += min(max_after[i],max_before[i]) - heights[i]
        
        return rain