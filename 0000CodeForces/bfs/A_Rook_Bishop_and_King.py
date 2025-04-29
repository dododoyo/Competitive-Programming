def bfs(start,end,MOVES):
  visited = [[0 for i in range(8)] for _ in range(8)]
  visited[start[0]][start[1]] = 1

  current_level = [start]
  level = 0
  while current_level:
    next_level = []

    for node in current_level:
        if node == end:
          return level
        cx,cy = node
        
        for x,y in generate_possible_moves(cx,cy,MOVES):

          # in grid 
          if -1 < x < 8 and -1 < y < 8:
            if not visited[x][y]:
                visited[x][y] = 1
                next_level.append((x,y))
    level += 1
    current_level = next_level[:]

  return 0


def generate_possible_moves(r,c,typ):
  moves = []
  cols = 8
  rows = 8

  if typ == "KING":
    for dx,dy in [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[0,1],[-1,0],[0,-1]]:
      x,y = dx+r,dy+c
      if -1 < r < 8 and -1 < c < 8:
        moves.append((x,y))

  elif typ == "BISHOP":
    # move as right up as you can
    x, y = r-1, c+1
    while x > -1 and y < cols:
      moves.append((x,y))
      x,y = x-1,y+1
  
    # move as right down as you can
    x,y = r+1,c+1
    while x < rows and y < cols:
      moves.append((x,y))
      x,y = x+1,y+1
  
    # move as left up as you can
    x,y = r-1,c-1
    while x > -1 and y > -1:
      moves.append((x,y))
      x, y = x-1, y-1
  
    x,y = r+1,c-1
    # move as left down as you can
    while x < rows and y > -1:
      moves.append((x,y))
      x, y = x+1, y-1
  
  elif typ == "ROOK":
    for i in range(r+1,rows):
      moves.append((i,c))
    for i in range(c+1,cols):
      moves.append((r,i))
    for i in range(0,r):
      moves.append((i,c))
    for i in range(0,c):
      moves.append((r,i))

  return moves 

r1,c1,r2,c2 = [int(i) -1 for i in input().split()]
start = (r1,c1)
end = (r2,c2)

king = bfs(start,end,'KING')
bishop = bfs(start,end,'BISHOP')
rook = bfs(start,end,'ROOK')

print(rook,bishop,king)