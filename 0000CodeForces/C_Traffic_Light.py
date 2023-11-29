def getPassSec(n,curr,arr):
  if curr == "g":return 0;
  paths = [0]*(2*countCurrentOccurrence(curr,arr))
  arr = arr + arr;
  j = 0
  i = 0
  while i < len(arr):
    index_till_g = 0
    if arr[i] == curr:
      while i < len(arr) and arr[i] != "g" :
        i += 1
        index_till_g +=1
      paths[j] = index_till_g;
      j += 1
    i += 1
  
  return max(paths);

def countCurrentOccurrence(curr,arr):
  occur = 0;
  for i in arr:
    if i == curr:
      occur += 1
  return occur


t = int(input())
for _ in range(t):
  n,curr = map(str,input().split());
  n = int(n);
  arr = input();
  print(getPassSec(n,curr,arr));