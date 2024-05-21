n, m = map(int, input().split())
from collections import defaultdict, deque
mine = defaultdict(list)
indegree = defaultdict(int)
visited = set()
for _ in range(m):
  c1, c2 = input().split()
  visited.add(c1)
  visited.add(c2)
  mine[c1].append(c2)
  indegree[c2] += 1

queue = deque([])
ans = []

for node in visited:
  if indegree[node] > 1:
    print('IMPOSSIBLE')
    exit()
  if indegree[node] == 0:
    queue.append(node)
    ans.append(node)
    visited.add(node)

visited=set()
while queue:
  cur = queue.popleft()
  for node in mine[cur]:
      if node in visited:
        print('IMPOSSIBLE')
        exit()
      ans.append(node)
      visited.add(node)
      queue.append(node)


print(*ans)