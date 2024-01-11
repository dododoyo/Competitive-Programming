class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left,right = 0,0
        while right < len(nums):
            k -= (nums[right] == 0)
            if k < 0:
                k += nums[left] == 0
                left += 1
            right += 1
        return right - left -1
