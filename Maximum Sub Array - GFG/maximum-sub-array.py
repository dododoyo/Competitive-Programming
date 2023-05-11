#User function Template for python3

class Solution:

	def findSubarray(self,a, n):
    	l = r = 0
    	max_sum = curr_sum = 0
    	max_range = [0,0]
    	while r < n:
    	    while((r < n) and (a[r] > -1)):curr_sum += a[r];r+=1;
    	    else: 
    	        if curr_sum > max_sum:
    	            max_sum = curr_sum
    	            max_range[0]=l;max_range[1]=r;
    	        elif curr_sum == max_sum and r-l > max_range[1]-max_range[0]:
    	            max_range[0]=l;max_range[1]=r;
    	        r+=1;l=r;curr_sum = 0
    	        
    	return a[max_range[0]:max_range[1]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends