# if sorted . . . no 
# find the break point from the back 
# min suffix  and max prefix should be tracked

for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  arr = [int(i) for i in input().split()]
  
  if sorted(arr) == arr:
    print("NO")
  else:
    print("YES")
    