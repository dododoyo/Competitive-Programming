# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

num_nodes, num_edges = map(int, input().split())
start_node, end_node = map(int, input().split())

graph = defaultdict(list)
for _ in range(num_edges):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

queue = deque([start_node])
visited = {start_node: None}

while queue:
    current_node = queue.popleft()
    if current_node == end_node:
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = visited[current_node]
        path.reverse()
        print(len(path) - 1)
        print(*path)
        exit()
    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            visited[neighbor] = current_node
            queue.append(neighbor)
print(-1)
