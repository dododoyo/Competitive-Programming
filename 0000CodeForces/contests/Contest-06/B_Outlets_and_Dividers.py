test_cases = int(input())
for i in range(test_cases):
    n,m = map(int,input().split())
    dividers = list(map(int,input().split()))
    dividers.sort(reverse=True)
    outlets,i = 2,0
    while outlets < n and i < m:
        #we subtract -1 to account for what is connected on previous dividor
        outlets = outlets - 1 + dividers[i]
        i+=1
    print(i) if outlets >= n else print(-1)