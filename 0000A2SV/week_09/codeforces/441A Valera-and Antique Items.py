n,v = map(int,input().split())
solution = []
for i in range(n):
  items = [int(i) for i in input().split()]
  k = items[0]
  for idx in range(1,len(items)):
    if items[idx] < v:
      solution.append(i+1)
      break
print(len(solution))
print(*solution)
