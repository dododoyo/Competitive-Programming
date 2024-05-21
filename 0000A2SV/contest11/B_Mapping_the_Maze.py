n,e = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(e):
  n1,n2 = map(lambda x: int(x)-1,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

def isBus(graph):
  graph.sort(key=lambda x:len(x))
  n = len(graph)
  for i in range(2,n):
    if len(graph[i]) != 2:
      return False
  return len(graph[0]) == 1 and len(graph[1]) == 1

def isRing(graph):
  return all([len(edges) == 2 for edges in graph])


def isStar(graph):
  graph.sort(key=lambda x:len(x))
  for i in range(n-1):
    if len(graph[i]) != 1:
      return False

  return len(graph[-1]) == n -1

topology = "unknown"
if isBus(graph):
  topology = "bus"
elif isRing(graph):
  topology = "ring"
elif isStar(graph):
  topology = "star"

print(f"{topology} topology")