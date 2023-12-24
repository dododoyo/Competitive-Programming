def attacks(matrix,row,col):
  total_sum = 0
  n,m = len(matrix),len(matrix[0])
  diagonals = 0
  #go up right
  if row != n-1 or col != m-1:
    diagonals +=1
    r,c = row,col
    while r > -1 and c < m:
      total_sum += matrix[r][c]
      r,c = r-1,c+1
  #go up left
  if row != 0 or col != 0: 
    diagonals +=1
    r,c = row,col
    while r > -1 and c > -1:
      total_sum += matrix[r][c]
      r,c = r-1,c-1    
  #go down right
  if row != n-1 or col != m-1:
    diagonals += 1
    r,c = row,col
    while r<n and c<m:
      total_sum += matrix[r][c] 
      r,c = r+1,c+1   
  #go down left
  if row != n-1 or col != 0:
    diagonals +=1
    r,c = row,col
    while r<n and c>-1:
      total_sum += matrix[r][c]
      r,c = r+1,c-1
  return total_sum - matrix[row][col]*(diagonals-1)
for _ in range(int(input())):
  n,m = map(int,input().split())
  matrix = []
  for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
  solution = 0
  if n == 1:
    print(max(matrix[0]))
    continue
  if m == 1:
    for row in range(n):
      for col in range(m):
        solution = max(solution,matrix[row][col])
    print(solution)
    continue

  for row in range(n):
    for col in range(m):
      solution = max(solution,attacks(matrix,row,col))
  print(solution)