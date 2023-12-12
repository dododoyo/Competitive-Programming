def findMaxProduct(arr):

  theMin = min(arr);
  foundMin = False;
  totalProduct = 1;

  for i in arr:
    if foundMin == False:
      if i == theMin:
        foundMin = True;
      else:
        totalProduct *= i;
    else:
      totalProduct *= i;
  
  return totalProduct*(theMin+1);

t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()));
  print(findMaxProduct(arr))