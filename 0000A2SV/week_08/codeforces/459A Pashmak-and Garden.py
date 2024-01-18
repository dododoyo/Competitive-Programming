''' The question asks given two points on
 the coordinate access
find out if they are points of 
a square parallel to the 
coordinate access if they are
print other possible vertexes 
if not print "-1" 
'''
x1,y1,x2,y2 = map(int,input().split())
solution = -1

# there are three possible scenarios
#1, points have the same x-coordinate
if x1 == x2:
  width = abs(y2 - y1)
  x3,x4 = x1 + width,x2 + width
  y3,y4 = y1,y2
  solution = [x3,y3,x4,y4]

#2, points have the same y-coordinate
if y1 == y2:
  height = abs(x2 - x1)
  x3,x4 = x1,x2
  y3,y4 = y1 + height,y2 + height
  solution = [x3,y3,x4,y4]

#3, points are the diagonal vertexes
width = abs(x2 - x1)
height = abs(y2 -y1)
if y1 != y2 and x1 != x2 and (width == height):
  x4,x3 = x2,x1
  y3,y4 = y2,y1
  solution = [x3,y3,x4,y4]

print(-1) if solution == -1 else print(*solution)