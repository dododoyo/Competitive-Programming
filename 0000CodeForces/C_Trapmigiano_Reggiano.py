from collections import defaultdict,deque
t = [int(i) for i in input().split()][0]

for _ in range(t):
  n,start,end = [int(i) for i in input().split()]
  graph = defaultdict(list)

  for j in range(n-1):
    u,v = [int(i) for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)

  path = []
  not_seen = [1]*(n+1)

  q = deque([end])

  while q:
    for i in range(len(q)):
      node = q.popleft()
      path.append(node)
      not_seen[node] = 0

      for neighbor in graph[node]:
        if not_seen[neighbor]:
          q.append(neighbor)

  print(*reversed(path))