# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = [int(i) for i in input().split()][0]
graph = [[] for _ in range(n)]

for i in range(n-1):
  x = [int(i) for i in input().split()][0]
  graph[x-1].append(i+1)


for v in range(len(graph)):
    not_leaf = graph[v]
    leafs_count = 0
    for neighbors in graph[v]:
      if not graph[neighbors]:
        leafs_count += 1

    if not_leaf and leafs_count < 3:
        print('No')
        break
else:
    print('Yes')