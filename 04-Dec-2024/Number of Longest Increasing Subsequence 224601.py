# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = [1]*len(nums)
        valid_ways = [1]*len(nums)
        max_index= 0

        for curr_index in range(1,len(nums)):
            for prev_index in range(curr_index):
                if nums[curr_index] > nums[prev_index]:

                    if memo[curr_index] == memo[prev_index] +1:
                        # another one is found add it's children too
                        valid_ways[curr_index] += valid_ways[prev_index]
                    elif memo[curr_index] < 1 + memo[prev_index]:
                        memo[curr_index] = 1 + memo[prev_index]
                        # just copy
                        valid_ways[curr_index] = valid_ways[prev_index]

            if memo[max_index] < memo[curr_index]:
                max_index = curr_index

        solution = 0
        for i in range(len(nums)):
            if memo[i] == memo[max_index]:
                solution += valid_ways[i]

        return solution
        