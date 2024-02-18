t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    count = {}
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    ans = 0
    for num in a:
        count[num] -= 1
        for i in range(-x, x+1):
            pair = num + i
            if pair % x == 0 and (num - pair) % y == 0 and pair in count:
                ans += count[pair]
    print(ans)