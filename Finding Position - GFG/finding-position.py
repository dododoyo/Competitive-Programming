#User function Template for python3
class Solution:
    def nthPosition (self, n):
        # code here 
        return 2**(n.bit_length() -1);


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthPosition(n))
# } Driver Code Ends