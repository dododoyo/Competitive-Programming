from collections import defaultdict

def bishop_path(position):
  r,c = position
  moves = []
  x, y = r-1, c+1
  # right up
  while x > -1 and y < chess_size and chess_board[x][y] != "#":
    moves.append((x, y))
    x, y = x-1, y+1

  x, y = r+1, c+1
  # right down
  while x < chess_size and y < chess_size and chess_board[x][y] != "#":
    moves.append((x, y))
    x, y = x+1, y+1

  x, y = r-1, c-1
  # left up
  while x > -1 and y > -1 and chess_board[x][y] != "#":
    moves.append((x, y))
    x, y = x-1, y-1

  x, y = r+1, c-1
  # left up
  while x < chess_size and y > -1 and chess_board[x][y] != "#":
    moves.append((x, y))
    x, y = x+1, y-1
  return moves

bishop_graph = defaultdict(int)


chess_size = int(input())
# for i in range(8):
#   for j in range(8):
#     bishop_graph[(i, j)] = bishop_path(i, j, size, chess_size)

startX,startY = map(int,input().split())
targetX,targetY = map(int,input().split())
chess_board = [input() for _ in range(chess_size)]

current_level = [(startX-1,startY-1)]
can_get = -1
visited = set()
level = 0

if startX == targetX and startY == targetY:
  print(0)
  exit(0)

while current_level:
  next_level = []
  for node in current_level:
    visited.add(node)
    # print(node)
    if node == (targetX-1,targetY-1):
      can_get = level-1
      break
    # r,c = node
    paths = bishop_path(node)
    for path in paths:
      pr,pc = path
      if path not in visited:
        next_level.append(path)
  level += 1
  current_level = next_level

print(can_get)