from sys import stdin, setrecursionlimit
from collections import defaultdict, Counter

setrecursionlimit(10**6)

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]

def backtrack(node, parent, path, values, graph, result):
    path.append(values[node-1])
    is_leaf = True
    for neighbor in graph[node]:
        if neighbor != parent:
            is_leaf = False
            backtrack(neighbor, node, path, values, graph, result)
    if is_leaf:
        freq = Counter(path)
        for key, count in freq.items():
            if count > len(path) // 2:
                result[key] = 1
    path.pop()

t = ls()[0]
answers = []
for _ in range(t):
    vertices = ls()[0]
    values = ls()
    graph = [[] for __ in range(vertices+1)]

    for __ in range(vertices-1):
        u, v = ls()
        graph[u].append(v)
        graph[v].append(u)

    result = [0] * (vertices + 1)
    for i in range(1, vertices + 1):
        backtrack(i, -1, [], values, graph, result)

    res = []
    for i in range(1, vertices + 1):
        if result[values[i-1]] == 1:
            res.append('1')
        else:
            res.append('0')

    answers.append("".join(res))

print("\n".join(answers))