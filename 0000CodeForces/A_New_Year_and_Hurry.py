n,k = [int(i) for i in input().split()]
available_time = 240 - k
def isValid(x):
  return 5 * (((x)*(x+1))//2) <= available_time


solution = 0

left,right = 1,n


while left <= right:
  middle = left + (right-left)//2

  if isValid(middle):
    solution = middle
    left = middle + 1
  else:
    right = middle - 1

print(solution)