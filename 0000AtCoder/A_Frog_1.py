
n = int(input())
stones = [int(num) for num in input().split()]

one_down = 0
two_down = float("inf")

for index in range(1, n):
    one_jump_cost = abs(stones[index] - stones[index-1])

    total_one_jump = one_jump_cost + one_down
    total_two_jump = float('inf')

    if index > 1:
        two_jump_cost = abs(stones[index] - stones[index-2])
        total_two_jump = two_jump_cost + two_down

    two_down = one_down # next two down will be current one down
    one_down = min(total_two_jump, total_one_jump)

print(one_down)
