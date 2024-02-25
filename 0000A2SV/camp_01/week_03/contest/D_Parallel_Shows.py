n = int(input())
shows = []
for _ in range(n):
  shows.append(list(map(int,input().split())))

shows.sort()

can_watch,tv_1,tv_2 = True,-1,-1

for start,end in shows:
  # we can see on tv1
  if tv_1 < start:tv_1 = end
  # we can see on tv2
  elif tv_2 < start:tv_2 = end
  # we can't see on both 
  else:
    can_watch = False
    break
print("YES" if can_watch else "NO")