from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

n,s = ls()
arr = ls()

left = 0
count = 0
running_sum = 0

for right in range(n):
  running_sum += arr[right]

  while running_sum > s:
    running_sum -= arr[left]
    left += 1

  # each valid window will contribute 
  # window number of subarrays
  window = right-left+1
  count += window

print(count)