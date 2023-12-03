squares_to_check = [[[0,0],[0,1],[1,0],[1,1]],
                    [[0,2],[0,1],[1,2],[1,1]],
                    [[0,2],[0,3],[1,2],[1,3]],
                    [[2,0],[2,1],[1,0],[1,1]],
                    [[2,2],[2,1],[1,2],[1,1]],
                    [[1,2],[1,3],[2,2],[2,3]],
                    [[2,0],[2,1],[3,0],[3,1]],
                    [[2,2],[2,1],[3,1],[3,2]],
                    [[3,2],[3,3],[2,2],[2,3]],
                    ]
matrix = []
for _ in range(4):
  matrix.append(list(input()))

for square in squares_to_check:
  hash_count = 0
  for each_comp in square:
    hash_count += matrix[each_comp[0]][each_comp[1]] == "#"
  dot_count = 4 - hash_count
  maximum_same = max(dot_count,hash_count);
  if maximum_same > 2:
    print("YES");
    exit(0);

print("NO")
    
