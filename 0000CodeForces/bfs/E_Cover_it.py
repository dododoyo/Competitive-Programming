from sys import stdin
def input(): return stdin.readline().strip()

for _ in range([int(i) for i in input().split()][0]):
  nodes,edges = [int(i) for i in input().split()]
  graph = [[] for _ in range(nodes)]

  for i in range(edges):
    u,v = [int(i)-1 for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)
    
  evens,odds = [],[]

  current_level = [0]
  height = 0
  seen = [0 for _ in range(nodes)]
  seen[0] = 1


  while current_level:
    next_level = []

    for node in current_level:
      if height%2 == 0:
        evens.append(node+1)
      else:
        odds.append(node+1)

      for nghbr in graph[node]:
        if not seen[nghbr]:
          seen[nghbr] = 1
          next_level.append(nghbr)

    current_level=next_level[:]
    height +=1

  if len(evens) <= len(odds):
    print(len(evens))
    print(*evens)
  else:
    print(len(odds))
    print(*odds)


"""
Proof why which ever level has the lesser number of nodes 
will have a node count less than or equal to (nodes//2)

let a = level with less number of nodes
let b = level with more number of nodes 

which means a <= b . . . . eqn-1
and we know a+b = n . . . . . eqn-2

add a to both sides of eqn-1

a+a <= b+a
2a <= b+a 
we know b+a == n

2a <= n 

which means a <= n/2

"""