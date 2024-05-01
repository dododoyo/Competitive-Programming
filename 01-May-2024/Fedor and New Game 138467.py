# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n,m,k = map(int,input().split())
frens_army = [int(input()) for _ in range(m+1)]

possible_frens = 0
for i in range(m):
    if (frens_army[i]^frens_army[m]).bit_count() <= k:
        possible_frens += 1

print(possible_frens)