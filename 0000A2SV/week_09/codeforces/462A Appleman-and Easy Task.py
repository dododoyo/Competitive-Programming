def count_adjacent(row,column,arr):
  count,n = 0,len(arr)
  if row == 0:
    # checking top left corner
    if column == 0:
      count += arr[0][1] == "o"
      count += arr[1][0] == "o"
      if count %2:return False
    # checking top right corner
    elif column == n-1:
      count += arr[0][n-2] == "o"
      count += arr[1][n-1] == "o"
      if count %2: return False
    else:
      adjacent = [[0,1],[0,-1],[1,0]]
      for dx,dy in adjacent:
        count += arr[row+dx][column+dy] == "o"
      if count %2:return False

  elif row == n-1:
    # checking bottom right corner
    if column == n-1:
      count += arr[n-1][n-2] == "o"
      count += arr[n-2][n-1] == "o"
      if count %2: 
        return False
    # checking bottom left corner
    elif column == 0:
      count += arr[n-2][0] == "o"
      count += arr[n-1][1] == "o"
      if count %2: 
        return False
    else:
      adjacent = [[0,1],[0,-1],[-1,0]]
      for dx,dy in adjacent:
        count += arr[row+dx][column+dy] == "o"
      if count %2:
        return False

  elif column == 0:
    adjacent = [[1,0],[-1,0],[0,1]]
    for dx,dy in adjacent:
      count += arr[row+dx][column+dy] == "o"
    if count %2:return False

  elif column == n-1:
    adjacent = [[1,0],[-1,0],[0,-1]]
    for dx,dy in adjacent:
      count += arr[row+dx][column+dy] == "o"
    if count %2:return False
  else:
    adjacent = [[1,0],[-1,0],[0,-1],[0,1]]
    for dx,dy in adjacent:
      count += arr[row+dx][column+dy] == "o"
    if count %2:return False

  return True
    
n = int(input())
matrix  = []
for _ in range(n):
  row = list(input())
  matrix.append(row)

if n == 1:
  print("YES");exit(0)
for row in range(n):
  for column in range(n):
    if not count_adjacent(row,column,matrix):
      # print(row,column)
      print("NO");exit(0)

print("YES")