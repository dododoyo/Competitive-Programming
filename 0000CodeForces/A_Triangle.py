# x1, y1, x2, y2, x3, y3 = map(int,input().split())
points = list(map(int, input().split()))

def il():
  return list(map(int, input().split()))

def isRightAngleTriangle(points):
  d12 = (points[0] - points[2])**2 + (points[1] - points[3])**2
  d13 = (points[0] - points[4])**2 + (points[1] - points[5])**2
  d23 = (points[2] - points[4])**2 + (points[3] - points[5])**2
  
  # if points for a triangle and they satisfy the pythagorous theorem return True
  return (d12 and d23 and d13) and (d12**0.5 + d23**0.5 > d13**0.5) and ((d12 == d23 + d13) or (d23 == d12 + d13) or (d13 == d12 + d23))


if isRightAngleTriangle(points):
  print("RIGHT")
  exit(0)

for i in range(6):
  points[i] += 1
  if isRightAngleTriangle(points):
    print("ALMOST")
    exit(0)

  points[i] -= 2
  if isRightAngleTriangle(points):
    print("ALMOST")
    exit(0)
  points[i] += 1

print("NEITHER")