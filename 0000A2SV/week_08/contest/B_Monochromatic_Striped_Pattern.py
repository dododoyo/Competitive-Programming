# return the maximum number of blacks in a window of k
for _ in range(int(input())):
  n,k = map(int,input().split())
  cell = input()
  max_blacks,current_blacks = 0,0
  for right in range(n):
    if right < k:
      max_blacks += cell[right] == "B"
      current_blacks = max_blacks
    else:
      current_blacks += (cell[right] == "B" and cell[right-k] == "W")
      current_blacks -= (cell[right] == "W" and cell[right-k] == "B")
    max_blacks = max(max_blacks,current_blacks)

  print(k - max_blacks)


