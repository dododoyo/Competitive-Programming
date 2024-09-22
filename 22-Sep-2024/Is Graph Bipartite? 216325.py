# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        def isBipartite(node):
                current_level = [node]
                colors[node] = True

                while current_level:
                    next_level = []

                    for node in current_level:
                        for neighbor in graph[node]:
                            if colors[neighbor] != -1:
                                if colors[neighbor] == colors[node]:
                                    return False
                            else:
                                colors[neighbor] = not colors[node]
                                next_level.append(neighbor)

                    current_level = next_level[:]
                return True
        
        for i in range(n):
            if colors[i] == -1 and (not isBipartite(i)):return False
        
        return True
