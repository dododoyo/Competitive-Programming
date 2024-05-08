# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
        self.components = size

    def find(self, x):

        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            self.components -= 1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    uf.union(i,j)
        return uf.components