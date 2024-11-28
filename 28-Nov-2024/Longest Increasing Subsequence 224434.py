# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        memo = [[-1 for i in range(n)] for _ in range(n)]

        def dp(index,prev):
            if index == n:
                return 0

            if memo[index][prev] != -1:
                return memo[index][prev]

            # dont take 
            solution = 0 + dp(index+1,prev)

            # take 
            if prev == -1 or nums[index] > nums[prev]:
                solution = max(solution,1 + dp(index+1,index))

            memo[index][prev] = solution

            return memo[index][prev]

        return dp(0,-1)