# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        seen = set()
        n,m = len(grid),len(grid[0])
        MOVES = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(row, col):
            current_level = [(row, col)]
            solution = grid[row][col]
            while current_level:
                next_level = []

                for current_row,current_column in current_level:
                    for dx,dy in MOVES:
                        r,c = current_row+dx,current_column+dy
                        if 0 <= r < n and 0 <= c < m and grid[r][c] and (r, c) not in seen and (r,c) != (row, col):
                            seen.add((r,c))
                            next_level.append((r,c))
                            solution += grid[r][c]
                current_level = next_level[:]

            return solution

        solution = 0
        for row in range(n):
            for col in range(m):
                if (row, col, grid[row][col]) not in seen and grid[row][col]:
                    seen.add((row, col))
                    solution = max(solution, bfs(row, col))
        
        return solution
