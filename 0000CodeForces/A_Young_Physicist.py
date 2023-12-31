def equilibrium(n,forces):
  #implementation
  x,y,z = 0,0,0
  for i in range(n):
    x += int(forces[i][0])
    y += forces[i][1]
    y += forces[i][2]
  return x==0 and y==0 and z==0

n = int(input())
forces = [list(map(int,input().split())) for _ in range(n)]

if equilibrium(n,forces):
  print("YES")
else:
  print("NO")