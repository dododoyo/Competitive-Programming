class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left,right = 0,len(nums)-1
        while left < right:
            if nums[left] == 0:
                for i in range(left,right):
                    nums[i] = nums[i+1]
                nums[right] = 0
                right -= 1
            else:
                left += 1