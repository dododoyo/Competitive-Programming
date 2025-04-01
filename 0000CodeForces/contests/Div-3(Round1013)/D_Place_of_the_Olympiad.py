for _ in range([int(i) for i in input().split()][0]):
  n,m,k = [int(i) for i in input().split()]
  max_for_rwo = k//n  
  if k%n != 0:
    max_for_rwo += 1
  empty = m - max_for_rwo + 1
  ans =  max_for_rwo // empty  + int(max_for_rwo % empty > 0)

  print(ans)