class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # try to minimize the maximum value in the array
        # by using only the specified operations
        solution = nums[0]
        running_sum = nums[0]
        for i in range(1,len(nums)):
            running_sum += nums[i]
            if running_sum % (i+1):
                solution = max(solution,running_sum//(i+1)+1)
            else:
                solution = max(solution,running_sum//(i+1))
        return solution