from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


# find minimum window size sum greater than or equal to k 

k = ls()[0]
flowers = ls()

flowers.sort(reverse=True)
months = 0
growth = 0 


for i in range(len(flowers)):
  if growth >= k:
    break 

  growth += flowers[i]
  months += 1



if growth >= k:
  print(months)
else:
  print(-1)
