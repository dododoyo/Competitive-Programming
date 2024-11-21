# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

from collections import deque
class Solution:
    def findFirstNode(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i,j)

    def isValid(self,x,y,n,m):
        return 0 <= x < n and 0 <= y < m
                

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # register the first island 
        first_node = self.findFirstNode(grid)


        # register the first island with dfs/bfs
        stack = [first_node]
        MOVES = [[-1,0],[1,0],[0,1],[0,-1]]
        seen = set(stack)

        while stack:
            node = stack.pop()
            seen.add(node)  
            for dx,dy in MOVES:
                x,y = dx+node[0], dy+node[1]
                if self.isValid(x,y,n,m) and ((x,y) not in seen) and grid[x][y]:
                        stack.append((x,y))  
                        seen.add((x,y))

        NEIGHBOURS = [(0,1),(0,-1),(1,0),(-1,0)]

        # # do multisource bfs to find the shortest path
        # # to the second island 
        solution = 0
        que = deque(seen)
        
        while que:
            q = len(que)
            for i in range(q):
                node = que.popleft()
                for dx,dy in NEIGHBOURS:
                    x,y = dx+node[0], dy+node[1]
                    if 0 <= x < n and 0 <= y < m and ((x,y) not in seen):
                        if grid[x][y] == 1:
                            return solution

                        que.append((x,y))
                        seen.add((x,y))

            solution += 1
        