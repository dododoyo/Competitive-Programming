#User function Template for python3
import collections
class Solution:

    def firstRepChar(self, s):
        freq_count = collections.defaultdict(int)
        for i in s: 
            if freq_count[i] > 0:
                return i
            else:
                freq_count[i] +=  1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends