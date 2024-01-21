n,k = map(int,input().split())
students = [int(i) for i in input().split()]
valid_students = 0
for student in students:
  valid_students += (6 > student+k)
print(valid_students//3)