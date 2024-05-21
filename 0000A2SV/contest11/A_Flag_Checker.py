n, m = map(int, input().split())
ans = prev = 'YES'


for _ in range(n):
    sr = set(input())
    if len(sr) > 1 or prev == sr:
        ans = 'NO'
    prev = sr

print(ans)


