dp = [[0]*101 for _ in range(101)]
for i in range(1,101):dp[0][i] = dp[0][i-1] + 1
for i in range(1,101):dp[i][0] = dp[i-1][0] + 1

for i in range(1,101):
  for j in range(1,101):
    coming_from_up = dp[i-1][j] + (j+1)
    coming_from_left = dp[i][j-1] + (i+1)
    dp[i][j] = min(coming_from_up,coming_from_left)

for _ in range(int(input())):
  row,column,k = map(int,input().split())
  print("NO" if dp[row-1][column-1] != k else "YES")