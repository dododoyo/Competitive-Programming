#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        
        '''Sort the array first
          Then use two pointers 
          to check  if each element is same'''
        #this approach showed time limit exceeded
        
        
        #another approach is to use a list of maximum size
        #and use it's index to check if the element is present
        helper_array,solution = [0]*100000,0
        for i in a:helper_array[i+1] = 1
        for i in b:
            if helper_array[i+1] == 1:solution+=1;helper_array[i+1]=0;
        return solution;
                  
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob = Solution()
        
        print(ob.NumberofElementsInIntersection(a,b,n,m))
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                
# } Driver Code Ends