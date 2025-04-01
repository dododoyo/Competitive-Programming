n,k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]


def binary_search(num):
  left,right = 0,n-1

  while left <= right:
    middle = left + (right-left)//2

    if arr[middle] > num:
      right = middle - 1
    elif arr[middle] < num:
      left = middle + 1
    else:
      return "YES"

  return "NO"

for number in queries:
  print(binary_search(number))