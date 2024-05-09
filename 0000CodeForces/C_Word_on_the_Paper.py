def find_starting_point(matrix):
  for i in range(8):
    for j in range(8):
      if matrix[i][j] != ".":
        return [i,j]
      

def get_word(matrix,row,column):
  solution = []
  while row < 8 and matrix[row][column] != ".":
    solution.append(matrix[row][column])
    row += 1
  return "".join(solution)

for _ in range(int(input())):
  matrix = [input() for _ in range(8)]
  row,column = find_starting_point(matrix)
  print(get_word(matrix,row,column))
