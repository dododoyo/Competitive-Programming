from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]



n1,n2,k1,k2 = ls()

if n1 > n2:
  print("First")
else:
  print("Second")