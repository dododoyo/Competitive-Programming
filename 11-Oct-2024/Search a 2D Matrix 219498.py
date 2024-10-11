# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row first
        solution_row = -1
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                solution_row = i
                break
        if solution_row == -1:
            return False

        low,high = 0,m-1

        while low <= high:
            mid = low + (high-low)//2
            current_cell = matrix[solution_row][mid]

            if current_cell > target:
                high = mid - 1 
            elif current_cell < target:
                low = mid + 1
            else:
                return True
            