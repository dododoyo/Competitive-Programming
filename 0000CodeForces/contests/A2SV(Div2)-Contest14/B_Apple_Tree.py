#USE BFS INSTEAD + REMOVED FUNCTION CALL(if it helps)

t = int(input());
for _ in range(t):
    num_nodes = int(input())
    edges = [[]*(num_nodes+1) for _ in range(num_nodes+1)]
    for _ in range(num_nodes-1):
        node1, node2 = map(int,input().split())
        edges[node1].append(node2)
        edges[node2].append(node1)
    queue, node_apples = [(1,0,0)],{}
    while queue:
        node, distance, parent = queue.pop()
        if distance == 0:
            queue.append((node,1,parent))
            for child in edges[node]:
                if child != parent:
                    queue.append((child,0,node))
        else:
            node_apples[node] = 1 if edges[node] == [parent] else sum(node_apples[child] for child in edges[node] if child != parent)
                
    num_queries = int(input())
    for _ in range(num_queries):
        start1, start2 = map(int,input().split())
        print(node_apples[start1]*node_apples[start2])