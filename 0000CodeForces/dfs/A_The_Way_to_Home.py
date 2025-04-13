from sys import stdin
def input(): return stdin.readline().strip()

n,d = [int(i) for i in input().split()]
memo = [-1 for _ in range(n)]
axis = input()

if axis[-1] == "0":
  print(-1)
  exit()

def dfs(index):
  if memo[index] != -1:
    return memo[index] != float('inf'),memo[index]
  
  if index == n-1:
    return True,0
  
  min_child_moves = float('inf')

  for dx in range(1,d+1):
    next_index = index + dx

    valid = next_index < n 
    
    if valid:
      can_step = axis[next_index] == '1'
      if can_step:
        can,steps = dfs(next_index)

        if can:
          min_child_moves = min(steps,min_child_moves)
  
  if min_child_moves == float('inf'):
    memo[index] = float('inf')
    return False,float('inf')
  else:
    memo[index] = min_child_moves + 1
    return True,min_child_moves + 1


can_reach,steps = dfs(0)

if can_reach:
  print(steps)
else:
  print(-1)