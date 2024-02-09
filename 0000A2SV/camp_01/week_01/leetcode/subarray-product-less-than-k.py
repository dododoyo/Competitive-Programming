class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int: 
        accumulator = 1
        solution,left = 0,0
        if k <= 1: return 0
        for right in range(len(nums)):
            accumulator *= nums[right]
            while accumulator >= k:
                accumulator //= nums[left]
                left += 1
            solution += right-left+1
        return solution
            
        