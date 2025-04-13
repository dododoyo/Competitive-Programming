from sys import stdin
from math import sqrt

def input(): return stdin.readline().strip()

animals = [int(i) for i in input().split()][0]
points = []
hasNegative = False 
hasPositive = False
max_y = 0

for _ in range(animals):
  x,y = [int(i) for i in input().split()]
  if y < 0:
    hasNegative = True
  if y > 0:
    hasPositive = True

  if hasPositive and hasNegative:
    print(-1)
    exit()

  abs_y = abs(y)
  points.append((x, abs_y))
  if abs_y > max_y:
      max_y = abs_y

  points.append([x,abs(y)])

def validCircle(radius):
  minX,maxX = -float('inf'),float('inf')

  for x,y in points:
    delta = 2*radius*y - y*y

    if delta < 0:
      return False 
    
    sqrt_delta = sqrt(delta)

    minX = max(minX,x-sqrt_delta)
    maxX = min(maxX,x+sqrt_delta)

    if minX > maxX:
      return False

  return True

low,high = max_y/2,10**14
diff = 10**-6

solution = high

for _ in range(150):
  mid1,mid2 = low + (high-low)/3, high - (high-low)/3

  if validCircle(mid1):
    solution = mid1
    high = mid1 - diff
  elif validCircle(mid2):
    solution = mid2
    high = mid2 - diff
  else:
    low = mid2 + diff

print(solution)