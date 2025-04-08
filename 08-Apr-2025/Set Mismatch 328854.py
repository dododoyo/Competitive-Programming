# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)

        while i < n:
            temp = nums[i]
            # skip if correct one or in place
            if nums[i] == i+1 or nums[i] == nums[temp-1]:
                i += 1
            else:
                nums[temp-1], nums[i] = nums[i], nums[temp-1]

        # after all iterations is over the duplicate 
        # element will be in the missings position
        for i in range(n):
            if nums[i] != i+1:
                return [nums[i],i+1]