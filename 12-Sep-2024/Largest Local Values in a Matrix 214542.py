# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, solution = len(grid), []

        for i in range(1, n - 1):
            curr_row = []
            for j in range(1, n - 1):
                maxx = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        maxx = max(maxx, grid[k][l])

                curr_row.append(maxx)
            solution.append(curr_row)

        return solution
        