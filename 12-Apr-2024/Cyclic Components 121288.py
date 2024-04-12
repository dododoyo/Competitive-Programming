# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

nodes,edges = map(int,input().split())
graph = [[] for _ in range(nodes)]
for _ in range(edges):
  n1,n2 = map(lambda x: int(x)-1,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)


def is_cyclic(start):
    stack,flag = [start],True

    while stack:
        node = stack.pop()

        if not visited[node]:
          visited[node] = True
          if len(graph[node]) != 2:
              flag = False

          for child in graph[node]:
              if not visited[child]:
                  stack.append(child)
    return flag

visited,cycles = [False]*nodes,0
for node in range(nodes):
    if not visited[node] and is_cyclic(node):
        cycles += 1

print(cycles)