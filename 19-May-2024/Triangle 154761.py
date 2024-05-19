# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = defaultdict(lambda : -1)
        rows = len(triangle)
        last_column = len(triangle[-1])
        
        def find_min_path(i,j):
            if i == 0 and j == 0:
                dp[i,j] = triangle[i][j]
                return dp[i,j]

            if j >= len(triangle[i]) or i < 0  or j < 0:
                return float("inf")

            if dp[i,j] != -1:
                return dp[i,j]
                
            current_cost = triangle[i][j]

            up = current_cost + find_min_path(i-1,j)
            up_then_left = current_cost + find_min_path(i-1,j-1)

            dp[i,j] = min(up,up_then_left)

            return dp[i,j]

        solution = float("inf")
        for column in range(last_column):
            solution = min(solution,find_min_path(rows-1,column))
        return solution