# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from collections import deque
class Solution:
    
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid),len(grid[0])

        def isValid(row,col):
            return 0 <= row < n and 0 <= col < m

        memo = [[-1 for i in range(m)] for _ in range(n)]
        MOVES = [[-1,0],[0,-1],[1,0],[0,1]]
        memo[0][0] = grid[0][0]

        que = deque([[0,0,0]]) # (row,col,obstacle_count)

        while que:
            current_node = que.popleft()
            x,y,obstacles = current_node
            for dx,dy in MOVES:
                nx,ny = dx+x,dy+y
                if isValid(nx,ny) and memo[nx][ny] == -1:
                    # obstacle
                    if grid[nx][ny]:
                        memo[nx][ny] = obstacles + 1
                        que.append([nx,ny,memo[nx][ny]])

                    # empty cell
                    else:
                        memo[nx][ny] = obstacles
                        que.appendleft([nx,ny,memo[nx][ny]])

        return memo[n-1][m-1]
