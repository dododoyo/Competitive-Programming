# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if not rows or not cols:
            return 0

        parent = [-1] * (rows * cols)

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
                if grid[r][c] == "1":
                    current_cell = r * cols + c 
                    if r > 0 and grid[r - 1][c] == "1":
                        upper_cell = (r - 1) * cols + c
                        union(current_cell,upper_cell)
                    if c > 0 and grid[r][c - 1] == "1":
                        left_cell = r * cols + (c - 1)
                        union(current_cell,left_cell)

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and parent[r * cols + c] < 0:
                    num_islands += 1

        return num_islands