from math import ceil
for _ in range(int(input())):
  x,y = map(int,input().split())

  if y == 0:
    print(ceil(x/15))
    continue

  total_y_area = y*4
  screens_for_y = ceil(total_y_area/8)

  full_ys = total_y_area//8
  last_screen_y = total_y_area%8

  last_screen_remain_x = 0
  if last_screen_y:
    last_screen_remain_x = 15 - last_screen_y

  total_x_available  = 7*full_ys + last_screen_remain_x

  extra_x = x-total_x_available

  if x > total_x_available:
    screens_for_y += ceil((extra_x)/15)
  
  
  print(screens_for_y)

