
class Solution:
    def minDist(self, arr, n, x, y):
        last_x_index = -1
        last_y_index = -1
        min_distance = 1000000
        for i in range(n):
            if arr[i] == x:
                last_x_index = i;
                if last_y_index != -1:
                    min_distance = min(min_distance,abs(last_y_index-last_x_index));
            if arr[i] == y:
                last_y_index = i;
                if last_x_index != -1:
                    min_distance = min(min_distance,abs(last_y_index-last_x_index));
                    
        return -1 if last_x_index == -1 or last_y_index == -1 else min_distance;
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends