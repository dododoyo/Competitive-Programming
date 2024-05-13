# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        solution = [1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    # solution[j] + 1 implies it is counting itself 
                    solution[i] = max(solution[i],solution[j] + 1)
        return max(solution)