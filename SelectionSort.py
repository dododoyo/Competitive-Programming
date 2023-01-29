#User function Template for python3


#Java Driver was not working so i used python


class Solution: 
    def select(self, arr, i):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
                
        return min
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        min = 0
        for i in range(n-1):
            min = self.select(arr,i)
            
            if(arr[min] != arr[i]):
                (arr[i],arr[min]) = (arr[min],arr[i])
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends