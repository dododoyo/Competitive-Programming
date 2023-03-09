class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        #let's use a variable
        solution = [A[-1]]
        max_til_now = A[-1]
        
        for i in range(N-2,-1,-1):
            if(A[i] >= max_til_now):
                max_til_now = A[i]
                solution.append(max_til_now)
        solution.reverse()
        return solution   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends