rows,columns = map(int,input().split())
grid = [list(input()) for _ in range(rows)]
MOD = 1e9 + 7

# . is empty, # is a wall
solution = [[0 for _ in range(columns)] for _ in range(rows)]

row = 0
while row < rows and grid[row][0] == ".":
  solution[row][0] = 1
  row += 1

column = 0
while column < columns and grid[0][column] == ".":
  solution[0][column] = 1
  column += 1

for row in range(1,rows):
  for column in range(1,columns):
    if grid[row][column] == ".":
      solution[row][column] = (solution[row-1][column] + solution[row][column-1])%MOD

print(int(solution[rows-1][columns-1]))