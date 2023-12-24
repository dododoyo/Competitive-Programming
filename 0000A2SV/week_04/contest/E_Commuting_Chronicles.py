
n,m = map(int,input().split())
city_map = []
for i in range(n):
  row = list(map(int,input().split()))
  city_map.append(row)

solution = 0
if n == 1:
  print(max(city_map[0]))
if m == 1:
  for row in range(n):
    for col in range(m):
      solution = max(solution,city_map[row][col])
  print(solution)

for row in range(n):
  for col in range(m):
    solution = max(solution,attacks(city_map,row,col))
print(solution)