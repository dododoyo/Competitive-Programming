# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:            
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]

        if n == 2 and len(edges) == 1: 
            return edges[0]

        graph = defaultdict(list)
        indegree = defaultdict(int)
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)

            indegree[k] += 1
            indegree[v] += 1

        q = deque()
        for node in graph:
            if indegree[node] == 1:q.append(node)

        visited = set()

        while q:
            solution = []
            layerSize = len(q)
            for i in range(layerSize):
                node = q.popleft()
                visited.add(node)
                solution.append(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        indegree[neighbor] -= 1 
                        if indegree[neighbor] == 1:
                            q.append(neighbor)
        return solution