from sys import stdin
def input(): return stdin.readline().strip()

n,x,y = [int(i) for i in input().split()]
faster = min(x,y)

def is_valid(seconds):
  # use the fastest copier to make a copy  
  # for the other copier
  seconds -= faster
  
  # add the first copy used on the second
  # machine in the count of copies
  copies = 1

  copies += seconds // x
  copies += seconds // y

  return  copies >= n

low,high = 0,faster + n*(faster+max(x,y))//2 + 1
solution = high

while low <= high:
  mid = low + (high-low)
  if is_valid(mid):
    solution = mid 
    high = mid - 1
  else:
    low = mid + 1

print(solution)