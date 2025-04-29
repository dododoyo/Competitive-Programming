for _ in range([int(i) for i in input().split()][0]):
  n,k = [int(i) for i in input().split()]
  max_even = k-1
  if n % 2 == 0: #even
      steps = (n - 2 + k) // max_even
  else: # odd
      steps = (n - 2) // max_even  + 1

  print(steps)