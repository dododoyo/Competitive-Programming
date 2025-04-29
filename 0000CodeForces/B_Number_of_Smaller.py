from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n,m = ls()
arr1 = ls()
arr2 = ls()


index1,index2 = 0,0

while index1 < n and index2 < m:
  if arr1[index1] < arr2[index2]:
    index1 += 1
  else:
    index2 += 1
    print(index1,end=" ")

while index1 < n:
  index1 += 1

while index2 < m:
  index2 += 1 
  print(index1,end=" ")