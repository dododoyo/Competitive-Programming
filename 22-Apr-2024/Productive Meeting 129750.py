# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from heapq import heapify,heappop,heappush
for _ in range(int(input())):
  n = int(input())
  sociability = [-int(num) for num in input().split()]
  max_heap = []

  for index,value in enumerate(sociability):
    if value != 0:
      heappush(max_heap,[value,index+1])

  solution = []
  while len(max_heap) > 1:
    p1 = heappop(max_heap)
    p2 = heappop(max_heap)
    solution.append([p1[1],p2[1]])
    p1[0],p2[0] = p1[0]+1,p2[0]+1
    if p1[0]:heappush(max_heap,p1)
    if p2[0]:heappush(max_heap,p2)
  sn = len(solution)
  print(sn)
  for i in range(sn):
    print(*solution[i])
