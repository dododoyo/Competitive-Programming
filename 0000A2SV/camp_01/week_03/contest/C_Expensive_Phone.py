for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  # monotonically increasing stack
  stack, solution = [], 0
  for i in range(n):
    number = a[n-i-1]
    while stack and stack[-1] >= number:
      stack.pop()
    if stack:
      solution += 1
    stack.append(number)
  print(solution)