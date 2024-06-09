# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []

        def backtrack(current, path):
            solution.append(path)
            for i in range(current, len(nums)):
                backtrack(i + 1, path + [nums[i]])
 
        backtrack(0, [])
        return solution