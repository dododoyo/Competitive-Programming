n,m = map(int,input().split())
for i in range(n):
  if i%2:
    print("#"+"."*(m-1)if (i-1)%4 else  "."*(m-1) + "#")
  else:
    print("#"*m)