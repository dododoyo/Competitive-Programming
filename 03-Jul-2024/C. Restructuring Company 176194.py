# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

from sys import stdin
def input(): return stdin.readline().strip()

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n+1)}
        self.rank = [1]*(n)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX-1] > self.rank[parentY-1]:
                self.parent[parentY] = parentX
            elif self.rank[parentX-1] < self.rank[parentY-1]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentX] = parentY
                self.rank[parentY-1] += 1

    def isConnected(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        return parentX == parentY


n, q = map(int, input().split())
uf = UnionFind(n)
decision2 = {i: i+1 for i in range(1, n+1)}


for i in range(q):
    decision, x, y = map(int, input().split())

    if decision == 1:
        uf.union(x, y)
    elif decision == 2:
        new_department = decision2[x]
        while new_department <= y:
            uf.union(new_department, x)

            temp = decision2[new_department]
            decision2[new_department] = decision2[y]

            new_department = temp
    elif decision == 3:
        print("YES" if uf.find(x) == uf.find(y) else "NO")