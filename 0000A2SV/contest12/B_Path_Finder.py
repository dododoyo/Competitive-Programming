n = int(input())
graph = [[] for _ in range(n)]
weights = {}

# find the max distance starting from the bottom to up

for _ in range(n-1):
  n1,n2,w = map(int,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)
  if n1 < n2:
    weights[(n1,n2)] = w
  else:
    weights[(n2,n1)] = w

visited = set()

def dfs(node,parent):
  visited.add(node)

  if len(graph[node]) == 1:

    if parent < node:
      return weights[(parent,node)]
    else:
      return weights[(node,parent)]
  max_path = 0
  for child in graph[node]:
    if child not in visited:
      child_path = dfs(child,node)
      max_path = max(child_path,max_path)

  if parent < node:
    return max_path + weights[(parent,node)]
  else:
    return max_path + weights[(node,parent)]
  


root_childs = graph[0]
max_path = 0
visited.add(0)
for child in root_childs:
  child_path = dfs(child,0)
  max_path = max(max_path,child_path)
print(max_path)

