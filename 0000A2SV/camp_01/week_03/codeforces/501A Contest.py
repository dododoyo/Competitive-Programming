a,b,c,d = map(int,input().split())
# a misha problem value
# b vasya problem value
# c = minutes taken by misha to solve problem
# d = minutes taken by vasya to solve problem
vasya_score = max(0.3*b, b - (0.004*b*d))
misha_score = max(0.3*a, a - (0.004*a*c))

if misha_score > vasya_score:
  print("Misha")
elif misha_score < vasya_score:
  print("Vasya")
else:
  print("Tie")