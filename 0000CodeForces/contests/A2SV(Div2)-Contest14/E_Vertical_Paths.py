from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    parents = list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        if parents[i-1] != i:
            tree[parents[i-1]].append(i)
        else:
            root = i
    paths = 0
    queue = deque([root])
    while queue:
        path = []
        for _ in range(len(queue)):
            node = queue.popleft()
            path.append(node)
            for child in tree[node]:
                queue.append(child)
        paths += 1
    print(paths)