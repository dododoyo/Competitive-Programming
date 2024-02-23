from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, list(input())))
    sum_map = defaultdict(int)
    sum_map[0], current_sum, solution = 1, 0, 0

    for right in range(n):
        digits[right] -= 1
        current_sum += digits[right]
        solution += sum_map[current_sum]
        sum_map[current_sum] += 1
        
    print(solution)