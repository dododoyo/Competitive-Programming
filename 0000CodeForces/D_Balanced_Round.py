from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


# find the longest valid subarray

for _ in range(ls()[0]):
  n,k = ls()
  arr = sorted(ls())

  left, valid = 0, 1

  for right in range(1, n):
    if arr[right]-arr[right-1] > k:
      left = right

    valid = max(valid, right-left+1)

  print(n - (valid))