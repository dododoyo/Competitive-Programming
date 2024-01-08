'''
m-lucky number is smallest number that occurs in all of the subarrays of the array having length m 
'''
def get_min(a,size):
  solution = set(a[:size])
  for i in range(1,len(a)-size+1):
    solution = solution & set(a[i:size+i])
  if solution:
    return min(solution)
  return -1

for _ in range(int(input())):
  n = int(input())
  a = [int(i) for i in input().split()]
  solution = [1]*n
  for i in range(n):
    solution[i] = get_min(a,i+1)
  print(*solution)

