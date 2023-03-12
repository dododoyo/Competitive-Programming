# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        sent_array = S.split(".")
        solution = sent_array[0]
        sent_len = len(sent_array)
        
        for i in range(1,sent_len):
            solution = sent_array[i] + "."+ solution 
        
        return solution

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends