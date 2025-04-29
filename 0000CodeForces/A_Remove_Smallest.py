from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  n = ls()[0]
  arr = ls()
  arr.sort()
  valid = "YES"

  for i in range(n-1):
    if (arr[i] < arr[i+1] - 1):
      valid = "NO"
      break
  
  print(valid)