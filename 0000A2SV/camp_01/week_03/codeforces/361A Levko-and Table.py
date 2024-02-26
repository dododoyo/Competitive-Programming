n,k = map(int,input().split())
# we will have n numbers 
matrix = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
  matrix[i][i] = k
for row in matrix:
  print(*row)