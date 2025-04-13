from sys import stdin
def input(): return stdin.readline().strip()

n = [int(i) for i in input().split()][0]
graph = [[] for _ in range(n)]

for _ in range(n):
    a, b, cost = [int(i)-1 for i in input().split()]
    graph[a].append((b, cost))
    graph[b].append((a, -cost))


visited = [False] * n
visited[0] = True

# print(graph)

def dfs(road,visited):
    curr_city,cst = road
    visited[curr_city] = True

    pos,neg = 0,0

    if cst < 0:
      neg += abs(cst)
    else:
      pos += cst
    
    for childRoad in graph[curr_city]:
        next_city = childRoad[0]
        if not visited[next_city]:
            child_pos,child_neg = dfs(childRoad,visited)
            pos += child_pos
            neg += child_neg

    return pos,neg

pos,neg = dfs(graph[0][0],visited)

if graph[0][1][1] < 0:
  pos += abs(graph[0][1][1])
else:
  neg += graph[0][1][1]

print(min(pos, neg))