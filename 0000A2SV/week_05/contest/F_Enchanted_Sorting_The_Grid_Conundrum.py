import time as tm
def isSorted(arr):
  for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
      return False
  return True

def isMagic(arr,n,m):
  j = 0
  while j < n and isSorted(arr[j]):
    j+=1
  if j == n:return []
  diff = []
  #get the differing elements
  for i in range(m):
    sorted_arr = sorted(arr[j])
    if arr[j][i] != sorted_arr[i]:diff.append(i+1)

  if len(diff) != 0 and len(diff) != 2:
      return diff
  #check for all the elements
  for i in range(n):
      row = arr[i]
      row[diff[0]-1],row[diff[1]-1] = row[diff[1]-1],row[diff[0]-1]
      if row != sorted(row):
        return [0,1,2]
  return diff


for _ in range(int(input())):
  n,m = map(int,input().split())
  start = tm.time()
  grid = [list(map(int,input().split())) for _ in range(n)]
  if m == 1:
    print(1,1)
    end = tm.time()
    print(end-start, "seconds")
    continue
  indeces = isMagic(grid,n,m)
  end = tm.time()
  print(end-start, "seconds")

  if len(indeces) == 0:
    print(1,1)
  elif len(indeces) == 2:
    print(*indeces)
  else:
    print(-1)
# test_arr = ["123342991"]*200000
# for i in test_arr:
#   print(i)
# n,m = 200000,1
# # n,m = map(int,input().split())
# start = tm.time()
# grid = [list(map(int,i)) for i in test_arr]
# indeces = isMagic(grid,n,m)
# end = tm.time()
# print(end-start, "ms")

