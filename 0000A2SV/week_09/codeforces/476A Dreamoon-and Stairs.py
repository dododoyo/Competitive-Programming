n,m = map(int,input().split())

if n < m:
  print(-1);exit(0)

if m < n/2:
  solution,i = 0,1
  while solution < n/2:
    solution = m*i;i+=1
else:
  solution = m
print(solution)