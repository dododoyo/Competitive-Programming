class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        current_sum = 0;
        for number in nums:
            # any negative subarray sum is useless and should be regarded
            if current_sum < 0:current_sum = 0;
                
            current_sum += number
            max_subarray = max(max_subarray,current_sum);
        return max_subarray;
        