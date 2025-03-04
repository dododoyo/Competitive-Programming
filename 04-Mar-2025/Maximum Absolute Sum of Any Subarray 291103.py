# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # maximum positive subarray
        positive_max = 0 

        # maximum negative subarray 
        negative_max = 0

        # running sum
        running_sum = 0
        for num in nums:
            running_sum += num
            positive_max = max(positive_max,running_sum)
            negative_max = min(negative_max,running_sum)

        # print(positive_max,negative_max)
        return positive_max - negative_max



        