class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        solution_len = sum([nums[i] for i in range(0,len(nums),2)])
        solution,solution_index = [0]*solution_len,0
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                solution[solution_index] = nums[i+1]
                solution_index += 1
        return solution;