def dfs(node):
  visited[node] = 1
  for neighbor in graph[node]:
    if visited[neighbor] == 1:
      print("Impossible")
      exit()
    if visited[neighbor] == 0:
      dfs(neighbor)
  visited[node] = 2
  output_order.append(chr(node+ord("a")))



n = int(input())
first_name = input()
graph,visited = [set() for _ in range(26)],[0]*26

for _ in range(1, n):
  current_name,i = input(),0

  while i < min(len(current_name), len(first_name)) and (current_name[i] == first_name[i]):
    i += 1

  if (i < min(len(first_name), len(current_name))) and (current_name[i] != first_name[i]):
    graph[ord(first_name[i])-ord("a")].add(ord(current_name[i])-ord("a"))

  elif len(first_name) > len(current_name):
    print("Impossible")
    exit()
  first_name = current_name

output_order = []

for i in range(26):
  if visited[i] == 0:
    dfs(i)
    
output_order.reverse()

print("".join(output_order))