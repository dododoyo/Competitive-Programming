#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pivot = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot-1)
            self.quickSort(arr,pivot+1,high)
            
    def partition(self,arr,low,high):
        i = low
        j = high
        while i < j:
            while(arr[i] <= arr[low] and i < high):
                i += 1
            while(arr[j] > arr[low] and j > low):
                j -= 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[low],arr[j] = arr[j],arr[low]
        return j
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends