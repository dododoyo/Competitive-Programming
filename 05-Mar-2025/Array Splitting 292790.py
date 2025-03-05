# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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


n,k = ls()
arr = ls()

arr.reverse()
for i in range(1, n):
    arr[i] += arr[i - 1]

# print(arr)

solution = arr.pop()
arr.sort(reverse = True)
solution += sum(arr[:(k - 1)])

# print(arr[:k-1])
print(solution)