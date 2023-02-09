class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        max_len = 0
        
        while r < len(nums):
            if nums[r] == 1:
                max_len = max(max_len, r-l+1)
                r += 1
            else:
                l = r+1
                r +=1
        return max_len