import math
left,right = -2 * (10**9),2* (10**9)
for _ in range(int(input())):
    sign, x, answer = input().split()
    x = int(x)
    if sign == ">=":
      if answer == "Y":
        left = max(x,left)
      else:
        right = min(right,x-1)

    elif sign == "<=":
      if answer == "Y":
        right = min(right,x)
      else:
        left = max(x,left)

    elif sign == "<":
      if answer == "Y":
        right = min(right, x-1)
      else:
        left = max(left,x)

    elif sign == ">":
      if answer == "Y":
        left = max(left,x+1)
      else:
        right = min(right,x)
    # print(left,right)

if right >= left:
  print(math.floor((right + left) / 2))
else:
  print("Impossible")