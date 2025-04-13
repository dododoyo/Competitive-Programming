from sys import stdin
from math import ceil

def input(): return stdin.readline().strip()

exams,max_grade,required_grade = [int(i) for i in input().split()]
exams_data = []
total_grade = 0

for _ in range(exams):
  grade,essays = [int(i) for i in input().split()]
  total_grade += grade
  exams_data.append([grade,essays])

if total_grade/exams >= required_grade:
  print(0)
  exit()

exams_data.sort(key=lambda x:x[1])
prefix_addition = [[0,0]]

for i in range(exams):
  added_mark = (max_grade-exams_data[i][0])
  required_essay = exams_data[i][1]*added_mark 

  prefix_addition.append([prefix_addition[-1][0]+added_mark,prefix_addition[-1][1]+required_essay])


low,high = 0,exams
solution = high
additional_required = required_grade*exams- total_grade

while low <= high:
  mid = low + (high-low)//2
  if prefix_addition[mid][0] >= additional_required:
    solution = mid
    high = mid - 1
  else:
    low = mid + 1

if prefix_addition[solution][0] == additional_required:
  print(prefix_addition[solution][1])
else:
  # find less
  prev_marks = prefix_addition[solution-1][0]
  prev_essay = prefix_addition[solution-1][1]

  left = additional_required - prev_marks
  add_req = left * exams_data[solution-1][1]

  print(prev_essay+add_req)