from typing import Counter


for _ in range([int(i) for i in input().split()][0]):
  n, k = [int(i) for i in input().split()]
  a = [int(i) for i in input().split()]

  # differ = [0]*n

  # for i in range(n):
  #   if a[i]%k:
  #     differ[i] = k*(a[i]//k + 1) - a[i]

  # solution = differ[0]
  # solution_list = [differ[0]]*n
  # differ.sort()

  # for i in range(1,n):
  #   if differ[i] != 0:
  #     if differ[i] == differ[i-1]:
  #       solution_list[i] = solution_list[i-1] + k
  #     else:
  #       solution_list[i] = differ[i]

  #     solution = max(solution,solution_list[i])

  # print(solution+1 if solution != 0 else solution)

  cc = Counter([x % k for x in a if x % k != 0])
  aa = [(x, cc[x]) for x in sorted(cc)]

  print(aa)
  res = 0
  y = 0
  for x in aa:
    res += (k - x[0])
    res += (x[1] - 1) * k
    res -= x[1]
    y += 1

  print(res)
