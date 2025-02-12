# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

def solve(s):
  target = "codeforces"
  diff = 0
  for i in range(len(s)):
    diff += int(target[i] != s[i])

  return diff
  
t = ls()[0]
for _ in range(t):
  s = inp()
  print(solve(s))
  