from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


for _ in range(ls()[0]):
  n = ls()[0]
  a = ls()
  b = ls()

  sums = set()
  for x in a:
    for y in b:
      sums.add(x+y)

  print("YES" if len(sums) > 2 else "NO")
