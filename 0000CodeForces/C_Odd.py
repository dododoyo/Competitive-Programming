from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]
from collections import defaultdict


for _ in range(ls()[0]):
  n = ls()[0]
  arr = ls()
  changed = set()

  for num in arr:
    while num %2 == 0:
      changed.add(num)
      num //= 2

  print(len(changed))
