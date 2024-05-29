# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # terminal => all edges are indegree edges | no outgoing edges

        # safe => every path starting from that node ends at a terminal node
        n = len(graph)

        reversed_graph = [[] for _ in range(n)]
        indegree = [0]*n

        for node in range(n):
            for neighbor in graph[node]:
                reversed_graph[neighbor].append(node)
                indegree[node] += 1

        bfs_que = [node for node in range(n) if not indegree[node]]

        solution = []
        while bfs_que:
            next_que = []
            solution.extend(bfs_que)

            for node in bfs_que:
                for neighbor in reversed_graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        next_que.append(neighbor)

            bfs_que = next_que[:]
        return sorted(solution)
        