n,k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

solution = 0

for i in range(n):
  solution += (arr[i] > 0) and (arr[i] >= arr[k-1])

print(solution)
