# find the index of the minimum number 
# anything before the first minimum index(if we had multiple minimums) can be sorted for the operations
# check if the array is sorted afterwards
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  min_index= 0
  for i in range(n):
    if arr[i] < arr[min_index]:
      min_index = i
  print(min_index if sorted(arr[min_index+1:]) == arr[min_index+1:] else -1)
