# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:

    def findCircleNum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        parent = [-1] * (rows)

        def find(i):
            if parent[i] < 0:
                return i 

            parent[i] = find(parent[i])

            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return 

            if parent[root_i] < parent[root_j]:
                parent[root_i] += parent[root_j]
                parent[root_j] = root_i
            else:
                parent[root_j] += parent[root_i]
                parent[root_i] = root_j


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    union(r,c)

        num_islands = sum([parent[i] < 0 for i in range(rows)])

        return num_islands