# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        solution = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(solution, matrix[i][j])

        for i in range(k - 1):heappop(solution)

        return solution[0]