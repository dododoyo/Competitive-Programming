#########################################################################
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
import heapq

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return [list(map(int, inp().split())) for _ in range(rows)]

# setrecursionlimit(10**6)
#########################################################################


s = inp()
stack = [s[0]]

for i in range(1,len(s)):
  if stack and stack[-1] == s[i]:
    stack.pop()
  else:
    stack.append(s[i])

print("".join(stack))