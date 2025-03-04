# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n = ls()[0]
stone_costs = ls()
sorted_costs = sorted(stone_costs)

normal_prefixs = [0]*(n+1)
sorted_prefixs = [0]*(n+1)

for i in range(n):
  normal_prefixs[i+1] = normal_prefixs[i] + stone_costs[i]
  sorted_prefixs[i+1] = sorted_prefixs[i] + sorted_costs[i]

queries = ls()[0]
# print(normal_prefixs)
for _ in range(queries):
  typ,left,right = ls()
  if typ == 1:
    print(normal_prefixs[right] - normal_prefixs[left-1])
  else:
    print(sorted_prefixs[right] - sorted_prefixs[left-1])

 