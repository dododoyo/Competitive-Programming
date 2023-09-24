class Solution:
    def find(self, parent: List[int], i: int) -> int:
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent: List[int], i: int, j: int) -> None:
        parent_i = self.find(parent, i)
        parent_j = self.find(parent, j)
        parent[parent_i] = parent_j

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    self.union(parent, i, j)
        return len(set([self.find(parent, i) for i in range(n)]))