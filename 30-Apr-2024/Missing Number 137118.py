# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n,solution= len(nums),0
        
        for number in nums:
            solution = solution ^ number
            
        for i in range(1, n + 1):
            solution = solution ^ i


        return solution
