n, m = map(int,input().split())
matrix = []
for i in range(n):
  # get mark for each student
  matrix.append(list(map(int,list(input()))))
max_grade = [0]*m

# for each column(subject) find out the maximum mark
for i in range(m):
  for j in range(n):
    max_grade[i] = max(max_grade[i],matrix[j][i])

solution = 0

for i in range(n):
  for j in range(m):
    # if a student is good at some subject 
    # if doesn't matter if he is good on others as well 
    # one is enough to count a student as successful
    if matrix[i][j] == max_grade[j]:
      solution += 1 
      break
print(solution)