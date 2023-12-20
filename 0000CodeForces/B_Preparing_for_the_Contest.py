for _ in range(int(input())):
  n,k = map(int,input().split())
  solution = [0]*n
  last_index = n-1
  for i in range(k):
    solution [last_index-i] = n
    n -= 1
  for i in range(n):
    solution[i] = n-i
  print(*solution)