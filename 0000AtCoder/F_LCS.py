s1 = input()
s2 = input()

m, n = len(s1), len(s2)
dp = [[0]*(n + 1) for _ in range(m + 1)]

for row in range(1, m + 1):
    for col in range(1, n + 1):
        if s1[row - 1] == s2[col - 1]:
            dp[row][col] = 1 + dp[row - 1][col - 1]
        else:
            dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

solution_length = dp[m][n]

solution = [""]*(solution_length)

i,j = m,n
solution_index = 0

while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        solution[solution_length-solution_index-1] = s1[i-1]
        i -= 1
        j -= 1
        solution_index += 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print("".join(solution))