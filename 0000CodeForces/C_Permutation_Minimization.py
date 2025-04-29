#########################################################################
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from heapq import heappop, heappush

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return [list(map(int, inp().split())) for _ in range(rows)]

# setrecursionlimit(10**6)
#########################################################################



for _ in range(ls()[0]):
  n = ls()[0]
  arr = ls()

  dq = deque([arr[0]])


  for i in range(1,n):
    if arr[i] < dq[0]:
      dq.appendleft(arr[i])
    else:
      dq.append(arr[i])

  print(*dq)