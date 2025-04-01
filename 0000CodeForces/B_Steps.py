from sys import stdin
def input(): return stdin.readline().strip()

yard_row,yard_col = [int(i) for i in input().split()]
start_row,start_col = [int(i) for i in input().split()]

k = [int(i) for i in input().split()][0]
vectors = []

for _ in range(k):
  vectors.append([int(i) for i in input().split()])

def in_bound(x,y):
  return -1 < x < yard_row and -1 < y < yard_col

def can_move(x):
  total_steps = 0
  curr_row,curr_col = start_row,start_col

  for i in range(k):
      dx, dy = vectors[i]

      x_moves = float('inf')
      y_moves = float('inf')

      if dx > 0:
          x_moves = (yard_row - curr_row) // dx
      elif dx < 0:
          x_moves = (curr_row - 1) // -dx

      if dy > 0:
          y_moves = (yard_col - curr_col) // dy
      elif dy < 0:
          y_moves = (curr_col - 1) // -dy
    

      steps = min(x_moves, y_moves)

      curr_row += steps * dx
      curr_col += steps * dy

      total_steps += steps

    # while in_bound(curr_row+dx,curr_col+dy):
    #   moves += 1
    #   curr_row = curr_row + dx 
    #   curr_col = curr_col + dy

  return total_steps >= x

left,right = 0,10**13
solution = 0

# given grid and the moves you can make 
# what is the maximum moves you can make 
# such that you stay in the grid 

while left <= right:
  middle = left + (right-left)//2
  if can_move(middle):
    solution = middle
    left = middle + 1
  else:
    right = middle - 1

print(solution)