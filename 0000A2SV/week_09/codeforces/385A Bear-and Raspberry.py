# honey is paid not in cash 
# but in kilos of raspberry 

#bear will lend barrel for c kilos of raspberry 

n,c  = map(int,input().split())
honey_prices = [int(i) for i in input().split()]

max_diff_index = 0

for right in range(n-1):
  current_diff = honey_prices[right] - honey_prices[right+1]
  max_diff = honey_prices[max_diff_index] - honey_prices[max_diff_index+1]
  if current_diff > max_diff:
    max_diff_index = right


max_diff = honey_prices[max_diff_index] - honey_prices[max_diff_index+1]
profit = max_diff-c
if profit < 0:
  # no profit for given prices 
  # so plan is not executed
  print(0)
else:
  print(profit)