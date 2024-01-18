s,n = map(int,input().split())
dragons,bonus = [0]*n,[0]*n
for i in range(n):
  dragons[i],bonus[i] = list(map(int,input().split()))
dragon_bonus_pair = sorted(list(zip(dragons,bonus)))
for i in range(n):
  if dragon_bonus_pair[i][0] < s:
    s += dragon_bonus_pair[i][1]
  else:
    print("NO");exit(0)
print("YES")