#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        p1 = 0
        p2 = 0
        total_sum = 0
        
        if(s == 0):
            return [-1]
       
        while(p2 < n):
            if(total_sum < s ):
               total_sum += arr[p2]
               
            while(total_sum > s ):
                total_sum -= arr[p1]
                p1 += 1
            p2 += 1
            
            if(total_sum == s):
                return [p1+1,p2]
            
        
                
        return [-1]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends