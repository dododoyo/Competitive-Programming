class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        valid_triplets = 0
        # print(arr)
        for i in range(n-2):
            left = i + 1
            right = n-1
            curr_sum = 0
            while left < right:
                curr_sum = arr[left] + arr[right] + arr[i]
                # print(i,left,right)
                if curr_sum < sumo:
                    valid_triplets += right-left
                    left += 1
                else:
                    right -= 1
        return valid_triplets
                
                


#{ 
 # Driver Code Starts

t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.countTriplets(a,n,k)
    print(ans)
# } Driver Code Ends