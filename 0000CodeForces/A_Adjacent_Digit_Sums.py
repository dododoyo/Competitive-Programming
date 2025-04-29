from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  x,y = ls()
  d = x - y + 1
  
  if d >= 0 and d % 9 == 0:
      print("YES")
  else:
      print("NO")