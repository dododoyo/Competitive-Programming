#two-pointers, comparison
def solve(n,k,arr):
  count,solution = 1,0
  for i in range(1,n):
    if arr[i-1] < 2*arr[i]:
      count +=1
    else:count = 1
    if count > k:
      solution +=1
  return solution
for _ in range(int(input())):
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  print(solve(n,k,arr))