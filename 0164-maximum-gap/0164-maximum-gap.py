class Solution:
    def maximumGap(self, nums: List[int]) -> int:  # Time: O(nlogn)
        if len(nums) < 2:
            return 0
        nums.sort()
        max_difference = 0
        for right in range(1,len(nums)):
            max_difference = max(max_difference,nums[right]-nums[right-1])
        return max_difference