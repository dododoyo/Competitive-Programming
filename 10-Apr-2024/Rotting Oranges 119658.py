# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves, m, n = [[0,1],[1,0],[0,-1],[-1,0]], len(grid), len(grid[0])
        final_grid = [[0]*n for i in range(m)]
        freshCount, bfsq = 0, deque()

        # generate new grid to track operations
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    final_grid[i][j] = 2
                    bfsq.append((i,j,0))
                elif grid[i][j] == 1:
                    freshCount += 1

        # tracks maximum number of levels we went
        solution = 0

        while bfsq:
            rotten = bfsq.popleft()
            r,c,t = rotten[0],rotten[1],rotten[2]
            solution = max(solution,t)

            for dx,dy in moves:
                x,y = dx+r,dy+c
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and final_grid[x][y] != 2:
                    bfsq.append((x,y,t+1))
                    final_grid[x][y] = 2

        for i in range(m):
            for j in range(n):
                # if there are any fresh orange that is not rottened 
                # return -1
                if grid[i][j] == 1 and final_grid[i][j] != 2:
                    return -1
        return solution