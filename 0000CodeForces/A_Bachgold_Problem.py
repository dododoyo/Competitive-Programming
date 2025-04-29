from sys import stdin
from collections import  defaultdict, Counter, deque
from bisect import  bisect_left,bisect_right
from math import ceil, sqrt, gcd

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n = ls()[0]

print(n//2)
print(" ".join(["2" for _ in range(n//2 - 1)]),2+n%2)