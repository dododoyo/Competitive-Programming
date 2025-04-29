from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  n,k = ls()
  arr = ls()

  if k in arr:
    print("YES")
  else:
    print("NO")