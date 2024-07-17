# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1 for c in range(n)] for r in range(n)]
        def solve(i,j):

            if i+1 == j:
                return 0 

            if dp[i][j] != -1:
                return dp[i][j]
            score = float('inf')

            for k in range(i+1,j):
                score = min(score, values[i]* (values[j] * values[k]) + solve(i,k) + solve(k,j))
                
            dp[i][j] = score
            return dp[i][j]

        return solve(0,n-1 )