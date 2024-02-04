n = int(input())
matrix = [""]*n
for i in range(n):
  matrix[i] = input()

x_element = matrix[0][0]
others = matrix[0][1]

if x_element == others:
  print("NO");exit(0)

# diagonals sum and difference is same 
for i in range(n):
  for j in range(n):
    if i-j == 0 or i+j == n-1:
      # if it is the part of x and not an x element
      if matrix[i][j] != x_element:
        print("NO");exit(0)
        
    else:
      # if it is not part of x and not same as other elements
      if matrix[i][j] != others:
        print("NO");exit(0)
print("YES")