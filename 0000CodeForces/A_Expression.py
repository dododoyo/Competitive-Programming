abc = [0,0,0]
for i in range(3):abc[i] = int(input())
solution = 0
solution = max(solution,abc[0]*abc[1]*abc[2])
solution = max(solution,abc[0]+abc[1]+abc[2])
solution = max(solution,abc[0]*abc[1]+abc[2])
solution = max(solution,abc[0]*(abc[1]+abc[2]))
solution = max(solution,(abc[0]+abc[1])*abc[2])
solution = max(solution,abc[0]+abc[1]*abc[2])
print(solution)