# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

n, m = map(int, input().split())
ans = 'YES'
prev = {""}

for _ in range(n):
    sr = set(input())
    if len(sr) > 1 or prev == sr:
        ans = 'NO'
    prev = sr

print(ans)
