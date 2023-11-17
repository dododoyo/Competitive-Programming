#User function Template for python3

class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        solution = [0]*q
        prefix_sum = [0]*(n+1)
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
        for i in range(q):
            solution[i] = prefix_sum[queries[2*i + 1]] - prefix_sum[queries[2*i]-1]
        return solution

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it,end=" ")
        print()
# } Driver Code Ends