class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right,solution  = 0,len(nums)-1,0
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > k:right -= 1
            elif current_sum < k:left += 1
            else:
                solution += 1
                left,right = left+1,right-1
        return solution

        