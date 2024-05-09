from collections import defaultdict
import sys
import threading

def input(): 
  return sys.stdin.readline().strip()


def main():
    for _ in range(int(input())):
      n = int(input())
      parents = [int(num) for num in input().split()]
      node_color = input()

      graph, solution = defaultdict(list), 0
      for index, node in enumerate(parents):
        graph[node].append(index+2)

      def dfs(node):
        nonlocal solution
        children = len(graph[node])
        if not children:
          return 1 if node_color[node-1] == "W" else -1

        children_sum = 0
        for child in graph[node]:
          child_val = dfs(child)
          solution += (child_val == 0)
          children_sum += child_val

        return ((1 if node_color[node-1] == "W" else -1) + children_sum)

      whole_tree = dfs(1)
      solution += (whole_tree == 0)
      print(solution)



if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
