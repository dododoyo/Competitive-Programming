r,c = map(int,input().split())
cake = [list(input()) for _ in range(r)]
cake_copy = y = [row[:] for row in cake]

solution = 0
# do a row traversal and count the valid cakes 
for column in range(c):
  column_count,found_strawberry = 0,False
  for row in range(r):
    if cake[row][column] == "S":
      found_strawberry = True
      break
    else:
      column_count += (cake[row][column] == ".")
  if column_count == r:
    for row in range(r):
      cake[row][column] = 0

  if not found_strawberry:
    solution += column_count

removed = solution//r

# do a column traversal and count the valid cakes
for row in range(r):
  row_count,found_strawberry = 0,False
  for column in range(c):
    if cake[row][column] == "S":
      found_strawberry = True
      break
    else:
      row_count += (cake[row][column] == ".")
  
  if not found_strawberry and row_count == c-removed:
    solution += row_count
print(solution)
