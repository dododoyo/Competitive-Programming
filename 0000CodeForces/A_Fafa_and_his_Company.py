n = int(input())
solution = 0

for i in range(2,n+1):
  if n%i == 0:
    solution += 1

print(solution)