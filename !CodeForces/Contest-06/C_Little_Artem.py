def colorGood(n,m):
    for i in range(n-1):
        print('B'*m)
    print('W'+'B'*(m-1))


t = int(input())
for i in range(t):
    n,m  = map(int,input().split())
    colorGood(n,m)
