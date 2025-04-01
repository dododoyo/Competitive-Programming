for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  if n%2:
    if n == 1:
      print(1)
    elif n == 3:
      print(*[1,3,2])
    else:
      last = n-1 
      solution = [0]*n
      for i in range(1,n+1):
        solution[i-last-1] = i
        last -= 1

      print(*solution)
  else:
    print(-1)