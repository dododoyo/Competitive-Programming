from collections import Counter
k = int(input())
k *= 2  # k for two hands

full_grid = "".join(input() for _ in range(4))
freq_counter = Counter(full_grid)

for key,val in freq_counter.items():
  if val > k and key != ".":
    print("NO")
    exit(0)

print("YES")