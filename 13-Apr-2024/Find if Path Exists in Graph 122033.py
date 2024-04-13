# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False]*n
        graph = [[] for i in range(n)]

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        current_level = [source]
        visited[source] = True

        while current_level:
            next_level = []
            for node in current_level:
                if node == destination:
                    return True
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        next_level.append(neighbour)
                        visited[neighbour] = True

            current_level = next_level

        return False