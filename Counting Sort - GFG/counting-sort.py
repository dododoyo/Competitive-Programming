#User function Template for python3

class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.
    def countSort(self,arr):
        #not getting n as input
        freq_arr = [0]*26
        ascii_arr = [0]*len(arr)
        
        #convert arr sting to list of ascii values
        for i in range(len(arr)):
            ascii_arr[i] = ord(arr[i])
        
        #get frequency of each element
        for i in ascii_arr:
            freq_arr[i - 97] += 1
        
        #get ending index of each element
        for i in range(1,len(freq_arr)):
            freq_arr[i] = freq_arr[i] + freq_arr[i-1]
        
        #create new array to save solution
        new_arr = [0]*len(arr)
        
        #append each element on it's respective position
        for i in range(len(arr)-1,-1,-1):
            new_arr[freq_arr[ascii_arr[i]-97] - 1] = ascii_arr[i]
            freq_arr[ascii_arr[i]-97] -= 1
            
        #convert ascii solution to character solution
        for i in range(len(new_arr)):
            new_arr[i] = chr(new_arr[i])
            
        return "".join(new_arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        n = int(input())
        arr = str(input())
        ob = Solution()
        print(ob.countSort(arr))

# } Driver Code Ends