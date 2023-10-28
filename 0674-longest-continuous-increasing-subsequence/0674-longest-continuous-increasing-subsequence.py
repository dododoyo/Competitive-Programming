class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l,max_len = 0,0
        for r in range(1,len(nums)):
            if nums[r] <= nums[r-1]:
                l = r
            max_len = max(max_len,r-l+1)
        return max_len
        