class Solution:
    def trap(self, heights: List[int]) -> int:
        solution,n = 0,len(heights)
        max_before, max_after = [heights[0]]*n, [heights[-1]]*n

        for i in range(1,n):
            max_before[i] = max(max_before[i-1], heights[i])
            max_after[n-1-i] = max(max_after[n-i], heights[n-1-i])
        for i in range(1,n-1):
            margin = min(max_before[i],max_after[i])
            if margin > heights[i]:
                solution += margin-heights[i]
        return solution