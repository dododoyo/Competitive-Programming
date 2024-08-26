# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        solution = set(range(n))      
        for i, j in edges:
            if j in solution:
                solution.remove(j)
                
        return list(solution)