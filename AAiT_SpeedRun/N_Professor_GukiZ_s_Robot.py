from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

x1,y1 = ls()
x2,y2 = ls()

dx,dy = abs(x1-x2),abs(y1-y2)

# go as much as you can diagonally
moves = min(dy,dx) + abs(dy-dx)

print(moves)