def solve(n,containers):
  if n == 1:return "YES"
  total_sum = sum(containers)
  goal = total_sum//n
  if total_sum%n:
    return "NO"
  
  prefix_array = [0]*n
  for i in range(n):
    if containers[i] != goal:
      prefix_array[i] =abs(containers[i] -goal)
  suffix_array = prefix_array
  for i in range(1,n):
    prefix_array[i] += prefix_array[i-1]
    suffix_array[n-i-1] += suffix_array[n-i]
  for i in range(1,n):
    if prefix_array[i] == prefix_array[i-1]:
      return "YES"
  return "NO"
          


for _ in range(int(input())):
  n = int(input())
  containers = list(map(int,input().split()))
  #is it possible to make the waters in all same?
  print(solve(n,containers))
    