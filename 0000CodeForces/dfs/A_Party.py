import sys, threading
from sys import stdin
def input(): return stdin.readline().strip()

def main():

  employees = [int(i) for i in input().split()][0]
  graph = [[] for _ in range(employees)]
  is_boss = [0 for _ in range(employees)]


  for i in range(employees):
    boss = [int(i)-1 for i in input().split()][0]
    if boss != -2:
      graph[boss].append(i)
    else:
      is_boss[i] = 1


  # get max level 
  def get_level(node):
    max_child_level = 0

    for nghbr in graph[node]:
      max_child_level = max(max_child_level,get_level(nghbr))

    return max_child_level + 1

  max_level = 1
  for node in range(employees):
    if is_boss[node]:
      max_level = max(max_level,get_level(node))


  print(max_level)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()