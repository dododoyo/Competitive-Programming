for _ in range(int(input())):
    n = int(input())
    instructions = input()

    freq = [0]*4

    for i in instructions:
        freq[0] += i == "N"
        freq[1] += i == "S"
        freq[2] += i == "E"
        freq[3] += i == "W"

    norths, souths, easts, wests = freq[0], freq[1], freq[2], freq[3]

    if (norths & 1 != souths & 1) or (easts & 1 != wests & 1):
        print('NO')
        continue

    solution = []
    path = ['H', 'R']
    p1, p2, p3, p4 = 1, 1, 0, 0

    for i in range(n):
        if instructions[i] == 'N':
            t = path[p1]
            p1 = p1 != 1
        elif instructions[i] == 'S':
            t = path[p2]
            p2 = p2 != 1 
        elif instructions[i] == 'E':
            t = path[p3]
            p3 = p3 != 1
        else:
            t = path[p4]
            p4 = p4 != 1
        solution.append(t)

    if solution.count('R') == 0 or solution.count('H') == 0:
        print('NO')
        continue
    print("".join(solution))
