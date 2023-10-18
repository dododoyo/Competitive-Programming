#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        #intialize neccesary variables
        prefix_sum = [0]*(N+1)
        max_sub = 0
        # create prefix sum to create the sum 
        for i in range(1,N+1):
            prefix_sum[i] = prefix_sum[i-1] + Arr[i-1]
        #slide over the prefix sum to find the maximum sum
        for r in range(K,N+1):
            max_sub = max(max_sub,prefix_sum[r] - prefix_sum[r-K])
        return max_sub
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends