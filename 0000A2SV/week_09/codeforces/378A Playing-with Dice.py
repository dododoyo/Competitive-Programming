a,b = map(int,input().split())
a_wins,draw,b_wins = 0,0,0
for i in range(1,7):
  a_wins += abs(a-i) < abs(b-i)
  b_wins += abs(a-i) > abs(b-i)
  draw += abs(a-i) == abs(b-i)

print(a_wins,draw,b_wins)
