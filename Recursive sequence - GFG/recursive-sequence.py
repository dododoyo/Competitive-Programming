#User function Template for python3

class Solution:
    def sequence(self, N):
        # code here
        if N == 1:
            return 1;
            
        additional = 1;
        last = (N*(N-1))//2;
        
        for i in range(1,N+1):
            additional *= (i+last);
            
        return self.sequence(N-1) + additional;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends