n,quality_map = int(input()),{}
prices,qualities = [0]*n,[0]*n
for i in range(n):
  price,quality = map(int,input().split())
  prices[i],qualities[i] = price,quality
for i in range(n):quality_map[prices[i]] = qualities[i]
prices.sort()
for i in range(n-1):
  if quality_map[prices[i]] > quality_map[prices[i+1]]:
    print("Happy Alex");exit(0)
print("Poor Alex")
