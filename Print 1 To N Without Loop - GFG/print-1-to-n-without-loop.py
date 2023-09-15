#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        if N == 1:
            print(1,end=' ');
            return 1
        nxt = 1 + self.printNos(N-1)
        print(nxt,end=' ');
        return nxt;

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends