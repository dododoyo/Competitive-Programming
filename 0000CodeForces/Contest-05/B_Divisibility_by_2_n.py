def powersOf2(x):
    #function to get each 2powers
    p = 0
    while x % 2 == 0:x //= 2;p += 1
    return p
def make_divisible(n,a):
    totalPower = 0
    for j in a:
        totalPower += powersOf2(j)
    b = [0]*(n//2);m=0
    #get valid indeces from all indeces
    #with their power
    for i in range(2,n+1,2):
        b[m]=powersOf2(i);m+=1

    #sort it in reverse to start from the maximum
    b.sort(reverse=True)
    solution = 0
    
    for l in b:
        if totalPower >= n:break
        totalPower += l;solution += 1
    return (solution if totalPower >= n else -1)
for i in range(int(input())):
    n = int(input())
    arr = map(int,input().split())
    print(make_divisible(n,arr))