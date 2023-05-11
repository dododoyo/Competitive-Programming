import collections
class Solution:
    def countOfSubstrings(self, S, K):
        freq_each = collections.defaultdict(int)
        l = 1
        r = j = sol =0
        
        #in each window track the freq of each 
        # element and the length of the dict will be the 
        # number of distinct characters
        
        
        #code only for the first window
        while r < K:
            freq_each[S[r]] +=1
            r+=1
        if len(freq_each) ==K-1:sol+=1
        
        #for the rest of the windows
        while r < len(S):
            #increase the frequency of new entered element to the window
            freq_each[S[r]] += 1
            #decrease the frequency of the element left
            freq_each[S[l-1]] -=1
            
            #if the freq of element is zero it means it is not 
            #in the window so remove it
            if freq_each[S[l-1]] == 0:
                del freq_each[S[l-1]]
            
            #append subarray length to the solution array
            #only if the the length of the dictionary
            if len(freq_each) == K-1:sol+=1
            r+=1;l+=1
            
        return sol
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends