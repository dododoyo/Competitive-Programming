from collections import defaultdict

def rook_path(r,c,rows,cols):
  moves = []
  for i in range(r+1,rows):
    moves.append((i,c))
  for i in range(c+1,cols):
    moves.append((r,i))
  for i in range(0,r):
    moves.append((i,c))
  for i in range(0,c):
    moves.append((r,i))
  return moves 

def king_path(r,c,rows,cols):
  moves = []
  for dx,dy in [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[0,1],[-1,0],[0,-1]]:
    x,y = dx+r,dy+c

    if 0 <= x < rows and 0 <= y < cols:
      moves.append((x,y))
  return moves

def bishop_path(r,c,rows,cols):
  moves =[]
  x, y = r-1, c+1
  # right up
  while x > -1 and y < cols:
    moves.append((x,y))
    x,y = x-1,y+1

  x,y = r+1,c+1
  # right down
  while x < rows and y < cols:
    moves.append((x,y))
    x,y = x+1,y+1

  x,y = r-1,c-1
  # left up
  while x > -1 and y > -1:
    moves.append((x,y))
    x, y = x-1, y-1

  x,y = r+1,c-1
  # left down
  while x < rows and y > -1:
    moves.append((x,y))
    x, y = x+1, y-1
  return moves


bishop_graph = defaultdict(list)
king_graph = defaultdict(list)
rook_graph = defaultdict(list)

for i in range(8):
  for j in range(8):
    bishop_graph[(i,j)] = bishop_path(i,j,8,8)
    king_graph[(i,j)] = king_path(i,j,8,8)
    rook_graph[(i,j)] = rook_path(i,j,8,8)


def bfs(start,end,graph):
  visited = {start}
  current_level = [start]
  level = 0
  while current_level:
    next_level = []

    for node in current_level:
        if node == end:
          return level
        # print(node)
        paths = graph[node]
        for neighbour in paths:

          if neighbour not in visited:
            visited.add(node)
            next_level.append(neighbour)
    level += 1
    current_level = next_level
  return 0

r1,c1,r2,c2 = map(int,input().split())
start,end = (r1-1,c1-1),(r2-1,c2-1)
king = bfs(start,end,king_graph)
bishop = bfs(start,end,bishop_graph)
rook = bfs(start,end,rook_graph)

print(rook,bishop,king)
