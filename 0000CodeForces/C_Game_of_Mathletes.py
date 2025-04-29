from sys import stdin
def i(): return stdin.readline().strip()
def ls(): return [int(i) for i in i().split()]
def mt(rows): return[list(map(int, i().split())) for _ in range(rows)]

t = ls()[0]

for _ in range(t):
  n,k = ls()
  arr = ls()

  arr.sort()

  left,right = 0,n-1
  score = 0

  while left < right:
    if arr[left] + arr[right] < k:
      left += 1
    elif arr[left] + arr[right] > k:
      right -= 1
    else:
      score += 1
      left += 1
      right -= 1

  print(score)