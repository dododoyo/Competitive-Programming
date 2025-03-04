# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  n = ls()[0]
  rs = ls()
  m = ls()[0]
  bs = ls()

  red_solution = 0
  red_running_sum = 0

  for i in range(n):
    red_running_sum += rs[i]
    red_solution = max(red_solution,red_running_sum)

  blue_runnning_sum = 0
  blue_solution = 0
  
  for i in range(m):
    blue_runnning_sum += bs[i]
    blue_solution = max(blue_solution,blue_runnning_sum)

  print(blue_solution + red_solution)