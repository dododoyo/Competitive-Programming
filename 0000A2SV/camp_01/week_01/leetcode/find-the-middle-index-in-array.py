class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward_prefix,backward_prefix  = [nums[0]]*n,[nums[-1]]*n
        for i in range(1,n):
            forward_prefix[i] = forward_prefix[i-1] + nums[i]
            backward_prefix[n-i-1] = backward_prefix[n-i] + nums[n-i-1]
        for i in range(n):
            if forward_prefix[i] == backward_prefix[i]:return i
        # if not index were found return -1
        return -1