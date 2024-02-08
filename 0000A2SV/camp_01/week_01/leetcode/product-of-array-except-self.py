class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_prefix,backward_prefix  = [nums[0]]*n,[nums[-1]]*n
        for i in range(1,n):
            forward_prefix[i] = nums[i] * forward_prefix[i-1]
            backward_prefix[n-i-1] = nums[n-i-1] * backward_prefix[n-i]
        for i in range(n):
            if i == 0:nums[i] = backward_prefix[i+1]
            elif i == n-1:nums[i] = forward_prefix[i-1]
            else:nums[i] = backward_prefix[i+1]*forward_prefix[i-1]
        return nums