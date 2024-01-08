n = int(input())
AASTU_Skills = [int(i) for i in input().split()]

m = int(input())
AAiT_Skills = [int(i) for i in input().split()]
AAiT_Skills.sort();AASTU_Skills.sort()
aait_pointer,aastu_pointer,solution = 0,0,0
while aastu_pointer < n and aait_pointer < m:
  aastu_skill,aait_skill =  AASTU_Skills[aastu_pointer] , AAiT_Skills[aait_pointer]
  if abs(aait_skill-aastu_skill) < 2:
    solution += 1
    aait_pointer,aastu_pointer = aait_pointer+1,aastu_pointer+1
  elif aait_skill > aastu_skill:
    aastu_pointer += 1
  else:
    aait_pointer += 1
print(solution)