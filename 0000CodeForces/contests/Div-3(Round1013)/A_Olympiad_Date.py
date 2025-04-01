from collections import defaultdict


for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  nums = [int(i) for i in input().split()]

  count = defaultdict(int)

  for i in range(len(nums)):
    count[nums[i]] += 1

    if count[0] > 2 and count[1] > 0 and count[2] > 1 and count[3] > 0 and count[5] > 0:
      print(i+1)
      break
  else:
    print(0)
