t = int(input())
for i in range(t):
  n, x = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  if i != t-1:
    input()
  a.sort()
  b.sort()
  can_rearrange = True
  for i in range(n):
    if a[i]+b[n-i-1] > x:
      can_rearrange = False
      break
  print("Yes" if can_rearrange else "No")