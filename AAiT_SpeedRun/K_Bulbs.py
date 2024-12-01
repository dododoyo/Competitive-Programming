from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

buttons,bulbs = ls()
bulbs_connected = set()

for _ in range(buttons):
  button_bulbs = ls()
  bulbs_connected = bulbs_connected.union(set(button_bulbs[1:]))

solution = list(bulbs_connected) == [i for i in range(1,bulbs+1)]
if solution:
  print("YES")
else:
  print("NO")


