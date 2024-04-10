# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

counter = 0

def is_sorted(arr):
  for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
      return False
  return True


def merge(arr1, arr2):
  # print(arr1,arr2)
  global counter
  if arr1[0] > arr2[0]:
    counter += 1
    return arr2+arr1
  else:
    return arr1+arr2


def mergeSort(arr):
  n = len(arr)
  if n == 1:
    return [arr[0]]
  middle = n//2

  left = mergeSort(arr[:middle])
  right = mergeSort(arr[middle:])

  return merge(left, right)

for _ in range(int(input())):
  n = int(input())
  nums = [int(num) for num in input().split()]
  counter = 0
  if is_sorted(mergeSort(nums)):
    print(counter)
  else:
    print(-1)