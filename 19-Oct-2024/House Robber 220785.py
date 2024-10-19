# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        memo = [-1]*n
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])


        for i in range(2,n):
            take = nums[i] + memo[i-2]
            not_take = memo[i-1]

            memo[i] = max(take,not_take)

        return memo[n-1]