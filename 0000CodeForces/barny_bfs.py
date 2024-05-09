from collections import defaultdict
GRAPH = defaultdict(list)


def bfs(node):
    level = [node]
    visited = {node}
    while level:
        next_level = []
        for node in level:
            for adj in GRAPH[node]:
                if adj not in visited:
                    next_level.append(adj)
        level = next_level