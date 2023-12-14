n = int(input())
gifts = list(map(int,input().split()))
solution = [0]*n
for index,gift in enumerate(gifts):
  solution[gift-1] = index+1
print(*solution) 