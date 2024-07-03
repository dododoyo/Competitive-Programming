# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from sys import stdin
def input(): return stdin.readline().strip()

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n+1)}
        self.rank = [1]*(n)
        self.max_node = {i: i for i in range(1, n+1)}
        self.min_node = {i: i for i in range(1, n+1)}
        self.node_count = {i: 1 for i in range(1, n+1)}

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
                p, c = parentX, parentY
            elif self.rank[parentX-1] < self.rank[parentY-1]:
                self.parent[parentX] = parentY
                p, c = parentY, parentX
            else:
                self.parent[parentX] = parentY
                p, c = parentY, parentX
                self.rank[parentY-1] += 1

            head = self.find(parentX)

            self.max_node[head] = max(self.max_node[parentX], self.max_node[parentY])
            self.min_node[head] = min(self.min_node[parentX], self.min_node[parentY])
            self.node_count[head] += self.node_count[c] 

    def getData(self, x):
        parentX = self.find(x)
        return [self.min_node[parentX], self.max_node[parentX], self.node_count[parentX]]


n, m = list(map(int, input().split()))
disjoint_set = UnionFind(n)

for _ in range(m):
    query = input().split()
    query_type = query[0]

    if query_type == "union":
        u = int(query[1])
        v = int(query[2])
        disjoint_set.union(u, v)

    elif query_type == "get":
        v = int(query[1])
        print(*disjoint_set.getData(v))
