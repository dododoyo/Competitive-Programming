from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

n,m = ls()
fok = [ls() for _ in range(n)]
count = 0

for i in range(n):
  for j in range(0,2*m,2):
    # print(fok[i][j] or fok[i][j+1])
    count += int(fok[i][j] or fok[i][j+1])

print(count)