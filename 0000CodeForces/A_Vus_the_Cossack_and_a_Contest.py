from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


n,m,k = ls()

min_ = min(m,k)

if min_ < n:
  print("No")
else:
  print("Yes")