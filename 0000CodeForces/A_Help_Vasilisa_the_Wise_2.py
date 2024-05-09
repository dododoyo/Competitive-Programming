r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

a = (d1+r1-c2)//2
b = (d2+r1-c1)//2
c = (d2+r2-c2)//2
d = (c2+r2-d2)//2

solutions = [a, b, c, d]
for i in solutions:
    if i > 9 or i < 1:
        print(-1)
        exit(0)

if len(set(solutions)) == 4 and a+b == r1 and c+d == r2 and a+c == c1 and b+d == c2 and a+d == d1 and b+c == d2:
    print(a, b)
    print(c, d)
else:
    print(-1)
