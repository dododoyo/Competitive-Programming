#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        
        if n == 1:
            return arr[0]
        
        com_prefix = arr[0]
        
        
        for i in range(1,n):
            cur_str = arr[i]
            min_len = min(len(com_prefix),len(cur_str))
            index = 0
            while(index < min_len):
                if(com_prefix[index] == cur_str[index]):
                    index += 1
                else:
                    break
            com_prefix = cur_str[:index]
        
        return -1 if com_prefix == "" else com_prefix


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends