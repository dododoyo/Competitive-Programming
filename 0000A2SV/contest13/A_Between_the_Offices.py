n = int(input())
des = input()
sf,fs = 0,0

for i in range(2,n+1):
  curr = des[i-2:i]
  if curr == "FS":
    fs += 1
  elif curr == "SF":
    sf += 1

if sf > fs:
  print("YES")
else:
  print("NO")
    