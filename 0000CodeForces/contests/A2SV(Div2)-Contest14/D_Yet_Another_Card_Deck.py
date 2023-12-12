# SAME AS PROBLEM A

n, q = map(int, input().split())
a = list(map(int, input().split()))
colors = list(map(int, input().split()))

for i in range(q):
    t = colors[i]
    j = a.index(t)
    print(j+1, end=" ")
    for k in range(j, 0, -1):
        a[k], a[k-1] = a[k-1], a[k]