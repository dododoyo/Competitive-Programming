def is_valid(n,arr):
    # use monotonically decreasing stack
    stack = []
    for i in range(n):
      curr_min = i
      while stack and arr[stack[-1][0]] < arr[i]:
          curr_min = stack[-1][1]
          stack.pop()

      if stack and arr[stack[-1][1]] != arr[stack[-1][0]]:
        return ("YES", [stack[-1][1]+1,stack[-1][0]+1,i+1])
      stack.append([i,curr_min])

    return ("NO",[])
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  solution = is_valid(n,arr)
  if solution[0] == "YES":
    print("YES")
    print(*solution[1])
  else:
    print("NO")

