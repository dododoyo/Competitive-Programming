import math
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  summ = sum(arr)
  sqrt_ = math.sqrt(summ)
  round_ = math.floor(sqrt_)
  if round_-sqrt_ == 0.0:
    print("YES")
  else:
    print("NO")