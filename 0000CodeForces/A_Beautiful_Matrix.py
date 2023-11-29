solution = [0,0]
for i in range(5):
    row = input()
    for j in range(0,9,2):
        if row[j] == '1':
            solution = [i+1,int(j/2)+1]
swaps = abs(solution[0] - 3)
swaps += abs(solution[1] - 3)
print(swaps)
