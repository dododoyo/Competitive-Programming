class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	solution = []
    	for i in arr:
    	    arr[i%n] += n
    	
    	
    	for i in range(n):
    	    val = arr[i]//n
    	    if(val > 1):
    	        solution.append(i)
    	    
        if(len(solution) == 0):
            return [-1]
        else:
            return solution
        

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends