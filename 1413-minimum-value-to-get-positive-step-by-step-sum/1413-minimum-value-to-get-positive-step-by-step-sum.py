class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 1
        prefix_sum = [nums[0]]*len(nums)
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        minn = min(prefix_sum)
        minn = min(minn,min_val)
        if minn < 0:
            return (-1*minn) +1
        return minn
        