from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]



n,m = ls()

odds = "#"*m
twos = "#" + "."*(m-1)
fours = "."*(m-1) + "#"
x = True
for i in range(n):
  if i%2:
    if x:
      print(fours)
    else:
      print(twos)
    x = not x 
  else:
    print(odds)