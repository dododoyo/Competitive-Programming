boys,girls = map(int,input().split())
solution = [""]
while boys and girls:
    solution.append('B')
    solution.append('G')
    boys-=1;girls-=1
while boys:
    solution.append('B');boys-=1;
while girls:
    solution.append('G');boys-=1;
print(''.join(solution))