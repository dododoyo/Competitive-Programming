class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left,curr_sum,max_len = 0,0,-1
        arr_sum = sum(nums)
        if arr_sum < x:
            return -1
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > arr_sum - x:
                curr_sum -= nums[left] 
                left += 1
            if curr_sum == arr_sum -x:
                max_len = max(max_len,right-left+1) 
        return len(nums) - max_len if max_len != -1 else -1

