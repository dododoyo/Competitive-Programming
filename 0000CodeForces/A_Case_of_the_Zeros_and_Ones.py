from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n = ls()[0]
s = inp()

stack = []
stack = [s[0]]

for i in range(1,n):
  if (not stack) or stack[-1] == s[i]:
    stack.append(s[i])
  else:
    stack.pop()

print(len(stack))