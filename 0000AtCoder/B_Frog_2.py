n, k = map(int, input().split())
stones = [int(num) for num in input().split()]
dp = [0]*n

for i in range(1, n):
    possible_moves = []
    if i < k:
        for j in range(i-1, -1, -1):
            possible_moves.append(dp[j] + abs(stones[j]-stones[i]))
    else:
        for j in range(1, k+1):
            possible_moves.append(dp[i-j] + abs(stones[i]-stones[i-j]))

    dp[i] = min(possible_moves)

print(dp[n-1])
