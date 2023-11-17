class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left,right,solution = 0,len(nums)-1,0
        while left < right:
            solution = max(solution,nums[left]+nums[right])
            left += 1;right -= 1
        return solution