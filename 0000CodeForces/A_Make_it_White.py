from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  n = ls()[0]
  s = inp()

  left,right = 0,n-1

  while left < right and s[left] == "W":
    left += 1

  while left < right and s[right] == "W":
    right -= 1

  if right == left and s[right] == "W":
    print(0)
  else:
    print(right-left + 1)