class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] == 0 and n == 1:
            return True

        max_destination = 1
        for i in range(n):
            # if we can't reach the current 
            # return "False"
            if i+1 > max_destination:
                return False
            # if not we go as far as we can 
            else:
                max_destination = max(max_destination,i+1+nums[i])
            
            if max_destination >= n:
                return True
