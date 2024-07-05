# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # original safe nodes don't have an indegree of 0 
        # So we need to reverse the edges and get all the nodes 
        # that can reach to the terminal nodes
        n = len(graph)

        # REVERSE THE GRAPH   
        reversed_graph = [[] for _ in range(n)]
        for node in range(n):
            for neighbors in graph[node]:
                reversed_graph[neighbors].append(node)

        # FIND SAFE STATES WITH TOPO-SORT
        indegrees = [0]*n
        for node in range(n):
            for neighbour in reversed_graph[node]:
                indegrees[neighbour] += 1
        
        current_level = [node for node in range(n) if indegrees[node] == 0]
        safe_states = []

        while current_level:
            next_level = []
            safe_states.extend(current_level)

            for node in current_level:
                for neighbour in reversed_graph[node]:
                    indegrees[neighbour] -= 1

                    if indegrees[neighbour] == 0:
                        next_level.append(neighbour)

            current_level = next_level[:]

        return sorted(safe_states)
    