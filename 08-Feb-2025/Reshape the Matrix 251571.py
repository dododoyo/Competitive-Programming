# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])

        if n*m != r*c:
            return mat

        solution = [[0 for i in range(c)] for _ in range(r)]

        old_row = 0
        old_col = 0

        for x in range(r):
            for y in range(c):
                if old_col == m:
                    old_row += 1
                    old_col = 0

                solution[x][y] = mat[old_row][old_col]
                old_col += 1

        return solution
