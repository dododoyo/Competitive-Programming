# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int: 
        max_square = 0
        largest = matrix.copy()
        n = len(matrix)
        m = len(matrix[0])

        for row in range(n):
            for col in range(m):
                largest[row][col] = int(largest[row][col])

        for row in range(1, n):
            for col in range(1, m):
                
                if matrix[row][col] == 1:
                    left = matrix[row][col - 1]
                    top = matrix[row - 1][col]

                    top_left = matrix[row - 1][col - 1]

                    if left and top and top_left:
                        left_max = largest[row][col - 1]
                        top_max = largest[row - 1][col]
                        top_left_max = largest[row - 1][col - 1]

                        largest[row][col] = 1 + min(left_max, top_max, top_left_max)
        
        for row in range(n):
            for col in range(m):
                max_square = max(max_square, largest[row][col])

        return max_square ** 2