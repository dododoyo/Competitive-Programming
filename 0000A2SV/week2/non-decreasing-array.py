class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        non_decreasing_count = 0
        #count consequative elements that are non_decreasing
        for current_index in range(1,len(nums)):
            if nums[current_index-1] > nums[current_index]:
                if non_decreasing_count == 1:
                    return False
                non_decreasing_count += 1
                #handeling an edge case
                if current_index > 1 and nums[current_index-2]>nums[current_index]:
                    nums[current_index]=nums[current_index-1]  
        return True
