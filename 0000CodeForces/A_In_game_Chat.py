for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  s = input()
  closing = 0

  while closing < n and s[n-closing-1] == ")":
    closing += 1

  print("Yes" if 2*closing > n else "No")