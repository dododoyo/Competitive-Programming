#  for all i the i-th element is greater than or equal to i
for _ in range(int(input())):
  n = int(input())
  nums = list(map(int,(input().split())))
  current_index, left, solution = 1, 0, 0
  for right in range(n):
    while left < n and current_index > nums[right]:
      left += 1
      current_index -= 1
    # any valid window will contribute 
    # number of sub-arrays equal to it's length
    solution += right-left+1
    # update current index for the next element
    current_index += 1
  print(solution)