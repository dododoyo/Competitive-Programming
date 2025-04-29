for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  counter = [0]*(n+1)

  for j in range(n-1):
    u,v = [int(i) for i in input().split()]
    counter[u] += 1
    counter[v] += 1

  leafs = counter.count(1)

  print((leafs+1)//2)


