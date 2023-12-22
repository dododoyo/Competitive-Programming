for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  left,max_len = 0,0
  for right in range(len(arr)):
    if arr[right] == 1:
      left = right+1
    else:
      max_len = max(max_len,right-left+1)
  print(max_len)


  #Sliding window