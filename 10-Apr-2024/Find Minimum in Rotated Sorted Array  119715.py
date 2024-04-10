# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        solution = nums[0]
        low,high = 0, len(nums)-1
        while low <= high:
            middle = low + (high-low)//2
            #left is sorted but it may or maynot have the answer
            if nums[low] <= nums[middle]:
                solution = min(solution,nums[low])
                low = middle + 1
            #right is sorted but it may or maynot have the answer
            else:
                solution = min(solution,nums[middle])
                high = middle - 1
        return solution
