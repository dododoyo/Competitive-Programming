def minSum (arr, n) : 
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            arr[i] += (arr[i-1] - arr[i] + 1)
        if arr[i] == arr[i-1]:
            arr[i] += 1
    return sum(arr)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = minSum(arr, n)
    print(res)


# } Driver Code Ends