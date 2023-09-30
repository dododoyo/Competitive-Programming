def is_symmetrical(n,arr):
    if arr[0] != n:
        return "NO"
    cnt = [0] * (n + 1)
    for x in arr:
        cnt[x] += 1
    for i in range(n-1, 0,-1):
        cnt[i] += cnt[i + 1]
    if cnt[1:] != arr:
        return "NO"
    else:
      return "YES"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(is_symmetrical(n,arr))
