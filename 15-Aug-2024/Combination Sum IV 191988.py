# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        total = {}

        def helper(amount):
            if amount > target:
                return 0
            if amount == target:
                return 1

            if amount in total:
                return total[amount]
            
            possibles = 0
            for num in nums:
                possibles += helper(amount + num)
            
            total[amount] = possibles

            return possibles
        
        return helper(0)
