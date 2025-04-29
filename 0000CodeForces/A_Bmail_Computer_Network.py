n = [int(i) for i in input().split()][0]
arr = [int(i) for i in input().split()]

solution = [n]
index = solution[-1]-2

while index > -1:
  solution.append(arr[index])
  if arr[index] == 1:
    break
  index = arr[index]-2
print(*reversed(solution))