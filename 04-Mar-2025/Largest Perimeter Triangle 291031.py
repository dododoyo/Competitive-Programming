# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        #sort the side lengths to get the max perimeter
        nums.sort(reverse=True)

        for current_index in range(2,len(nums)):

            #check if any of the elements satisfy triangle's theorem
            if nums[current_index-2] < (nums[current_index-1] + nums[current_index]):
                return  nums[current_index-2] + nums[current_index-1] + nums[current_index]
                
        return 0