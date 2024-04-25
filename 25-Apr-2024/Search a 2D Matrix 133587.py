# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        linear_matrix = []
        for row in matrix:linear_matrix.extend(row)

        low,high = 0,len(linear_matrix)-1
        while low <= high:
            middle = low + (high-low)//2
            if linear_matrix[middle] == target:
                return True
            elif linear_matrix[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        return False
        