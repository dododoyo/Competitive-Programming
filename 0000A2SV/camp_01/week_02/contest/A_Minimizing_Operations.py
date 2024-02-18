"""
In one operation, he can take some indices in the array
and increase the elements of the array at those indices by 1
."""
def solver(n,arr):
  arr.sort()
  left = n-1
  solution = 0
  while left:
    solution += arr[left] - arr[left-1]
    left -= 1
  return solution
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  print(solver(n,arr))
