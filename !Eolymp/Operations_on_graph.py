n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]

for i in range(k):
    op = input().split()
    if op[0] == '1':
        u, v = map(int, op[1:])
        graph[u].append(v)
        graph[v].append(u)
    else:
        u = int(op[1])
        print(*graph[u] if graph[u] else [])