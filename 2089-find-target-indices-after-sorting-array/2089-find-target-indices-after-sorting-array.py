class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        solution = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                solution.append(i)
        return solution
        