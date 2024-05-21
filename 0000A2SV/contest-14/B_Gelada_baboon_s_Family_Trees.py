n = int(input())
values = [int(n) for n in input().split()]
trees = 0

if n == 1:
  print(1)
else:
  for i in range(n):
    if (values[i] >= i + 1) and (values[values[i] - 1] == i+1):
      trees += 1

  print(trees)

