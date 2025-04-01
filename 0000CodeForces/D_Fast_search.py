from sys import stdin
def input(): return stdin.readline().strip()

n = [int(i) for i in input().split()][0]
nums = sorted([int(i) for i in input().split()])

def lower_bound(left):
  low, high = 0, n - 1
  solution = n  

  while low <= high:
    middle = low + (high - low) // 2
    if nums[middle] >= left:
      solution = middle
      high = middle - 1
    else:
      low = middle + 1

  return solution

def upper_bound(right):
  low, high = 0, n - 1
  solution = -1  

  while low <= high:
    middle = low + (high - low) // 2
    if nums[middle] <= right:
      solution = middle
      low = middle + 1
    else:
      high = middle - 1

  return solution

def count_in_range(left, right):
  x = upper_bound(right)
  y = lower_bound(left)
  
  return max(0, x - y + 1)

k = int(input())

for _ in range(k):
  left, right = map(int, input().split())
  print(count_in_range(left, right), end=" ")
