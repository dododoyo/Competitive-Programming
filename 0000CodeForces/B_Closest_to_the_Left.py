from sys import stdin
def input(): return stdin.readline().strip()

n,k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]


def lower_bound(num):
  left,right = 0,n-1
  bound = 0

  while left <= right:
    middle = left + (right-left)//2

    if arr[middle] <= num:
      bound = middle + 1
      left = middle + 1
    else:
      right = middle - 1

  return bound

for q in queries:
  print(lower_bound(q))