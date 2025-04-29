from sys import stdin
def input(): return stdin.readline().strip()

king_start = list(input())
king_desitination = list(input())

index_map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
move_map = {(0,1):'D',(-1,0):'R',(0,-1):'U',(1,0):'L',
            (-1,1):'RD',(-1,-1):'RU',(1,1):'LD',(1,-1):'LU'}
MOVES = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

ksx,ksy = (index_map[king_start[0]],int(king_start[1]))
kdx,kdy = (index_map[king_desitination[0]],int(king_desitination[1]))

seen = [[0 for i in range(9)] for _ in range(9)]
parent = [[(-1,-1) for i in range(9)] for _ in range(9)]

seen[ksx][ksy] = 1
current_level = [(ksx,ksy)]

while current_level:
  next_level = []

  for cx,cy in current_level:

    if (cx,cy) == (kdx,kdy):
      break

    for dx,dy in MOVES:
      x,y = cx+dx,cy+dy
      in_grid = 0 < x < 9 and 0 < y < 9

      if in_grid:
        if not seen[x][y]:
          next_level.append((x,y))
          seen[x][y] = 1
          parent[x][y] = (cx,cy)

  current_level = next_level[:]


x,y = kdx,kdy

path = [(x,y)]
while parent[x][y] != (-1,-1):
  (x,y) = parent[x][y]
  path.append((x,y))


u = len(path)
print(len(path)-1)

for i in range(u-2,-1,-1):
  curr = path[i]
  prev = path[i+1]
  dx = prev[0]-curr[0]
  dy = prev[1]-curr[1]

  print(move_map[(dx,dy)])


# #     0         1        2        3      4        5      6       7      8   
# 0 [[(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)], 
# 1 [(-1, -1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (-1, -1)], 
# 2 [(-1, -1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 8)], 
# 3 [(-1, -1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 8)], 
# 4 [(-1, -1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 8)], 
# 5 [(-1, -1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 8)], 
# 6 [(-1, -1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 8)], 
# 7 [(-1, -1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 8)], 
# 8[(-1, -1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 8)]]
