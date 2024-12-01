from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

red,blue = ls()
fashion,not_fashion = 0,0
if red > blue:
  not_fashion = red - blue
  fashion = blue
else:
  not_fashion = blue - red
  fashion = red

print(fashion,not_fashion//2)


