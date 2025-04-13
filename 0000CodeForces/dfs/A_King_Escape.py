from sys import stdin
def input(): return stdin.readline().strip()

n = [int(i) for i in input().split()][0]

alice_queen = [int(i)-1 for i in input().split()]
bob_king = [int(i)-1 for i in input().split()]
win_position = [int(i)-1 for i in input().split()]

seen = [[0 for _ in range(n)] for i in range(n)]
KING_MOVES = [(0,0),(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

def dfs(r,c):

  if [r,c] == win_position:
    return True
  
  stack = [[r,c]]

  while stack:
    r,c = stack.pop()

    seen[r][c] = 1

    for dx,dy in KING_MOVES:
      x,y = dx+r,dy+c

      in_bound = -1 < x < n and -1 < y < n

      if not in_bound:
        continue

      if [x,y] == win_position:
        return True

      if seen[x][y] or (x == alice_queen[0]) or (y == alice_queen[1]) or (x-y == alice_queen[0]-alice_queen[1]) or (x+y == alice_queen[0]+alice_queen[1]):
        continue

      # if seen[x][y]:
      #   continue

      # # same_row 
      # if (x == alice_queen[0]):
      #   continue

      # # same_column 
      # if (y == alice_queen[1]):
      #   continue

      # # same_main_diagonal 
      # if (x-y == alice_queen[0]-alice_queen[1]):
      #   continue

      # # same_secondary_diagonal 
      # if (x+y == alice_queen[0]+alice_queen[1]):
      #   continue

      stack.append([x,y])
    
  return False 

print("YES" if dfs(bob_king[0],bob_king[1]) else "NO")
