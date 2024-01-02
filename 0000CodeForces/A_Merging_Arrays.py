n,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
solution = [0]*(len(a)+len(b))
pointer_1,pointer_2,solution_index = 0,0,0

while pointer_1 < len(a) and pointer_2 < len(b):
  if a[pointer_1] > b[pointer_2]:
    solution[solution_index] = b[pointer_2]
    pointer_2 += 1
  else:
    solution[solution_index] = a[pointer_1]
    pointer_1 += 1
  solution_index += 1

while pointer_1 < len(a):
  solution[solution_index] = a[pointer_1]
  pointer_1 += 1
  solution_index += 1
while pointer_2 < len(b):
  solution[solution_index] = b[pointer_2]
  pointer_2 += 1
  solution_index += 1

print(*solution)