"""
If a customer purchases at least x items, 
y cheapest from the x items are free.
"""
n,q = map(int,input().split())
prices = list(map(int,input().split()))
prices.sort()
prefix_prices = [0]*(n+1)
for i in range(1,n+1):
  prefix_prices[i] = prefix_prices[i-1] + prices[i-1]

for _ in range(q):
  x,y = map(int,input().split())
  print(prefix_prices[n-x+y] - prefix_prices[n-x])
