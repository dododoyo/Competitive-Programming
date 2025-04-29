from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd
from random import randint
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  x = randint(0,5439)
  shelves,bottles = ls()
  distinct_brands = defaultdict(int)

  for _ in range(bottles):
    brand,cost = ls()
    distinct_brands[brand^x] += cost

  brands_list = sorted(list(distinct_brands.values()),reverse=True)

  print(sum(brands_list[:min(shelves,len(distinct_brands))]))