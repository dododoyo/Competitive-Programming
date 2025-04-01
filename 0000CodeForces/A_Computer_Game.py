for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  grid = []
  for _ in range(2):
    grid.append(input())
  MOVES = [[1,0],[0,1],[1,1],[-1,1]]

  def dfs(i,j):
    if (i,j) == (1,n-1):
      return True
    
    for dx,dy in MOVES:
      x,y = dx+i,dy+j

      if -1 < x < 2 and -1 < y < n and grid[x][y] == "0":
        if dfs(x,y):
          return True

    return False
  
  print("YES" if dfs(0,0) else "NO")
