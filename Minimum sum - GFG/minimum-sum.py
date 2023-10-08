#User function Template for python3

class Solution:
    def solve(self, arr, n):
        arr.sort()
        evens = [""]*(n)
        odds = [""]*(n)
        for i in range(n):
            if i %2 == 0:
                evens[i] = str(arr[i])
            else:
                odds[i] = str(arr[i])
        evens = "".join(evens)
        odds = "".join(odds)
        if not evens:
            return int(odds)
        if not odds:
            return int(evens)
            
        return int(odds)+int(evens)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends