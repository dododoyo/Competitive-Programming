# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        solution = [set() for i in range(n)]
      
        indegrees = [0]*n
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            indegrees[end] += 1

        current_level = []
        for i in range(n):
            if indegrees[i] ==  0:
                current_level.append(i)
                
        while current_level:
            next_level = []
            for node in current_level:
                for neighbor in graph[node]:
                    for x in solution[node]:
                        solution[neighbor].add(x)

                    solution[neighbor].add(node)
                    indegrees[neighbor] -= 1

                    if indegrees[neighbor] == 0:
                        next_level.append(neighbor)

            current_level = next_level[:]

        return [sorted(list(i)) for i in solution]
                
            
            





