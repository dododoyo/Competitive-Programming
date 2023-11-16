class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= nums[right] == 0
            if k < 0:
                k += nums[left] == 0
                left += 1
        return right-left+1
