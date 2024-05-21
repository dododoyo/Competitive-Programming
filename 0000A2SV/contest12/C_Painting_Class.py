nodes = int(input())
edges = [int(num)-1 for num in input().split()]
colors = [int(num) for num in input().split()]

graph = [[] for _ in range(nodes)]

for i in range(1,nodes):
  graph[i].append(edges[i-1])
  graph[edges[i-1]].append(i)

visited,moves = set(),1
current_level = [(0,colors[0])]

while current_level:
  next_level = []
  for node,parent_color in current_level:
    visited.add(node)
    for child in graph[node]:
      if child not in visited:
        if colors[child] == colors[node]:
          next_level.append((child,colors[child]))
        else:
          next_level.append((child,parent_color))
          moves += 1
  current_level = next_level

print(moves)