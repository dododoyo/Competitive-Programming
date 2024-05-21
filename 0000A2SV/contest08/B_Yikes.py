n = int(input())
simon = list(map(int,input().split()))
m = int(input())
nardos = list(map(int,input().split()))

prefix_sum = [0]*n
prefix_sum[0] = simon[0]

for i in range(1,n):
  prefix_sum[i] += simon[i]  + prefix_sum[i-1]

# find first element greater than current
for number in nardos:
  low, high = 0, n - 1
  while low <= high:
    middle = low + (high-low)//2
    if prefix_sum[middle] >= number:
      high = middle -1
    else:
      low = middle + 1
  print(low+1)