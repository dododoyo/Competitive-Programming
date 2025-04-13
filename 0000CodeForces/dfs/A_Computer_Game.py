from sys import stdin
def input(): return stdin.readline().strip()


for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  grid = []
  seen = [[0 for _ in range(n)] for i in range(2)]
  # MOVES = [[0,1],[1,0],[-1,0],[-1,1],[1,1],[1,-1],[-1,-1],[0,-1]]
  MOVES = [[0,1],[1,0],[-1,0],[-1,1],[1,1]]

  for _ in range(2):
    grid.append(input())

  def dfs(i,j):
    seen[i][j] = 1
    if (i,j) == (1,n-1):
      return grid[1][n-1] == '0'
    
    for dx,dy in MOVES:
      x,y = dx+i,dy+j
      in_bound = -1 < x < 2 and -1 < y < n
    
      if in_bound:
        if not seen[x][y]:
          if grid[x][y] == '0':
            if dfs(x,y):
              return True
        
    return False 
  
  print("YES" if dfs(0,0) else "NO")
  
