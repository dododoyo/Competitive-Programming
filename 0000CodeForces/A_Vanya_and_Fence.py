def solve(n,h,arr):
  longs = sum([i>h  for i in arr])
  return n if longs == 0 else longs+n
n,h = map(int,input().split())
arr = list(map(int,input().split()))
print(solve(n,h,arr))
