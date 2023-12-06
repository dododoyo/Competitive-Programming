class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        solution = [0]*(2*n)
        for x_index in range(n):
            solution[2*x_index] = nums[x_index]
            solution[2*x_index+1] = nums[x_index+n]
        return solution