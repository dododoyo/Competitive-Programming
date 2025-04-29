from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]



for _ in range(ls()[0]):
  n,swaps = ls()
  a = sorted(ls())
  b = sorted(ls(),reverse=True)

  pointer1 = 0
  pointer2 = 0

  while (pointer1 < n) and (pointer2 < n) and (a[pointer1] < b[pointer2]) and swaps > 0:
    a[pointer1] = b[pointer2]
    pointer2 += 1
    pointer1 += 1
    swaps -= 1

  print(sum(a))