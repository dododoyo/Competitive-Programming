# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        solution  = nums[0]

        for number in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += number
            solution = max(solution,current_sum)

        return solution
        