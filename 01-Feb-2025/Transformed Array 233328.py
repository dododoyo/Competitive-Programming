# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        results = nums[:]
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                results[i] = nums[(i + nums[i]) % n]
            elif nums[i] < 0:
                results[i] = nums[(i + nums[i]) % n]

        return results
