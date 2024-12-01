from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

n = ls()[0]
students = ls()
solution = [0]*n

def find_greater(student,students):
  greater = 0
  for x in students:
    greater += x > student

  return 1 + greater

for i in range(n):
  solution[i] = find_greater(students[i],students)

print(*solution)