# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # only one number occurs ones 
        # the rest always occurs twice

        solution = 0
        for number in nums:
            solution = solution ^ number
        
        return solution
        