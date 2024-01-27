""" given n integers representing 
which repeats themselves in 
modulo of three 
which exercise will get trained the most 
"""
chest,bicep,back = 0,0,0
n = int(input())
exercises = list(map(int,input().split()))

for i in range(n):
  if i%3 == 0:chest += exercises[i]
  elif i%3 == 1:bicep += exercises[i]
  else:back += exercises[i]

if bicep > chest and bicep > back:
  print("biceps")
elif bicep < chest and  back < chest:
  print("chest")
else:
  print("back")
