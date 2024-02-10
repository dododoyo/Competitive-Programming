def solve(n,new_list):
  new_list.sort()
  if new_list[0] != 1:
    return "NO"
  running_sum = 1
  '''for each element we can construct numbers from
  1 upto their sum from the numbers'''
  for i in range(1,n):
    # if the number we are checking 
    # is greater than the sum it can't be generated
    if new_list[i]  > running_sum:
      return "NO"
    running_sum += new_list[i]
  return "YES"

for _ in range(int(input())):
  n = int(input())
  new_list = list(map(int,input().split()))
  print(solve(n,new_list))