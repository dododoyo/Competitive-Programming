def findEqualing(a,b,c):
  big = max(a,b);
  small = min(a,b);
  moves = 0
  
  while big > small:
    moves += 1
    small += c
    big -= c
  
  return  moves

t = int(input());
for _ in range(t):
  a,b,c = map(int,input().split());

  print(findEqualing(a,b,c));