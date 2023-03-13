#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here 
        #let's handle some base cases 
        if(n < 3):
            return 1
        
        n0 = 1
        n1 = 1
        
        while(n>2):
            n1 = n0 + n1
            n0 = n1 - n0
            n -= 1
            
        return n1%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends