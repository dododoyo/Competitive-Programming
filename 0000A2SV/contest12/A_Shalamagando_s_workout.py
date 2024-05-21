n = int(input())
exercises = [int(num) for num in input().split()]

muscles = [0]*3

for i in range(n):
  muscles[i%3] += exercises[i]

if muscles[0] > muscles[1] and muscles[0] > muscles[2]:
  print("chest")

elif muscles[1] > muscles[0] and muscles[1] > muscles[2]:
  print("biceps")

else:
  print("back")
