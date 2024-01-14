n = int(input())
little_x = list(map(int,input().split()))
little_y = list(map(int,input().split()))
total_levels = set()
total_levels.update(little_x[1:little_x[0]+1])
total_levels.update(little_y[1:little_y[0]+1])

solution = "Oh, my keyboard!"
if sum(total_levels) == (n*(n+1))//2:
  solution = "I become the guy."
print(solution)