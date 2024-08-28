# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        mark_row = [0]*row
        mark_col = [0]*col

        # register the rows and columns to be marked
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    mark_row[r] = 1
                    mark_col[c] = 1


        # cell will be marked by either it's row or it's column
        for r in range(row):
            for c in range(col):
                if mark_row[r] or mark_col[c]:
                    matrix[r][c] = 0
                    
        # Time(n^2)   #Space (n)
        
        