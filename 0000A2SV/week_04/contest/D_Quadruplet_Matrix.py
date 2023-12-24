
def rotate( matrix):
    matrix = transpose(matrix)
    return invert(matrix)
def transpose(matrix):
    last_row = 1
    for i in range(len(matrix)-1):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
def invert(matrix):
    for i in range(len(matrix)):
        l,r = 0,len(matrix)-1
        while l < r:
            matrix[i][l],matrix[i][r] = matrix[i][r],matrix[i][l]
            l,r = l+1,r-1
    return matrix
    
for _ in range(int(input())):
  matrix = []
  n = int(input())
  for i in range(n):
    row = [int(i) for i in input()]
    matrix.append(row)
  if n == 1:print(0);continue
  print(rotate(matrix))
  # if n %2:
    #if it is odd x,cross,dot
  # else:
