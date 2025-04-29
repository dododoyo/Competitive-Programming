from bisect import bisect_left
from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


# solution starts here 

for _ in range(int(input())):
    n , m = ls()
    a = ls()
    b = ls()
    b.sort()

    a[0] = min(a[0], b[0]-a[0])

    for i in range(1,n):
        j = bisect_left(b, a[i-1]+a[i] )

        if j != m:
            if a[i]<a[i-1]:
                a[i] = b[j]-a[i]
            else:
                a[i]= min(b[j]-a[i],a[i])

    print("YES" if sorted(a)==a else "NO")