# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        memo = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(col):
            # everything else after an obstacle should be zero 
            # because there is no way to reach it: (tl.dr break)
            if obstacleGrid[0][i]:break

            # there is one way for the rest provided they're not obstacles
            else:memo[0][i] = int(obstacleGrid[0][i] != 1)
        
        for i in range(row):
            # everything else after an obstacle should be zero 
            # because there is no way to reach it: (tl.dr break)
            if obstacleGrid[i][0]:break

            # there is one way for the rest provided they're not obstacles
            else:memo[i][0] = int(obstacleGrid[i][0] != 1)


        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j]:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]

        return memo[row-1][col-1]