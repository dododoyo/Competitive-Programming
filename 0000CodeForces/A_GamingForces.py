from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  n = ls()[0]
  arr = ls()

  arr.sort(reverse=True)

  index = 0
  operations = 0

  while arr[index] > 0:
    arr[index] = 0

    if index < n-1:
      arr[index+1] -= 1
    
    if index < n-2:
      arr[index+2] -= 1

    index += 1
    operations += 1

  print(operations)