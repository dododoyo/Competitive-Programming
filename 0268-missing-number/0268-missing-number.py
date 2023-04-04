class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums)*(len(nums)+1))/2) - sum(nums)