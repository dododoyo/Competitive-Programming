# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        solution = -1
        for i in range(len(edges)): 
            current = i
            path = []
            while edges[current] >= 0: 
                path.append(current)
                next = edges[current]
                edges[current] = -1 
                current = next
                
            if current in path:
                solution = max(solution, len(path)-path.index(current))
        return solution