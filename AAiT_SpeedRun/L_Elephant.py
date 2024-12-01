from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

x = ls()[0]
moves = 0

while x:
  if x > 4:
    x -= 5
  elif x > 3:
    x -= 4
  elif x > 2:
    x -= 3
  elif x > 1:
    x -= 2
  else:
    x -= 1
  moves += 1

print(moves)