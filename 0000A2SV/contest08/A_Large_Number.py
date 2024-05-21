for _ in range(int(input())):
    n_d = input().split()
    nums = list(input())
    n, d = int(n_d[0]), n_d[1]
    solution = n
    for i in range(n):
        if nums[i] < d:
            solution = i
            break
    answer = nums[:solution] + [d] + nums[solution:]
    print(''.join(answer))
