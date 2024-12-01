from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

d1,d2,d3 = ls()
print(min(2*(d1+d2), 2*(d3+d2),2*(d1+d3),d1+d2+d3))