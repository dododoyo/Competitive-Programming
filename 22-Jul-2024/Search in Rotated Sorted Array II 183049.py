# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # the only difference from part one is this has 
        # an edge case 
        low, high = 0, len(nums)-1
        while low <= high:
            middle = low + (high-low)//2
            if nums[middle] == target:
                return True

            # if both look sorted minimize window by two 
            if nums[low] == nums[middle] and nums[middle] == nums[high]:
                low += 1
                high -= 1
            # if the left is sorted
            elif nums[low] <= nums[middle]:
                # the number is in the sorted part
                if nums[low] <= target and target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # if the right is sorted
            else:
                # the number is in the sorted part
                if nums[middle] <= target and target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
        return False