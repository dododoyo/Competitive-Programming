class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        solution,unique_count = 0,0
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                unique_count += 1
            solution += unique_count
        return solution
        