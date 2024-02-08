class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_map = defaultdict(int)
        sum_map[0] = 1
        accumulator,solution = 0,0
        for i in range(len(nums)):
            accumulator += nums[i]
            solution += sum_map[accumulator - goal]
            sum_map[accumulator] += 1
        return solution
