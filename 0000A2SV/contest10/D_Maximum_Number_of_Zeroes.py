from math import gcd
from collections import defaultdict


def simplify(b, a):
    if b == 0:
        return 0, 1
    gcd_ab = gcd(a, b)
    b //= gcd_ab
    a //= gcd_ab
    
    if a < 0:
        b, a = -b, -a
    return b, a


n, d_freq = int(input()), defaultdict(int)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
extra = 0

for i in range(n):
    if a[i] == 0 and b[i] == 0:
        extra += 1
    elif a[i] != 0:
        d = simplify(-b[i], a[i])
        d_freq[d] += 1

solution = 0
for i in d_freq.values():
    solution = max(i, solution)
print(solution+extra)
