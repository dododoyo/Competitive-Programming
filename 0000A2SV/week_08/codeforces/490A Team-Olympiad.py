n = int(input())
students = [int(i) for i in input().split()]

skill_count=[0,0,0]
for skill in students:
  skill_count[0]+= skill == 1
  skill_count[1] += skill == 2
  skill_count[2] += skill == 3

teams = min(skill_count)
print(teams)

if teams:
  i,j,k = 0,0,0
  ones,twos,threes = [0]*teams,[0]*teams,[0]*teams
  for index,value in enumerate(students):
    if value == 1 and i < teams:
      ones[i] = index;i += 1
    if value == 2 and j < teams:
      twos[j] = index;j += 1
    if value == 3 and k < teams:
      threes[k] = index;k += 1

for i in range(teams):
  print(ones[i]+1,twos[i]+1,threes[i]+1)