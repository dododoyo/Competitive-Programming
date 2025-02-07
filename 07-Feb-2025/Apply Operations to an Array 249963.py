# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # apply operations 
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # swap using holder and seeker
        holder = 0

        for seeker in range(n):
            if nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker],nums[holder]
                holder += 1

        return nums