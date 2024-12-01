from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

n = ls()[0]
original = input()
correct = input()

def count_min(x,y):
  x = int(x)
  y = int(y)

  if x > y:
    return min(x - y, 10 - x + y)
  else:
    return min(y - x, 10 - y + x)

solution = 0 
for i in range(n):
  solution += count_min(original[i],correct[i])
  
print(solution)