class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,current_sum,min_len = 0,0,float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len,right-left+1)
                current_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

        