n = int(input())
arr = [int(num) for num in input().split()]
max_,min_,solution = max(arr),min(arr),0
for i in arr:
  if i < max_ and i > min_:
    solution += 1

print(solution)
