# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        edges = {0: defaultdict(list), 1: defaultdict(list)}
        
        for src,dest in redEdges:
            edges[0][src].append(dest)
        
        for src,dest in blueEdges:
            edges[1][src].append(dest)
            
            
        queue,path1, path2 = [(0,1,0),(0,0,0)], [float("inf")]*n, [float("inf")]*n
        
        path1[0], path2[0] = 0, 0
        while queue:
            node, direction, distance = queue.pop(0)
            for nghbr in edges[direction][node]:
                if direction and path2[nghbr] > distance + 1:
                    path2[nghbr] = 1 + distance
                    queue.append((nghbr, 1 - direction, 1 + distance))
                elif not direction and path1[nghbr] > distance + 1:
                    path1[nghbr] = 1 + distance
                    queue.append((nghbr, 1 - direction, 1 + distance))
                    
        for i in range(n):
            path1[i] = min(path1[i], path2[i])
            if path1[i] == float("inf"):
                path1[i] = -1
        return path1