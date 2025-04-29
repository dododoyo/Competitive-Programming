from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
  a,b,c = ls()
  print(max(a,max(b,c)+1)- a ,max(b, max(a,c) + 1) - b,max(c,max(a,b)+1) - c)
  