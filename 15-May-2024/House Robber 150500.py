# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:return nums[0]
        if n == 2:return max(nums)

        dp = [0]*(n)

        for i in range(n):
            pick,not_pick = 0,0
            if i == 0:
                pick = nums[0]
            elif i == 1:
                pick = nums[i]
                not_pick = dp[i-1]
            else:
                pick = nums[i] + dp[i-2]
                not_pick = dp[i-1]

            dp[i] = max(pick,not_pick)

        return dp[n-1]