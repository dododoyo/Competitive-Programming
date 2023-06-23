n = int(input())
for _ in range(n):
    solution = 'B'
    input()
    for i in range(8):
        row = input()
        if row == 'RRRRRRRR':
            solution = 'R'
    print(solution)