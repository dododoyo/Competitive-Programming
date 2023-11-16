class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = 0 
        for right in range(len(nums)):
            k -= nums[right] != 1
            if k < 0:
                k += nums[left] != 1
                left +=1
        return right-left