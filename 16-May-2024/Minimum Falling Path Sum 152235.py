# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # we keep track of rows and columns as a state
        dp = {}
        rows = len(matrix)
        columns = len(matrix[0])
        MOVES = [[1,-1],[1,0],[1,1]]

        for i in range(columns):
            dp[rows-1,i] = matrix[rows-1][i]
        for i in range(rows-2,-1,-1):
            for j in range(columns):
                valid_below_cells = []
                for dx,dy in MOVES:
                    x,y = dx+i,dy+j
                    if 0 <= x < rows and 0 <= y < columns:
                        valid_below_cells.append(dp[x,y])
                dp[i,j] = min(valid_below_cells) + matrix[i][j]
        return min([dp[0,j] for j in range(columns)])
                