import collections
class Solution:
    def countDistinct(self, A, N, K):
        freq_each = collections.defaultdict(int)
        sol = [0]*(N-K+1)
        l = 1
        r = j = 0
        
        #in each window track the freq of each 
        # element and the length of the dict will be the 
        #number of distinct characters
        #only for the first window
        while r < K:
            freq_each[A[r]] +=1
            r+=1
        sol[j] = len(freq_each);j+=1
        
        #for the rest of the windows
        while r < N:
            #increase the frequency of new entered element to the window
            freq_each[A[r]] += 1
            #decrease the frequency of the element left
            freq_each[A[l-1]] -=1
            
            #if the freq of element is zero it means it is not 
            #in the window so remove it
            if freq_each[A[l-1]] == 0:
                del freq_each[A[l-1]]
            
            #append subarray length to the solution array
            sol[j] = len(freq_each);j+=1
            r+=1;l+=1
            
        return sol
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends