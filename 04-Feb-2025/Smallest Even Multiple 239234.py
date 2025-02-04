# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # even 
        if n % 2 == 0:
            # return the number
            return n 
            
        # odd 
        else:
            # return 2*num
            return 2*n
        