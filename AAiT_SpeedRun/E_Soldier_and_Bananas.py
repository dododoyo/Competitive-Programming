from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


k,n,w = ls()
total = (((1+w)*w)//2)*k

if total > n:
  print(total-n)
else:
  print(0)