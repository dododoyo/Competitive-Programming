#User function Template for python3
class Solution:
    def sortArr(self, arr, n): 
        arr.sort();return arr
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends