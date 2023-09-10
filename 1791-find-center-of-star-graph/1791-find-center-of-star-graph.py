class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degr = [0] * (n+1)
        for u, v in edges:
            degr[u] += 1
            degr[v] += 1
        for i in range(1, n+1):
            if degr[i] == n-1:
                return i