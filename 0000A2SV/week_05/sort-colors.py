class Solution:
    def swapElements(self,nums,swap_1,swap_2):
        left,right = 0,len(nums)-1
        while left < right:
            while left < right and nums[left] != swap_2:left += 1
            while left < right and nums[right] != swap_1:right -= 1
            nums[left],nums[right] = nums[right],nums[left]
        return nums
    def sortColors(self, nums: List[int]) -> None:
        nums = self.swapElements(nums,0,2)
        nums = self.swapElements(nums,0,1)
        nums = self.swapElements(nums,1,2)
        return nums


        