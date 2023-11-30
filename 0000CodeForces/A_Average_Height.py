for _ in range(int(input())):
  n = int(input());
  a = list(map(int,input().split()));
  evens = [height for height in a if not height % 2]
  odds = [height for height in a if height % 2]
  print(*(evens+odds))

