# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low, solution, high = 0, 0, x

        while low <= high:

            middle = low + (high - low)//2

            squared = middle * middle
            if squared <= x:
                solution = middle
                low = middle + 1
            else:
                high = middle -1 
                
        return solution

        