from collections import deque

n = [int(i) for i in input().split()][0]
points=[tuple(map(int,input().split(' '))) for _ in range(n)]

points_set=set(points)

solution={}
q=deque()
MOVES=((1,0),(-1,0),(0,1),(0,-1))

for x,y in points:
    for dx,dy in MOVES:
        nx,ny=dx+x,dy+y
        # immediate neighbors might work
        if (nx,ny) not in points_set:
          solution[x,y]=(nx,ny)
          q.append((x,y))
          break

while q:
    # parent
    x,y=q.popleft()

    for dx,dy in MOVES:
        k=(dx+x,dy+y)

        if (k in points_set):
          
          if (k not in solution):
            solution[k]=solution[x,y]
            q.append(k)

for x,y in points:
    i,j=solution[x,y]
    print(i,j)