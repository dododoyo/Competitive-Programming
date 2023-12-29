def solve(n,l):
    p = [0]
    for i in range(n):
        p.append(p[-1] + ((-1) ** i) * l[i])
    ans = 'NO'
    p.sort()
    for i in range(n):
        if p[i] == p[i + 1]:
            ans = 'YES'
            break
    return ans

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(n,l))
  