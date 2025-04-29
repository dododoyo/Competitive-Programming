#https://codeforces.com/problemset/problem/1699/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

for _ in range(ls()[0]):
  n,m = ls()
  for i in range(n):
    for j in range(m):
      print((i^j^(i//2)^(j//2))%2, end=' ')
    print()