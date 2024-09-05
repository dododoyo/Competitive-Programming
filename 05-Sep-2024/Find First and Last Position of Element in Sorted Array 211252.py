# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # use independent binary search 
        # to find starting and ending positions
        starting,ending = -1,-1
        n = len(nums)

        # find starting index
        low,high = 0,n-1
        while low <= high:
            middle = low + (high-low)//2

            if nums[middle] == target:
                starting = middle
                high = middle - 1
            elif nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1

        # find ending index
        low,high = 0,n-1
        while low <= high:
            middle = low + (high-low)//2

            if nums[middle] == target:
                ending = middle
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1

        return starting,ending
        