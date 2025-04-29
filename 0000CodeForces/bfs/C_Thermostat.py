from sys import stdin
def input(): return stdin.readline().strip()

for _ in range([int(i) for i in input().split()][0]):
  left,right,change = [int(i) for i in input().split()]
  initial,final = sorted([int(i) for i in input().split()])
  # l <= b <= r

  current_level = [initial]
  # visited = set()
  # visited.add(initial)
  level = 0

  found = False 
  while current_level and (not found):
    next_level = []

    for num in current_level:
      if num == final:
        found = True

      # go down
      if num-change >= left:
        for new_num in range(left,num-change+1):
          # if new_num not in visited:
            # visited.add(new_num)
            next_level.append(new_num)

      # go up
      if num+change <= right:
        for new_num in range(num+change,right+1):
          # if new_num not in visited:
            # visited.add(new_num)
            next_level.append(new_num)

    # print(current_level)
    current_level = next_level[:]

    if not found:
      level += 1

  if not found:
    print(-1)
  else:
    print(level)
