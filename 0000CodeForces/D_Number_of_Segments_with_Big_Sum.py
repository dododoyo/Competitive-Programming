from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

n,s = ls()
arr = ls()

left = 0
solution = 0
running_sum = 0


for right in range(n):
  # for each right boundary we want to count 
  # how many subarrays we have that end at right 
  # that are good 

  # if anything within our window have a sum of s 
  # anything we add on that will also be valid

  running_sum += arr[right]

  while running_sum >= s:
    running_sum -= arr[left]
    left += 1

  solution += left

print(solution)