def getWinner():
  a,b,c = map(int,input().split());
  if c%2 != 0:
    a+=1
  return 'First' if b < a else 'Second'
 
t = int(input())
for _ in range(t):
  print(getWinner());