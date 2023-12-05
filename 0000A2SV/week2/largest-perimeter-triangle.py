class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #sort the side lengths to get the max perimeter
        nums.sort(reverse=True)
        for current_index in range(2,len(nums)):
            #check if any of the elements satisfy triangle's theorem
            if nums[current_index-2] < (nums[current_index-1] + nums[current_index]):
                return  sum(nums[current_index-2:current_index+1])
        return 0