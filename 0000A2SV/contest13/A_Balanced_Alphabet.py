for _ in range(int(input())):
  n,k = map(int,input().split())
  solution = []
  for i in range(n):
        solution.append(chr((i % k) + ord("a")))
  print("".join(solution))
