from math import log2
for _ in range(int(input())):
  num = int(input())
  log_val = log2(num)
  print("NO" if log_val == int(log_val) else "YES")
  