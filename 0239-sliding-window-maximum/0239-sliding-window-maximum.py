from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = [0]*(len(nums)-k+1)
        l = r = j = 0
        dq = deque()
        while r < len(nums):
            
            #before we append to to our que we have to 
            #make sure no smaller values exist within 
            #our que so while the top elementis less
            #pop it and append the new one
            while len(dq) and nums[dq[-1]] < nums[r]:
               dq.pop()
            dq.append(r)

            #if the left index is greater than the max 
            # in the queue it means greater index in the queue
            # is out of the window remove it
            if l > dq[0]:dq.popleft();
                
            #check if the windown is size k works only for the first window
            #append the solution and slide the window
            if (r+1) >= k:
                sol[j] = nums[dq[0]]
                l+=1;j+=1;
            r+=1
        return sol
        