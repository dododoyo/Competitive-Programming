#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        sol = A[M-1] - A[0]
        for i in range(N-M):
            sol = min(sol,A[M+i] - A[i+1])
        return sol

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends