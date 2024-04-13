# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        solution = [[0]*n for _ in range(m)]

        def getNeighbours(node):
            neighbours = []
            moves = [(0,1),(1,0),(-1,0),(0,-1)]
            for dx,dy in moves:
                x,y = dx+node[0],dy+node[1]
                if 0 <= x < m and 0 <= y < n:
                    neighbours.append([x,y])
            return neighbours

        def bfs(current_level):
            flood_time, level,visited = [[0]*n for _ in range(m)],1,[[False]*n for _ in range(m)]
            for node in current_level:
                visited[node[0]][node[1]] = True
            
            while current_level:
                next_level = []
                for node in current_level:
                    neighbours = getNeighbours(node)
                    for nghbr in neighbours:
                        if not visited[nghbr[0]][nghbr[1]]:
                            flood_time[nghbr[0]][nghbr[1]] = level
                            visited[nghbr[0]][nghbr[1]] = True
                            next_level.append(nghbr)
                level += 1
                current_level = next_level
            return flood_time

        current_level = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    current_level.append([i,j])

        return bfs(current_level)