for _ in range(int(input())):
  n = int(input())
  cakes = [int(i) for i in input().split()]
  aman, simon = float('-inf'), sum(cakes)
  current_sum,current_length = 0,0
  # kdane's algorithm with length limitation
  for i in range(n):
      if cakes[i] > 0:
          current_sum += cakes[i]
          current_length += 1
      else:
          current_sum = cakes[i]
          current_length = 1

      if current_length < n:
          aman = max(aman, current_sum)

  print("YES") if simon > aman else print("NO")