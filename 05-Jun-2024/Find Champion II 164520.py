# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        m = len(edges)
        indegree = [0] * n

        for i in range(m):
            indegree[edges[i][1]] += 1

        solution = [i for i in range(n) if indegree[i] == 0]
        # for i in range(n):
        #     if indegree[i] == 0:
        #         solution.append(i)

        if len(solution) > 1:
            return -1

        return solution[0]