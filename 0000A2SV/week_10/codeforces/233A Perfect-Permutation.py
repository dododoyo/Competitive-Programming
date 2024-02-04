n=int(input())
# odd numbers wont work
if n%2: 
  print(-1)
# reversed integers will work
else: 
  print(*range(n,0,-1))