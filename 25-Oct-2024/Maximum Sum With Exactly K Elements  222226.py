# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        solution = 0
        for i in range(k):
            
            m = nums[-1]
            solution += m
            nums[-1] = m + 1
            
            nums.sort()
        
        return solution
