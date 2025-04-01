from sys import stdin
def input(): return stdin.readline().strip()

c = float(input())

def is_valid(num):
  # print((num*num) + (num**0.5) , (num*num) + (num**0.5) <= c)
  return (num**2) + (num**0.5) <= c

low,high = 0,1e10
diff = 1e-6

solution = high

while low <= high:
  mid = low + (high-low)/2

  if is_valid(mid):
    solution = mid
    low = mid + diff
  else:
    high = mid - diff

print(solution)