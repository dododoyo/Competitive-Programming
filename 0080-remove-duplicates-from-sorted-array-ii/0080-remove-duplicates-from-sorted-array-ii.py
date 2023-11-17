class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0,0
        while right < len(nums):
            current_count = 1
            while right + 1 < len(nums) and nums[right+1] == nums[right]:
                right += 1
                current_count += 1
            for duplicates in range(min(2,current_count)):
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
            