n = int(input())
arr  = [int(i) for i in input().split()]
for i in range(n):arr[i] = arr[i]%2
summ = sum(arr)
if summ == 1:
  # includes one odd
  for i in range(n):
    if arr[i] == 1:
      index = i+1;break
else:
  # includes one even
  for i in range(n):
    if arr[i] == 0:
      index = i+1;break
print(index)