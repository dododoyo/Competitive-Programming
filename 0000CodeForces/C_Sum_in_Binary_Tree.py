from math import log2
for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  # n = 2^(x-1) + 1 
  # n - 1 = 2^(x-1)
  # log2(n-1) = x - 1
  # log2(n-1) + 1 = x
  summ = 0

  while n != 1:
    summ += n 
    n //= 2

  print(summ+1)