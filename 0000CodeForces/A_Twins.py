n = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
total_sum = sum(coins)
cfy = 0 # coins for you
for i in range(len(coins)):
  cfy += coins[i]
  if cfy > total_sum-cfy:
    print(i+1)
    break
  