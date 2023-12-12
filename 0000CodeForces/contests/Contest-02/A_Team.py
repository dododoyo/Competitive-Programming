n = int(input())
total_correct = 0
for i in range(n):
    if input().count('1')> 1: total_correct += 1
print(total_correct)
