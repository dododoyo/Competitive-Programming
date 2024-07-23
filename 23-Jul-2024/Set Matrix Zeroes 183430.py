# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        for r in range(n):
            for c in range(m):

                if matrix[r][c] == 0:
                    for dx in range(n):
                        if matrix[dx][c] != 0:
                            matrix[dx][c] = "x"

                    for dy in range(m):
                        if matrix[r][dy] != 0:
                            matrix[r][dy] = "x"

        for r in range(n):
            for c in range(m):
                if matrix[r][c]=='x':
                    matrix[r][c]=0
        
        