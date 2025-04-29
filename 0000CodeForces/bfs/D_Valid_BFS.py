n = int(input())
adj = [[] for _ in range(n+1)]


for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sequence = list(map(int, input().split()))

order = [-1]*(n+1)
for i in range(n):
    order[sequence[i]] = i

for i in range(1, n+1):
    adj[i].sort(key=lambda x: order[x])

visited = [False] * (n+1)

current_level = [1]
visited[1] = True

result = []

while current_level:
  next_level = []

  for node in current_level:
    result.append(node)

    for v in adj[node]:
        if not visited[v]:
            visited[v] = True
            next_level.append(v)

  current_level = next_level[:]

  
print("Yes" if result == sequence else "No")