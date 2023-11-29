n = int(input())
solution = count = 0
for i in range(n):
    for j in input():
        if j == '1':count += 1
    if count > 1:solution += 1
    count = 0
print(solution)