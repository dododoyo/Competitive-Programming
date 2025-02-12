# Problem: Sum - https://codeforces.com/contest/1742/problem/A

from sys import stdin
def i(): return stdin.readline().strip()
def ls(): return [int(i) for i in i().split()]
def mt(rows): return[list(map(int, i().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  a,b,c = ls()
  condition1 = a == (b+c)
  condition2 = b == (a+c)
  condition3 = c == (a+b)
  print("YES" if (condition1 or condition2 or condition3) else "NO")