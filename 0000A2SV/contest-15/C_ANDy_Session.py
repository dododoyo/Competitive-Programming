for _ in range(int(input())):
    n, k = map(int, input().split())
    numbers = [int(num) for num in input().split()]
    solution = 0
    for bit_position in range(30, -1, -1):
        unset_numbers_count = 0
        for number in numbers:
            unset_numbers_count += ((number & (1 << bit_position)) == 0)
        if unset_numbers_count <= k:
            k -= unset_numbers_count
            solution = solution | (1 << bit_position)
    print(solution)
