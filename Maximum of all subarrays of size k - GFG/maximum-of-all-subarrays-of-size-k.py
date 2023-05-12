import collections
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        dq = collections.deque()
        solution = [0]*(n-k+1)
        l=r=j=0
    
        #code for the first window
        while r < k:
            while len(dq)>0 and dq[-1] < arr[r]:dq.pop()
            dq.append(arr[r]);r+=1;
        solution[j] = dq[0]
        l+=1;j+=1
            
        #code for the rest of array
        while r < n:
            #loop to maintain a monotonic queue
            while len(dq)>0 and dq[-1] < arr[r]:dq.pop()
            dq.append(arr[r])
            
            #condition to check if the max element in the 
            #queue is out of bound
            if dq[0] == arr[l-1]:dq.popleft();
            
            #append the solution of current array
            #slide the window and solution's index
            solution[j] = dq[0]
            r+=1;l+=1;j+=1
        return solution;
            
        
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends