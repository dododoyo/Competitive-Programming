n = int(input())
d = int(input())
e = int(input()) * 5

ans = n % d

while n >= e:
    # print(ans)
    n -= e
    ans = min(ans, n % d)


print(ans)
