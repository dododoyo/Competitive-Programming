class Solution:
    def numSubarraysWithSum(self, nums, goal):
        return self.atMost(nums,goal) - self.atMost(nums,goal - 1)

    def atMost(self,nums,goal):
        if goal < 0: return 0
        solution,left = 0,0
        for right in range(len(nums)):
            goal -= nums[right]
            while goal < 0:
                goal += nums[left]
                left += 1
            solution += right - left + 1
        return solution