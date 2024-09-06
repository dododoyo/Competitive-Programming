# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)-1
        low,high = 0,n
        while low <= high:
            mid = low + (high-low)//2
            if mid > 0 and nums[mid-1] > nums[mid]:
                high = mid - 1
            elif mid < n and nums[mid+1] > nums[mid]:
                low = mid + 1
            else:
                return mid