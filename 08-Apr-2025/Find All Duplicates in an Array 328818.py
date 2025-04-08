# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # sort using cyclic sort 
        solution = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                solution.append(abs(nums[i]))

            nums[abs(nums[i])-1] *= -1

        return solution