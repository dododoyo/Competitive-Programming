def valid_subs(n,k,arr):
    solution = 0
    j = 1
    #j > k shows we have window greater than k
    #if more than k +1 it means they are consequative.  
    for i in range(n-1):
        if arr[i] < (arr[i+1]*2):j+=1;
        else:j=1
        if j > k:solution+=1
    return solution
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    print(valid_subs(n,k,arr))

