for _ in range(int(input())):
  points = []
  for i in range(4):
    points.append(list(map(int,input().split())))
  points.sort()
  width = abs(points[0][0] - points[2][0])
  height  = abs(points[0][1] -points[1][1])
  print(int(width*height))