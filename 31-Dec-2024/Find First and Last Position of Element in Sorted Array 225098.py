# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1,-1

        # use independent binary search 
        # to find starting and ending positions

        n = len(nums)

        # find starting point
        starting = -1
        low,high = 0,n-1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                starting = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1

        if starting == -1:
            return [-1,-1]

        ending = -1
        low,high = 0,n-1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                ending = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid -1

        return starting,ending
