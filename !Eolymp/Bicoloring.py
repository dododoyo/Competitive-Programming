from collections import deque

def is_bicolorable(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    colors = [-1] * n
    
    # Use BFS to traverse the graph and assign colors to nodes
    queue = deque([0])
    colors[0] = 0
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                queue.append(v)
            elif colors[v] == colors[u]:
                return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    l = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(l)]
    
    if is_bicolorable(n, edges):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")