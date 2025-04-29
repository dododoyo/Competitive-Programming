from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  burles = ls()[0] # to be paid 
  x = burles // 3
  remainder = burles % 3

  if remainder == 0:
    print(x,x)
  elif remainder == 1:
    print(x+1,x)
  else:
    print(x,x + 1)