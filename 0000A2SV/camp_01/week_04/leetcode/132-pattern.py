class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_till = nums[0]
        for right in range(1,len(nums)):
            while stack and stack[-1][0] <= nums[right]:
                stack.pop()
            if stack and nums[right] > stack[-1][1]:
                return True
            stack.append([nums[right],min_till])
            min_till = min(min_till,nums[right])
        return False