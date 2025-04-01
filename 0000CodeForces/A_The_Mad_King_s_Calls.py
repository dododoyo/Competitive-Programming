for _ in range([int(i) for i in input().split()][0]):
  n = input()
  print(10*(ord(n[0]) - 49) + 10*(len(n) == 4) + 6*(len(n) == 3) + 3*(len(n) == 2) + (len(n) == 1))