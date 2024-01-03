class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0,1
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            else:
                if right < len(nums):
                    nums[left+1] = nums[right]
                    left += 1
            right += 1
        return left+1