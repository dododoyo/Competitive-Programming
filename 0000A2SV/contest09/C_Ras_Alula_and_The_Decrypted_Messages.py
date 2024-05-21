def solve(n,prefix_s,m,w_sum):
  for i in range(m,n+1):
    if prefix_s[i] - prefix_s[i-m] == w_sum:
      return "YES"
  return "NO"   
for _ in range(int(input())):
  n,m = map(int,input().split())
  s = [ord(i) for i in input()]
  w_sum = sum([ord(i) for i in input()])
  prefix_s = [0]*(n+1)
  for i in range(n):
    prefix_s[i+1] = prefix_s[i] + s[i]
  print(solve(n,prefix_s,m,w_sum))
  
