# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1

        moves = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
        visited,n = {(0,0)}, len(grid)
        current_level,level = [(0,0)],1
   
        def inBound(r,c):
            return 0 <= r < n and 0 <= c < n

        while current_level:
            next_level = []

            for node in current_level:
                r,c = node
                for dx,dy in moves:
                    x, y = r+dx, c +dy
                    
                    if (x,y) == (n-1,n-1) and grid[x][y] == 0:
                        return level+1

                    if inBound(x,y) and grid[x][y] == 0 and (x,y) not in visited:
                        next_level.append((x,y))
                        visited.add((x,y))

            current_level = next_level
            level += 1
        return -1 