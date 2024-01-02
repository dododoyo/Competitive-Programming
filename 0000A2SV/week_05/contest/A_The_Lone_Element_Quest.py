from collections import Counter
for _ in range(int(input())):
  n = int(input())
  arr = [int(i) for i in input().split()]
  minn = min(arr)
  maxi = max(arr)
  freq = [0,0]
  for i in arr:
    if i == minn:
      freq[0] += 1
    else:
      freq[1] += 1
  if freq[0] == 1:
    print(arr.index(minn)+1)
  else:
    print(arr.index(maxi)+1)