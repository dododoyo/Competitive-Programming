class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minimumLength = 10**6

        
        # get the prefix sum
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        #use sliding window
        while(r < len(nums)):
            if(l == 0):
                if(nums[r] < target):
                    r += 1
                else:
                    minimumLength = min(minimumLength,r-l+1)
                    l += 1
                        
        
            else:
                if(nums[r] - nums[l-1]< target):
                    r += 1
                else:
                    minimumLength = min(minimumLength,r-l+1)
                    l += 1
                    
        if minimumLength == 10**6: return 0
        
        else: return minimumLength
                
                
        