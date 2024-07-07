# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        OFFSET = ord("a")
        indegree = [0] * n
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1

        counts = [[0]*26 for _ in range(n)]

        for i in range(n):
            counts[i][ord(colors[i]) - OFFSET] += 1

        max_count = 0
        nodes_count = 0
        current_level = [i for i in range(n) if indegree[i] == 0]

        while current_level:
            next_level = []
            nodes_count += len(current_level)

            for node in current_level:
                for neighbor in graph[node]:
                    for i in range(26):
                        x = (ord(colors[neighbor]) - OFFSET) == i
                        counts[neighbor][i] = max(counts[neighbor][i],counts[node][i] + x)

                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        next_level.append(neighbor)
                        
                max_count = max(max_count,max(counts[node]))

            current_level = next_level[:]
        return max_count if nodes_count == n else -1