def solve(s,n):  
  for i in range(1,n):
    if (s[i],s[i-1]) in [("R","B"),("B","R")]:
      return True
    
  return False

for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  s = input().split("W")

  for x in s:
    if x:
      if not solve(x,len(x)):
        print("NO")
        break
  else:
    print("YES")