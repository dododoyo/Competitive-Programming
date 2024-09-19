# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
  def __init__(self, n):
    self.root = [i for i in range(n)]
    self.rank = [1]*n
  
  def find(self, x):
    if x == self.root[x]:
      return x
    return self.find(self.root[x])
  
  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    
    if rootX != rootY:
      if self.rank[rootX] > self.rank[rootY]:
        self.root[rootY] = rootX
        self.rank[rootX] += 1
      else:
        self.root[rootX] = rootY
        self.rank[rootY] += 1

class Solution:
  def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    uf = UnionFind(len(s))
    
    for parent, child in pairs:
      uf.union(parent, child)
    

    groups = defaultdict(list)
    for i in range(len(s)):
      groups[uf.find(i)].append(s[i])
    for key in groups.keys():
      groups[key].sort(reverse=True)
    res = []
    for i in range(len(s)):
      res.append(groups[uf.find(i)].pop())
    return "".join(res)