from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


luke_width,press,v1,v2 = ls()
print((press-luke_width)/(v1+v2))