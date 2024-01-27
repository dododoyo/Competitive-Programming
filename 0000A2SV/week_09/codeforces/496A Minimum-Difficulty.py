n = int(input())
holds = list(map(int,input().split()))

# difficulty of the track is the maximum difference between any consecutive heights

# task if to remove one element and get the minimum difficulty still

# we can't remove the first and the last options

#sliding window
min_index = 2

for right in range(2,n):
  if holds[right] - holds[right-2] < holds[min_index] - holds[min_index-2]:
    min_index = right

holds[min_index-1] = holds[min_index-2]
max_diff = 0
for right in range(1,n):
  if holds[right] - holds[right-1] > max_diff:
    max_diff = holds[right] - holds[right-1]

print(max_diff)