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

  odd_defect = 0
  even_defect = 0

  for i in range(n):
    odd_defect += (i%2) and (arr[i]%2 == 0)
    even_defect += (i%2 == 0) and (arr[i]%2 != 0)

  
  if even_defect == odd_defect:
    print(even_defect)
  else:
    print(-1)