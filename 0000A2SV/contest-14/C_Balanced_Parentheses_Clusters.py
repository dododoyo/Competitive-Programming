for _ in range(int(input())):
  n = int(input())
  s = input()
  solution = 1
  for i in range(1,2*n):
    if s[i] == ")" and s[i-1] == ")":
      solution += 1
  print(solution)
