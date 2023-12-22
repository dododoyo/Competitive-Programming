for _ in range(int(input())):
  n = int(input())
  solution = []
  while n:
    solution.append(n%10)
    n //= 10
  
  for i in range(len(solution)):
    if solution[i] != 0:
      print(solution[i]*(10**i),end=" ")
  print()