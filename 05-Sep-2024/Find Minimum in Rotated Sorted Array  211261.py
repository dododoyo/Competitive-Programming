# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        solution = nums[0]
        low,high = 0, len(nums)-1
        while low <= high:
            middle = low + (high-low)//2
            # if left is sorted solution is 
            # definetly the left most element
            # from the left subarray
            if nums[low] <= nums[middle]:
                solution = min(solution,nums[low])

                # search minimum in the right subarray
                low = middle + 1
            # if right is sorted solution is 
            # definitely the left most element
            # from the right subarray
            else:
                solution = min(solution,nums[middle])

                # search minimum in the left subarray
                high = middle - 1
        return solution
