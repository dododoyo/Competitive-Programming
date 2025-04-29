from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

mapp = {"L":3,"M":2,"S":1}

for _ in range(ls()[0]):
  a,b = input().split()

  if a == b:
    print("=")
  elif a[-1] == b[-1]:
    if a[-1] == "S"
    if a[-1] == 
    print(">" if len(a) < len(b) else "<")
  else:
    print(">" if mapp[a[-1]] > mapp[b[-1]] else "<")
  