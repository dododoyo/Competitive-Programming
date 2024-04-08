# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

# A loop is an edge, which connects a node with itself.
# A cycle and a loop aren't the same .


import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    nodes = int(input())
    graph = [[] for i in range(nodes)]

    for _ in range(nodes-1):
        n1, n2 = map(lambda x: int(x)-1, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)


    def isBip(graph, n):
        colors = [0]*nodes

        def helper(color, node):
            if colors[node] != 0:
                return [colors[node] == color, colors]
            colors[node] = color
            for nghbr in graph[node]:
                nghbr_color = -color
                if not helper(nghbr_color, nghbr):
                    return [False, colors]
            return True, colors

        for node in range(n):
            if colors[node] == 0 and not helper(1, node):
                return [False, colors]
        return [True, colors]


    result = isBip(graph, nodes)[1]
    validity = [0]*nodes
    blues = sum([result[i] == 1 for i in range(nodes)])
    total = blues*(nodes-blues)

    print(total-nodes+1)

if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
