n = int(input())
middle = n//2
matrix = []
summ = 0
for i in range(n):
  row = [int(i) for i in input().split()]
  if i == middle:
    summ += sum(row)
  matrix.append(row)
for i in range(n):
  for j in range(n):
    if i-j == 0:
      summ += matrix[i][j]
    elif j == middle:
      summ += matrix[i][j]
    elif i+j == n-1:
      summ += matrix[i][j]
print(summ - matrix[middle][middle])