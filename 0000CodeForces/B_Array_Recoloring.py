for _ in range([int(i) for i in input().split()][0]):
  n,k = [int(i) for i in input().split()]
  arr = [int(i) for i in input().split()]

  # if k > 2:
  print(sum(sorted(arr,reverse=True)[:k+1]))
  # else:
