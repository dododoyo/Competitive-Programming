# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])

        # initialize the first row
        last_row_paths = [0]*n
        row_index = 0
        while row_index < n and (obstacleGrid[row_index][0] == 0):
            last_row_paths[row_index] = 1
            row_index += 1

        # initialize the first column 
        last_column_paths = [0]*m
        column_index = 0
        while column_index < m and (obstacleGrid[0][column_index] == 0):
            last_column_paths[column_index] = 1
            column_index += 1
        # if n == 1:
        #     return last_column_paths
        for i in range(1,n):
            for j in range(1,m):
                current_paths = 0
                if obstacleGrid[i][j] == 0:
                    current_paths = last_row_paths[i] + last_column_paths[j]
                last_row_paths[i] = current_paths
                last_column_paths[j] = current_paths

        # taking min for edge cases when (row is 1) or (column is 1)

        return min(last_row_paths[n-1],last_column_paths[m-1])