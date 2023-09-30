from collections import defaultdict
def valid_indices(n,arr):
    sol=0
    dic=defaultdict(int)
    for i in range(n):
        x=arr[i]-i
        sol+=dic[x]
        dic[x]+=1
    return sol


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(valid_indices(n,arr))

