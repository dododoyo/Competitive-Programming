from sys import stdin
def input(): return stdin.readline().strip()

nodes,edges = [int(i) for i in input().split()]

graph = [[] for _ in range(nodes)]

for _ in range(edges):
  u,v = [int(i)-1 for i in input().split()]
  graph[u].append(v)
  graph[v].append(u)

def is_cycle():
  for i in range(nodes):
    if len(graph[i]) != 2:
      return False
    
  return True

def is_bus():
  ones = 0
  twos = 0

  for i in range(nodes):
    ones += len(graph[i]) == 1
    twos += len(graph[i]) == 2

  return ones == 2 and twos == nodes - 2

def is_star():
  ones = 0
  center = 0

  for i in range(nodes):
    ones += len(graph[i]) == 1
    center += len(graph[i]) == nodes - 1

  return ones == nodes - 1  and center == 1

if is_cycle():
  print('ring topology')
elif is_bus():
  print('bus topology')
elif is_star():
  print('star topology')
else:
  print('unknown topology')