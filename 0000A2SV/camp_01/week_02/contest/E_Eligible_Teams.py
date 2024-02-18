for _ in range(int(input())):
  n,x = map(int,input().split())
  skills = list(map(int,input().split()))
  skills.sort()
  solution = 0
  right = left = n-1
  while left > -1 :
    if skills[left]*(right-left+1) >= x:
      solution += 1
      right = left -1
    left -= 1
  print(solution)