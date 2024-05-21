t = int(input())
from collections import defaultdict, deque
for _ in range(t):
  mine = defaultdict(list)
  n, m = map(int, input().split())

  for i in range(m):
    u, v = map(int, input().split())
    mine[u].append(v)
    mine[v].append(u)

  queue = deque([1])
  visited = {1}
  f = False
  while queue:
    cur = queue.popleft()
    if cur == n:
      f = True
      break
      
    for node in mine[cur]:
      if node not in visited:
        visited.add(node)
        queue.append(node)

  if not f:
    print('NO')
  else: 
    print('YES')